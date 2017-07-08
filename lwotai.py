"""
LWOTai - A Python implementation of the Single-Player AI for Labyrinth: the War on Terror by GMT Games.
Mike Houser, 2011

Thanks to Dave Horn for implementing the Save and Undo system.

1. A save game is created after every single command whether you want it or not. If someone screws up and closes the
   window, PC battery dies, crashes, whatever, no problem, load it up again and you will be asked if you want to load
   the suspended game.

2. Rollback files are created at the beginning of each turn. You can roll back to any previous turn using the 'roll' or
   'rollback' command. You will be prompted to enter the turn to which you want to roll back.

3. An undo file is created after every card played. The player can undo to the last card at any time (with two
   exceptions) by typing 'undo'. The exceptions are:
   - when you load from a previously suspended game, or
   - after executing a rollback. The undo file is removed at that exact point, to prevent the player from undoing
     themselves to some other game from the past!

Thanks to Peter Shaw for implementing the Adjust system and for a bunch of bug fixes and cleanup.
"""

#    Change indicated by comment with 20150616PS:
#    1. Made use of CTR consistent - was adding CRT but testing for CTR (reported by Morten Kristensen)
#
#    Change indicated by comment with 20150312PS:
#    1. Fixed missing line for card 102 (reported by Thomas Chipman)
#
#    Change indicated by comment with 20150303PS:
#    1. Prevent double processing when major jihad failure sets besieged status (reported by Magnus Kvevlander)
#
#    Changes indicated by comment with 20150131PS:
#    1. Fixed spelling of besieged in Country class
#    2. Added untested countries with data to 'status' command so that 'status' can be used to reconstruct the board
#    3. Fixed 'help dep'
#    4. Added valid global markers, country markers and lapsing markers for use by 'adjust' command
#    5. Added 'adjust' command for ideology, prestige, funding, event markers, lapsing markers and country data
#    6. Additional changes for multiple aid markers when adding or removing
#    7. In plot resolution, remove one aid for each successful roll
#    8. In WOI roll adjustment, add 1 to modifiers for each aid marker
#    9. Ignore "The door of Itjihad is closed" when checking playable if playing as US (reported by Dave Horn)
#    10. Changed removeCell to remove sleeper then Sadr then active if playing as US; but active then sleeper then Sadr if Jihadist
#    11. Fixed test for infectious ideology when setting difficulty
#    12. Added 'summary' command to display state of each track
#    13. Changed message if no Islamist Rule countries at 'turn'
#    14. Changed message when card 1 event activated

import cmd
import os.path
import random
import sys

try:
    import cPickle as pickle
except:
    import pickle

SUSPEND_FILE = "suspend.lwot"
UNDO_FILE = "undo.lwot"
ROLLBACK_FILE = "turn."
RELEASE = "1.06162015.1"


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def require_type_or_none(value, required_type):
        """
        Asserts that the given value is either of the given type or is None
        :param value: the value to check
        :param required_type: the required type
        :return: the checked value
        """
        if value is None:
            return value
        return Utils.require_type(value, required_type)

    @staticmethod
    def require_type(value, required_type):
        """
        Asserts that the given value is of the given type
        :param value: the value to check
        :param required_type: the required type
        :return: the checked value
        """
        assert isinstance(value, required_type)
        return value

    @staticmethod
    def count(iterable, predicate):
        """
        Counts the items in the given iterable that match the given predicate
        :param iterable the iterable to filter
        :param predicate a function that takes one item and returns a boolean
        """
        return sum(1 for item in iterable if predicate(item))


class Alignment:
    """
    The alignment of a country relative to the US.
    :param name the display name of this alignment
    """
    def __init__(self, name):
        self.__name = Utils.require_type(name, str)
        
    def __repr__(self):
        return self.__name
        
    def __str__(self):
        return self.__name


# The possible alignments (or None)
# noinspection PyGlobalUndefined
class Alignments:
    def __init__(self):
        pass

    global ADVERSARY, ALLY, NEUTRAL
    ADVERSARY = Alignment("Adversary")
    ALLY = Alignment("Ally")
    NEUTRAL = Alignment("Neutral")


class Randomizer:
    """Picks things at random"""
    def __init__(self):
        pass

    def pick(self, quantity, candidates):
        """Picks the given quantity of items from the given list of candidates (returns a list)"""
        assert quantity <= len(candidates)
        new_list = list(candidates)
        random.shuffle(new_list)
        return new_list[0:quantity]

    def pick_one(self, candidates):
        """Picks the one item from the given list of candidates (returns the item)"""
        return self.pick(1, candidates)[0]

    def roll_d6(self, times):
        """Returns the result of rolling a six-sided die the given number of
        times (returns a list of that size containing numbers from 1 to 6)"""
        return [self.pick_one(range(1, 7)) for index in range(times)]


class Governance:
    def __init__(self, name, max_success_roll, levels_above_poor):
        self.__name = Utils.require_type(name, str)
        self.__max_success_roll = Utils.require_type(max_success_roll, int)
        self.__levels_above_poor = levels_above_poor

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.__name == self.__name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'Governance("{}", {}, {})'.format(self.__name, self.__max_success_roll, self.__levels_above_poor)

    def __str__(self):
        return self.__name

    def max_success_roll(self):
        return self.__max_success_roll

    def __hash__(self):
        return self.max_success_roll()

    def is_success(self, roll):
        return roll <= self.max_success_roll()

    def set_next_better_and_worse(self, next_better, next_worse):
        self.__next_better = Utils.require_type_or_none(next_better, Governance)
        self.__next_worse = Utils.require_type_or_none(next_worse, Governance)

    def improve(self):
        if self.__next_better is None:
            return self
        return self.__next_better

    def worsen(self):
        if self.__next_worse is None:
            return self
        return self.__next_worse

    def is_better_than(self, other):
        return self.__max_success_roll < other.__max_success_roll

    def is_worse_than(self, other):
        return self.__max_success_roll > other.__max_success_roll

    def levels_above_poor(self):
        return self.__levels_above_poor

    def min_us_ops(self):
        return self.__max_success_roll


# The possible Governances (or None)
class Governances:
    def __init__(self):
        pass

    global GOOD, FAIR, POOR, ISLAMIST_RULE
    GOOD = Governance("Good", 1, 2)
    FAIR = Governance("Fair", 2, 1)
    POOR = Governance("Poor", 3, 0)
    ISLAMIST_RULE = Governance("Islamist Rule", 4, -1)
    # The relative values of governances
    GOOD.set_next_better_and_worse(None, FAIR)
    FAIR.set_next_better_and_worse(GOOD, POOR)
    POOR.set_next_better_and_worse(FAIR, None)  # Islamist Rule requires revolution

    __values = {
        0: None,
        1: GOOD,
        2: FAIR,
        3: POOR,
        4: ISLAMIST_RULE
    }

    @classmethod
    def with_index(cls, index):
        try:
            return cls.__values[index]
        except KeyError:
            raise ValueError("Invalid governance value - {}".format(index))


class Country:
    __alignment = None
    __governance = None
    app = None
    name = ""
    type = ""
    posture = ""
    schengen = False
    recruit = 0
    troopCubes = 0
    activeCells = 0
    sleeperCells = 0
    oil = False
    resources = 0
    links = []
    markers = []
    schengenLink = False
    aid = 0
    besieged = 0    #20150131PS - fixed spelling
    regimeChange = 0
    cadre = 0
    plots = 0
    
    def __init__(self, theApp, theName, theType, thePosture, theGovernance, theSchengen, theRecruit, no1, no2, no3, theOil, theResources):
        self.app = theApp
        self.name = theName
        self.type = theType
        self.posture = thePosture
        self.make_governance(theGovernance)
        self.schengen = theSchengen
        self.recruit = theRecruit
        self.troopCubes = 0
        self.activeCells = 0
        self.sleeperCells = 0
        self.oil = theOil
        self.resources = theResources
        self.aid = 0
        self.besieged = 0
        self.regimeChange = 0
        self.cadre = 0
        self.plots = 0
        self.links = []
        self.markers = []
        self.schengenLink = False

    def alignment(self):
        return self.__alignment
    
    def is_adversary(self):
        return self.__alignment == ADVERSARY

    def is_ally(self):
        return self.__alignment == ALLY

    def is_neutral(self):
        return self.__alignment == NEUTRAL

    def is_aligned(self):
        return self.__alignment is not None

    def is_unaligned(self):
        return self.__alignment is None

    def make_adversary(self):
        self.__alignment = ADVERSARY

    def make_ally(self):
        self.__alignment = ALLY

    def make_neutral(self):
        self.__alignment = NEUTRAL

    def is_good(self):
        return self.__governance == GOOD

    def is_fair(self):
        return self.__governance == FAIR

    def is_poor(self):
        return self.__governance == POOR

    def is_islamist_rule(self):
        return self.__governance == ISLAMIST_RULE

    def is_governed(self):
        return self.__governance is not None

    def is_ungoverned(self):
        return self.__governance is None

    def make_good(self):
        self.__governance = GOOD

    def make_fair(self):
        self.__governance = FAIR

    def make_poor(self):
        self.__governance = POOR

    def make_islamist_rule(self):
        self.__governance = ISLAMIST_RULE

    def make_ungoverned(self):
        self.__governance = None

    def make_governance(self, governance):
        self.__governance = Utils.require_type_or_none(governance, Governance)

    def make_hard(self):
        """Sets a Non-Muslim country to Hard posture"""
        if self.type == "Non-Muslim":
            self.posture = "Hard"

    def make_soft(self):
        """Sets a Non-Muslim country to Soft posture"""
        if self.type == "Non-Muslim":
            self.posture = "Soft"

    def remove_posture(self):
        """Removes any posture from a Non-Muslim country"""
        if self.type == "Non-Muslim":
            self.posture = ""

    def is_non_recruit_success(self, roll):
        return self.is_governed() and self.__governance.is_success(roll)

    def is_recruit_success(self, roll, recruit_override = None):
        max_recruit_roll = self.max_recruit_roll(recruit_override)
        return max_recruit_roll is not None and roll <= max_recruit_roll

    def improve_governance(self):
        self.__governance = self.__governance.improve()
        if self.is_good():
            self.regimeChange = 0
            self.aid = 0
            self.besieged = 0

    def worsenGovernance(self):
        self.__governance = self.__governance.worsen()

    def governance_is_better_than(self, governance):
        return self.__governance is not None and self.__governance.is_better_than(governance)

    def governance_is_worse_than(self, governance):
        return self.__governance is not None and self.__governance.is_worse_than(governance)

    def is_muslim(self):
        return self.type == "Suni" or self.type == "Shia-Mix"

    def is_major_jihad_possible(self, ops, excess_cells_needed, bhutto_in_play):
        if self.is_islamist_rule():
            return False
        if not self.is_muslim():
            return False
        if bhutto_in_play and self.name == "Pakistan":
            return False
        if self.totalCells(True) - self.troops() < excess_cells_needed:
            return False
        ops_needed_from_poor = 1 if self.besieged else 2
        ops_needed = ops_needed_from_poor + self.__governance.levels_above_poor()
        return ops >= ops_needed

    def can_recruit(self, madrassas):
        return (self.totalCells(True) > 0 or
                self.cadre > 0 or
                (madrassas and self.governance_is_worse_than(FAIR)))

    def is_regime_change(self):
        return self.regimeChange > 0

    def is_disruptable(self):
        return (
            (self.totalCells() > 0 or self.cadre > 0) and
            (self.is_ally() or self.troops() >= 2 or self.type == "Non-Muslim")
        )

    def get_disrupt_summary(self):
        postureStr = ""
        troopsStr = ""
        if self.type == "Non-Muslim":
            postureStr = ", Posture %s" % self.posture
        else:
            troopsStr = ", Troops: %d" % self.troops()
        return "%s - %d Active Cells, %d Sleeper Cells, %d Cadre, Ops Reqd %d%s%s" % (self.name, self.activeCells,
                self.sleeperCells, self.cadre, self.__governance.min_us_ops(), troopsStr, postureStr)

    def max_recruit_roll(self, recruit_override = None):
        if recruit_override:
            return recruit_override
        if self.recruit > 0:
            return self.recruit
        if self.is_governed():
            return self.__governance.max_success_roll()
        return None

    def governance_as_funding(self):
        return self.__governance.max_success_roll()

    def get_recruit_score(self, ops):
        if self.is_regime_change() and self.troops() - self.totalCells(True) >= 5:
            return 100000000
        if self.is_islamist_rule() and self.totalCells(True) < 2 * ops:
            return 10000000
        if not self.is_islamist_rule() and not self.is_regime_change():
            return self.max_recruit_roll() * 1000000
        return None

    def totalCells(self, includeSadr = False):
        total = self.activeCells + self.sleeperCells
        if includeSadr and "Sadr" in self.markers:
            total += 1
        return total
    
    def numActiveCells(self):
        total = self.activeCells
        if "Sadr" in self.markers:
            total += 1
        return total

    def reduce_aid_by(self, aid_lost):
        """Reduces the level of aid by the given amount, but not below zero"""
        self.aid = max(self.aid - aid_lost, 0)
    
    def removeActiveCell(self):
        self.activeCells -= 1
        if self.activeCells < 0:        #20150131PS - changed from <= to <
            if "Sadr" in self.markers:
                self.markers.remove("Sadr")
                self.app.outputToHistory("Sadr removed from %s" % self.name, False)
                self.activeCells = 0    # 20150131PS - added
                return
            else:
                self.activeCells = 0
        self.app.outputToHistory("Active cell Removed to Funding Track", False)
        self.app.cells += 1
    
    def troops(self):
        troopCount = self.troopCubes
        if "NATO" in self.markers:
            troopCount += 2
        return troopCount
        
    def changeTroops(self, delta):
        self.troopCubes += delta
        if self.troopCubes < 0:
            if "NATO" in self.markers:
                self.markers.remove("NATO")
                self.app.outputToHistory("NATO removed from %s" % self.name, True)
            self.troopCubes = 0
        
    def govStr(self):
        if self.is_ungoverned():
            return "Untested"
        return str(self.__governance)

    @staticmethod
    def typePretty(theType):
        if theType == "Non-Muslim":
            return "NM"
        elif theType == "Suni":
            return "SU"
        elif theType == "Shia-Mix":
            return "SM"
        else:
            return "IR"
        
    def countryStr(self):
        markersStr = ""
        if len(self.markers) != 0:
            markersStr = "\n   Markers: %s" % ", ".join(self.markers)
        if self.type == "Shia-Mix" or self.type == "Suni":
            return "%s, %s %s, %d Resource(s)\n   Troops:%d Active:%d Sleeper:%d Cadre:%d Aid:%d Besieged:%d Reg Ch:%d Plots:%d %s" % (self.name, self.govStr(), self.__alignment, self.app.countryResources(self.name), self.troops(), self.activeCells, self.sleeperCells, self.cadre, self.aid, self.besieged, self.regimeChange, self.plots, markersStr)
        elif self.name == "Philippines":
            return "%s - Posture:%s\n   Troops:%d Active:%d Sleeper:%d Cadre:%d Plots:%d %s" % (self.name, self.posture, self.troops(), self.activeCells, self.sleeperCells, self.cadre, self.plots, markersStr)
        elif self.type == "Non-Muslim" and self.type != "United States":    # 20150131PS This is illogical but does no harm
            return "%s - Posture:%s\n   Active:%d Sleeper:%d Cadre:%d Plots:%d %s" % (self.name, self.posture, self.activeCells, self.sleeperCells, self.cadre, self.plots, markersStr)
        elif self.type == "Iran":
            return "%s, %s\n   Active:%d Sleeper:%d Cadre:%d Plots:%d %s" % (self.name, self.govStr(), self.activeCells, self.sleeperCells, self.cadre, self.plots, markersStr)
            
    def printCountry(self):
        print self.countryStr()


class Card:
    number = 0
    name = ""
    type = ""
    ops = 0
    remove = False
    mark = False
    lapsing = False
    
    def __init__(self, number, card_type, name, ops, remove, mark, lapsing):
        self.number = number
        self.name = name
        self.type = card_type
        self.ops = ops
        self.remove = remove
        self.mark = mark
        self.lapsing = lapsing
        
    def playable(self, side, app, ignoreItjihad):
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        elif self.type == "US" and side == "US":
            if self.number == 1:  # Backlash
                for country in app.map:
                    if (app.map[country].type != "Non-Muslim") and (app.map[country].plots > 0):
                        return True
                return False
            elif self.number == 2:  # Biometrics
                return True
            elif self.number == 3:  # CTR    20150616PS
                return app.map["United States"].posture == "Soft"
            elif self.number == 2:  # Biometrics
                return True
            elif self.number == 4:  # Moro Talks
                return True
            elif self.number == 5:  # NEST
                return True
            elif self.number == 6 or self.number == 7 :  # Sanctions
                return "Patriot Act" in app.markers
            elif self.number == 8 or self.number == 9 or self.number == 10:  # Special Forces
                for country in app.map:
                    if app.map[country].totalCells(True) > 0:
                        for subCountry in app.map:
                            if country == subCountry or app.isAdjacent(subCountry, country):
                                if app.map[subCountry].troops() > 0:
                                    return True
                return False
            elif self.number == 11:  # Abbas
                return True
            elif self.number == 12:  # Al-Azhar
                return True
            elif self.number == 13:  # Anbar Awakening
                return (app.map["Iraq"].troops() > 0) or (app.map["Syria"].troops() > 0)
            elif self.number == 14:  # Covert Action
                for country in app.map:
                    if app.map[country].is_adversary():
                        return True
                return False
            elif self.number == 15:  # Ethiopia Strikes
                return (app.map["Somalia"].is_islamist_rule()) or (app.map["Sudan"].is_islamist_rule())
            elif self.number == 16:  # Euro-Islam
                return True
            elif self.number == 17:  # FSB
                return True
            elif self.number == 18:  # Intel Community
                return True
            elif self.number == 19:  # Kemalist Republic
                return True
            elif self.number == 20:  # King Abdullah
                return True
            elif self.number == 21:  # Let's Roll
                allyGoodPlotCountries = 0
                for country in app.map:
                    if app.map[country].plots > 0:
                        if app.map[country].is_ally() or app.map[country].is_good():
                            allyGoodPlotCountries += 1
                return allyGoodPlotCountries > 0
            elif self.number == 22:  # Mossad and Shin Bet
                targetCells = 0
                targetCells += app.map["Israel"].totalCells()
                targetCells += app.map["Jordan"].totalCells()
                targetCells += app.map["Lebanon"].totalCells()
                return targetCells > 0
            elif self.number == 23 or self.number == 24 or self.number == 25:  # Predator
                numMuslimCellCountries = 0
                for country in app.map:
                    if app.map[country].totalCells(True) > 0:
                        if app.map[country].type == "Suni" or app.map[country].type == "Shia-Mix":
                            numMuslimCellCountries += 1
                return numMuslimCellCountries > 0
            elif self.number == 26:  # Quartet
                if not "Abbas" in app.markers:
                    return False
                if app.troops <= 4:
                    return False
                for country in app.map:
                    if app.isAdjacent(country, "Israel"):
                        if app.map[country].is_islamist_rule():
                            return False
                return True
            elif self.number == 27:  # Saddam Captured
                return app.map["Iraq"].troops() > 0
            elif self.number == 28:  # Sharia
                return app.numBesieged() > 0
            elif self.number == 29:  # Tony Blair
                return True
            elif self.number == 30:  # UN Nation Building
                numRC = app.numRegimeChange()
                return (numRC > 0) and ("Vieira de Mello Slain" not in app.markers)
            elif self.number == 31:  # Wiretapping
                if "Leak-Wiretapping" in app.markers:
                    return False
                for country in ["United States", "United Kingdom", "Canada"]:
                    if app.map[country].totalCells() > 0 or app.map[country].cadre > 0 or app.map[country].plots > 0:
                        return True
                return False
            elif self.number == 32:  # Back Channel
                if app.map["United States"].posture == "Hard":
                    return False
                numAdv = app.numAdversary()
                if numAdv <= 0:
                    return False
                app.listAdversaryCountries()
                return app.getYesNoFromUser("Do you have a card with a value that exactly matches an Adversary's Resources? (y/n): ")
            elif self.number == 33:  # Benazir Bhutto
                if "Bhutto Shot" in app.markers:
                    return False
                if app.map["Pakistan"].is_islamist_rule():
                    return False
                for countryObj in app.map["Pakistan"].links:
                    if countryObj.is_islamist_rule():
                        return False
                return True
            elif self.number == 34:  # Enhanced Measures
                if "Leak-Enhanced Measures" in app.markers or app.map["United States"].posture == "Soft":
                    return False
                return app.num_disruptable() > 0
            elif self.number == 35:  # Hajib
                return app.numIslamistRule() == 0
            elif self.number == 36:  # Indo-Pakistani Talks
                if app.map['Pakistan'].is_good() or app.map['Pakistan'].is_fair():
                    return True
                return False
            elif self.number == 37:  # Iraqi WMD
                if app.map["United States"].posture == "Hard" and app.map["Iraq"].is_adversary():
                    return True
                return False
            elif self.number == 38:  # Libyan Deal
                if app.map["Libya"].is_poor():
                    if app.map["Iraq"].is_ally() or app.map["Syria"].is_ally():
                        return True
                return False
            elif self.number == 39:  # Libyan WMD
                if app.map["United States"].posture == "Hard" and app.map["Libya"].is_adversary() and "Libyan Deal" not in app.markers:
                    return True
                return False
            elif self.number == 40:  # Mass Turnout
                return app.numRegimeChange() > 0
            elif self.number == 41:  # NATO
                return (app.numRegimeChange() > 0) and (app.gwotPenalty() >= 0)
            elif self.number == 42:  # Pakistani Offensive
                return (app.map["Pakistan"].is_ally()) and ("FATA" in app.map["Pakistan"].markers)
            elif self.number == 43:  # Patriot Act
                return True
            elif self.number == 44:  # Renditions
                return (app.map["United States"].posture == "Hard") and ("Leak-Renditions" not in app.markers)
            elif self.number == 45:  # Safer Now
                if app.numIslamistRule() > 0:
                    return False
                for country in app.map:
                    if app.map[country].is_good():
                        if app.map[country].totalCells(True) > 0 or app.map[country].plots > 0:
                            return False
                return True
            elif self.number == 46:  # Sistani
                targetCountries = 0
                for country in app.map:
                    if app.map[country].type == "Shia-Mix":
                        if app.map[country].regimeChange > 0:
                            if (app.map[country].totalCells(True)) > 0:
                                targetCountries += 1
                return targetCountries > 0
            elif self.number == 47:  # The door of Itjihad was closed
                return True
            else:
                return False
        elif self.type == "Jihadist" and side == "Jihadist":
            if "The door of Itjihad was closed" in app.lapsing and not ignoreItjihad:
                return False
            if self.number == 48:  # Adam Gadahn
                if app.numCellsAvailable() <= 0:
                    return False
                return app.getYesNoFromUser("Is this the 1st card of the Jihadist Action Phase? (y/n): ")
            elif self.number == 49:  # Al-Ittihad al-Islami
                return True
            elif self.number == 50:  # Ansar al-Islam
                return app.map["Iraq"].governance_is_worse_than(GOOD)
            elif self.number == 51:  # FREs
                return app.map["Iraq"].troops() > 0
            elif self.number == 52:  # IDEs
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if (app.map[country].totalCells(True)) > 0:
                            return True
                return False
            elif self.number == 53:  # Madrassas
                return app.getYesNoFromUser("Is this the 1st card of the Jihadist Action Phase? (y/n): ")
            elif self.number == 54:  # Moqtada al-Sadr
                return app.map["Iraq"].troops() > 0
            elif self.number == 55:  # Uyghur Jihad
                return True
            elif self.number == 56:  # Vieira de Mello Slain
                for country in app.map:
                    if app.map[country].regimeChange > 0 and app.map[country].totalCells() > 0:
                        return True
                return False
            elif self.number == 57:  # Abu Sayyaf
                return "Moro Talks" not in app.markers
            elif self.number == 58:  # Al-Anbar
                return "Anbar Awakening" not in app.markers
            elif self.number == 59:  # Amerithrax
                return True
            elif self.number == 60:  # Bhutto Shot
                return app.map["Pakistan"].totalCells() > 0
            elif self.number == 61:  # Detainee Release
                if "GTMO" in app.lapsing or "Renditions" in app.markers:
                    return False
                return app.getYesNoFromUser("Did the US Disrupt during this or the last Action Phase? (y/n): ")
            elif self.number == 62:  # Ex-KGB
                return True
            elif self.number == 63:  # Gaza War
                return True
            elif self.number == 64:  # Hariri Killed
                return True
            elif self.number == 65:  # HEU
                possibles = 0
                if app.map["Russia"].totalCells() > 0 and "CTR" not in app.map["Russia"].markers:
                    possibles += 1
                if app.map["Central Asia"].totalCells() > 0 and "CTR" not in app.map["Central Asia"].markers:
                    possibles += 1
                return possibles > 0
            elif self.number == 66:  # Homegrown
                return True
            elif self.number == 67:  # Islamic Jihad Union
                return True
            elif self.number == 68:  # Jemaah Islamiya
                return True
            elif self.number == 69:  # Kazakh Strain
                return app.map["Central Asia"].totalCells() > 0 and "CTR" not in app.map["Central Asia"].markers
            elif self.number == 70:  # Lashkar-e-Tayyiba
                return "Indo-Pakistani Talks" not in app.markers
            elif self.number == 71:  # Loose Nuke
                return app.map["Russia"].totalCells() > 0 and "CTR" not in app.map["Russia"].markers
            elif self.number == 72:  # Opium
                return app.map["Afghanistan"].totalCells() > 0
            elif self.number == 73:  # Pirates
                return app.map["Somalia"].is_islamist_rule() or app.map["Yemen"].is_islamist_rule()
            elif self.number == 74:  # Schengen Visas
                return True
            elif self.number == 75:  # Schroeder & Chirac
                return app.map["United States"].posture == "Hard"
            elif self.number == 76:  # Abu Ghurayb
                targetCountries = 0
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if (app.map[country].totalCells(True)) > 0:
                            targetCountries += 1
                return targetCountries > 0
            elif self.number == 77:  # Al Jazeera
                if app.map["Saudi Arabia"].troops() > 0:
                    return True
                for country in app.map:
                    if app.isAdjacent("Saudi Arabia", country):
                        if app.map[country].troops() > 0:
                            return True
                return False                
            elif self.number == 78:  # Axis of Evil
                return True
            elif self.number == 79:  # Clean Operatives
                return True
            elif self.number == 80:  # FATA
                return True
            elif self.number == 81:  # Foreign Fighters
                return app.numRegimeChange() > 0
            elif self.number == 82:  # Jihadist Videos
                return True
            elif self.number == 83:  # Kashmir
                return "Indo-Pakistani Talks" not in app.markers
            elif self.number == 84 or self.number == 85:  # Leak
                return ("Enhanced Measures" in app.markers) or ("Renditions" in app.markers) or ("Wiretapping" in app.markers)
            elif self.number == 86:  # Lebanon War
                return True
            elif self.number == 87 or self.number == 88 or self.number == 89:  # Martyrdom Operation
                for country in app.map:
                    if not app.map[country].is_islamist_rule():
                        if app.map[country].totalCells(True) > 0:
                            return True
                return False
            elif self.number == 90:  # Quagmire
                if app.prestige >= 7:
                    return False
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if app.map[country].totalCells(True) > 0:
                            return True
                return False
            elif self.number == 91:  # Regional al-Qaeda
                num = 0
                for country in app.map:
                    if app.map[country].type == "Suni" or app.map[country].type == "Shia-Mix":
                        if app.map[country].is_ungoverned():
                            num += 1
                return num >= 2
            elif self.number == 92:  # Saddam
                if "Saddam Captured" in app.markers:
                    return False
                return (app.map["Iraq"].is_poor()) and (app.map["Iraq"].is_adversary())
            elif self.number == 93:  # Taliban
                return True
            elif self.number == 94:  # The door of Itjihad was closed
                return app.getYesNoFromUser("Was a country tested or improved to Fair or Good this or last Action Phase.? (y/n): ")
            elif self.number == 95:  # Wahhabism
                return True
        else:  # Unassociated Events
            if side == "Jihadist" and "The door of Itjihad was closed" in app.lapsing and not ignoreItjihad:
                return False
            if self.number == 96:  # Danish Cartoons
                return True
            elif self.number == 97:  # Fatwa
                return app.getYesNoFromUser("Do both sides have cards remaining beyond this one? (y/n): ")
            elif self.number == 98:  # Gaza Withdrawl
                return True
            elif self.number == 99:  # HAMAS Elected
                return True
            elif self.number == 100:  # His Ut-Tahrir
                return True
            elif self.number == 101:  # Kosovo
                return True
            elif self.number == 102:  # Former Soviet Union    #20150312PS
                return True
            elif self.number == 103:  # Hizballah
                return True
            elif self.number == 104 or self.number == 105:  # Iran
                return True
            elif self.number == 106:  # Jaysh al-Mahdi
                for country in app.map:
                    if app.map[country].type == "Shia-Mix":
                        if app.map[country].troops() > 0 and app.map[country].totalCells() > 0:
                            return True
                return False
            elif self.number == 107:  # Kurdistan
                return True
            elif self.number == 108:  # Musharraf
                if "Benazir Bhutto" in app.markers:
                    return False
                return app.map["Pakistan"].totalCells() > 0
            elif self.number == 109:  # Tora Bora
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if app.map[country].totalCells() >= 2:
                            return True
                return False
            elif self.number == 110:  # Zarqawi
                return app.map["Iraq"].troops() > 0 or app.map["Syria"].troops() > 0 or app.map["Lebanon"].troops() > 0 or app.map["Jordan"].troops() > 0
            elif self.number == 111:  # Zawahiri
                if side == "US":
                    if "FATA" in app.map["Pakistan"].markers:
                        return False
                    if "Al-Anbar" in app.markers:
                        return False
                    return app.numIslamistRule() == 0
                else:
                    return True
            elif self.number == 112:  # Bin Ladin
                if side == "US":
                    if "FATA" in app.map["Pakistan"].markers:
                        return False
                    if "Al-Anbar" in app.markers:
                        return False
                    return app.numIslamistRule() == 0
                else:
                    return True
            elif self.number == 113:  # Darfur
                return True
            elif self.number == 114:  # GTMO
                return True
            elif self.number == 115:  # Hambali
                possibles = ["Indonesia/Malaysia"]
                for countryObj in app.map["Indonesia/Malaysia"].links:
                    possibles.append(countryObj.name)
                for country in possibles:
                    if app.map[country].totalCells(True) > 0:
                        if app.map[country].type == "Non-Muslim":
                            if app.map[country].posture == "Hard":
                                return True
                        else:
                            if app.map[country].is_ally():
                                return True
            elif self.number == 116:  # KSM
                if side == "US":
                    for country in app.map:
                        if app.map[country].plots > 0:
                            if app.map[country].type == "Non-Muslim" or app.map[country].is_ally():
                                return True
                    return False
                else:
                    return True
            elif self.number == 117 or self.number == 118:  # Oil Price Spike
                return True
            elif self.number == 119:  # Saleh
                return True
            elif self.number == 120:  # US Election
                return True
            return False
                
    def putsCell(self, app):
        if self.number == 48:  # Adam Gadahn
            return True
        elif self.number == 49:  # Al-Ittihad al-Islami
            return True
        elif self.number == 50:  # Ansar al-Islam
            return True
        elif self.number == 51:  # FREs
            return True
        elif self.number == 52:  # IDEs
            return False
        elif self.number == 53:  # Madrassas
            return True
        elif self.number == 54:  # Moqtada al-Sadr
            return False
        elif self.number == 55:  # Uyghur Jihad
            return True
        elif self.number == 56:  # Vieira de Mello Slain
            return False
        elif self.number == 57:  # Abu Sayyaf
            return True
        elif self.number == 58:  # Al-Anbar
            return True
        elif self.number == 59:  # Amerithrax
            return False
        elif self.number == 60:  # Bhutto Shot
            return False
        elif self.number == 61:  # Detainee Release
            return True
        elif self.number == 62:  # Ex-KGB
            return False
        elif self.number == 63:  # Gaza War
            return False
        elif self.number == 64:  # Hariri Killed
            return False
        elif self.number == 65:  # HEU
            return False
        elif self.number == 66:  # Homegrown
            return True
        elif self.number == 67:  # Islamic Jihad Union
            return True
        elif self.number == 68:  # Jemaah Islamiya
            return True
        elif self.number == 69:  # Kazakh Strain
            return False
        elif self.number == 70:  # Lashkar-e-Tayyiba
            return True
        elif self.number == 71:  # Loose Nuke
            return False
        elif self.number == 72:  # Opium
            return True
        elif self.number == 73:  # Pirates
            return False
        elif self.number == 74:  # Schengen Visas
            return False
        elif self.number == 75:  # Schroeder & Chirac
            return False
        elif self.number == 76:  # Abu Ghurayb
            return False
        elif self.number == 77:  # Al Jazeera
            return False
        elif self.number == 78:  # Axis of Evil
            return False
        elif self.number == 79:  # Clean Operatives
            return False
        elif self.number == 80:  # FATA
            return True
        elif self.number == 81:  # Foreign Fighters
            return True
        elif self.number == 82:  # Jihadist Videos
            return True
        elif self.number == 83:  # Kashmir
            return True
        elif self.number == 84 or self.number == 85:  # Leak
            return False
        elif self.number == 86:  # Lebanon War
            return True
        elif self.number == 87 or self.number == 88 or self.number == 89:  # Martyrdom Operation
            return False
        elif self.number == 90:  # Quagmire
            return False
        elif self.number == 91:  # Regional al-Qaeda
            return True
        elif self.number == 92:  # Saddam
            return False
        elif self.number == 93:  # Taliban
            return True
        elif self.number == 94:  # The door of Itjihad was closed
            return False
        elif self.number == 95:  # Wahhabism
            return False
        elif self.number == 96:  # Danish Cartoons
            return False
        elif self.number == 97:  # Fatwa
            return False
        elif self.number == 98:  # Gaza Withdrawl
            return True
        elif self.number == 99:  # HAMAS Elected
            return False
        elif self.number == 100:  # His Ut-Tahrir
            return False
        elif self.number == 101:  # Kosovo
            return False
        elif self.number == 102:  # Former Soviet Union
            return False
        elif self.number == 103:  # Hizballah
            return False
        elif self.number == 104 or self.number == 105:  # Iran
            return False
        elif self.number == 106:  # Jaysh al-Mahdi
            return False
        elif self.number == 107:  # Kurdistan
            return False
        elif self.number == 108:  # Musharraf
            return False
        elif self.number == 109:  # Tora Bora
            return False
        elif self.number == 110:  # Zarqawi
            return True
        elif self.number == 111:  # Zawahiri
            return False
        elif self.number == 112:  # Bin Ladin
            return False
        elif self.number == 113:  # Darfur
            return False
        elif self.number == 114:  # GTMO
            return False
        elif self.number == 115:  # Hambali
            return False
        elif self.number == 116:  # KSM
            return False
        elif self.number == 117 or self.number == 118:  # Oil Price Spike
            return False
        elif self.number == 119:  # Saleh
            return False
        elif self.number == 120:  # US Election
            return False
        return False
    
    def playEvent(self, side, app):
        app.outputToHistory("Card played for Event.", True)
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        elif self.type == "US" and side == "US":
            if self.number == 1:  # Backlash
                for country in app.map:
                    if (app.map[country].type != "Non-Muslim") and (app.map[country].plots > 0):
                        app.outputToHistory("Plot in Muslim country found. Select the plot during plot phase. Backlash in play", True)  #20150131PS
                        app.backlashInPlay = True
                        return True
                return False
            elif self.number == 2:  # Biometrics
                app.lapsing.append("Biometrics")
                app.outputToHistory("Biometrics in play. This turn, travel to adjacent Good countries must roll to succeed and no non-adjacent travel.", True)
            elif self.number == 3:  # CTR    20150616PS
                app.map["Russia"].markers.append("CTR")    # 20150616PS
                app.outputToHistory("CTR Marker added Russia", True)    # 20150616PS
                if (app.map["Central Asia"].is_ally()) or (app.map["Central Asia"].is_neutral()):
                    app.map["Central Asia"].markers.append("CTR")    # 20150616PS
                    app.outputToHistory("CTR Marker added in Central Asia", True)    # 20150616PS
            elif self.number == 4:  # Moro Talks
                app.markers.append("Moro Talks")
                app.outputToHistory("Moro Talks in play.", False)
                app.testCountry("Philippines")
                app.changeFunding(-1)
            elif self.number == 5:  # NEST
                app.markers.append("NEST")
                app.outputToHistory("NEST in play. If jihadists have WMD, all plots in the US placed face up.", True)
            elif self.number == 6 or self.number == 7:  # Sanctions
                if "Patriot Act" in app.markers:
                    app.changeFunding(-2)
                else:
                    return False
            elif self.number == 8 or self.number == 9 or self.number == 10:  # Special Forces
                while True:
                    input = app.getCountryFromUser("Remove a cell from what country that has troops or is adjacent to a country with troops (? for list)?: ",  "XXX", app.listCountriesWithCellAndAdjacentTroops)    
                    if input == "":
                        print ""
                        return
                    else:
                        if app.map[input].totalCells(True) <= 0:
                            print "There are no cells in %s" % input
                            print ""
                        else:
                            foundTroops = False
                            for country in app.map:
                                if country == input or app.isAdjacent(input, country):
                                    if app.map[country].troops() > 0:
                                        foundTroops = True
                                        break
                            if not foundTroops:
                                print "Neither this or any adjacent country have troops."
                                print ""
                            else:
                                app.removeCell(input, side)    # 20150131PS added side
                                app.outputToHistory(app.map[input].countryStr(), True)
                                break
            elif self.number == 11:  # Abbas
                numIRIsrael = 0
                for country in app.map:
                    if app.isAdjacent(country, "Israel"):
                        if app.map[country].is_islamist_rule():
                            numIRIsrael = 1
                            break
                app.markers.append("Abbas")
                app.outputToHistory("Abbas in play.", False)
                if app.troops >= 5 and numIRIsrael <= 0:
                    app.changePrestige(1, False)
                    app.changeFunding(-2, True)
            elif self.number == 12:  # Al-Azhar
                app.testCountry("Egypt")
                numIR = app.numIslamistRule()
                if numIR <= 0:
                    app.changeFunding(-4, True)
                else:
                    app.changeFunding(-2, True)
            elif self.number == 13:  # Anbar Awakening
                if (app.map["Iraq"].troops() > 0) or (app.map["Syria"].troops() > 0):
                    app.markers.append("Anbar Awakening")
                    app.outputToHistory("Anbar Awakening in play.", False)
                    if app.map["Iraq"].troops() == 0:
                        app.map["Syria"].aid += 1 #20150131PS changed to add rather than set to 1
                        app.outputToHistory("Aid in Syria.", False)
                    elif app.map["Syria"].troops() == 0:
                        app.map["Iraq"].aid += 1    #20150131PS changed to add rather than set to 1
                        app.outputToHistory("Aid in Iraq.", False)
                    else:
                        print "There are troops in both Iraq and Syria."
                        if app.getYesNoFromUser("Do you want to add the Aid to Iraq? (y/n): "):
                            app.map["Iraq"].aid += 1
                            app.outputToHistory("Aid in Iraq.", False)
                        else:
                            app.map["Syria"].aid += 1
                            app.outputToHistory("Aid in Syria.", False)
                    app.changePrestige(1, False)
                    print ""
                else:
                    return False
            elif self.number == 14:  # Covert Action
                targetCountry = ""
                numAdv = 0
                for country in app.map:
                    if app.map[country].is_adversary():
                        targetCountry = country
                        numAdv += 1
                if numAdv == 0:
                    return False
                elif numAdv > 1:                    
                    while True:
                        input = app.getCountryFromUser("Choose an Adversary country to attempt Covert Action (? for list): ",  "XXX", app.listAdversaryCountries)    
                        if input == "":
                            print ""
                            return
                        elif app.map[input].is_adversary():
                            targetCountry = input
                            break
                        else:
                            print "%s is not an Adversary." % input
                            print ""
                actionRoll = app.getRollFromUser("Enter Covert Action roll or r to have program roll: ")
                if actionRoll >= 4:
                    app.map[targetCountry].make_neutral()
                    app.outputToHistory("Covert Action successful, %s now Neutral." % targetCountry, False)
                    app.outputToHistory(app.map[input].countryStr(), True)
                else:
                    app.outputToHistory("Covert Action fails.", True)
            elif self.number == 15:  # Ethiopia Strikes
                if (app.map["Somalia"].is_islamist_rule()) or (app.map["Sudan"].is_islamist_rule()):
                    if not app.map["Somalia"].is_islamist_rule():
                        app.map["Sudan"].make_poor()
                        app.map["Sudan"].make_neutral()
                        app.outputToHistory("Sudan now Poor Neutral.", False)
                        app.outputToHistory(app.map["Sudan"].countryStr(), True)
                    elif not app.map["Sudan"].is_islamist_rule():
                        app.map["Somalia"].make_poor()
                        app.map["Somalia"].make_neutral()
                        app.outputToHistory("Somalia now Poor Neutral.", False)
                        app.outputToHistory(app.map["Somalia"].countryStr(), True)
                    else:
                        print "Both Somalia and Sudan are under Islamist Rule."
                        if app.getYesNoFromUser("Do you want Somalia to be set to Poor Neutral? (y/n): "):
                            app.map["Somalia"].make_poor()
                            app.map["Somalia"].make_neutral()
                            app.outputToHistory("Somalia now Poor Neutral.", False)
                            app.outputToHistory(app.map["Somalia"].countryStr(), True)
                        else:
                            app.map["Sudan"].make_poor()
                            app.map["Sudan"].make_neutral()
                            app.outputToHistory("Sudan now Poor Neutral.", False)
                            app.outputToHistory(app.map["Sudan"].countryStr(), True)
                    print ""
                else:
                    return False
            elif self.number == 16:  # Euro-Islam
                posStr = app.getPostureFromUser("Select Benelux's Posture (hard or soft): ")
                app.executeCardEuroIslam(posStr)
            elif self.number == 17:  # FSB
                app.outputToHistory("Examine Jihadist hand for Loose Nukes, HEU, or Kazakh Strain.", False)
                hasThem = app.getYesNoFromUser("Does the Jihadist hand have Loose Nukes, HEU, or Kazakh Strain? (y/n): ")
                if hasThem:
                    app.outputToHistory("Discard Loose Nukes, HEU, or Kazakh Strain from the Jihadist hand.", False)
                else:
                    russiaCells = app.map["Russia"].totalCells(True)
                    cenAsiaCells = app.map["Central Asia"].totalCells(True)
                    if russiaCells > 0 or cenAsiaCells > 0:
                        if russiaCells == 0:
                            app.removeCell("Central Asia", side)    # 20150131PS added side
                            app.outputToHistory(app.map["Central Asia"].countryStr(), True)
                        elif cenAsiaCells == 0:
                            app.removeCell("Russia", side)    # 20150131PS added side
                            app.outputToHistory(app.map["Russia"].countryStr(), True)
                        else:
                            isRussia = app.getYesNoFromUser("There are cells in both Russia and Central Asia. Do you want to remove a cell in Russia? (y/n): ")
                            if isRussia:
                                app.removeCell("Russia", side)    # 20150131PS added side
                                app.outputToHistory(app.map["Russia"].countryStr(), True)
                            else:
                                app.removeCell("Central Asia", side)    # 20150131PS added side
                                app.outputToHistory(app.map["Central Asia"].countryStr(), False)
                    else:
                        app.outputToHistory("There are no cells in Russia or Central Asia.", False)    
                app.outputToHistory("Shuffle Jihadist hand.", True)
            elif self.number == 18:  # Intel Community
                app.outputToHistory("Examine Jihadist hand. Do not change order of cards.", False)
                app.outputToHistory("Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi).", False)
                app.outputToHistory("You may now interrupt this action phase to play another card (Use the u command).", True)
            elif self.number == 19:  # Kemalist Republic
                app.outputToHistory("Turkey now a Fair Ally.", False)
                app.map["Turkey"].make_fair()
                app.map["Turkey"].make_ally()
                app.outputToHistory(app.map["Turkey"].countryStr(), True)
            elif self.number == 20:  # King Abdullah
                app.outputToHistory("Jordan now a Fair Ally.", False)
                app.map["Jordan"].make_fair()
                app.map["Jordan"].make_ally()
                app.outputToHistory(app.map["Jordan"].countryStr(), True)
                app.changePrestige(1)
                app.changeFunding(-1)
            elif self.number == 21:  # Let's Roll
                while True:
                    plotCountry = app.getCountryFromUser("Draw a card.  Choose an Ally or Good country to remove a plot from (? for list): ", "XXX", app.listGoodAllyPlotCountries)
                    if plotCountry == "":
                        print ""
                        return
                    else:
                        if not app.map[plotCountry].is_good() and not app.map[plotCountry].is_ally():
                            print "%s is neither Good nor an Ally." % plotCountry
                            print ""
                        elif app.map[plotCountry].plots <= 0:
                            print "%s has no plots." % plotCountry
                            print ""
                        else:
                            while True:
                                postureCountry = app.getCountryFromUser("Now choose a non-US country to set its Posture: ", "XXX", None)
                                if postureCountry == "":
                                    print ""
                                    return
                                else:
                                    if postureCountry == "United States":
                                        print "Choose a non-US country."
                                        print ""
                                    else:
                                        postureStr = app.getPostureFromUser("What Posture should %s have (h or s)? " % postureCountry)
                                        app.executeCardLetsRoll(plotCountry, postureCountry, postureStr)
                                        return
            elif self.number == 22:  # Mossad and Shin Bet
                app.removeAllCellsFromCountry("Israel")
                app.removeAllCellsFromCountry("Jordan")
                app.removeAllCellsFromCountry("Lebanon")
                app.outputToHistory("", False)
            elif self.number == 23 or self.number == 24 or self.number == 25:  # Predator
                while True:
                    input = app.getCountryFromUser("Choose non-Iran Muslim Country to remove a cell from (? for list): ", "XXX", app.listMuslimCountriesWithCells)
                    if input == "":
                        print ""
                        return
                    else:
                        if app.map[input].totalCells(True) == 0:
                            print "%s has no cells." % input
                            print ""
                        elif app.map[input].type == "Iran":
                            print "Iran is not allowed."
                            print ""
                        elif app.map[input].type == "Non-Muslim":
                            print "Choose a Muslim country."
                            print ""
                        else:
                            app.removeCell(input, side)    # 20150131PS added side
                            app.outputToHistory(app.map[input].countryStr(), True)
                            break
            elif self.number == 26:  # Quartet
                if not "Abbas" in app.markers:
                    return False
                if app.troops <= 4:
                    return False
                for country in app.map:
                    if app.isAdjacent(country, "Israel"):
                        if app.map[country].is_islamist_rule():
                            return False
                app.changePrestige(2)
                app.changeFunding(-3)
                app.outputToHistory("", False)
            elif self.number == 27:  # Saddam Captured
                if app.map["Iraq"].troops() == 0:
                    return False
                app.markers.append("Saddam Captured")
                app.map["Iraq"].aid += 1
                app.outputToHistory("Aid added in Iraq", False)
                app.changePrestige(1)
                app.outputToHistory(app.map["Iraq"].countryStr(), True)
            elif self.number == 28:  # Sharia
                numBesieged = app.numBesieged()
                target = ""
                if numBesieged <= 0:
                    return False
                elif numBesieged == 1:
                    for country in app.map:
                        if app.map[country].besieged > 0:
                            target = country
                            break
                else:
                    while True:
                        input = app.getCountryFromUser("Choose a country with a Besieged Regime marker to remove (? for list): ",  "XXX", app.listBesiegedCountries)    
                        if input == "":
                            print ""
                            return
                        else:
                            if app.map[input].besieged <= 0:
                                print "%s is not a Besieged Regime." % input
                                print ""
                            else:
                                target = input
                                break
                app.map[target].besieged = 0
                app.outputToHistory("%s is no longer a Besieged Regime." % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)                
            elif self.number == 29:  # Tony Blair
                app.map["United Kingdom"].posture = app.map["United States"].posture
                app.outputToHistory("United Kingdom posture now %s" % app.map["United Kingdom"].posture, False)
                print "You may roll War of Ideas in up to 3 Schengen countries."
                for i in range(3):
                    target = ""
                    finishedPicking = False
                    while not target:
                        input = app.getCountryFromUser("Choose Schengen country to make a WOI roll (done to stop rolling) (? for list)?: ",  "done", app.listSchengenCountries)
                        if input == "":
                            print ""
                            return
                        elif input == "done":
                            finishedPicking = True
                            break
                        else:
                            if not app.map[input].schengen:
                                print "%s is not a Schengen country." % input
                                print ""
                                return
                            else:
                                target = input
                                postureRoll = app.getRollFromUser("Enter Posture Roll or r to have program roll: ")
                                app.executeNonMuslimWOI(target, postureRoll)
                    if finishedPicking:
                        break
                app.outputToHistory("", False)
            elif self.number == 30:  # UN Nation Building
                numRC = app.numRegimeChange()
                if (numRC <= 0) or ("Vieira de Mello Slain" in app.markers):
                    return False
                target = ""
                if numRC == 1:
                    for country in app.map:
                        if app.map[country].regimeChange > 0:
                            target = country
                            break
                else:
                    while True:
                        input = app.getCountryFromUser("Choose a Regime Change country (? for list): ",  "XXX", app.listRegimeChangeCountries)    
                        if input == "":
                            print ""
                            return
                        else:
                            if app.map[input].regimeChange <= 0:
                                print "%s is not a Regime Change country." % input
                                print ""
                            else:
                                target = input
                                break
                app.map[target].aid += 1
                app.outputToHistory("Aid added to %s." % target, False)
                woiRoll = app.getRollFromUser("Enter WOI Roll or r to have program roll: ")
                modRoll = app.modifiedWoIRoll(woiRoll, target, False)
                app.handleMuslimWoI(modRoll, target)                
            elif self.number == 31:  # Wiretapping
                if "Leak-Wiretapping" in app.markers:
                    return False
                for country in ["United States", "United Kingdom", "Canada"]:
                    if app.map[country].activeCells > 0:
                        num = app.map[country].activeCells
                        if num > 0:
                            app.map[country].activeCells -= num
                            app.cells += num
                            app.outputToHistory("%d Active Cell(s) removed from %s." % (num, country), False)
                    if app.map[country].sleeperCells > 0:
                        num = app.map[country].sleeperCells
                        if num > 0:
                            app.map[country].sleeperCells -= num
                            app.cells += num
                            app.outputToHistory("%d Sleeper Cell(s) removed from %s." % (num, country), False)
                    if app.map[country].cadre > 0:
                        num = app.map[country].cadre
                        if num > 0:
                            app.map[country].cadre = 0
                            app.outputToHistory("Cadre removed from %s." % country, False)
                    if app.map[country].plots > 0:
                        num = app.map[country].plots
                        if num > 0:
                            app.map[country].plots -= num
                            app.outputToHistory("%d Plots remove(d) from %s." % (num, country), False)
                app.markers.append("Wiretapping")
                app.outputToHistory("Wiretapping in Play.", True)
            elif self.number == 32:  # Back Channel
                if app.map["United States"].posture == "Hard":
                    return False
                numAdv = app.numAdversary()
                if numAdv <= 0:
                    return False
                if app.getYesNoFromUser("Do you want to discard a card with a value that exactly matches an Adversary's Resources? (y/n): "):
                    while True:
                        input = app.getCountryFromUser("Choose an Adversary country (? for list): ",  "XXX", app.listAdversaryCountries)    
                        if input == "":
                            print ""
                            return False
                        else:
                            if not app.map[input].is_adversary():
                                print "%s is not a Adversary country." % input
                                print ""
                            else:
                                app.map[input].make_neutral()
                                app.outputToHistory("%s now Neutral" % input, False)
                                app.map[input].aid += 1
                                app.outputToHistory("Aid added to %s." % input, False)
                                app.outputToHistory(app.map[input].countryStr(), True)
                                break
            elif self.number == 33:  # Benazir Bhutto
                app.markers.append("Benazir Bhutto")
                app.outputToHistory("Benazir Bhutto in Play.", False)
                if app.map["Pakistan"].is_poor():
                    app.map["Pakistan"].make_fair()
                    app.outputToHistory("Pakistan now Fair governance.", False)
                app.outputToHistory("No Jihads in Pakistan.", False)
                app.outputToHistory(app.map["Pakistan"].countryStr(), True)
            elif self.number == 34:  # Enhanced Measures
                app.markers.append("Enhanced Measures")
                app.outputToHistory("Enhanced Measures in Play.", False)
                app.outputToHistory("Take a random card from the Jihadist hand.", False)
                app.do_disrupt("")
                app.outputToHistory("", False)
            elif self.number == 35:  # Hajib
                app.testCountry("Turkey")
                app.map["Turkey"].improve_governance()
                app.outputToHistory("Turkey Governance now %s." % app.map["Turkey"].govStr(), False)
                app.changeFunding(-2)
                posStr = app.getPostureFromUser("Select Frances's Posture (hard or soft): ")
                app.map["France"].posture = posStr
                app.outputToHistory(app.map["Turkey"].countryStr(), False)
                app.outputToHistory(app.map["France"].countryStr(), True)
            elif self.number == 36:  # Indo-Pakistani Talks
                app.markers.append("Indo-Pakistani Talks")
                app.outputToHistory("Indo-Pakistani Talks in Play.", False)
                app.map['Pakistan'].make_ally()
                app.outputToHistory("Pakistan now Ally", False)
                posStr = app.getPostureFromUser("Select India's Posture (hard or soft): ")
                app.map["India"].posture = posStr
                app.outputToHistory(app.map["Pakistan"].countryStr(), False)
                app.outputToHistory(app.map["India"].countryStr(), True)
            elif self.number == 37:  # Iraqi WMD
                app.markers.append("Iraqi WMD")
                app.outputToHistory("Iraqi WMD in Play.", False)
                app.outputToHistory("Use this or a later card for Regime Change in Iraq at any Governance.", True)
            elif self.number == 38:  # Libyan Deal
                app.markers.append("Libyan Deal")
                app.outputToHistory("Libyan Deal in Play.", False)
                app.map["Libya"].is_ally()
                app.outputToHistory("Libya now Ally", False)
                app.changePrestige(1)
                print "Select the Posture of 2 Schengen countries."
                for i in range(2):
                    target = ""
                    while not target:
                        input = app.getCountryFromUser("Choose Schengen country (? for list)?: ", "XXX", app.listSchengenCountries)
                        if input == "":
                            print ""
                        else:
                            if not app.map[input].schengen:
                                print "%s is not a Schengen country." % input
                                print ""
                                return
                            else:
                                target = input
                                posStr = app.getPostureFromUser("Select %s's Posture (hard or soft): " % target)
                                app.map[target].posture = posStr
                                app.outputToHistory(app.map[target].countryStr(), False)
                app.outputToHistory("", False)                
            elif self.number == 39:  # Libyan WMD
                app.markers.append("Libyan WMD")
                app.outputToHistory("Libyan WMD in Play.", False)
                app.outputToHistory("Use this or a later card for Regime Change in Libya at any Governance.", True)
            elif self.number == 40:  # Mass Turnout
                numRC = app.numRegimeChange()
                target = ""
                if numRC <= 0:
                    return False
                elif numRC == 1:
                    for country in app.map:
                        if app.map[country].regimeChange > 0:
                            target = country
                            break
                else:
                    while True:
                        input = app.getCountryFromUser("Choose a Regime Change Country to improve governance (? for list): ",  "XXX", app.listRegimeChangeCountries)    
                        if input == "":
                            print ""
                            return
                        else:
                            if app.map[input].regimeChange <= 0:
                                print "%s is not a Regime Change country." % input
                                print ""
                            else:
                                target = input
                                break
                app.improveGovernance(target)
                app.outputToHistory("%s Governance improved." % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)                
            elif self.number == 41:  # NATO
                numRC = app.numRegimeChange()
                target = ""
                if numRC <= 0:
                    return False
                elif numRC == 1:
                    for country in app.map:
                        if app.map[country].regimeChange > 0:
                            target = country
                            break
                else:
                    while True:
                        input = app.getCountryFromUser("Choose a Regime Change Country to land NATO troops (? for list): ",  "XXX", app.listRegimeChangeCountries)    
                        if input == "":
                            print ""
                            return
                        else:
                            if app.map[input].regimeChange <= 0:
                                print "%s is not a Regime Change country." % input
                                print ""
                            else:
                                target = input
                                break            
                app.map[target].markers.append("NATO")
                app.outputToHistory("NATO added in %s" % target, False)
                app.map[target].aid += 1
                app.outputToHistory("Aid added in %s" % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)                
            elif self.number == 42:  # Pakistani Offensive
                if "FATA" in app.map["Pakistan"].markers:
                    app.map["Pakistan"].markers.remove("FATA")
                    app.outputToHistory("FATA removed from Pakistan", True)
            elif self.number == 43:  # Patriot Act
                app.markers.append("Patriot Act")
            elif self.number == 44:  # Renditions
                app.markers.append("Renditions")
                app.outputToHistory("Renditions in Play.", False)
                app.outputToHistory("Discard a random card from the Jihadist hand.", False)
                if app.num_disruptable() > 0:
                    app.do_disrupt("")
                app.outputToHistory("", False)
            elif self.number == 45:  # Safer Now
                app.changePrestige(3)
                postureRoll = app.getRollFromUser("Enter US Posture Roll or r to have program roll: ")
                if postureRoll <= 4:
                    app.map["United States"].posture = "Soft"
                    app.outputToHistory("US Posture now Soft.", False)
                else:
                    app.map["United States"].posture = "Hard"
                    app.outputToHistory("US Posture now Hard.", False)
                while True:
                    postureCountry = app.getCountryFromUser("Now choose a non-US country to set its Posture: ", "XXX", None)
                    if postureCountry == "":
                        print ""
                    else:
                        if postureCountry == "United States":
                            print "Choos a non-US country."
                            print ""
                        else:
                            postureStr = app.getPostureFromUser("What Posture should %s have (h or s)? " % postureCountry)
                            app.outputToHistory("%s Posture now %s" % (postureCountry, postureStr), False)
                            app.map[postureCountry].posture = postureStr
                            app.outputToHistory(app.map["United States"].countryStr(), False)                
                            app.outputToHistory(app.map[postureCountry].countryStr(), True)    
                            break
            elif self.number == 46:  # Sistani
                targetCountries = []
                for country in app.map:
                    if app.map[country].type == "Shia-Mix":
                        if app.map[country].regimeChange > 0:
                            if (app.map[country].totalCells(True)) > 0:
                                targetCountries.append(country)
                if len(targetCountries) == 1:
                    target = targetCountries[0]
                else:
                    target = None
                while not target:
                    input = app.getCountryFromUser("Choose a Shia-Mix Regime Change Country with a cell to improve governance (? for list): ",  "XXX", app.listShiaMixRegimeChangeCountriesWithCells)    
                    if input == "":
                        print ""
                    else:
                        if input not in targetCountries:
                            print "%s is not a Shi-Mix Regime Change Country with a cell." % input
                            print ""
                        else:
                            target = input
                            break
                app.improveGovernance(target)
                app.outputToHistory("%s Governance improved." % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)                
            elif self.number == 47:  # The door of Itjihad was closed
                app.lapsing.append("The door of Itjihad was closed")
            else:
                return False
        elif self.type == "Jihadist" and side == "Jihadist":
            if self.number == 48:  # Adam Gadahn
                cardNum = app.getCardNumFromUser("Enter the number of the next Jihadist card or none if there are none left: ")
                if cardNum == "none":
                    app.outputToHistory("No cards left to recruit to US.", True)
                    return
                ops = app.deck[str(cardNum)].ops
                rolls = app.randomizer.roll_d6(ops)
                app.executeRecruit("United States", ops, rolls, 2)
            elif self.number == 49:  # Al-Ittihad al-Islami
                app.placeCells("Somalia", 1)
            elif self.number == 50:  # Ansar al-Islam
                possible = ["Iraq", "Iran"]
                target = random.choice(possible)
                app.placeCells(target, 1)
            elif self.number == 51:  # FREs
                if "Saddam Captured" in app.markers:
                    cellsToMove = 2
                else:
                    cellsToMove = 4                    
                cellsToMove = min(cellsToMove, app.cells)
                app.placeCells("Iraq", cellsToMove)
            elif self.number == 52:  # IDEs
                app.outputToHistory("US randomly discards one card.", True)
            elif self.number == 53:  # Madrassas
                app.handleRecruit(1, True)
                cardNum = app.getCardNumFromUser("Enter the number of the next Jihadist card or none if there are none left: ")
                if cardNum == "none":
                    app.outputToHistory("No cards left to recruit.", True)
                    #app.outputToHistory("Jihadist Activity Phase finished, enter plot command.", True)
                    return
                ops = app.deck[str(cardNum)].ops
                app.handleRecruit(ops, True)        
                #app.outputToHistory("Jihadist Activity Phase finished, enter plot command.", True)
            elif self.number == 54:  # Moqtada al-Sadr
                app.map["Iraq"].markers.append("Sadr")
                app.outputToHistory("Sadr Marker added in Iraq", True)
            elif self.number == 55:  # Uyghur Jihad
                app.testCountry("China")
                if app.cells > 0:
                    if app.map["China"].posture == "Soft":
                        app.place_cell("China")
                    else:
                        app.place_cell("Central Asia")
                else:
                    app.outputToHistory("No cells to place.", True)
            elif self.number == 56:  # Vieira de Mello Slain
                app.markers.append("Vieira de Mello Slain")
                app.outputToHistory("Vieira de Mello Slain in play.", False)
                app.changePrestige(-1)
            elif self.number == 57:  # Abu Sayyaf
                app.placeCells("Philippines", 1)
                app.markers.append("Abu Sayyaf")
            elif self.number == 58:  # Al-Anbar
                app.markers.append("Al-Anbar")
                app.outputToHistory("Al-Anbar in play.", True)
                app.testCountry("Iraq")
                if app.cells > 0:
                    app.place_cell("Iraq")
            elif self.number == 59:  # Amerithrax
                app.outputToHistory("US side discards its highest-value US-associated event card, if it has any.", True)
            elif self.number == 60:  # Bhutto Shot
                app.markers.append("Bhutto Shot")
                app.outputToHistory("Bhutto Shot in play.", True)
            elif self.number == 61:  # Detainee Release
                if app.cells > 0:
                    target = None
                    while not target:
                        input = app.getCountryFromUser("Choose a country where Disrupt occured this or last Action Phase: ",  "XXX", None)    
                        if input == "":
                            print ""
                            return
                        else:
                            target = input
                            break
                    app.place_cell(target)
                app.outputToHistory("Draw a card for the Jihadist and put it on the top of their hand.", True)
            elif self.number == 62:  # Ex-KGB
                if "CTR" in app.map["Russia"].markers:
                    app.map["Russia"].markers.remove("CTR")
                    app.outputToHistory("CTR removed from Russia.", True)
                else:
                    targetCaucasus = False
                    if app.map["Caucasus"].posture == "" or app.map["Caucasus"].posture == app.map["United States"].posture:
                        if app.gwotPenalty() == 0:
                            cacPosture = app.map["Caucasus"].posture
                            if app.map["United States"].posture == "Hard":
                                app.map["Caucasus"].posture = "Soft"
                            else:
                                app.map["Caucasus"].posture = "Hard"
                            if app.gwotPenalty() < 0:
                                targetCaucasus = True
                            app.map["Caucasus"].posture = cacPosture
                    if targetCaucasus:
                        if app.map["United States"].posture == "Hard":
                            app.map["Caucasus"].posture = "Soft"
                        else:
                            app.map["Caucasus"].posture = "Hard"
                        app.outputToHistory("Caucasus posture now %s" % app.map["Caucasus"].posture, False)
                        app.outputToHistory(app.map["Caucasus"].countryStr(), True)
                    else:
                        app.testCountry("Central Asia")
                        if app.map["Central Asia"].is_ally():
                            app.map["Central Asia"].make_neutral()
                            app.outputToHistory("Central Asia now Neutral.", True)
                        elif app.map["Central Asia"].is_neutral():
                            app.map["Central Asia"].make_adversary()
                            app.outputToHistory("Central Asia now Adversary.", True)
                        app.outputToHistory(app.map["Central Asia"].countryStr(), True)
            elif self.number == 63:  # Gaza War
                app.changeFunding(1)
                app.changePrestige(-1)
                app.outputToHistory("US discards a random card.", True)
            elif self.number == 64:  # Hariri Killed
                app.testCountry("Lebanon")
                app.testCountry("Syria")
                app.map["Syria"].make_adversary()
                app.outputToHistory("Syria now Adversary.", False)
                if app.map["Syria"].governance_is_better_than(POOR):
                    app.worsenGovernance("Syria")
                    app.outputToHistory("Governance in Syria worsened.", False)
                    app.outputToHistory(app.map["Syria"].countryStr(), True)
                app.outputToHistory(app.map["Lebanon"].countryStr(), True)
            elif self.number == 65:  # HEU
                possibles = []
                if app.map["Russia"].totalCells() > 0 and "CTR" not in app.map["Russia"].markers:
                    possibles.append("Russia")
                if app.map["Central Asia"].totalCells() > 0 and "CTR" not in app.map["Central Asia"].markers:
                    possibles.append("Central Asia")
                target = random.choice(possibles)
                roll = random.randint(1,6)
                app.executeCardHEU(target, roll)
            elif self.number == 66:  # Homegrown
                app.placeCells("United Kingdom", 1)
            elif self.number == 67:  # Islamic Jihad Union
                app.placeCells("Central Asia", 1)
                if app.cells > 0:
                    app.placeCells("Afghanistan", 1)
            elif self.number == 68:  # Jemaah Islamiya
                app.placeCells("Indonesia/Malaysia", 2)
            elif self.number == 69:  # Kazakh Strain
                roll = random.randint(1,6)
                app.executeCardHEU("Central Asia", roll)
            elif self.number == 70:  # Lashkar-e-Tayyiba
                app.placeCells("Pakistan", 1)
                if app.cells > 0:
                    app.placeCells("India", 1)
            elif self.number == 71:  # Loose Nuke
                roll = random.randint(1,6)
                app.executeCardHEU("Russia", roll)
            elif self.number == 72:  # Opium
                cellsToPlace = min(app.cells, 3)
                if app.map["Afghanistan"].is_islamist_rule():
                    cellsToPlace = app.cells
                app.placeCells("Afghanistan", cellsToPlace)
            elif self.number == 73:  # Pirates
                app.markers.append("Pirates")
                app.outputToHistory("Pirates in play.", False)
            elif self.number == 74:  # Schengen Visas
                if app.cells == 15:
                    app.outputToHistory("No cells to travel.", False)
                    return
                app.handleTravel(2, False, True)
            elif self.number == 75:  # Schroeder & Chirac
                app.map["Germany"].posture = "Soft"
                app.outputToHistory("%s Posture now %s" % ("Germany", app.map["Germany"].posture), True)
                app.map["France"].posture = "Soft"
                app.outputToHistory("%s Posture now %s" % ("France", app.map["France"].posture), True)
                app.changePrestige(-1)
            elif self.number == 76:  # Abu Ghurayb
                app.outputToHistory("Draw 2 cards.", False)
                app.changePrestige(-2)
                allys = app.minorJihadInGoodFairChoice(1, True)
                if not allys:
                    app.outputToHistory("No Allys to shift.", True)
                else:
                    target = allys[0][0]
                    app.map[target].make_neutral()
                    app.outputToHistory("%s Alignment shifted to Neutral." % target, True)
            elif self.number == 77:  # Al Jazeera
                choices = app.minorJihadInGoodFairChoice(1, False, True)
                if not choices:
                    app.outputToHistory("No countries to shift.", True)
                else:
                    target = choices[0][0]
                    if app.map[target].is_ally():
                        app.map[target].make_neutral()
                    elif app.map[target].is_neutral():    
                        app.map[target].make_adversary()
                    app.outputToHistory("%s Alignment shifted to %s." % (target, app.map[target].alignment()), True)
            elif self.number == 78:  # Axis of Evil
                app.outputToHistory("US discards any Iran, Hizballah, or Jaysh al-Mahdi cards from hand.", False)
                if app.map["United States"].posture == "Soft":
                    app.map["United States"].posture = "Hard"
                    app.outputToHistory("US Posture now Hard.", False)
                prestigeRolls = []
                for i in range(3):
                    prestigeRolls.append(random.randint(1,6))
                presMultiplier = 1
                if prestigeRolls[0] <= 4:
                    presMultiplier = -1
                app.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
            elif self.number == 79:  # Clean Operatives
                app.handleTravel(2, False, False, True)
            elif self.number == 80:  # FATA
                app.testCountry("Pakistan")
                if app.map["Pakistan"].markers.count("FATA") == 0:
                    app.map["Pakistan"].markers.append("FATA")
                    app.outputToHistory("FATA marker added in Pakistan", True)
                app.placeCells("Pakistan", 1)
            elif self.number == 81:  # Foreign Fighters
                possibles = []
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        possibles.append(country)
                if len(possibles) <= 0:
                    return False
                target = random.choice(possibles)
                app.placeCells(target, 5)
                if app.map[target].aid > 0:
                    app.map[target].aid -= 1
                    app.outputToHistory("Aid removed from %s" % target, False)
                else:
                    app.map[target].besieged = 1
                    app.outputToHistory("%s to Besieged Regime" % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 82:  # Jihadist Videos
                possibles = []
                for country in app.map:
                    if app.map[country].totalCells() == 0:
                        possibles.append(country)
                random.shuffle(possibles)
                for i in range(3):
                    app.testCountry(possibles[i])
                    # number of available cells does not matter for Jihadist Videos
                    # if app.cells > 0:
                    rolls = [random.randint(1, 6)]
                    app.executeRecruit(possibles[i], 1, rolls, False, True)
            elif self.number == 83:  # Kashmir
                app.placeCells("Pakistan", 1)
                if app.map["Pakistan"].is_ally():
                    app.map["Pakistan"].make_neutral()
                elif app.map["Pakistan"].is_neutral():    
                    app.map["Pakistan"].make_adversary()
                app.outputToHistory("%s Alignment shifted to %s." % ("Pakistan", app.map["Pakistan"].alignment()), True)
                app.outputToHistory(app.map["Pakistan"].countryStr(), True)
            elif self.number == 84 or self.number == 85:  # Leak
                possibles = []
                if "Enhanced Measures" in app.markers:
                    possibles.append("Enhanced Measures")
                if "Renditions" in app.markers:
                    possibles.append("Renditions")
                if "Wiretapping" in app.markers:
                    possibles.append("Wiretapping")
                target = random.choice(possibles)
                app.markers.remove(target)
                app.markers.append("Leak-"+target)
                app.outputToHistory("%s removed and can no longer be played." % target, False)    
                usPrestigeRolls = []
                for i in range(3):
                    usPrestigeRolls.append(random.randint(1,6))
                postureRoll = random.randint(1,6)
                presMultiplier = 1
                if usPrestigeRolls[0] <= 4:
                    presMultiplier = -1
                app.changePrestige(min(usPrestigeRolls[1], usPrestigeRolls[2]) * presMultiplier, False)
                if postureRoll <= 4:
                    app.map["United States"].posture = "Soft"
                else:
                    app.map["United States"].posture = "Hard"
                app.outputToHistory("US Posture now %s" % app.map["United States"].posture, True)
                allies = app.minorJihadInGoodFairChoice(1, True)
                if not allies:
                    app.outputToHistory("No Allies to shift.", True)
                else:
                    target = allies[0][0]
                    app.map[target].make_neutral()
                    app.outputToHistory("%s Alignment shifted to Neutral." % target, True)
            elif self.number == 86:  # Lebanon War
                app.outputToHistory("US discards a random card.", False)    
                app.changePrestige(-1, False)
                possibles = []
                for country in app.map:
                    if app.map[country].type == "Shia-Mix":
                        possibles.append(country)
                target = random.choice(possibles)
                app.placeCells(target, 1)
            elif self.number == 87 or self.number == 88 or self.number == 89:  # Martyrdom Operation
                if app.executePlot(1, False, [1], True) == 1:
                    app.outputToHistory("No plots could be placed.", True)
                    app.handleRadicalization(app.deck[str(self.number)].ops)                    
            elif self.number == 90:  # Quagmire
                app.map["United States"].posture = "Soft"
                app.outputToHistory("US Posture now Soft.", False)
                app.outputToHistory("US randomly discards two cards and Jihadist plays them.", False)
                app.outputToHistory("Do this using the j # command for each card.", True)
            elif self.number == 91:  # Regional al-Qaeda
                possibles = []
                for country in app.map:
                    if app.map[country].is_muslim() and app.map[country].is_ungoverned():
                        possibles.append(country)
                random.shuffle(possibles)
                if app.numIslamistRule() > 0:
                    app.placeCells(possibles[0], 2)
                    app.placeCells(possibles[1], 2)
                else:
                    app.placeCells(possibles[0], 1)
                    app.placeCells(possibles[1], 1)
            elif self.number == 92:  # Saddam
                app.funding = 9
                app.outputToHistory("Jihadist Funding now 9.", True)
            elif self.number == 93:  # Taliban
                app.testCountry("Afghanistan")
                app.map["Afghanistan"].besieged = 1
                app.outputToHistory("Afghanistan is now a Besieged Regime.", False)
                app.placeCells("Afghanistan", 1)
                app.placeCells("Pakistan", 1)
                if (app.map["Afghanistan"].is_islamist_rule()) or (app.map["Pakistan"].is_islamist_rule()):
                    app.changePrestige(-3)
                else:
                    app.changePrestige(-1)
            elif self.number == 94:  # The door of Itjihad was closed
                target = None
                while not target:
                    country = app.getCountryFromUser("Choose a country tested or improved to Fair or Good this or last Action Phase: ", "XXX", None)
                    if country == "":
                        print ""
                    elif app.map[country].is_fair() or app.map[country].is_good():
                        target = country
                    else:
                        print "%s is neither Fair nor Good."
                app.map[target].worsenGovernance()
                app.outputToHistory("%s Governance worsened." % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 95:  # Wahhabism
                if app.map["Saudi Arabia"].is_islamist_rule():
                    app.changeFunding(9)
                else:
                    app.changeFunding(app.map["Saudi Arabia"].governance_as_funding())
        else:
            if self.number == 96:  # Danish Cartoons
                posStr = app.getPostureFromUser("Select Scandinavia's Posture (hard or soft): ")
                app.map["Scandinavia"].posture = posStr
                app.outputToHistory("Scandinavia posture now %s." % posStr, False)
                possibles = []
                for country in app.map:
                    if app.map[country].is_muslim() and not app.map[country].is_islamist_rule():
                        possibles.append(country)
                target = random.choice(possibles)
                app.testCountry(target)
                if app.numIslamistRule() > 0:
                    app.outputToHistory("Place any available plot in %s." % target, False)
                else:
                    app.outputToHistory("Place a Plot 1 in %s." % target, False)
                app.map[target].plots += 1
            elif self.number == 97:  # Fatwa
                app.outputToHistory("Trade random cards.", False)
                if side == "US":
                    app.outputToHistory("Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi).", False)
                else:
                    app.aiFlowChartMajorJihad(97)                
            elif self.number == 98:  # Gaza Withdrawl
                if side == "US":
                    app.changeFunding(-1)
                else:
                    app.placeCells("Israel", 1)
            elif self.number == 99:  # HAMAS Elected
                app.outputToHistory("US selects and discards one card.", False)
                app.changePrestige(-1)
                app.changeFunding(-1)    
            elif self.number == 100:  # His Ut-Tahrir
                if app.troops >= 10:
                    app.changeFunding(-2)
                elif app.troops < 5:
                    app.changeFunding(2)
            elif self.number == 101:  # Kosovo
                app.changePrestige(1)
                app.testCountry("Serbia")
                if app.map["United States"].posture == "Soft":
                    app.map["Serbia"].posture = "Hard"
                else:
                    app.map["Serbia"].posture = "Soft"
                app.outputToHistory("Serbia Posture now %s." %                         app.map["Serbia"].posture, True)        
            elif self.number == 102:  # Former Soviet Union
                testRoll = random.randint(1,6)
                if testRoll <= 4:
                    app.map["Central Asia"].make_poor()
                else:
                    app.map["Central Asia"].make_fair()
                app.map["Central Asia"].make_neutral()
                app.outputToHistory("%s tested, governance %s" % (app.map["Central Asia"].name, app.map["Central Asia"].govStr()), False)
            elif self.number == 103:  # Hizballah
                if side == "US":
                    oneAway = []
                    twoAway = []
                    threeAway = []
                    for countryObj in app.map["Lebanon"].links:    
                        oneAway.append(countryObj.name)
                    for country in oneAway:
                        for subCountryObj in app.map[country].links:
                            if subCountryObj.name not in twoAway and subCountryObj.name not in oneAway and subCountryObj.name != "Lebanon":
                                twoAway.append(subCountryObj.name)
                    for country in twoAway:
                        for subCountryObj in app.map[country].links:
                            if subCountryObj.name not in threeAway and subCountryObj.name not in twoAway and subCountryObj.name not in oneAway and subCountryObj.name != "Lebanon":
                                threeAway.append(subCountryObj.name)
                    possibles = []
                    for country in oneAway:
                        if country not in possibles and app.map[country].totalCells(True) > 0 and app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    for country in twoAway:
                        if country not in possibles and app.map[country].totalCells(True) > 0 and app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    for country in threeAway:
                        if country not in possibles and app.map[country].totalCells(True) > 0 and app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    if len(possibles) <= 0:
                        app.outputToHistory("No Shia-Mix countries with cells within 3 countries of Lebanon.", True)
                        target = None
                    elif len(possibles) == 1:
                        target = possibles[0]
                    else:
                        target = None
                        while not target:
                            input = app.getCountryFromUser("Remove a cell from what Shia-Mix country within 3 countries of Lebanon (? for list)?: ",  "XXX", app.listCountriesInParam, possibles)    
                            if input == "":
                                print ""
                            else:
                                if app.map[input].totalCells(True) <= 0:
                                    print "There are no cells in %s" % input
                                    print ""
                                elif input not in possibles:
                                    print "%s not a Shia-Mix country within 3 countries of Lebanon." % input
                                    print ""
                                else:
                                    target = input
                    if target:
                        app.removeCell(target, side)    # 20150131PS added side
                        app.outputToHistory(app.map[target].countryStr(), True)
                else:
                    app.testCountry("Lebanon")
                    app.map["Lebanon"].make_poor()
                    app.outputToHistory("Lebanon governance now Poor.", False)
                    app.map["Lebanon"].make_neutral()
                    app.outputToHistory("Lebanon alignment now Neutral.", True)
            elif self.number == 104 or self.number == 105:  # Iran
                if side == "US":
                    target = None
                    while not target:
                        input = app.getCountryFromUser("Choose a Shia-Mix country to test. You can then remove a cell from there or Iran (? for list)?: ",  "XXX", app.listShiaMixCountries)    
                        if input == "":
                            print ""
                        else:
                            if app.map[input].type != "Shia-Mix":
                                print "%s is not a Shia-Mix country." % input
                                print ""
                            else:
                                target = input
                    picked = target
                    app.testCountry(picked)
                    if app.map["Iran"].totalCells(True) > 0:
                        target = None
                        while not target:
                            input = app.getCountryFromUser("Remove a cell from %s or %s: " % (picked, "Iran"),  "XXX", None)    
                            if input == "":
                                print ""
                            else:
                                if input != picked and input != "Iran":
                                    print "Remove a cell from %s or %s: " % (picked, "Iran")
                                    print ""
                                else:
                                    target = input
                    else:
                        target = picked
                    app.removeCell(target, side)    # 20150131PS added side
                    app.outputToHistory(app.map[target].countryStr(), True)
                else:
                    possibles = []
                    for country in app.map:
                        if app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    target = random.choice(possibles)
                    app.testCountry(target)
                    tested = target
                    target = None
                    goods = []
                    for country in app.map:
                        if app.map[country].type == "Shia-Mix" or app.map[country].type == "Suni":
                            if app.map[country].is_good():
                                goods.append(country)
                    if len(goods) > 1:
                        distances = []
                        for country in goods:
                            distances.append((app.countryDistance(tested, country), country))
                        distances.sort()
                        target = distances[0][1]
                    elif len(goods) == 1:
                        target = goods[0]
                    else:
                        fairs = []
                        for country in app.map:
                            if app.map[country].type == "Shia-Mix" or app.map[country].type == "Suni":
                                if app.map[country].is_fair():
                                    fairs.append(country)
                        if len(fairs) > 1:
                            distances = []
                            for country in fairs:
                                distances.append((app.countryDistance(tested, country), country))
                            distances.sort()
                            target = distances[0][1]
                        elif len(fairs) == 1:
                            target = fairs[0]
                        else:
                            app.outputToHistory("No Good or Fair countries to Jihad in.", True)
                            return
                    app.outputToHistory("%s selected for jihad rolls." % target, False)
                    for i in range(2):
                        roll = random.randint(1,6)
                        app.outputToHistory("Rolled: " + str(roll), False)
                        if app.map[target].is_non_recruit_success(roll):
                            if app.map[target].governance_is_better_than(POOR):
                                app.map[target].worsenGovernance()
                                app.outputToHistory("Governance worsened in %s." % target, False)
                                app.outputToHistory(app.map[target].countryStr(), True)
                        else:
                            app.outputToHistory("Roll failed.  No change to governance in %s." % target, False)
                            
            elif self.number == 106:  # Jaysh al-Mahdi
                if side == "US":
                    target = None
                    possibles = []
                    for country in app.map:
                        if app.map[country].type == "Shia-Mix":
                            if app.map[country].troops() > 0 and app.map[country].totalCells() > 0:
                                possibles.append(country)
                    if len(possibles) == 1:
                        target = possibles[0]
                    while not target:
                        input = app.getCountryFromUser("Choose a Shia-Mix country with cells and troops (? for list)?: ",  "XXX", app.listShiaMixCountriesWithCellsTroops)    
                        if input == "":
                            print ""
                        else:
                            if input not in possibles:
                                print "%s is not a Shia-Mix country with cells and troops." % input
                                print ""
                            else:
                                target = input
                    app.removeCell(target, side)    # 20150131PS added side
                    app.removeCell(target, side)    # 20150131PS added side
                    app.outputToHistory(app.map[target].countryStr(), True)
                else:   # jihadist play
                    possibles = []
                    for country in app.map:
                        if app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    target = random.choice(possibles)
                    app.testCountry(target)
                    tested = target
                    target = None
                    goods = []
                    for country in app.map:
                        if app.map[country].is_muslim():
                            if app.map[country].is_good():
                                goods.append(country)
                    if len(goods) > 1:
                        distances = []
                        for country in goods:
                            distances.append((app.countryDistance(tested, country), country))
                        distances.sort()
                        target = distances[0][1]
                    elif len(goods) == 1:
                        target = goods[0]
                    else:
                        fairs = []
                        for country in app.map:
                            if app.map[country].type == "Shia-Mix" or app.map[country].type == "Suni":
                                if app.map[country].is_fair():
                                    fairs.append(country)
                        if len(fairs) > 1:
                            distances = []
                            for country in fairs:
                                distances.append((app.countryDistance(tested, country), country))
                            distances.sort()
                            target = distances[0][1]
                        elif len(fairs) == 1:
                            target = fairs[0]
                        else:
                            app.outputToHistory("No Good or Fair countries to worsen Governance in.", True)
                            return
                        if app.map[target].governance_is_better_than(ISLAMIST_RULE):
                            app.map[target].worsenGovernance()
                            app.outputToHistory("Governance worsened in %s." % target, False)
                            app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 107:  # Kurdistan
                if side == "US":
                    app.testCountry("Iraq")
                    app.map["Iraq"].aid += 1
                    app.outputToHistory("Aid added to Iraq.", False)
                    app.outputToHistory(app.map["Iraq"].countryStr(), True)
                else:
                    app.testCountry("Turkey")
                    target = None
                    possibles = []
                    if app.map["Turkey"].governance_is_better_than(POOR):
                        possibles.append("Turkey")
                    if app.map["Iraq"].is_governed() and app.map["Iraq"].governance_is_better_than(POOR):
                        possibles.append("Iraq")
                    if len(possibles) == 0:
                        app.outputToHistory("Iraq and Turkey cannot have governance worsened.", True)
                        return
                    elif len(possibles) == 0:
                        target = possibles[0]
                    else:
                        countryScores = {}
                        for country in possibles:
                            countryScores[country] = 0
                            if app.map[country].aid > 0:
                                countryScores[country] += 10000
                            if app.map[country].besieged > 0:
                                countryScores[country] += 1000
                            countryScores[country] += (app.countryResources(country) * 100)
                            countryScores[country] += random.randint(1,99)
                        countryOrder = []
                        for country in countryScores:
                            countryOrder.append((countryScores[country], (app.map[country].totalCells(True)), country))
                        countryOrder.sort()
                        countryOrder.reverse()
                        target = countryOrder[0][2]
                    app.map[target].worsenGovernance()
                    app.outputToHistory("Governance worsened in %s." % target, False)
                    app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 108:  # Musharraf
                app.removeCell("Pakistan", side)    # 20150131PS added side
                app.map["Pakistan"].make_poor()
                app.map["Pakistan"].make_ally()
                app.outputToHistory("Pakistan now Poor Ally.", False)
                app.outputToHistory(app.map["Pakistan"].countryStr(), True)
            elif self.number == 109:  # Tora Bora
                possibles = []
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if app.map[country].totalCells() >= 2:
                            possibles.append(country)
                target = None
                if len(possibles) == 0:
                    return False
                if len(possibles) == 1:
                    target = possibles[0]
                else:
                    if side == "US":
                        app.outputToHistory("US draws one card.", False)
                        while not target:
                            input = app.getCountryFromUser("Choose a Regime Change country with at least 2 troops. (? for list)?: ",  "XXX", app.listRegimeChangeWithTwoCells)    
                            if input == "":
                                print ""
                            else:
                                if input not in possibles:
                                    print "%s is not a Regime Change country with at least 2 troops." % input
                                    print ""
                                else:
                                    target = input
                    else:
                        app.outputToHistory("Jihadist draws one card.", False)
                        target = random.choice(possibles)
                app.removeCell(target, side)    # 20150131PS added side
                app.removeCell(target, side)    # 20150131PS added side
                prestigeRolls = []
                for i in range(3):
                    prestigeRolls.append(random.randint(1,6))
                presMultiplier = 1
                if prestigeRolls[0] <= 4:
                    presMultiplier = -1
                app.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
            elif self.number == 110:  # Zarqawi
                if side == "US":
                    app.changePrestige(3)
                    app.outputToHistory("Remove card from game.", False)
                else:
                    possibles = []
                    for country in ["Iraq", "Syria", "Lebanon", "Jordan"]:
                        if app.map[country].troops() > 0:
                            possibles.append(country)
                    target = random.choice(possibles)
                    app.placeCells(target, 3)
                    app.map[target].plots += 1
                    app.outputToHistory("Add a Plot 2 to %s." % target, False)
                    app.outputToHistory(app.map[target].countryStr(), True)                
            elif self.number == 111:  # Zawahiri
                if side == "US":
                    app.changeFunding(-2)
                else:
                    if app.numIslamistRule() > 0:
                        app.changePrestige(-3)
                    else:
                        app.changePrestige(-1)
            elif self.number == 112:  # Bin Ladin
                if side == "US":
                    app.changeFunding(-4)
                    app.changePrestige(1)
                    app.outputToHistory("Remove card from game.", False)
                else:
                    if app.numIslamistRule() > 0:
                        app.changePrestige(-4)
                    else:
                        app.changePrestige(-2)
            elif self.number == 113:  # Darfur
                app.testCountry("Sudan")
                if app.prestige >= 7:
                    app.map["Sudan"].aid += 1
                    app.outputToHistory("Aid added to Sudan.", False)
                    if app.map["Sudan"].is_adversary():
                        app.map["Sudan"].make_neutral()
                        app.outputToHistory("Sudan alignment improved.", False)
                    elif app.map["Sudan"].is_neutral():
                        app.map["Sudan"].make_ally()
                        app.outputToHistory("Sudan alignment improved.", False)
                else:
                    app.map["Sudan"].besieged = 1
                    app.outputToHistory("Sudan now Besieged Regime.", False)
                    if app.map["Sudan"].is_ally():
                        app.map["Sudan"].make_neutral()
                        app.outputToHistory("Sudan alignment worsened.", False)
                    elif app.map["Sudan"].is_neutral():
                        app.map["Sudan"].make_adversary()
                        app.outputToHistory("Sudan alignment worsened.", False)
                app.outputToHistory(app.map["Sudan"].countryStr(), True)                
            elif self.number == 114:  # GTMO
                app.lapsing.append("GTMO")
                app.outputToHistory("GTMO in play. No recruit operations or Detainee Release the rest of this turn.", False)
                prestigeRolls = []
                for i in range(3):
                    prestigeRolls.append(random.randint(1,6))
                presMultiplier = 1
                if prestigeRolls[0] <= 4:
                    presMultiplier = -1
                app.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)                                
            elif self.number == 115:  # Hambali
                if side == "US":
                    possibles = ["Indonesia/Malaysia"]
                    targets = []
                    target = None
                    for countryObj in app.map["Indonesia/Malaysia"].links:
                        possibles.append(countryObj.name)
                    for country in possibles:
                        if app.map[country].totalCells(True) > 0:
                            if app.map[country].type == "Non-Muslim":
                                if app.map[country].posture == "Hard":
                                    targets.append(country)
                            else:
                                if app.map[country].is_ally():
                                    targets.append(country)
                    if len(targets) == 1:
                        target = targets[0]
                    else:
                        while not target:
                            input = app.getCountryFromUser("Choose Indonesia or an adjacent country that has a cell and is Ally or Hard. (? for list)?: ",  "XXX", app.listHambali)    
                            if input == "":
                                print ""
                            else:
                                if input not in targets:
                                    print "%s is not Indonesia or an adjacent country that has a cell and is Ally or Hard." % input
                                    print ""
                                else:
                                    target = input
                    app.removeCell(target, side)    # 20150131PS added side
                    app.outputToHistory("US draw 2 cards.", False)
                else:
                    possibles = ["Indonesia/Malaysia"]
                    targets = []
                    target = None
                    for countryObj in app.map["Indonesia/Malaysia"].links:
                        possibles.append(countryObj.name)
                    for country in possibles:
                        if app.map[country].totalCells(True) > 0:
                            if app.map[country].type == "Non-Muslim":
                                if app.map[country].posture == "Hard":
                                    targets.append(country)
                            else:
                                if app.map[country].is_ally():
                                    targets.append(country)
                    target = random.choice(targets)
                    app.map[target].plots += 1
                    app.outputToHistory("Place an plot in %s." % target, True)
            elif self.number == 116:  # KSM
                if side == "US":
                    for country in app.map:
                        if app.map[country].plots > 0:
                            if app.map[country].is_ally() or app.map[country].type == "Non-Muslim":
                                numPlots = app.map[country].plots
                                app.map[country].plots = 0
                                app.outputToHistory("%d Plots removed from %s." % (numPlots, country), False)
                    app.outputToHistory("US draws 2 cards.", True)
                else:
                    if app.executePlot(1, False, [1], False, False, True) == 1:
                        app.outputToHistory("No plots could be placed.", True)
            elif self.number == 117 or self.number == 118:  # Oil Price Spike
                app.lapsing.append("Oil Price Spike")
                app.outputToHistory("Oil Price Spike in play. Add +1 to the resources of each Oil Exporter country for the turn.", False)
                if side == "US":
                    app.outputToHistory("Select, reveal, and draw a card other than Oil Price Spike from the discard pile or a box.", True)
                else:
                    if app.getYesNoFromUser("Are there any Jihadist event cards in the discard pile? "):
                        app.outputToHistory("Draw from the Discard Pile randomly among the highest-value Jihadist-associated event cards. Put the card on top of the Jihadist hand.", True)
            elif self.number == 119:  # Saleh
                app.testCountry("Yemen")
                if side == "US":
                    if not app.map["Yemen"].is_islamist_rule():
                        if app.map["Yemen"].is_adversary():
                            app.map["Yemen"].make_neutral()
                        elif app.map["Yemen"].is_neutral():
                            app.map["Yemen"].make_ally()
                        app.outputToHistory("Yemen Alignment improved to %s." % app.map["Yemen"].alignment(), False)
                        app.map["Yemen"].aid += 1
                        app.outputToHistory("Aid added to Yemen.", True)
                else:
                    if app.map["Yemen"].is_ally():
                        app.map["Yemen"].make_neutral()
                    elif app.map["Yemen"].is_neutral():
                        app.map["Yemen"].make_adversary()
                    app.outputToHistory("Yemen Alignment worsened to %s." % app.map["Yemen"].alignment(), False)
                    app.map["Yemen"].besieged = 1
                    app.outputToHistory("Yemen now Besieged Regime.", True)
            elif self.number == 120:  # US Election
                app.executeCardUSElection(random.randint(1,6))
        if self.remove:
            app.outputToHistory("Remove card from game.", True)
        if self.mark:
            app.outputToHistory("Place marker for card.", True)
        if self.lapsing:
            app.outputToHistory("Place card in Lapsing.", True)


class Labyrinth(cmd.Cmd):

    map = {}
    undo = False
    rollturn = -1
    scenario = 0
    ideology = 0
    prestige = 0
    troops = 0
    cells = 0
    funding = 0
    startYear = 0
    turn = 0
    uCard = 0
    jCard = 0
    phase = ""
    markers = []
    lapsing = []
    history = []
    validGlobalMarkers = [] # 20150131PS
    validCountryMarkers = [] # 20150131PS
    validLapsingMarkers = [] #20150131PS
    whichPlayer = ""    #20150131PS
    deck = {}
    gameOver = False
    backlashInPlay = False
    testUserInput = []

    def __init__(self, scenario, ideology, setup_function = None, test_user_input=[], **kwargs):
        cmd.Cmd.__init__(self)
        self.scenario = scenario
        self.ideology = ideology
        self.prestige = 0
        self.troops = 0
        self.cells = 0
        self.funding = 0
        self.startYear = 0
        self.turn = 1
        self.uCard = 1
        self.jCard = 1
        self.phase = ""
        self.map = {}
        self.mapSetup()
        self.history = []
        self.markers = []
        self.lapsing = []
        self.validGlobalMarkers = []
        self.validCountryMarkers = []
        self.validLapsingMarkers = []
        self.whichPlayer= ""
        self.testUserInput = test_user_input
        self.randomizer = kwargs.get('randomizer', Randomizer())
        if setup_function:
            setup_function(self)
        else:
            self.scenarioSetup()
        self.prompt = "Command: "
        self.gameOver = False
        self.backlashInPlay = False

        if self.scenario == 1:
            self.outputToHistory("Scenario: Let's Roll!", False)
        elif self.scenario == 2:
            self.outputToHistory("Scenario: You Can Call Me Al", False)
        elif self.scenario == 3:
            self.outputToHistory("Scenario: Anaconda", False)
        elif self.scenario == 4:
            self.outputToHistory("Scenario: Mission Accomplished?", False)

        if self.ideology == 1:
            self.outputToHistory("Jihadist Ideology: Normal", False)
        elif self.ideology == 2:
            self.outputToHistory("Jihadist Ideology: Coherent", False)
        elif self.ideology == 3:
            self.outputToHistory("Jihadist Ideology: Attractive", False)
        elif self.ideology == 4:
            self.outputToHistory("Jihadist Ideology: Potent", False)
        elif self.ideology == 5:    # 20150131PS - should be 5
            self.outputToHistory("Jihadist Ideology: Infectious", False)
        elif self.ideology == 6:
            self.outputToHistory("Jihadist Ideology: Virulent", False)
        
        print ""
        
        self.outputToHistory("Game Start")
        self.outputToHistory("")
        self.outputToHistory("[[ %d (Turn %s) ]]" % (self.startYear + (self.turn - 1), self.turn), True)
        self.deck = {}
        self.deckSetup()
        self.validMarkersSetup() # 20150131PS - added
        
    def postcmd(self, stop, line):
        
        self.Save(SUSPEND_FILE)

        if line == "quit":
            return True

        if self.undo:
            return True
            
        if self.rollturn >= 0:
            return True

    # Cells test
        cellCount = 0
        for country in self.map:
            cellCount += self.map[country].sleeperCells
            cellCount += self.map[country].activeCells
        cellCount += self.cells
        if cellCount != 15:
            print "DEBUG: CELL COUNT %d" % cellCount
    # Troops test
        troopCount = 0
        for country in self.map:
            troopCount += self.map[country].troops()
        troopCount += self.troops
        if troopCount != 15:
            print "DEBUG: TROOP COUNT %d" % troopCount
    # Countries tested test
        for country in self.map:
            badCountry = False
            if (self.map[country].sleeperCells > 0) or (self.map[country].activeCells > 0) or (self.map[country].troopCubes > 0) or (self.map[country].aid > 0) or (self.map[country].regimeChange > 0) or (self.map[country].cadre > 0) or (self.map[country].plots > 0):
                if self.map[country].is_ungoverned():
                    badCountry = True
                if self.map[country].type == "Non-Muslim":
                    if self.map[country].posture == "":
                        badCountry = True
                elif self.map[country].type != "Iran":
                    if self.map[country].is_unaligned():
                        badCountry = True
            if badCountry:
                print "DEBUG: UNTESTED COUNTRY"
                self.map[country].printCountry()
                
    def emptyline(self):
        print "%d (Turn %s)" % (self.startYear + (self.turn - 1), self.turn)
        print ""
            
    @staticmethod
    def debugPrint(str):
        return
        # print str
        
    def outputToHistory(self, output, lineFeed = True):
        print output
        self.history.append(output)
        if lineFeed:
            print ""
        
    def mapSetup(self):
        self.map["Canada"] = Country(self, "Canada", "Non-Muslim", "", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["United States"] = Country(self, "United States", "Non-Muslim", "Hard", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["United Kingdom"] = Country(self, "United Kingdom", "Non-Muslim", "", GOOD, False, 3, 0, 0, 0, False, 0)
        self.map["Serbia"] = Country(self, "Serbia", "Non-Muslim", "", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["Israel"] = Country(self, "Israel", "Non-Muslim", "Hard", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["India"] = Country(self, "India", "Non-Muslim", "", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["Scandinavia"] = Country(self, "Scandinavia", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["Eastern Europe"] = Country(self, "Eastern Europe", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["Benelux"] = Country(self, "Benelux", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["Germany"] = Country(self, "Germany", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["France"] = Country(self, "France", "Non-Muslim", "", GOOD, True, 2, 0, 0, 0, False, 0)
        self.map["Italy"] = Country(self, "Italy", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["Spain"] = Country(self, "Spain", "Non-Muslim", "", GOOD, True, 2, 0, 0, 0, False, 0)
        self.map["Russia"] = Country(self, "Russia", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["Caucasus"] = Country(self, "Caucasus", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["China"] = Country(self, "China", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["Kenya/Tanzania"] = Country(self, "Kenya/Tanzania", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["Thailand"] = Country(self, "Thailand", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["Philippines"] = Country(self, "Philippines", "Non-Muslim", "", FAIR, False, 3, 0, 0, 0, False, 0)
        self.map["Morocco"] = Country(self, "Morocco", "Suni", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Algeria/Tunisia"] = Country(self, "Algeria/Tunisia", "Suni", "", None, False, 0, 0, 0, 0, True, 2)
        self.map["Libya"] = Country(self, "Libya", "Suni", "", None, False, 0, 0, 0, 0, True, 1)
        self.map["Egypt"] = Country(self, "Egypt", "Suni", "", None, False, 0, 0, 0, 0, False, 3)
        self.map["Sudan"] = Country(self, "Sudan", "Suni", "", None, False, 0, 0, 0, 0, True, 1)
        self.map["Somalia"] = Country(self, "Somalia", "Suni", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Jordan"] = Country(self, "Jordan", "Suni", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Syria"] = Country(self, "Syria", "Suni", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Central Asia"] = Country(self, "Central Asia", "Suni", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Indonesia/Malaysia"] = Country(self, "Indonesia/Malaysia", "Suni", "", None, False, 0, 0, 0, 0, True, 3)
        self.map["Turkey"] = Country(self, "Turkey", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Lebanon"] = Country(self, "Lebanon", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Yemen"] = Country(self, "Yemen", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Iraq"] = Country(self, "Iraq", "Shia-Mix", "", None, False, 0, 0, 0, 0, True, 3)
        self.map["Saudi Arabia"] = Country(self, "Saudi Arabia", "Shia-Mix", "", None, False, 0, 2, 0, 0, True, 3)
        self.map["Gulf States"] = Country(self, "Gulf States", "Shia-Mix", "", None, False, 0, 2, 0, 0, True, 3)
        self.map["Pakistan"] = Country(self, "Pakistan", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Afghanistan"] = Country(self, "Afghanistan", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Iran"] = Country(self, "Iran", "Iran", None, FAIR, False, 0, 0, 0, 0, False, 0)
    
        # Canada
        self.map["Canada"].links.append(self.map["United States"])
        self.map["Canada"].links.append(self.map["United Kingdom"])
        self.map["Canada"].schengenLink = True
        # United States
        self.map["United States"].links.append(self.map["Canada"])
        self.map["United States"].links.append(self.map["United Kingdom"])
        self.map["United States"].links.append(self.map["Philippines"])
        self.map["United States"].schengenLink = True
        # United Kingdom
        self.map["United Kingdom"].links.append(self.map["Canada"])
        self.map["United Kingdom"].links.append(self.map["United States"])
        self.map["United Kingdom"].schengenLink = True
        # Serbia
        self.map["Serbia"].links.append(self.map["Russia"])
        self.map["Serbia"].links.append(self.map["Turkey"])
        self.map["Serbia"].schengenLink = True
        # Israel
        self.map["Israel"].links.append(self.map["Lebanon"])
        self.map["Israel"].links.append(self.map["Jordan"])
        self.map["Israel"].links.append(self.map["Egypt"])
        # India
        self.map["India"].links.append(self.map["Pakistan"])
        self.map["India"].links.append(self.map["Indonesia/Malaysia"])
        # Russia
        self.map["Russia"].links.append(self.map["Serbia"])
        self.map["Russia"].links.append(self.map["Turkey"])
        self.map["Russia"].links.append(self.map["Caucasus"])
        self.map["Russia"].links.append(self.map["Central Asia"])
        self.map["Russia"].schengenLink = True
        # Caucasus
        self.map["Caucasus"].links.append(self.map["Russia"])
        self.map["Caucasus"].links.append(self.map["Turkey"])
        self.map["Caucasus"].links.append(self.map["Iran"])
        self.map["Caucasus"].links.append(self.map["Central Asia"])
        # China
        self.map["China"].links.append(self.map["Central Asia"])
        self.map["China"].links.append(self.map["Thailand"])
        # Kenya/Tanzania
        self.map["Kenya/Tanzania"].links.append(self.map["Sudan"])
        self.map["Kenya/Tanzania"].links.append(self.map["Somalia"])
        # Thailand
        self.map["Thailand"].links.append(self.map["China"])
        self.map["Thailand"].links.append(self.map["Philippines"])
        self.map["Thailand"].links.append(self.map["Indonesia/Malaysia"])
        # Philippines
        self.map["Philippines"].links.append(self.map["United States"])
        self.map["Philippines"].links.append(self.map["Thailand"])
        self.map["Philippines"].links.append(self.map["Indonesia/Malaysia"])
        # Morocco
        self.map["Morocco"].links.append(self.map["Algeria/Tunisia"])
        self.map["Morocco"].schengenLink = True
        # Algeria/Tunisia
        self.map["Algeria/Tunisia"].links.append(self.map["Morocco"])
        self.map["Algeria/Tunisia"].links.append(self.map["Libya"])
        self.map["Algeria/Tunisia"].schengenLink = True
        # Libya
        self.map["Libya"].links.append(self.map["Algeria/Tunisia"])
        self.map["Libya"].links.append(self.map["Egypt"])
        self.map["Libya"].links.append(self.map["Sudan"])
        self.map["Libya"].schengenLink = True
        # Egypt
        self.map["Egypt"].links.append(self.map["Libya"])
        self.map["Egypt"].links.append(self.map["Israel"])
        self.map["Egypt"].links.append(self.map["Sudan"])
        # Sudan
        self.map["Sudan"].links.append(self.map["Libya"])
        self.map["Sudan"].links.append(self.map["Egypt"])
        self.map["Sudan"].links.append(self.map["Kenya/Tanzania"])
        self.map["Sudan"].links.append(self.map["Somalia"])
        # Somalia
        self.map["Somalia"].links.append(self.map["Sudan"])
        self.map["Somalia"].links.append(self.map["Kenya/Tanzania"])
        self.map["Somalia"].links.append(self.map["Yemen"])
        # Jordan
        self.map["Jordan"].links.append(self.map["Israel"])
        self.map["Jordan"].links.append(self.map["Syria"])
        self.map["Jordan"].links.append(self.map["Iraq"])
        self.map["Jordan"].links.append(self.map["Saudi Arabia"])
        # Syria
        self.map["Syria"].links.append(self.map["Turkey"])
        self.map["Syria"].links.append(self.map["Lebanon"])
        self.map["Syria"].links.append(self.map["Jordan"])
        self.map["Syria"].links.append(self.map["Iraq"])
        # Central Asia
        self.map["Central Asia"].links.append(self.map["Russia"])
        self.map["Central Asia"].links.append(self.map["Caucasus"])
        self.map["Central Asia"].links.append(self.map["Iran"])
        self.map["Central Asia"].links.append(self.map["Afghanistan"])
        self.map["Central Asia"].links.append(self.map["China"])
        # Indonesia/Malaysia
        self.map["Indonesia/Malaysia"].links.append(self.map["Thailand"])
        self.map["Indonesia/Malaysia"].links.append(self.map["India"])
        self.map["Indonesia/Malaysia"].links.append(self.map["Philippines"])
        self.map["Indonesia/Malaysia"].links.append(self.map["Pakistan"])
        # Turkey
        self.map["Turkey"].links.append(self.map["Serbia"])
        self.map["Turkey"].links.append(self.map["Russia"])
        self.map["Turkey"].links.append(self.map["Caucasus"])
        self.map["Turkey"].links.append(self.map["Iran"])
        self.map["Turkey"].links.append(self.map["Syria"])
        self.map["Turkey"].links.append(self.map["Iraq"])
        self.map["Turkey"].schengenLink = True
        # Lebanon
        self.map["Lebanon"].links.append(self.map["Syria"])
        self.map["Lebanon"].links.append(self.map["Israel"])
        self.map["Lebanon"].schengenLink = True
        # Yemen
        self.map["Yemen"].links.append(self.map["Saudi Arabia"])
        self.map["Yemen"].links.append(self.map["Somalia"])
        # Iraq
        self.map["Iraq"].links.append(self.map["Syria"])
        self.map["Iraq"].links.append(self.map["Turkey"])
        self.map["Iraq"].links.append(self.map["Iran"])
        self.map["Iraq"].links.append(self.map["Gulf States"])
        self.map["Iraq"].links.append(self.map["Saudi Arabia"])
        self.map["Iraq"].links.append(self.map["Jordan"])
        # Saudi Arabia
        self.map["Saudi Arabia"].links.append(self.map["Jordan"])
        self.map["Saudi Arabia"].links.append(self.map["Iraq"])
        self.map["Saudi Arabia"].links.append(self.map["Gulf States"])
        self.map["Saudi Arabia"].links.append(self.map["Yemen"])
        # Gulf States
        self.map["Gulf States"].links.append(self.map["Iran"])
        self.map["Gulf States"].links.append(self.map["Pakistan"])
        self.map["Gulf States"].links.append(self.map["Saudi Arabia"])
        self.map["Gulf States"].links.append(self.map["Iraq"])
        # Pakistan
        self.map["Pakistan"].links.append(self.map["Iran"])
        self.map["Pakistan"].links.append(self.map["Afghanistan"])
        self.map["Pakistan"].links.append(self.map["India"])
        self.map["Pakistan"].links.append(self.map["Gulf States"])
        self.map["Pakistan"].links.append(self.map["Indonesia/Malaysia"])
        # Afghanistan
        self.map["Afghanistan"].links.append(self.map["Central Asia"])
        self.map["Afghanistan"].links.append(self.map["Pakistan"])
        self.map["Afghanistan"].links.append(self.map["Iran"])
        # Iran
        self.map["Iran"].links.append(self.map["Central Asia"])
        self.map["Iran"].links.append(self.map["Afghanistan"])
        self.map["Iran"].links.append(self.map["Pakistan"])
        self.map["Iran"].links.append(self.map["Gulf States"])
        self.map["Iran"].links.append(self.map["Iraq"])
        self.map["Iran"].links.append(self.map["Turkey"])
        self.map["Iran"].links.append(self.map["Caucasus"])
        
    def scenarioSetup(self):
        if self.scenario == 1 or self.scenario == 2:  # Let's Roll
            self.startYear = 2001
            self.turn = 1
            self.prestige = 7
            self.troops = 11
            self.funding = 9
            self.cells = 11
            self.phase = "Jihadist Action Phase"
            self.map["Libya"].make_poor()
            self.map["Libya"].make_adversary()
            self.map["Syria"].make_fair()
            self.map["Syria"].make_adversary()
            self.map["Iraq"].make_poor()
            self.map["Iraq"].make_adversary()
            self.map["Saudi Arabia"].make_poor()
            self.map["Saudi Arabia"].make_ally()
            self.map["Saudi Arabia"].troopCubes = 2
            self.map["Gulf States"].make_fair()
            self.map["Gulf States"].make_ally()
            self.map["Gulf States"].troopCubes = 2
            self.map["Pakistan"].make_fair()
            self.map["Pakistan"].make_neutral()
            self.map["Afghanistan"].make_islamist_rule()
            self.map["Afghanistan"].make_adversary()
            self.map["Afghanistan"].sleeperCells = 4
            self.map["Somalia"].besieged = 1
            if self.scenario == 1:
                self.map["United States"].posture = "Hard"
            else:
                self.map["United States"].posture = "Soft"    
                print "Remove the card Axis of Evil from the game."
                print ""
        elif self.scenario == 3:
            self.startYear = 2002
            self.turn = 1
            self.prestige = 8
            self.troops = 5
            self.funding = 6
            self.cells = 13
            self.map["Libya"].make_poor()
            self.map["Libya"].make_adversary()
            self.map["Syria"].make_fair()
            self.map["Syria"].make_adversary()
            self.map["Iraq"].make_poor()
            self.map["Iraq"].make_adversary()
            self.map["Saudi Arabia"].make_poor()
            self.map["Saudi Arabia"].make_ally()
            self.map["Saudi Arabia"].troopCubes = 2
            self.map["Gulf States"].make_fair()
            self.map["Gulf States"].make_ally()
            self.map["Gulf States"].troopCubes = 2
            self.map["Pakistan"].make_poor()
            self.map["Pakistan"].make_ally()
            self.map["Pakistan"].sleeperCells = 1
            self.map["Pakistan"].markers.append("FATA")
            self.map["Afghanistan"].make_poor()
            self.map["Afghanistan"].make_ally()
            self.map["Afghanistan"].sleeperCells = 1
            self.map["Afghanistan"].troopCubes = 6
            self.map["Afghanistan"].regimeChange = 1
            self.map["Somalia"].besieged = 1
            self.map["Central Asia"].make_poor()
            self.map["Central Asia"].make_ally()
            self.markers.append("Patriot Act")
            possibles = []
            for country in self.map:
                if country != "United States":
                    possibles.append(country)
            random.shuffle(possibles)
            for i in range(3):
                self.testCountry(possibles[i])
                self.placeCells(possibles[i], 1)
            print "Remove the cards Patriot Act and Tora Bora from the game."
            print ""
        elif self.scenario == 4:
            self.startYear = 2003
            self.turn = 1
            self.prestige = 3
            self.troops = 0
            self.funding = 5
            self.cells = 5
            self.map["Libya"].make_poor()
            self.map["Libya"].make_adversary()
            self.map["Syria"].make_fair()
            self.map["Syria"].make_adversary()
            self.map["Syria"].sleeperCells = 1
            self.map["Iraq"].make_poor()
            self.map["Iraq"].make_ally()
            self.map["Iraq"].troopCubes = 6
            self.map["Iraq"].sleeperCells = 3
            self.map["Iraq"].regimeChange = 1
            self.map["Iran"].sleeperCells = 1
            self.map["Saudi Arabia"].make_poor()
            self.map["Saudi Arabia"].make_ally()
            self.map["Saudi Arabia"].sleeperCells = 1
            self.map["Gulf States"].make_fair()
            self.map["Gulf States"].make_ally()
            self.map["Gulf States"].troopCubes = 2
            self.map["Pakistan"].make_fair()
            self.map["Pakistan"].make_ally()
            self.map["Pakistan"].sleeperCells = 1
            self.map["Pakistan"].markers.append("FATA")
            self.map["Afghanistan"].make_poor()
            self.map["Afghanistan"].make_ally()
            self.map["Afghanistan"].sleeperCells = 1
            self.map["Afghanistan"].troopCubes = 5
            self.map["Afghanistan"].regimeChange = 1
            self.map["Somalia"].besieged = 1
            self.map["Central Asia"].make_fair()
            self.map["Central Asia"].make_neutral()
            self.map["Indonesia/Malaysia"].make_fair()
            self.map["Indonesia/Malaysia"].make_neutral()
            self.map["Indonesia/Malaysia"].sleeperCells = 1
            self.map["Philippines"].posture = "Soft"
            self.map["Philippines"].troopCubes = 2
            self.map["Philippines"].sleeperCells = 1
            self.map["United Kingdom"].posture = "Hard"
            self.markers.append("Abu Sayyaf")
            self.markers.append("Patriot Act")
            self.markers.append("NEST")
            self.markers.append("Enhanced Measures")
            self.markers.append("Renditions")
            self.markers.append("Wiretapping")
            possibles = []
            for country in self.map:
                if self.map[country].schengen:
                    self.testCountry(country)
            print ""
            print "Remove the cards Patriot Act, Tora Bora, NEST, Abu Sayyaf, KSM and Iraqi WMD from the game."
            print ""
        goodRes = 0
        islamRes = 0
        goodC = 0
        islamC = 0
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni": 
                if self.map[country].is_good():
                    goodC += 1
                    goodRes += self.countryResources(country)
                elif self.map[country].is_fair():
                    goodC += 1
                elif self.map[country].is_poor():
                    islamC += 1
                elif self.map[country].is_islamist_rule():
                    islamC += 1
                    islamRes += self.countryResources(country)
            elif self.map[country].type != "Iran" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        print "Good Resources   : %d" % goodRes
        print "Islamist Resources: %d" % islamRes
        print "---"
        print "Good/Fair Countries   : %d" % goodC
        print "Poor/Islamist Countries: %d" % islamC
        print ""
        print "GWOT"
        print "US Posture: %s" % self.map["United States"].posture
        if worldPos > 0:
            worldPosStr = "Hard"
        elif worldPos < 0:
            worldPosStr = "Soft"
        else:
            worldPosStr = "Even"
        print "World Posture: %s %d" % (worldPosStr, abs(worldPos))
        print "US Prestige: %d" % self.prestige
        print ""
            
    
    def testScenarioSetup(self):
        if self.scenario == 1 or self.scenario == 2:  # Let's Roll
            self.startYear = 2001
            self.turn = 1
            self.prestige = 7
            self.troops = 11
            self.funding = 9
            self.cells = 11
            self.phase = "Jihadist Action Phase"
            self.map["France"].posture = "Hard"
            self.map["France"].cadre = 1
            self.map["Spain"].posture = "Soft"
            self.map["Spain"].sleeperCells = 1
            self.map["Germany"].posture = "Hard"
            self.map["Germany"].activeCells = 1
            self.map["Germany"].sleeperCells = 1
            self.map["United States"].plots = 1
            self.map["Libya"].make_poor()
            self.map["Libya"].make_adversary()
            self.map["Syria"].make_fair()
            self.map["Syria"].make_adversary()
            self.map["Iraq"].make_poor()
            self.map["Iraq"].make_adversary()
            self.map["Iraq"].plots = 2
            self.map["Saudi Arabia"].make_poor()
            self.map["Saudi Arabia"].make_ally()
            self.map["Saudi Arabia"].troopCubes = 2
            self.map["Pakistan"].make_poor()
            self.map["Pakistan"].make_ally()
            self.map["Pakistan"].troopCubes = 2
            self.map["Pakistan"].activeCells = 4
            self.map["Gulf States"].make_poor()
            self.map["Gulf States"].make_ally()
            self.map["Gulf States"].troopCubes = 2
            self.map["Gulf States"].sleeperCells = 10
            self.map["Gulf States"].activeCells = 4
            self.map["Pakistan"].make_fair()
            self.map["Pakistan"].make_neutral()
            self.map["Afghanistan"].make_islamist_rule()
            self.map["Afghanistan"].make_adversary()
            self.map["Afghanistan"].sleeperCells = 4
            self.map["Somalia"].besieged = 1
            if self.scenario == 1:
                self.map["United States"].posture = "Hard"
            else:
                self.map["United States"].posture = "Soft"        
                
    def deckSetup(self):
        self.deck["1"] = Card(1,"US","Backlash",1,False,False,False)
        self.deck["2"] = Card(2,"US","Biometrics",1,False,False,True)
        self.deck["3"] = Card(3,"US","CTR",1,False,True,False)
        self.deck["4"] = Card(4,"US","Moro Talks",1,True,True,False)
        self.deck["5"] = Card(5,"US","NEST",1,True,True,False)
        self.deck["6"] = Card(6,"US","Sanctions",1,False,False,False)
        self.deck["7"] = Card(7,"US","Sanctions",1,False,False,False)
        self.deck["8"] = Card(8,"US","Special Forces",1,False,False,False)
        self.deck["9"] = Card(9,"US","Special Forces",1,False,False,False)
        self.deck["10"] = Card(10,"US","Special Forces",1,False,False,False)
        self.deck["11"] = Card(11,"US","Abbas",2,True,True,False)
        self.deck["12"] = Card(12,"US","Al-Azhar",2,False,False,False)
        self.deck["13"] = Card(13,"US","Anbar Awakening",2,False,True,False)
        self.deck["14"] = Card(14,"US","Covert Action",2,False,False,False)
        self.deck["15"] = Card(15,"US","Ethiopia Strikes",2,True,False,False)
        self.deck["16"] = Card(16,"US","Euro-Islam",2,True,False,False)
        self.deck["17"] = Card(17,"US","FSB",2,False,False,False)
        self.deck["18"] = Card(18,"US","Intel Community",2,False,False,False)
        self.deck["19"] = Card(19,"US","Kemalist Republic",2,False,False,False)
        self.deck["20"] = Card(20,"US","King Abdullah",2,True,False,False)
        self.deck["21"] = Card(21,"US","Let's Roll",2,False,False,False)
        self.deck["22"] = Card(22,"US","Mossad and Shin Bet",2,False,False,False)
        self.deck["23"] = Card(23,"US","Predator",2,False,False,False)
        self.deck["24"] = Card(24,"US","Predator",2,False,False,False)
        self.deck["25"] = Card(25,"US","Predator",2,False,False,False)
        self.deck["26"] = Card(26,"US","Quartet",2,False,False,False)
        self.deck["27"] = Card(27,"US","Sadam Captured",2,True,True,False)
        self.deck["28"] = Card(28,"US","Sharia",2,False,False,False)
        self.deck["29"] = Card(29,"US","Tony Blair",2,True,False,False)
        self.deck["30"] = Card(30,"US","UN Nation Building",2,False,False,False)
        self.deck["31"] = Card(31,"US","Wiretapping",2,False,True,False)
        self.deck["32"] = Card(32,"US","Back Channel",3,False,False,False)
        self.deck["33"] = Card(33,"US","Benazir Bhutto",3,True,True,False)
        self.deck["34"] = Card(34,"US","Enhanced Measures",3,False,True,False)
        self.deck["35"] = Card(35,"US","Hijab",3,True,False,False)
        self.deck["36"] = Card(36,"US","Indo-Pakistani Talks",3,True,True,False)
        self.deck["37"] = Card(37,"US","Iraqi WMD",3,True,True,False)
        self.deck["38"] = Card(38,"US","Libyan Deal",3,True,True,False)
        self.deck["39"] = Card(39,"US","Libyan WMD",3,True,True,False)
        self.deck["40"] = Card(40,"US","Mass Turnout",3,False,False,False)
        self.deck["41"] = Card(41,"US","NATO",3,False,True,False)
        self.deck["42"] = Card(42,"US","Pakistani Offensive",3,False,False,False)
        self.deck["43"] = Card(43,"US","Patriot Act",3,True,True,False)
        self.deck["44"] = Card(44,"US","Renditions",3,False,True,False)
        self.deck["45"] = Card(45,"US","Safer Now",3,False,False,False)
        self.deck["46"] = Card(46,"US","Sistani",3,False,False,False)
        self.deck["47"] = Card(47,"US","The door of Itjihad was closed",3,False,False,True)
        self.deck["48"] = Card(48,"Jihadist","Adam Gadahn",1,False,False,False)
        self.deck["49"] = Card(49,"Jihadist","Al-Ittihad al-Islami",1,True,False,False)
        self.deck["50"] = Card(50,"Jihadist","Ansar al-Islam",1,True,False,False)
        self.deck["51"] = Card(51,"Jihadist","FREs",1,False,False,False)
        self.deck["52"] = Card(52,"Jihadist","IEDs",1,False,False,False)
        self.deck["53"] = Card(53,"Jihadist","Madrassas",1,False,False,False)
        self.deck["54"] = Card(54,"Jihadist","Moqtada al-Sadr",1,True,True,False)
        self.deck["55"] = Card(55,"Jihadist","Uyghur Jihad",1,True,False,False)
        self.deck["56"] = Card(56,"Jihadist","Vieira de Mello Slain",1,True,True,False)
        self.deck["57"] = Card(57,"Jihadist","Abu Sayyaf",2,True,True,False)
        self.deck["58"] = Card(58,"Jihadist","Al-Anbar",2,True,True,False)
        self.deck["59"] = Card(59,"Jihadist","Amerithrax",2,False,False,False)
        self.deck["60"] = Card(60,"Jihadist","Bhutto Shot",2,True,True,False)
        self.deck["61"] = Card(61,"Jihadist","Detainee Release",2,False,False,False)
        self.deck["62"] = Card(62,"Jihadist","Ex-KGB",2,False,False,False)
        self.deck["63"] = Card(63,"Jihadist","Gaza War",2,False,False,False)
        self.deck["64"] = Card(64,"Jihadist","Hariri Killed",2,True,False,False)
        self.deck["65"] = Card(65,"Jihadist","HEU",2,True,False,False)
        self.deck["66"] = Card(66,"Jihadist","Homegrown",2,False,False,False)
        self.deck["67"] = Card(67,"Jihadist","Islamic Jihad Union",2,True,False,False)
        self.deck["68"] = Card(68,"Jihadist","Jemaah Islamiya",2,False,False,False)
        self.deck["69"] = Card(69,"Jihadist","Kazakh Strain",2,True,False,False)
        self.deck["70"] = Card(70,"Jihadist","Lashkar-e-Tayyiba",2,False,False,False)
        self.deck["71"] = Card(71,"Jihadist","Loose Nuke",2,True,False,False)
        self.deck["72"] = Card(72,"Jihadist","Opium",2,False,False,False)
        self.deck["73"] = Card(73,"Jihadist","Pirates",2,True,True,False)
        self.deck["74"] = Card(74,"Jihadist","Schengen Visas",2,False,False,False)
        self.deck["75"] = Card(75,"Jihadist","Schroeder & Chirac",2,True,False,False)
        self.deck["76"] = Card(76,"Jihadist","Abu Ghurayb",3,True,False,False)
        self.deck["77"] = Card(77,"Jihadist","Al Jazeera",3,False,False,False)
        self.deck["78"] = Card(78,"Jihadist","Axis of Evil",3,False,False,False)
        self.deck["79"] = Card(79,"Jihadist","Clean Operatives",3,False,False,False)
        self.deck["80"] = Card(80,"Jihadist","FATA",3,False,True,False)
        self.deck["81"] = Card(81,"Jihadist","Foreign Fighters",3,False,False,False)
        self.deck["82"] = Card(82,"Jihadist","Jihadist Videos",3,False,False,False)
        self.deck["83"] = Card(83,"Jihadist","Kashmir",3,False,False,False)
        self.deck["84"] = Card(84,"Jihadist","Leak",3,False,False,False)
        self.deck["85"] = Card(85,"Jihadist","Leak",3,False,False,False)
        self.deck["86"] = Card(86,"Jihadist","Lebanon War",3,False,False,False)
        self.deck["87"] = Card(87,"Jihadist","Martyrdom Operation",3,False,False,False)
        self.deck["88"] = Card(88,"Jihadist","Martyrdom Operation",3,False,False,False)
        self.deck["89"] = Card(89,"Jihadist","Martyrdom Operation",3,False,False,False)
        self.deck["90"] = Card(90,"Jihadist","Quagmire",3,False,False,False)
        self.deck["91"] = Card(91,"Jihadist","Regional al-Qaeda",3,False,False,False)
        self.deck["92"] = Card(92,"Jihadist","Saddam",3,False,False,False)
        self.deck["93"] = Card(93,"Jihadist","Taliban",3,False,False,False)
        self.deck["94"] = Card(94,"Jihadist","The door of Itjihad was closed",3,False,False,False)
        self.deck["95"] = Card(95,"Jihadist","Wahhabism",3,False,False,False)
        self.deck["96"] = Card(96,"Unassociated","Danish Cartoons",1,True,False,False)
        self.deck["97"] = Card(97,"Unassociated","Fatwa",1,False,False,False)
        self.deck["98"] = Card(98,"Unassociated","Gaza Withdrawal",1,True,False,False)
        self.deck["99"] = Card(99,"Unassociated","HAMAS Elected",1,True,False,False)
        self.deck["100"] = Card(100,"Unassociated","Hizb Ut-Tahrir",1,False,False,False)
        self.deck["101"] = Card(101,"Unassociated","Kosovo",1,False,False,False)
        self.deck["102"] = Card(102,"Unassociated","Former Soviet Union",2,False,False,False)
        self.deck["103"] = Card(103,"Unassociated","Hizballah",2,False,False,False)
        self.deck["104"] = Card(104,"Unassociated","Iran",2,False,False,False)
        self.deck["105"] = Card(105,"Unassociated","Iran",2,False,False,False)
        self.deck["106"] = Card(106,"Unassociated","Jaysh al-Mahdi",2,False,False,False)
        self.deck["107"] = Card(107,"Unassociated","Kurdistan",2,False,False,False)
        self.deck["108"] = Card(108,"Unassociated","Musharraf",2,False,False,False)
        self.deck["109"] = Card(109,"Unassociated","Tora Bora",2,True,False,False)
        self.deck["110"] = Card(110,"Unassociated","Zarqawi",2,False,False,False)
        self.deck["111"] = Card(111,"Unassociated","Zawahiri",2,False,False,False)
        self.deck["112"] = Card(112,"Unassociated","Bin Ladin",3,False,False,False)
        self.deck["113"] = Card(113,"Unassociated","Darfur",3,False,False,False)
        self.deck["114"] = Card(114,"Unassociated","GTMO",3,False,False,True)
        self.deck["115"] = Card(115,"Unassociated","Hambali",3,False,False,False)
        self.deck["116"] = Card(116,"Unassociated","KSM",3,False,False,False)
        self.deck["117"] = Card(117,"Unassociated","Oil Price Spike",3,False,False,True)
        self.deck["118"] = Card(118,"Unassociated","Oil Price Spike",3,False,False,True)
        self.deck["119"] = Card(119,"Unassociated","Saleh",3,False,False,False)
        self.deck["120"] = Card(120,"Unassociated","US Election",3,False,False,False)

    # 20150131PS Start

    def validMarkersSetup(self):
        self.validGlobalMarkers.append("Moro Talks")
        self.validGlobalMarkers.append("NEST")
        self.validGlobalMarkers.append("Abbas")
        self.validGlobalMarkers.append("Anbar Awakening")
        self.validGlobalMarkers.append("Saddam Captured")
        self.validGlobalMarkers.append("Wiretapping")
        self.validGlobalMarkers.append("Benazir Bhutto")
        self.validGlobalMarkers.append("Enhanced Measures")
        self.validGlobalMarkers.append("Indo-Pakistani Talks")
        self.validGlobalMarkers.append("Iraqi WMD")
        self.validGlobalMarkers.append("Libyan Deal")
        self.validGlobalMarkers.append("Libyan WMD")
        self.validGlobalMarkers.append("Patriot Act")
        self.validGlobalMarkers.append("Renditions")
        self.validGlobalMarkers.append("Vieira de Mello Slain")
        self.validGlobalMarkers.append("Abu Sayyaf")
        self.validGlobalMarkers.append("Al-Anbar")
        self.validGlobalMarkers.append("Bhutto Shot")
        self.validGlobalMarkers.append("Pirates")
        self.validGlobalMarkers.append("Leak-Enhanced Measures")
        self.validGlobalMarkers.append("Leak-Wiretapping")
        self.validGlobalMarkers.append("Leak-Renditions")
        self.validCountryMarkers.append("CTR")    #20150616PS
        self.validCountryMarkers.append("NATO")
        self.validCountryMarkers.append("Sadr")
        self.validCountryMarkers.append("FATA")
        self.validLapsingMarkers.append("Biometrics")
        self.validLapsingMarkers.append("The door of Itjihad was closed")
        self.validLapsingMarkers.append("GTMO")
        self.validLapsingMarkers.append("Oil Price Spike")

    #20150131PS End    

    def my_raw_input(self, prompt):
        """Reads a line from the test input, if any is left, otherwise from standard input"""
        if len(self.testUserInput) > 0:
            retVal = self.testUserInput[0]
            self.testUserInput.remove(retVal)
            print "TEST: Prompt: %s VAL: %s" % (prompt, retVal)
            return retVal
        else:
            return raw_input(prompt)

    def getCountryFromUser(self, prompt, special, helpFunction, helpParameter = None):
        goodCountry = None
        while not goodCountry:
            input = self.my_raw_input(prompt)
            if input == "":
                return ""
            elif input == "?" and helpFunction:
                helpFunction(helpParameter)
                continue
            elif input == special:
                return special
            possible = []
            for country in self.map:
                if input.lower() == country.lower():
                    possible = [country]
                    break
                elif input.lower() in country.lower():
                    possible.append(country)
            if len(possible) == 0:
                print "Unrecognized country."
                print ""
            elif len(possible) > 1:
                print "Be more specific", possible
                print ""
            else:
                goodCountry = possible[0]
        return goodCountry
    
    def getNumTroopsFromUser(self, prompt, max):
        goodNum = None
        while not goodNum:
            try:
                input = self.my_raw_input(prompt)
                input = int(input)
                if input <= max:
                    return input
                else:
                    print "Not enough troops."
                    print ""
            except:
                print "Entry error"
                print ""

    def getCardNumFromUser(self, prompt):
        goodNum = None
        while not goodNum:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "none":
                    return "none"
                input = int(input)
                if input <= 120:
                    return input
                else:
                    print "Enter a card number."
                    print ""
            except:
                print "Enter a card number."
                print ""

    def getPlotTypeFromUser(self, prompt):
        goodNum = None
        while not goodNum:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "w" or input.lower() == "wmd":
                    return "WMD"
                input = int(input)
                if 1 <= input <= 3:
                    return input
                else:
                    print "Enter 1, 2, 3 or W for WMD."
                    print ""
            except:
                print "Enter 1, 2, 3 or W for WMD."
                print ""
        
    def getRollFromUser(self, prompt):
        goodNum = None
        while not goodNum:
            try:
                input = self.my_raw_input(prompt)
                if input == "r":
                    roll = random.randint(1,6)
                    print "Roll: %d" % roll
                    return roll
                input = int(input)
                if 1 <= input <= 6:
                    return input
                else:
                    raise
            except:
                print "Entry error"
                print ""
                
    def getYesNoFromUser(self, prompt):
        good = None
        while not good:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "y" or input.lower() == "yes":
                    return True
                elif input.lower() == "n" or input.lower() == "no":
                    return False
                else:
                    print "Enter y or n."
                    print ""
            except:
                print "Enter y or n."
                print ""

    def getPostureFromUser(self, prompt):
        good = None
        while not good:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "h" or input.lower() == "hard":
                    return "Hard"
                elif input.lower() == "s" or input.lower() == "soft":
                    return "Soft"
                else:
                    print "Enter h or s."
                    print ""
            except:
                print "Enter h or s."
                print ""

    def getEventOrOpsFromUser(self, prompt):
        good = None
        while not good:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "e" or input.lower() == "event":
                    return "event"
                elif input.lower() == "o" or input.lower() == "ops":
                    return "ops"
                else:
                    print "Enter e or o."
                    print ""
            except:
                print "Enter e or o."
                print ""
        
    def modifiedWoIRoll(self, baseRoll, country, useGWOTPenalty = True):
        modRoll = baseRoll
        #print "DEBUG: base roll:%d" % modRoll
        
        if self.prestige <= 3:
            modRoll -= 1
            self.outputToHistory("-1 for Prestige", False)
        elif self.prestige >= 7 and self.prestige <=9:
            modRoll += 1
            self.outputToHistory("+1 for Prestige", False)
        elif self.prestige >= 10:
            modRoll += 2
            self.outputToHistory("+2 for Prestige", False)
        #print "DEBUG: w/prestige mod:%d" % modRoll
        
        if self.map[country].is_ally() and self.map[country].is_fair():
            modRoll -= 1
            self.outputToHistory("-1 for Attempt to shift to Good", False)
        #print "DEBUG: w/to good mod:%d" % modRoll
        
        if useGWOTPenalty:
            modRoll += self.gwotPenalty()
            if self.gwotPenalty() <> 0:
                self.outputToHistory("-1 for GWOT Relations Penalty", False)
        #print "DEBUG: w/GWOT penalty:%d" % modRoll
        
        if self.map[country].aid > 0:
            modRoll += self.map[country].aid    # 20150131PS use number of aid markers rather than 1
            self.outputToHistory("+%s for Aid" % self.map[country].aid, False)
        #print "DEBUG: w/aid:%d" % modRoll
        
        for adj in self.map[country].links:
            if adj.is_ally() and adj.is_good():
                modRoll += 1
                self.outputToHistory("+1 for Adjacent Good Ally", False)
                break
        #print "DEBUG: w/adj good:%d" % modRoll
        return modRoll
        
    def gwotPenalty(self):
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Non-Muslim" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        if worldPos > 0:
            worldPosStr = "Hard"
        elif worldPos < 0:
            worldPosStr = "Soft"
        else:
            worldPosStr = "Even"
        if worldPos > 3:
            worldPos = 3
        elif worldPos < -3:
            worldPos = -3
        if self.map["United States"].posture != worldPosStr:
            return -(abs(worldPos))
        else:
            return 0
            
    def changePrestige(self, delta, lineFeed = True):
        self.prestige += delta
        if self.prestige < 1:
            self.prestige = 1
        elif self.prestige > 12:
            self.prestige = 12
        self.outputToHistory("Prestige now %d" % self.prestige, lineFeed)
                
    def changeFunding(self, delta, lineFeed = True):
        self.funding += delta
        if self.funding < 1:
            self.funding = 1
        elif self.funding > 9:
            self.funding = 9
        self.outputToHistory("Jihadist Funding now %d" % self.funding, lineFeed)
        
    def placeCells(self, country, numCells):
        if self.cells == 0:
            self.outputToHistory("No cells are on the Funding Track.", True)
        else:
            self.testCountry(country)
            cellsToMove = min(numCells, self.cells)
            self.map[country].sleeperCells += cellsToMove
            # remove cadre 
            self.map[country].cadre = 0
            self.cells -= cellsToMove
            self.outputToHistory("%d Sleeper Cell(s) placed in %s" % (cellsToMove, country), False)
            self.outputToHistory(self.map[country].countryStr(), True)
                
    def removeCell(self, country, side):
        #20150131PS included Sadr in cell count, added test for side to determine order of removal
        if self.map[country].totalCells(True) == 0:
            return
        if side == "US":
            if self.map[country].sleeperCells > 0:
                self.map[country].sleeperCells -= 1
                self.cells += 1
                self.outputToHistory("Sleeper Cell removed from %s." % country, True)
            elif "Sadr" in self.map[country].markers:
                self.map[country].markers.remove("Sadr")
                self.outputToHistory("Sadr removed from %s." % country, True)            
            elif self.map[country].activeCells > 0:
                self.map[country].activeCells -= 1
                self.cells += 1
                self.outputToHistory("Active Cell removed from %s." % country, True)
        else:
            if self.map[country].activeCells > 0:
                self.map[country].activeCells -= 1
                self.cells += 1
                self.outputToHistory("Active Cell removed from %s." % country, True)
            elif self.map[country].sleeperCells > 0:
                self.map[country].sleeperCells -= 1
                self.cells += 1
                self.outputToHistory("Sleeper Cell removed from %s." % country, True)
            elif "Sadr" in self.map[country].markers:
                self.map[country].markers.remove("Sadr")
                self.outputToHistory("Sadr removed from %s." % country, True)            
        if self.map[country].totalCells() == 0:
            self.outputToHistory("Cadre added in %s." % country, True)
            self.map[country].cadre = 1
    
    def removeAllCellsFromCountry(self, country):
        cellsToRemove = self.map[country].totalCells()
        if self.map[country].sleeperCells > 0:
            numCells = self.map[country].sleeperCells
            self.map[country].sleeperCells -= numCells
            self.cells += numCells
            self.outputToHistory("%d Sleeper Cell(s) removed from %s." % (numCells, country), False)
        if self.map[country].activeCells > 0:
            numCells = self.map[country].activeCells
            self.map[country].activeCells -= numCells
            self.cells += numCells
            self.outputToHistory("%d Active Cell(s) removed from %s." % (numCells, country), False)
        if cellsToRemove > 0:
            self.outputToHistory("Cadre added in %s." % country, False)
            self.map[country].cadre = 1
    
    def improveGovernance(self, country):
        self.map[country].improve_governance()

    def worsenGovernance(self, country):
        self.map[country].worsenGovernance()

    def numCellsAvailable(self, ignoreFunding = False):
        
        retVal = self.cells
        if ignoreFunding:
            return retVal
        
        if self.funding <= 3:
            retVal -= 10
        elif self.funding <= 6:
            retVal -= 5
        return max(retVal, 0)
        
    def numIslamistRule(self):
        numIR = 0
        for country in self.map:
            if self.map[country].is_islamist_rule():
                numIR += 1
        return numIR
        
    def numBesieged(self):
        numBesieged = 0
        for country in self.map:
            if self.map[country].besieged > 0:
                numBesieged += 1
        return numBesieged

    def numRegimeChange(self):
        numRC = 0
        for country in self.map:
            if self.map[country].regimeChange > 0:
                numRC += 1
        return numRC
        
    def numAdversary(self):
        numAdv = 0
        for country in self.map:
            if self.map[country].is_adversary():
                numAdv += 1
        return numAdv
        
    def num_disruptable(self):
        """Returns the number of countries in which the US player can Disrupt"""
        return Utils.count(self.map.values(), Country.is_disruptable)

    def countryResources(self, country):
        res = self.map[country].resources
        if self.map[country].oil:
            spikes = 0
            for event in self.lapsing:
                if event == "Oil Price Spike":
                    spikes += 1
            res += spikes
        return res

    def handleMuslimWoI(self, roll, country):
        if roll <= 3:
            self.outputToHistory("* WoI in %s failed." % country)
        elif roll == 4:
            if self.map[country].aid == 0:        #20150131PS check for existing aid marker
                self.map[country].aid = 1
                self.outputToHistory("* WoI in %s adds Aid." % country, False)
                self.outputToHistory(self.map[country].countryStr(), True)
        else:
            if self.map[country].is_neutral():
                self.map[country].make_ally()
                self.outputToHistory("* WoI in %s succeeded - Alignment now Ally." % country, False)
                self.outputToHistory(self.map[country].countryStr(), True)
            elif self.map[country].is_ally():
                self.improveGovernance(country)
                self.outputToHistory("* WoI in %s succeeded - Governance now %s." % (country, self.map[country].govStr()), False)
                self.outputToHistory(self.map[country].countryStr(), True)
                
    def handleAlert(self, country):
        if self.map[country].plots > 0:
            self.map[country].plots -= 1
            self.outputToHistory("* Alert in %s - %d plot(s) remain." % (country, self.map[country].plots))
            
    def handleReassessment(self):
        if self.map["United States"].posture == "Hard":
            self.map["United States"].posture = "Soft"
        else:
            self.map["United States"].posture = "Hard"
        self.outputToHistory("* Reassessment = US Posture now %s" % self.map["United States"].posture)
        
    def handleRegimeChange(self, where, moveFrom, howMany, govRoll, prestigeRolls):
        if self.map["United States"].posture == "Soft":
            return
        if moveFrom == 'track':
            self.troops -= howMany
        else:    
            self.map[moveFrom].changeTroops(-howMany)
        self.map[where].changeTroops(howMany)
        sleepers = self.map[where].sleeperCells
        self.map[where].sleeperCells = 0
        self.map[where].activeCells += sleepers
        self.map[where].make_ally()
        if govRoll <= 4:
            self.map[where].make_poor()
        else:
            self.map[where].make_fair()
        self.map[where].regimeChange = 1
        presMultiplier = 1
        if prestigeRolls[0] <= 4:
            presMultiplier = -1
        self.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
        self.outputToHistory("* Regime Change in %s" % where, False)
        self.outputToHistory(self.map[where].countryStr(), False)
        if moveFrom == "track":
            self.outputToHistory("%d Troops on Troop Track" % self.troops, False)
        else:
            self.outputToHistory("%d Troops in %s" % (self.map[moveFrom].troops(), moveFrom), False)
        self.outputToHistory("US Prestige %d" % self.prestige)
        if where == "Iraq" and "Iraqi WMD" in self.markers:
            self.markers.remove("Iraqi WMD")
            self.outputToHistory("Iraqi WMD no longer in play.", True)
        if where == "Libya" and "Libyan WMD" in self.markers:
            self.markers.remove("Libyan WMD")
            self.outputToHistory("Libyan WMD no longer in play.", True)
        
    def handleWithdraw(self, moveFrom, moveTo, howMany, prestigeRolls):
        if self.map["United States"].posture == "Hard":
            return
        self.map[moveFrom].changeTroops(-howMany)
        if moveTo == "track":
            self.troops += howMany
        else:
            self.map[moveTo].changeTroops(howMany)
        self.map[moveFrom].aid = 0
        self.map[moveFrom].besieged = 1
        presMultiplier = 1
        if prestigeRolls[0] <= 4:
            presMultiplier = -1
        self.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
        self.outputToHistory("* Withdraw troops from %s" % moveFrom, False)
        self.outputToHistory(self.map[moveFrom].countryStr(), False)
        if moveTo == "track":
            self.outputToHistory("%d Troops on Troop Track" % self.troops, False)
        else:
            self.outputToHistory("%d Troops in %s" % (self.map[moveTo].troops(), moveTo), False)
            self.outputToHistory(self.map[moveTo].countryStr(), False)
        self.outputToHistory("US Prestige %d" % self.prestige)
        
    def handleDisrupt(self, where):
        numToDisrupt = 1
        if "Al-Anbar" in self.markers and (where == "Iraq" or where == "Syria"):
            numToDisrupt = 1
        elif self.map[where].troops() >= 2 or self.map[where].posture == "Hard":
            numToDisrupt = min(2, self.map[where].totalCells(False))
        if self.map[where].totalCells(False) <= 0 and self.map[where].cadre > 0:
            if "Al-Anbar" not in self.markers or (where != "Iraq" and where != "Syria"):
                self.outputToHistory("* Cadre removed in %s" % where)
                self.map[where].cadre = 0
        elif self.map[where].totalCells(False) <= numToDisrupt:
            self.outputToHistory("* %d cell(s) disrupted in %s." % (self.map[where].totalCells(False), where), False)
            if self.map[where].sleeperCells > 0:
                self.map[where].activeCells += self.map[where].sleeperCells
                numToDisrupt -= self.map[where].sleeperCells
                self.map[where].sleeperCells = 0
            if numToDisrupt > 0:
                self.map[where].activeCells -= numToDisrupt
                self.cells += numToDisrupt
                if self.map[where].activeCells < 0:
                    self.map[where].activeCells = 0
                if self.cells > 15:
                    self.cells = 15
            if self.map[where].totalCells(False) <= 0:
                self.outputToHistory("Cadre added in %s." % where, False)
                self.map[where].cadre = 1
            if self.map[where].troops() >= 2:
                self.prestige += 1
                if self.prestige > 12:
                    self.prestige = 12
                self.outputToHistory("US Prestige now %d." % self.prestige, False)
            self.outputToHistory(self.map[where].countryStr(), True)
        else:
            if self.map[where].activeCells == 0:
                self.map[where].activeCells += numToDisrupt
                self.map[where].sleeperCells -= numToDisrupt
                self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where), False)
            elif self.map[where].sleeperCells == 0:
                self.map[where].activeCells -= numToDisrupt
                self.cells += numToDisrupt
                self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where), False)
                if self.map[where].totalCells(False) <= 0:
                    self.outputToHistory("Cadre added in %s." % where, False)
                    self.map[where].cadre = 1
            else:
                if numToDisrupt == 1:
                    disStr = None
                    while not disStr:
                        input = self.my_raw_input("You can disrupt one cell. Enter a or s for either an active or sleeper cell: ")
                        input = input.lower()
                        if input == "a" or input == "s":
                            disStr = input
                    if disStr == "a":
                        self.map[where].activeCells -= numToDisrupt
                        self.cells += numToDisrupt
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
                    else:
                        self.map[where].sleeperCells -= numToDisrupt
                        self.map[where].activeCells += numToDisrupt
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
                else:
                    disStr = None
                    while not disStr:
                        if self.map[where].sleeperCells >= 2 and self.map[where].activeCells >= 2:
                            input = self.my_raw_input("You can disrupt two cells. Enter aa, as, or ss for active or sleeper cells: ")
                            input = input.lower()
                            if input == "aa" or input == "as" or input == "sa" or input == "ss":
                                disStr = input
                        elif self.map[where].sleeperCells >= 2:
                            input = self.my_raw_input("You can disrupt two cells. Enter as, or ss for active or sleeper cells: ")
                            input = input.lower()
                            if input == "as" or input == "sa" or input == "ss":
                                disStr = input
                        elif self.map[where].activeCells >= 2:
                            input = self.my_raw_input("You can disrupt two cells. Enter aa, or as for active or sleeper cells: ")
                            input = input.lower()
                            if input == "as" or input == "sa" or input == "aa":
                                disStr = input
                    if input == "aa":
                        self.map[where].activeCells -= 2
                        self.cells += 2
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
                    elif input == "as" or input == "sa":
                        self.map[where].sleeperCells -= 1
                        self.cells += 1
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
                    else:
                        self.map[where].sleeperCells -= 2
                        self.map[where].activeCells += 2
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
            if self.map[where].troops() >= 2:
                self.prestige += 1
                if self.prestige > 12:
                    self.prestige = 12
                self.outputToHistory("US Prestige now %d." % self.prestige, False)
            self.outputToHistory(self.map[where].countryStr(), True)
        
    def executeJihad(self, country, rollList):
        successes = 0
        failures = 0
        target_country = self.map[country]
        originalBesieged = target_country.besieged    #20150303PS save besieged status in case changed by major jihad failure
        for roll in rollList:
            if target_country.is_non_recruit_success(roll):
                successes += 1
            else:
                failures += 1
        target_country.reduce_aid_by(successes)  # Same for major and minor
        isMajorJihad = country in self.majorJihadPossible(len(rollList))
        self.outputToHistory("Jihad operation.  %d Successes rolled, %d Failures rolled" % (successes, failures), False)
        if isMajorJihad:  # all cells go active
            self.outputToHistory("* Major Jihad attempt in %s" % country, False) 
            sleepers = target_country.sleeperCells
            target_country.sleeperCells = 0
            target_country.activeCells += sleepers
            self.outputToHistory("All cells go Active", False)
            if ((failures >= 2  and target_country.besieged == 0) or (failures == 3 and target_country.besieged == 1))  and (len(rollList) == 3) and target_country.is_poor():
                self.outputToHistory("Major Jihad Failure", False) 
                target_country.besieged = 1
                self.outputToHistory("Besieged Regime", False) 
                if target_country.is_adversary():
                    target_country.make_neutral()
                elif target_country.is_neutral():
                    target_country.make_ally()
                self.outputToHistory("Alignment %s" % target_country.alignment(), False)
        else:  # a cell is active for each roll
            self.outputToHistory("* Minor Jihad attempt in %s" % country, False) 
            for i in range(len(rollList) - target_country.numActiveCells()):
                self.outputToHistory("Cell goes Active", False)
                target_country.sleeperCells -= 1
                target_country.activeCells += 1
        while successes > 0 and target_country.governance_is_better_than(POOR):
            target_country.worsenGovernance()
            successes -= 1
            self.outputToHistory("Governance to %s" % target_country.govStr(), False)
        if isMajorJihad and ((successes >= 2) or ((originalBesieged > 0) and (successes >= 1))) :  # Major Jihad
            self.outputToHistory("Islamist Revolution in %s" % country, False)
            target_country.make_islamist_rule()
            self.outputToHistory("Governance to Islamist Rule", False)
            target_country.make_adversary()
            self.outputToHistory("Alignment to Adversary", False) 
            target_country.regimeChange = 0
            if target_country.besieged > 0:
                self.outputToHistory("Besieged Regime marker removed.", False) 
                
            target_country.besieged = 0
            target_country.aid = 0
            self.funding = min(9, self.funding + self.countryResources(country))
            self.outputToHistory("Funding now %d" % self.funding, False) 
            if target_country.troops() > 0:
                self.prestige = 1
                self.outputToHistory("Troops present so US Prestige now 1", False) 
        if self.ideology <= 5:
            for i in range(failures):
                if target_country.numActiveCells() > 0:
                    target_country.removeActiveCell()
                else:
                    target_country.sleeperCells -= 1
                    self.outputToHistory("Sleeper cell Removed to Funding Track", False)
                    self.cells += 1
        self.outputToHistory(target_country.countryStr(), False)
        print ""
        
    def handleJihad(self, country, ops):
        """Returns number of unused Ops"""
        cells = self.map[country].totalCells(True)
        rollList = []
        for i in range(min(cells, ops)):
            rollList.append(random.randint(1,6))
        self.executeJihad(country, rollList)
        return ops - len(rollList)
        
    def handleMinorJihad(self, countryList, ops):
        opsRemaining = ops
        for countryData in countryList:
            self.handleJihad(countryData[0], countryData[1])
            opsRemaining -= countryData[1]
        return opsRemaining

    def excessCellsNeededForMajorJihad(self):
        if self.ideology >= 4:
            return 3
        return 5

    def bhutto_in_play(self):
        return "Benazir Bhutto" in self.markers

    def majorJihadPossible(self, ops):
        """Return list of countries where major jihad is possible."""
        targets = []
        excessCellsNeeded = self.excessCellsNeededForMajorJihad()
        bhutto = self.bhutto_in_play()
        for country in self.map:
            if self.map[country].is_major_jihad_possible(ops, excessCellsNeeded, bhutto):
                targets.append(country)
        return targets
                
    def majorJihadChoice(self, ops):
        """Return AI choice country."""
        possible = self.majorJihadPossible(ops)
        if possible == []:
            return False
        else:
            if "Pakistan" in possible:
                return "Pakistan"
            else:
                maxResource = 0
                for country in possible:
                    if self.countryResources(country) > maxResource:
                        maxResource = self.countryResources(country)
                newPossible = []
                for country in possible:
                    if self.countryResources(country) == maxResource:
                        newPossible.append(country)
                return random.choice(newPossible)

    def minorJihadInGoodFairChoice(self, ops, isAbuGhurayb = False, isAlJazeera = False):
        possible = []
        for country in self.map:
            if isAbuGhurayb:
                if self.map[country].is_ally() and not self.map[country].is_islamist_rule():
                    possible.append(country)
            elif isAlJazeera:
                if country == "Saudi Arabia" or self.isAdjacent(country, "Saudi Arabia"):
                    if self.map[country].troops() > 0:
                        possible.append(country)
            elif (self.map[country].is_muslim()) and (self.map[country].is_good() or self.map[country].is_fair()) and (self.map[country].totalCells(True) > 0):
                if "Benazir Bhutto" in self.markers and country == "Pakistan":
                    continue
                possible.append(country)
        if len(possible) == 0:
            return False
        else:
            countryScores = {}
            for country in possible:
                if self.map[country].is_good():
                    countryScores[country] = 2000000
                else:
                    countryScores[country] = 1000000
                if country == "Pakistan":
                    countryScores[country] += 100000
                if self.map[country].aid > 0:
                    countryScores[country] += 10000
                if self.map[country].besieged > 0:
                    countryScores[country] += 1000
                countryScores[country] += (self.countryResources(country) * 100)
                countryScores[country] += random.randint(1,99)
            countryOrder = []
            for country in countryScores:
                countryOrder.append((countryScores[country], (self.map[country].totalCells(True)), country))
            countryOrder.sort()
            countryOrder.reverse()
            returnList = []
            opsRemaining = ops
            for countryData in countryOrder:
                rolls = min(opsRemaining, countryData[1])
                returnList.append((countryData[2], rolls))
                opsRemaining -= rolls
                if opsRemaining <= 0:
                    break
            return returnList
            
    def recruitChoice(self, ops, isMadrassas = False):
        self.debugPrint("DEBUG: recruit with remaining %d ops" % ops)
        self.debugPrint("DEBUG: recruit with remaining %d ops" % (2*ops))
        countryScores = {}
        for country_name in self.map:
            country = self.map[country_name]
            if country.can_recruit(isMadrassas):
                country_recruit_score = country.get_recruit_score(ops)
                if not country_recruit_score is None:
                    countryScores[country_name] = country_recruit_score
        for country in countryScores:
            self.debugPrint("c")
            if self.map[country].besieged > 0:
                countryScores[country] += 100000
            countryScores[country] += (1000 * (self.map[country].troops() + self.map[country].totalCells(True)))
            countryScores[country] += 100 * self.countryResources(country)
            countryScores[country] += random.randint(1,99)
        countryOrder = []
        for country in countryScores:
            self.debugPrint("here: %d " % countryScores[country])
            if countryScores[country] > 0:
                countryOrder.append((countryScores[country], (self.map[country].totalCells(True)), country))
        countryOrder.sort()
        countryOrder.reverse()
        if countryOrder == []:
            self.debugPrint("d")
            return False
        else:
            self.debugPrint("e")
            return countryOrder[0][2]
    
    def executeRecruit(self, country, ops, rolls, recruitOverride = None, isJihadistVideos = False, isMadrassas = False):
        self.outputToHistory("* Recruit to %s" % country)
        cellsRequested = ops
        if self.ideology >= 3:
            cellsRequested = ops * 2

        cells = self.numCellsAvailable(isMadrassas or isJihadistVideos)

        cellsToRecruit = min(cellsRequested, cells)
        if self.map[country].regimeChange or self.map[country].is_islamist_rule():
            if self.map[country].regimeChange:
                self.outputToHistory("Recruit to Regime Change country automatically successful.", False)
            else:
                self.outputToHistory("Recruit to Islamist Rule country automatically successful.", False)
            self.cells -= cellsToRecruit
            self.map[country].sleeperCells += cellsToRecruit
            
            if cellsToRecruit == 0 and isJihadistVideos:
                self.map[country].cadre = 1
                self.outputToHistory("No cells available to recruit.  Cadre added.", False)
                self.outputToHistory(self.map[country].countryStr(), True)
                return ops - 1
            else:            
                self.map[country].cadre = 0
                
            self.outputToHistory("%d sleeper cells recruited to %s." % (cellsToRecruit, country), False)
            self.outputToHistory(self.map[country].countryStr(), True)
            if self.ideology >= 3:
                return ops - ((cellsToRecruit / 2) + (cellsToRecruit % 2))
            else:
                return ops - cellsToRecruit
        else:
            opsRemaining = ops
            i = 0

            if self.numCellsAvailable(isJihadistVideos) <= 0 and opsRemaining > 0:
                self.map[country].cadre = 1
                self.outputToHistory("No cells available to recruit. Cadre added.", False)
                self.outputToHistory(self.map[country].countryStr(), True)
                return ops - 1
            else:            
                while self.numCellsAvailable(isMadrassas or isJihadistVideos) > 0 and opsRemaining > 0:
                    if self.map[country].is_recruit_success(rolls[i], recruitOverride):
                        if self.ideology >= 3:
                            cellsMoving = min(self.numCellsAvailable(isMadrassas or isJihadistVideos), 2)
                        else:
                            cellsMoving = min(self.numCellsAvailable(isMadrassas or isJihadistVideos), 1)
                        self.cells -= cellsMoving
                        self.map[country].sleeperCells += cellsMoving
                        self.map[country].cadre = 0
                        self.outputToHistory("Roll successful, %d sleeper cell(s) recruited." % cellsMoving, False)
                    else:
                        self.outputToHistory("Roll failed.", False)
                        if isJihadistVideos:
                            self.map[country].cadre = 1
                            self.outputToHistory("Cadre added.", False)
                    opsRemaining -= 1
                    i += 1
                self.outputToHistory(self.map[country].countryStr(), True)
                return opsRemaining
                    
    def handleRecruit(self, ops, isMadrassas = False):
        self.debugPrint("recruit ops: ")
        self.debugPrint("DEBUG: recruit with remaining %d ops" % ops)
        country = self.recruitChoice(ops, isMadrassas)
        if not country:
            self.outputToHistory("* No countries qualify to Recruit.", True)
            return ops
        else:
            if isMadrassas:
                cells = self.cells
            else:
                if "GTMO" in self.lapsing:
                    self.outputToHistory("* Cannot Recruit due to GTMO.", True)
                    return ops
                cells = self.numCellsAvailable()
            if cells <= 0:
                self.outputToHistory("* No cells available to Recruit.", True)
                return ops
            else:
                rolls = []
                for i in range(ops):
                    rolls.append(random.randint(1,6))
                return self.executeRecruit(country, ops, rolls, None, False, isMadrassas)
                
    def isAdjacent(self, here, there):
        if "Patriot Act" in self.markers:
            if here == "United States" or there == "United States":
                if here == "Canada" or there == "Canada":
                    return True
                else:
                    return False
        if self.map[here] in self.map[there].links:
            return True
        if self.map[here].schengen and self.map[there].schengen:
            return True
        if self.map[here].schengenLink and self.map[there].schengen:
            return True
        if self.map[here].schengen and self.map[there].schengenLink:
            return True
        return False
                
    def adjacentCountryHasCell(self, targetCountry):
        for country in self.map:
            if self.isAdjacent(targetCountry, country):
                if self.map[country].totalCells(True) > 0:
                    return True
        return False
    
    @staticmethod
    def inLists(country, lists):
        for list in lists:
            if country in lists:    
                return True
        return False
    
    def countryDistance(self, start, end):
        if start == end:
            return 0
        distanceGroups = []
        distanceGroups.append([start])
        distance = 1
        while not self.inLists(end, distanceGroups):
            list = distanceGroups[distance - 1]
            nextWave = []
            for country in list:
                for subCountry in self.map:
                    if not self.inLists(subCountry, distanceGroups):
                        if self.isAdjacent(subCountry, country):
                            if subCountry == end:
                                return distance
                            if subCountry not in nextWave:
                                nextWave.append(subCountry)
            distanceGroups.append(nextWave)
            distance += 1
        
    def travelDestinationChooseBasedOnPriority(self, countryList):
        for country in countryList:
            if country == "Pakistan":
                return country
        maxResources = 0
        for country in countryList:
            if self.countryResources(country) > maxResources:
                maxResources = self.countryResources(country)
        maxdests = []
        for country in countryList:
            if self.countryResources(country) == maxResources:
                maxdests.append(country)
        return random.choice(maxdests)
            
    def travelDestinations(self, ops, isRadicalization = False):
        dests = []
        # A non-Islamist Rule country with Regime Change, Besieged Regime, or Aid, if any
        if not isRadicalization:
            subdests = []
            for country in self.map:
                if (not self.map[country].is_islamist_rule()) and ((self.map[country].besieged > 0) or (self.map[country].regimeChange > 0) or (self.map[country].aid > 0)):
                    if ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                        continue
                    subdests.append(country)
            if len(subdests) == 1:
                dests.append(subdests[0])
            elif len(subdests) > 1:
                dests.append(self.travelDestinationChooseBasedOnPriority(subdests))
            if len(dests) == ops:
                return dests
            
        # A Poor country where Major Jihad would be possible if two (or fewer) cells were added.
        subdests = []
        for country in self.map:
            if (self.map[country].is_poor()) and (((self.map[country].totalCells(True) + 2) - self.map[country].troops()) >= self.excessCellsNeededForMajorJihad()):
                if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                    continue
                subdests.append(country)
        if len(subdests) == 1:
            dests.append(subdests[0])
        elif len(subdests) > 1:
            dests.append(self.travelDestinationChooseBasedOnPriority(subdests))
        if len(dests) == ops:
            return dests
            
        # A Good or Fair Muslim country with at least one cell adjacent.
        subdests = []
        for country in self.map:
            if (self.map[country].is_good() or self.map[country].is_fair()) and self.map[country].is_muslim():
                if self.adjacentCountryHasCell(country):
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                        continue
                    subdests.append(country)
        if len(subdests) == 1:
            dests.append(subdests[0])
        elif len(subdests) > 1:
            dests.append(self.travelDestinationChooseBasedOnPriority(subdests))
        if len(dests) == ops:
            return dests
    
        # An unmarked non-Muslim country if US Posture is Hard, or a Soft non-Muslim country if US Posture is Soft.
        subdests = []
        if self.map["United States"].posture == "Hard":
            for country in self.map:
                if self.map[country].type == "Non-Muslim" and self.map[country].posture == "":
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                        continue
                    subdests.append(country)
        else:
            for country in self.map:
                if country != "United States" and self.map[country].type == "Non-Muslim" and self.map[country].posture == "Soft":
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                        continue
                    subdests.append(country)
        if len(subdests) == 1:
            dests.append(subdests[0])
        elif len(subdests) > 1:
            dests.append(random.choice(subdests))
        if len(dests) == ops:
            return dests
            
    # Random
        if (not isRadicalization) and ("Biometrics" in self.lapsing):
            subdests = []
            for country in self.map:
                if self.adjacentCountryHasCell(country):
                    subdests.append(country)
            if len(subdests) > 0:
                while len(dests) < ops:
                    dests.append(random.choice(subdests))        
        else:
            while len(dests) < ops:
                dests.append(random.choice(self.map.keys()))        
        
        return dests

    def names_of_countries(self, predicate):
        """Returns the names of countries matching the given predicate"""
        return [country for country in self.map if predicate(self.map[country])]
    
    def travelDestinationsSchengenVisas(self):
        """
        Returns the names of countries that are valid travel
        destinations for the Schengen Visas event
        """
        if self.map["United States"].posture == "Hard":
            candidates = self.names_of_countries(lambda c: c.schengen and c.posture == '')
        else:
            candidates = self.names_of_countries(lambda c: c.schengen and c.posture == 'Soft')
        if len(candidates) == 1:
            return [candidates[0], candidates[0]]  # yes, same one twice
        if len(candidates) > 1:
            return self.randomizer.pick(2, candidates)
        schengens = self.names_of_countries(lambda c: c.schengen)
        return self.randomizer.pick(2, schengens)
    
    def travelSourceChooseBasedOnPriority(self, countryList, i, destinations):
        subPossibles = []
        for country in countryList:
            if self.map[country].activeCells > 0:
                subPossibles.append(country)
        if len(subPossibles) == 1:
            return subPossibles[0]
        elif len(subPossibles) > 1:
            return random.choice(subPossibles)
        else:
            subPossibles = []
            for country in countryList:
                notAnotherDest = True
                for j in range(len(destinations)):
                    if (i != j) and (country == destinations[j]):
                        subPossibles.append(country)
        if len(subPossibles) == 1:
            return subPossibles[0]
        elif len(subPossibles) > 1:
            return random.choice(subPossibles)
        else:
            return random.choice(countryList)
            
    def travelSourceBoxOne(self, i, destinations, sources, ops, isRadicalization = False):
        possibles = []
        for country in self.map:
            if self.map[country].is_islamist_rule():
                numTimesIsSource = 0
                for source in sources:
                    if source == country:
                        numTimesIsSource += 1
                if ((self.map[country].sleeperCells + self.map[country].activeCells) - numTimesIsSource) > ops:
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.isAdjacent(country, destinations[i])):
                        continue
                    possibles.append(country)
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travelSourceChooseBasedOnPriority(possibles, i, destinations)
    
    def travelSourceBoxTwo(self, i, destinations, sources, isRadicalization = False):
        possibles = []
        for country in self.map:
            if self.map[country].regimeChange > 0:
                numTimesIsSource = 0
                for source in sources:
                    if source == country:
                        numTimesIsSource += 1
                if ((self.map[country].sleeperCells + self.map[country].activeCells) - numTimesIsSource) > self.map[country].troops():
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.isAdjacent(country, destinations[i])):
                        continue
                    possibles.append(country)
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travelSourceChooseBasedOnPriority(possibles, i, destinations)                    

    def travelSourceBoxThree(self, i, destinations, sources, isRadicalization = False):
        possibles = []
        for country in self.map:
            if self.isAdjacent(destinations[i], country):
                adjacent = self.map[country]
                numTimesIsSource = 0
                for source in sources:
                    if source == adjacent.name:
                        numTimesIsSource += 1
                if ((adjacent.sleeperCells + adjacent.activeCells) - numTimesIsSource) > 0:
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.isAdjacent(country, destinations[i])):
                        continue
                    possibles.append(adjacent.name)
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travelSourceChooseBasedOnPriority(possibles, i, destinations)                    

    def travelSourceBoxFour(self, i, destinations, sources, isRadicalization = False):
        possibles = []
        for country in self.map:
            numTimesIsSource = 0
            for source in sources:
                if source == country:
                    numTimesIsSource += 1
            if ((self.map[country].sleeperCells + self.map[country].activeCells) - numTimesIsSource) > 0:
                if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.isAdjacent(country, destinations[i])):
                    continue
                possibles.append(country)
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travelSourceChooseBasedOnPriority(possibles, i, destinations)                    

    def travelSources(self, destinations, ops, isRadicalization = False):
        sources = []
        for i in range(len(destinations)):
            source = self.travelSourceBoxOne(i, destinations, sources, ops, isRadicalization)
            if source:
                sources.append(source)
            else:
                source = self.travelSourceBoxTwo(i, destinations, sources, isRadicalization)
                if source:
                    sources.append(source)
                else:
                    source = self.travelSourceBoxThree(i, destinations, sources, isRadicalization)
                    if source:
                        sources.append(source)
                    else:
                        source = self.travelSourceBoxFour(i, destinations, sources, isRadicalization)
                        if source:
                            sources.append(source)
        return sources
        
    def testCountry(self, country):
        # Country testing if necessary        
        if self.map[country].type == "Non-Muslim" and self.map[country].posture == "":
            testRoll = random.randint(1,6)
            if testRoll <= 4:
                self.map[country].posture = "Soft"
            else:
                self.map[country].posture = "Hard"
            self.outputToHistory("%s tested, posture %s" % (self.map[country].name, self.map[country].posture), False)
        elif self.map[country].is_ungoverned():
            testRoll = random.randint(1,6)
            if testRoll <= 4:
                self.map[country].make_poor()
            else:
                self.map[country].make_fair()
            self.map[country].make_neutral()
            self.outputToHistory("%s tested, governance %s" % (self.map[country].name, self.map[country].govStr()), False)
            
    def getCountriesWithUSPostureByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if (country != "United States") and (self.map[country].posture == self.map["United States"].posture):
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict
    
    def getCountriesWithTroopsByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if self.map[country].troops() > 0:
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict
    
    def getCountriesWithAidByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if self.map[country].aid > 0:
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict
    
    def getNonMuslimCountriesByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if (country != "United States") and (self.map[country].type == "Non-Muslim"):
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict
    
    def getMuslimCountriesByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if self.map[country].type != "Non-Muslim":
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict
    
    def handleTravel(self, ops, isRadicalization = False, isSchengenVisas = False, isCleanOperatives = False):
        if isSchengenVisas:
            destinations = self.travelDestinationsSchengenVisas()
        elif isCleanOperatives:
            destinations = ["United States", "United States"]
        else:
            destinations = self.travelDestinations(ops, isRadicalization)
        sources = self.travelSources(destinations, ops, isRadicalization)
        if not isRadicalization and not isSchengenVisas and not isCleanOperatives:
            self.outputToHistory("* Cells Travel", False)
        for i in range(len(sources)):
            self.outputToHistory("->Travel from %s to %s." % (sources[i], destinations[i]), False)
            success = False
            displayStr = "BLAH!!"
            if isRadicalization:
                success = True
                displayStr = ("Travel by Radicalization is automatically successful.")
            elif isSchengenVisas:
                success = True
                displayStr = ("Travel by Schengen Visas is automatically successful.")
            elif isCleanOperatives:
                success = True
                displayStr = ("Travel by Clean Operatives is automatically successful.")
            else:
                if sources[i] == destinations[i]:
                    success = True
                    displayStr = ("Travel within country automatically successful.")
                else:
                    if self.isAdjacent(sources[i], destinations[i]): 
                        if not "Biometrics" in self.lapsing:
                            success = True
                            displayStr = ("Travel to adjacent country automatically successful.")
                        else:
                            roll = random.randint(1, 6)
                            if self.map[destinations[i]].is_non_recruit_success(roll):
                                success = True
                                displayStr = ("Travel roll needed due to Biometrics - roll successful.")
                            else:
                                displayStr = ("Travel roll needed due to Biometrics -  roll failed, cell to funding track.")
                    else:
                        roll = random.randint(1, 6)
                        if self.map[destinations[i]].is_non_recruit_success(roll):
                            success = True
                            displayStr = ("Travel roll successful.")
                        else:
                            displayStr = ("Travel roll failed, cell to funding track.")
            self.outputToHistory(displayStr, True)
            self.testCountry(destinations[i])
            if success:
                if self.map[sources[i]].activeCells > 0:
                    self.map[sources[i]].activeCells -= 1
                else:
                    self.map[sources[i]].sleeperCells -= 1
                self.map[destinations[i]].sleeperCells += 1
                self.outputToHistory(self.map[sources[i]].countryStr(), False)
                self.outputToHistory(self.map[destinations[i]].countryStr(), True)
            else:
                if self.map[sources[i]].activeCells > 0:
                    self.map[sources[i]].activeCells -= 1
                else:
                    self.map[sources[i]].sleeperCells -= 1
                self.cells += 1
                self.outputToHistory(self.map[sources[i]].countryStr(), True)                
        return ops - len(sources)
        
    def placePlots(self, country, rollPosition, plotRolls, isMartyrdomOperation = False, isDanishCartoons = False, isKSM = False):
        if (self.map[country].totalCells(True)) > 0:
            if isMartyrdomOperation:
                self.removeCell(country, "Jihadist")    # 20150131PS added side
                self.outputToHistory("Place 2 available plots in %s." % country, False)
                self.map[country].plots += 2
                rollPosition = 1
            elif isDanishCartoons:
                if self.numIslamistRule() > 0:
                    self.outputToHistory("Place any available plot in %s." % country, False)
                else:
                    self.outputToHistory("Place a Plot 1 in %s." % country, False)
                self.map[country].plots += 1
                rollPosition = 1
            elif isKSM:
                if not self.map[country].is_islamist_rule():
                    self.outputToHistory("Place any available plot in %s." % country, False)
                    self.map[country].plots += 1
                    rollPosition = 1
            else:
                opsRemaining = len(plotRolls) - rollPosition
                cellsAvailable = self.map[country].totalCells(True)
                plotsToPlace = min(cellsAvailable, opsRemaining)
                self.outputToHistory("--> %s plot attempt(s) in %s." % (plotsToPlace, country), False)
                successes = 0
                failures = 0
                for i in range(rollPosition, rollPosition + plotsToPlace):
                    if self.map[country].is_non_recruit_success(plotRolls[i]):
                        successes += 1
                    else:
                        failures += 1
                self.outputToHistory("Plot rolls: %d Successes rolled, %d Failures rolled" % (successes, failures), False)
                for i in range(plotsToPlace - self.map[country].numActiveCells()):
                    self.outputToHistory("Cell goes Active", False)
                    self.map[country].sleeperCells -= 1
                    self.map[country].activeCells += 1
                if self.ideology == 1:
                    self.map[country].plots += successes
                    self.outputToHistory("%d Plot(s) placed in %s." % (successes, country), False)
                if self.ideology >= 2:
                    self.map[country].plots += successes * 2
                    self.outputToHistory("%d Plot(s) placed in %s." % (successes * 2, country), False)
                if "Abu Sayyaf" in self.markers and country == "Philippines" and self.map[country].troops() <= self.map[country].totalCells() and successes > 0:
                    self.outputToHistory("Prestige loss due to Abu Sayyaf.", False)
                    self.changePrestige(-successes)
                if "NEST" in self.markers and country == "Unites States":
                    self.outputToHistory("NEST in play. If jihadists have WMD, all plots in the US placed face up.", False)
                self.outputToHistory(self.map[country].countryStr(), True)
                rollPosition += plotsToPlace
        return rollPosition
        
    def handlePlotPriorities(self, countriesDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation = False, isDanishCartoons = False, isKSM = False):
        if isOps:
            if len(countriesDict[FAIR]) > 0:
                targets = countriesDict[FAIR]
                random.shuffle(targets)
                i = 0
                while rollPosition < ops and i < len(targets):
                    rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                    i += 1
            if rollPosition == ops:
                return rollPosition
            if len(countriesDict[GOOD]) > 0:
                targets = countriesDict[GOOD]
                random.shuffle(targets)
                i = 0
                while rollPosition < ops and i < len(targets):
                    rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                    i += 1
            if rollPosition == ops:
                return rollPosition
        else:
            if len(countriesDict[GOOD]) > 0:
                targets = countriesDict[GOOD]
                random.shuffle(targets)
                i = 0
                while rollPosition < ops and i < len(targets):
                    rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                    i += 1
            if rollPosition == ops:
                return rollPosition
            if len(countriesDict[FAIR]) > 0:
                targets = countriesDict[FAIR]
                random.shuffle(targets)
                i = 0
                while rollPosition < ops and i < len(targets):
                    rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                    i += 1
            if rollPosition == ops:
                return rollPosition
        if len(countriesDict[POOR]) > 0:
            targets = countriesDict[POOR]
            random.shuffle(targets)
            i = 0
            while rollPosition < ops and i < len(targets):
                rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                i += 1
        return rollPosition
                
    def executePlot(self, ops, isOps, plotRolls, isMartyrdomOperation = False, isDanishCartoons = False, isKSM = False):
        if not isMartyrdomOperation and not isDanishCartoons and not isKSM:
            self.outputToHistory("* Jihadists Plotting", False)
        # In US
        self.debugPrint("DEBUG: In US")
        rollPosition = self.placePlots("United States", 0, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
        if rollPosition == ops:
            return 0
        if self.prestige >= 4:
            # Prestige high
            self.debugPrint("DEBUG: Prestige high")
            if ("Abu Sayyaf" in self.markers) and ((self.map["Philippines"].totalCells(True)) >= self.map["Philippines"].troops()):
                # In Philippines
                self.debugPrint("DEBUG: Philippines")
                rollPosition = self.placePlots("Philippines", rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                if rollPosition == ops:
                    return 0
            # With troops
            self.debugPrint("DEBUG: troops")
            troopDict = self.getCountriesWithTroopsByGovernance()
            rollPosition = self.handlePlotPriorities(troopDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
            if rollPosition == ops:
                return 0
        # No GWOT Penalty
        if self.gwotPenalty() >= 0:            
            self.debugPrint("DEBUG: No GWOT Penalty")
            postureDict = self.getCountriesWithUSPostureByGovernance()
            rollPosition = self.handlePlotPriorities(postureDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
            if rollPosition == ops:
                return 0
        # With aid
        self.debugPrint("DEBUG: aid")
        aidDict = self.getCountriesWithAidByGovernance()
        rollPosition = self.handlePlotPriorities(aidDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
        if rollPosition == ops:
            return 0
        # Funding < 9
        if self.funding < 9:
            self.debugPrint("DEBUG: Funding < 9")
            nonMuslimDict = self.getNonMuslimCountriesByGovernance()
            rollPosition = self.handlePlotPriorities(nonMuslimDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
            if rollPosition == ops:
                return 0
            muslimDict = self.getMuslimCountriesByGovernance()
            rollPosition = self.handlePlotPriorities(muslimDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
            if rollPosition == ops:
                return 0
        return len(plotRolls) - rollPosition
        
    def handlePlot(self, ops, isOps):
        plotRolls = []
        for i in range(ops):
            plotRolls.append(random.randint(1,6))
        return self.executePlot(ops, isOps, plotRolls)

    def place_cell(self, country_name):
        """Places a cell from the funding track into the given country"""
        country = self.map[country_name]
        country.cadre = 0
        country.sleeperCells += 1
        self.cells -= 1
        self.testCountry(country_name)
        self.outputToHistory("--> Sleeper Cell placed in %s." % country_name, True)
        self.outputToHistory(self.map[country_name].countryStr(), True)

    def handleRadicalization(self, ops):
        self.outputToHistory("* Radicalization with %d ops." % ops, False)
        opsRemaining = ops
    # First box
        if opsRemaining > 0:
            if self.cells > 0:
                country_name = self.randomizer.pick_one(self.map.keys())
                self.place_cell(country_name)
                opsRemaining -= 1
    # Second box
        if opsRemaining > 0:
            if self.cells < 15:
                self.handleTravel(1, True)
                opsRemaining -= 1
    # Third box
        if opsRemaining > 0:
            if self.funding < 9:
                possibles = []
                for country in self.map:
                    if not self.map[country].is_islamist_rule():
                        if (self.map[country].totalCells(True)) > 0:
                            possibles.append(country)
                if len(possibles) > 0:
                    location = random.choice(possibles)
                    self.testCountry(location)
                    self.map[location].plots += 1
                    self.outputToHistory("--> Plot placed in %s." % location, True)
                    opsRemaining -= 1
    # Fourth box
        while opsRemaining > 0:
            possibles = []
            for country in self.map:
                if (self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni") and (self.map[country].is_good() or self.map[country].is_fair()):
                    possibles.append(country)
            if len(possibles) == 0:
                self.outputToHistory("--> No remaining Good or Fair countries.", True)
                break
            else:
                location = random.choice(possibles)
                self.map[location].worsenGovernance()
                self.outputToHistory("--> Governance in %s worsens to %s." % (location, self.map[location].govStr()), True)
                self.outputToHistory(self.map[location].countryStr(), True)
                opsRemaining -= 1
                        
    def resolvePlot(self, country, plotType, postureRoll, usPrestigeRolls, schCountries, schPostureRolls, govRolls, isBacklash = False):
        self.outputToHistory("--> Resolve \"%s\" plot in %s" % (str(plotType), country), False)
        if country == "United States":
            if plotType == "WMD":
                self.gameOver = True
                self.outputToHistory("== GAME OVER - JIHADIST AUTOMATIC VICTORY ==", True)
            else:
                self.funding = 9
                self.outputToHistory("Jihadist Funding now 9", False)
                presMultiplier = 1
                if usPrestigeRolls[0] <= 4:
                    presMultiplier = -1
                self.changePrestige(min(usPrestigeRolls[1], usPrestigeRolls[2]) * presMultiplier)
                self.outputToHistory("US Prestige now %d" % self.prestige, False)    
                if postureRoll <= 4:
                    self.map["United States"].posture = "Soft"
                else:
                    self.map["United States"].posture = "Hard"
                self.outputToHistory("US Posture now %s" % self.map["United States"].posture, True)    
        elif self.map[country].type != "Non-Muslim":
            if not isBacklash:
                if self.map[country].is_good():
                    self.changeFunding(2)
                else:
                    self.changeFunding(1)
                self.outputToHistory("Jihadist Funding now %d" % self.funding, False)
            else:
                if plotType == "WMD":
                    self.funding = 1
                else:
                    self.funding -= 1
                    if self.map[country].is_good():
                        self.funding -= 1
                    if self.funding < 1:
                        self.funding = 1
                self.outputToHistory("BACKLASH: Jihadist Funding now %d" % self.funding, False)
            if self.map[country].troops() > 0:
                if plotType == "WMD":
                    self.prestige = 1
                else:
                    self.prestige -= 1
                if self.prestige < 1:
                    self.prestige = 1
                self.outputToHistory("Troops present so US Prestige now %d" % self.prestige, False)
            if country != "Iran":
                successes = 0
                failures = 0
                for roll in govRolls:
                    if self.map[country].is_non_recruit_success(roll):
                        successes += 1
                    else:
                        failures += 1
                self.outputToHistory("Governance rolls: %d Successes rolled, %d Failures rolled" % (successes, failures), False)
                if self.map[country].aid and successes > 0:
                    self.map[country].aid -= successes    #20150131PS remove 1 aid for each success
                    if self.map[country].aid < 0:
                        self.map[country].aid = 0
                    self.outputToHistory("Aid removed.", False)
                if self.map[country].is_poor() and successes > 0:
                    self.outputToHistory("Governance stays at %s" % self.map[country].govStr(), True)
                while successes > 0 and self.map[country].governance_is_better_than(POOR):
                    self.map[country].worsenGovernance()
                    successes -= 1
                    self.outputToHistory("Governance to %s" % self.map[country].govStr(), True)
        elif self.map[country].type == "Non-Muslim":
            if country == "Israel" and "Abbas" in self.markers:
                self.markers.remove("Abbas")
                self.outputToHistory("Abbas no longer in play.", True)
            if country == "India" and "Indo-Pakistani Talks" in self.markers:
                self.markers.remove("Indo-Pakistani Talks")
                self.outputToHistory("Indo-Pakistani Talks no longer in play.", True)
            if plotType == "WMD":
                self.funding = 9
            else:
                if self.map[country].is_good():
                    self.changeFunding(plotType * 2)
                else:
                    self.changeFunding(plotType)
            self.outputToHistory("Jihadist Funding now %d" % self.funding, False)
            if country != "Israel":
                if postureRoll <= 4:
                    self.map[country].posture = "Soft"
                else:
                    self.map[country].posture = "Hard"
                self.outputToHistory("%s Posture now %s" % (country, self.map[country].posture), True)

            if self.map[country].troops() > 0:
                if plotType == "WMD":
                    self.prestige = 1
                else:
                    self.prestige -= 1
                if self.prestige < 1:
                    self.prestige = 1
                self.outputToHistory("Troops present so US Prestige now %d" % self.prestige, False)


            if self.map[country].schengen:
                for i in range(len(schCountries)):
                    if schPostureRolls[i] <= 4:
                        self.map[schCountries[i]].posture = "Soft"
                    else:
                        self.map[schCountries[i]].posture = "Hard"
                    self.outputToHistory("%s Posture now %s" % (schCountries[i], self.map[schCountries[i]].posture), False)
            self.outputToHistory("", False)
        self.map[country].plots -= 1
        if self.map[country].plots < 0:
            self.map[country].plots = 0
    
    def eventPutsCell(self, cardNum):
        return self.deck[str(cardNum)].putsCell(self)
        
    def playableNonUSEvent(self, cardNum):
        return self.deck[str(cardNum)].type != "US" and  self.deck[str(cardNum)].playable("Jihadist", self, False)

    def playableUSEvent(self, cardNum):
        return self.deck[str(cardNum)].type == "US" and  self.deck[str(cardNum)].playable("US", self, False)
        
    def aiFlowChartTop(self, cardNum):
        self.debugPrint("DEBUG: START")
        self.debugPrint("DEBUG: Playable Non-US event? [1]")
        if self.playableNonUSEvent(cardNum):
            self.debugPrint("DEBUG: YES")
            self.outputToHistory("Playable Non-US Event.", False)
            self.debugPrint("Event Recruits or places cell? [2]")
            if self.eventPutsCell(cardNum):
                self.debugPrint("DEBUG: YES")
                self.debugPrint("Track has cell? [3]")
                if self.cells > 0:
                    self.debugPrint("DEBUG: YES")
                    self.aiFlowChartPlayEvent(cardNum)
                else:
                    self.debugPrint("DEBUG: NO")
                    self.debugPrint("DEBUG: Radicalization [4]")
                    self.handleRadicalization(self.deck[str(cardNum)].ops)
            else:
                self.debugPrint("DEBUG: NO")
                self.aiFlowChartPlayEvent(cardNum)
        else:
            self.debugPrint("DEBUG: NO")
            self.debugPrint("DEBUG: Playble US event? [7]")
            if self.playableUSEvent(cardNum):
                self.debugPrint("DEBUG: YES")
                self.debugPrint("DEBUG: Plot Here [5]")
                self.outputToHistory("Playable US Event.", False)
                unusedOps = self.handlePlot(self.deck[str(cardNum)].ops, True)
                if unusedOps > 0:
                    self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                    self.handleRadicalization(unusedOps)
                self.debugPrint("DEBUG: END")
            else:
                self.debugPrint("DEBUG: NO")
                self.outputToHistory("Unplayable Event. Using Ops for Operations.", False)
                self.aiFlowChartMajorJihad(cardNum)

    def aiFlowChartPlayEvent(self, cardNum):
        self.debugPrint("Play Event [6]")
        self.deck[str(cardNum)].playEvent("Jihadist", self)
        self.debugPrint("Unassociated Event? [8]")
        if self.deck[str(cardNum)].type == "Unassociated":
            self.debugPrint("DEBUG: YES")
            self.outputToHistory("Unassociated event now being used for Ops.", False)
            self.aiFlowChartMajorJihad(cardNum)
        else:
            self.debugPrint("DEBUG: NO")
            self.debugPrint("end [9]")

    def aiFlowChartMajorJihad(self, cardNum):
        self.debugPrint("DEBUG: Major Jihad success possible? [10]")
        country = self.majorJihadChoice(self.deck[str(cardNum)].ops)
        if country:
            self.debugPrint("DEBUG: YES")
            self.debugPrint("DEBUG: Major Jihad [11]")
            unusedOps = self.handleJihad(country, self.deck[str(cardNum)].ops)
            if unusedOps > 0:
                self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                self.handleRadicalization(unusedOps)
        else:
            self.debugPrint("DEBUG: NO")
            self.debugPrint("DEBUG: Jihad possible in Good/Fair? [12]")
            countryList = self.minorJihadInGoodFairChoice(self.deck[str(cardNum)].ops)
            if countryList:
                self.debugPrint("DEBUG: YES")
                unusedOps = self.handleMinorJihad(countryList, self.deck[str(cardNum)].ops)
                if unusedOps > 0:
                    self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                    self.handleRadicalization(unusedOps)
            else:
                self.debugPrint("DEBUG: NO")
                self.debugPrint("DEBUG: Cells Available? [14]")
                if self.numCellsAvailable() > 0:
                    self.debugPrint("DEBUG: YES")
                    self.debugPrint("DEBUG: Recruit [15]")
                    unusedOps = self.handleRecruit(self.deck[str(cardNum)].ops)
                    if unusedOps > 0:
                        self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                        self.handleRadicalization(unusedOps)
                else:
                    self.debugPrint("DEBUG: NO")
                    self.debugPrint("DEBUG: Travel [16]")
                    unusedOps = self.handleTravel(self.deck[str(cardNum)].ops)
                    if unusedOps > 0:
                        self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                        self.handleRadicalization(unusedOps)
                        
    def executeNonMuslimWOI(self, country, postureRoll):
        if postureRoll > 4:
            self.map[country].posture = "Hard"
            self.outputToHistory("* War of Ideas in %s - Posture Hard" % country, False)
            if self.map["United States"].posture == "Hard":
                self.changePrestige(1)
        else:
            self.map[country].posture = "Soft"
            self.outputToHistory("* War of Ideas in %s - Posture Soft" % country, False)
            if self.map["United States"].posture == "Soft":
                self.changePrestige(1)
                
    def executeCardEuroIslam(self, posStr):
        self.map["Benelux"].posture = posStr
        if self.numIslamistRule() == 0:
            self.funding -= 1
            if self.funding < 1:
                self.funding = 1
            self.outputToHistory("Jihadist Funding now %d" % self.funding, False)
        self.outputToHistory(self.map["Benelux"].countryStr(), True)
        
    def executeCardLetsRoll(self, plotCountry, postureCountry, postureStr):
        self.map[plotCountry].plots = max(0, self.map[plotCountry].plots - 1)
        self.outputToHistory("Plot removed from %s." % plotCountry, False)
        self.map[postureCountry].posture = postureStr
        self.outputToHistory("%s Posture now %s." % (postureCountry, postureStr), False)
        self.outputToHistory(self.map[plotCountry].countryStr(), False)
        self.outputToHistory(self.map[postureCountry].countryStr(), True)

    def executeCardHEU(self, country, roll):
        if self.map[country].is_non_recruit_success(roll):
            self.outputToHistory("Add a WMD to available Plots.", True)
        else:
            self.removeCell(country, "Jihadist")    # 20150131PS added side

    def executeCardUSElection(self, postureRoll):
        if postureRoll <= 4:
            self.map["United States"].posture = "Soft"
            self.outputToHistory("United States Posture now Soft.", False)
        else:
            self.map["United States"].posture = "Hard"
            self.outputToHistory("United States Posture now Hard.", False)
        if self.gwotPenalty() == 0:
            self.changePrestige(1)
        else:
            self.changePrestige(-1)
        
    def listCountriesInParam(self, needed = None):
        print ""
        print "Contries"
        print "--------"
        for country in needed:
            self.map[country].printCountry()
        print ""

    def listCountriesWithTroops(self, needed = None):
        print ""
        print "Contries with Troops"
        print "--------------------"
        if needed is None:
            needed = 0
        if self.troops > needed:
            print "Troop Track: %d" % self.troops
        for country in self.map:
            if self.map[country].troops() > needed:
                print "%s: %d" % (country, self.map[country].troops())
        print ""

    def listDeployOptions(self, na = None):
        print ""
        print "Deploy Options"
        print "--------------"
        for country in self.map:
            if self.map[country].is_ally() or ("Abu Sayyaf" in self.markers and country == "Philippines"):
                print "%s: %d troops" % (country, self.map[country].troops())
        print ""

    def listDisruptableCountries(self, na = None):
        print ""
        print "Disruptable Countries"
        print "--------------------"
        for country in self.map:
            if self.map[country].is_disruptable():
                print self.map[country].get_disrupt_summary()
        print ""
        
    def listWoICountries(self, na = None):
        print ""
        print "War of Ideas Eligible Countries"
        print "-------------------------------"
        for country in self.map:
            if self.map[country].is_neutral() or self.map[country].is_ally() or self.map[country].is_ungoverned():
                print "%s, %s %s - %d Active Cells, %d Sleeper Cells, %d Cadre, %d troops" % (country, self.map[country].govStr(), self.map[country].__alignment, self.map[country].activeCells, self.map[country].sleeperCells, self.map[country].cadre, self.map[country].troops())
        for country in self.map:
            if self.map[country].type == "Non-Muslim" and country != "United States" and self.map[country].posture == "Hard":
                print "%s, Posture %s" % (country, self.map[country].posture)
        for country in self.map:
            if self.map[country].type == "Non-Muslim" and country != "United States" and self.map[country].posture == "Soft":
                print "%s, Posture %s" % (country, self.map[country].posture)
        for country in self.map:
            if self.map[country].type == "Non-Muslim" and country != "United States" and self.map[country].posture == "":
                print "%s, Untested" % country
        
    def listPlotCountries(self, na = None):
        print ""
        print "Contries with Active Plots"
        print "--------------------------"
        for country in self.map:
            if self.map[country].plots > 0:
                self.map[country].printCountry()
        print ""
        
    def listIslamistCountries(self, na = None):
        print ""
        print "Islamist Rule Countries"
        print "----------------------"
        for country in self.map:
            if self.map[country].is_islamist_rule():
                self.map[country].printCountry()
        print ""
        
    def listRegimeChangeCountries(self, na = None):
        print ""
        print "Regime Change Countries"
        print "-----------------------"
        for country in self.map:
            if self.map[country].regimeChange > 0:
                self.map[country].printCountry()
        print ""

    def listRegimeChangeWithTwoCells(self, na = None):
        print ""
        print "Regime Change Countries with Two Cells"
        print "---------------------------------------"
        for country in self.map:
            if self.map[country].regimeChange > 0:
                if self.map[country].totalCells() >= 2:
                    self.map[country].printCountry()
        print ""
        
    def listCountriesWithCellAndAdjacentTroops(self, na = None):
        print ""
        print "Countries with Cells and with Troops or adjacent to Troops"
        print "----------------------------------------------------------"
        for country in self.map:
            if self.map[country].totalCells(True) > 0:
                if self.map[country].troops() > 0:
                    self.map[country].printCountry()
                else:
                    for subCountry in self.map:
                        if subCountry != country:
                            if self.map[subCountry].troops() > 0 and self.isAdjacent(country, subCountry):
                                self.map[country].printCountry()
                                break
        print ""

    def listAdversaryCountries(self, na = None):
        print ""
        print "Adversary Countries"
        print "-------------------"
        for country in self.map:
            if self.map[country].is_adversary():
                self.map[country].printCountry()
        print ""
        
    def listGoodAllyPlotCountries(self, na = None):
        print ""
        print "Ally or Good Countries with Plots"
        print "---------------------------------"
        for country in self.map:
            if self.map[country].plots > 0:
                if self.map[country].is_ally() or self.map[country].is_good():
                    self.map[country].printCountry()
        print ""

    def listMuslimCountriesWithCells(self, na = None):
        print ""
        print "Muslim Countries with Cells"
        print "---------------------------"
        for country in self.map:
            if self.map[country].totalCells(True) > 0:
                if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni":
                    self.map[country].printCountry()
        print ""

    def listBesiegedCountries(self, na = None):
        print ""
        print "Besieged Regimes"
        print "----------------"
        for country in self.map:
            if self.map[country].besieged > 0:
                self.map[country].printCountry()
        print ""

    def listShiaMixRegimeChangeCountriesWithCells(self, na = None):
        print ""
        print "Shia-Mix Regime Change Countries with Cells"
        print "-------------------------------------------"
        for country in self.map:
            if self.map[country].type == "Shia-Mix":
                if self.map[country].regimeChange > 0:
                    if (self.map[country].totalCells(True)) > 0:
                        self.map[country].printCountry()
        print ""

    def listShiaMixCountries(self, na = None):
        print ""
        print "Shia-Mix Countries"
        print "------------------"
        for country in self.map:
            if self.map[country].type == "Shia-Mix":
                self.map[country].printCountry()
        print ""

    def listShiaMixCountriesWithCellsTroops(self, na = None):
        print ""
        print "Shia-Mix Countries with Cells and Troops"
        print "----------------------------------------"
        for country in self.map:
            if self.map[country].type == "Shia-Mix":
                if self.map[country].troops() > 0 and self.map[country].totalCells() > 0:
                    self.map[country].printCountry()
        print ""

    def listSchengenCountries(self, na = None):
        print ""
        print "Schengen Countries"
        print "------------------"
        for country in self.map:
            if self.map[country].schengen > 0:
                self.map[country].printCountry()
        print ""

    def listHambali(self, na = None):
        print ""
        print "Indonesia or adjacent country with cell and Ally or Hard"
        print "--------------------------------------------------------"
        possibles = ["Indonesia/Malaysia"]
        for countryObj in self.map["Indonesia/Malaysia"].links:
            possibles.append(countryObj.name)
        for country in possibles:
            if self.map[country].totalCells(True) > 0:
                if self.map[country].type == "Non-Muslim":
                    if self.map[country].posture == "Hard":
                        self.map[country].printCountry()
                else:
                    if self.map[country].is_ally():
                        self.map[country].printCountry()

    def do_status(self, country_name):
        
        if country_name:
            goodCountry = False
            possible = []
            for country in self.map:
                if country_name.lower() == country.lower():
                    possible = [country]
                    break
                elif country_name.lower() in country.lower():
                    possible.append(country)
            if len(possible) == 0:
                print "Unrecognized country."
                print ""
            elif len(possible) > 1:
                print "Be more specific", possible
                print ""
            else:
                goodCountry = possible[0]
            
            if goodCountry:
                self.map[goodCountry].printCountry()
                return
            else:
                return
            
        
        goodRes = 0
        islamRes = 0
        goodC = 0
        islamC = 0
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni": 
                if self.map[country].is_good():
                    goodC += 1
                    goodRes += self.countryResources(country)
                elif self.map[country].is_fair():
                    goodC += 1
                elif self.map[country].is_poor():
                    islamC += 1
                elif self.map[country].is_islamist_rule():
                    islamC += 1
                    islamRes += self.countryResources(country)
            elif self.map[country].type != "Iran" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        print ""
        print "GOOD GOVERNANCE"
        num = 0
        for country in self.map:
            if self.map[country].type != "Non-Muslim" and self.map[country].is_good():
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "FAIR GOVERNANCE"
        num = 0
        for country in self.map:
            if self.map[country].type != "Non-Muslim" and self.map[country].is_fair():
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "POOR GOVERNANCE"
        num = 0
        for country in self.map:
            if self.map[country].type != "Non-Muslim" and self.map[country].is_poor():
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "ISLAMIST RULE"
        num = 0
        for country in self.map:
            if self.map[country].type != "Non-Muslim" and self.map[country].is_islamist_rule():
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""

        # 20150131PS Start

        print "UNTESTED WITH DATA"
        num = 0
        for country in self.map:
            if self.map[country].is_ungoverned()    \
            and (self.map[country].troopCubes != 0  \
            or self.map[country].activeCells != 0   \
            or self.map[country].sleeperCells != 0  \
            or self.map[country].aid != 0           \
            or self.map[country].besieged != 0      \
            or self.map[country].regimeChange != 0  \
            or self.map[country].cadre != 0         \
            or self.map[country].plots != 0         \
            or len(self.map[country].markers) != 0 ):
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""

        # 20150131PS End

        print "HARD POSTURE"
        num = 0
        for country in self.map:
            if self.map[country].posture == "Hard":
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "SOFT POSTURE"
        num = 0
        for country in self.map:
            if self.map[country].posture == "Soft":
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "PLOTS"
        plotCountries = 0
        for country in self.map:
            if self.map[country].plots > 0:
                plotCountries += 1
                print "%s: %d plot(s)" % (country, self.map[country].plots)
        if plotCountries == 0:
            print "No Plots"
        print ""
        print "VICTORY"
        print "Good Resources   : %d" % goodRes
        print "Islamist Resources: %d" % islamRes
        print "---"
        print "Good/Fair Countries   : %d" % goodC
        print "Poor/Islamist Countries: %d" % islamC
        print ""
        print "GWOT"
        print "US Posture: %s" % self.map["United States"].posture
        if worldPos > 0:
            worldPosStr = "Hard"
        elif worldPos < 0:
            worldPosStr = "Soft"
        else:
            worldPosStr = "Even"
        print "World Posture: %s %d" % (worldPosStr, abs(worldPos))
        print "US Prestige: %d" % self.prestige
        print ""
        print "TROOPS"
        if self.troops >= 10:
            print "Low Intensity: %d troops available" % self.troops
        elif self.troops >= 5:
            print "War: %d troops available" % self.troops
        else:
            print "Overstretch: %d troops available" % self.troops
        print ""
        print "JIHADIST FUNDING"
        print "Funding: %d" % self.funding
        print "Cells Available: %d" % self.cells
        print ""
        print "EVENTS"
        if len(self.markers) == 0:
            print "Markers: None"
        else:
            print "Markers: %s" % ", ".join(self.markers)
        if len(self.lapsing) == 0:
            print "Lapsing: None"
        else:
            print "Lapsing: %s" % ", ".join(self.lapsing)
        print ""
        print "DATE"
        print "%d (Turn %s)" % (self.startYear + (self.turn - 1), self.turn)
        print ""
        
    @staticmethod
    def help_status():
        print "Display game status.  status [country] will print out status of single country.\n"

    def do_sta(self, rest):
        """Alias for the 'status' command"""
        self.do_status(rest)
        
    def help_sta(self):
        self.help_status()

# 20150131PS Start

    def do_summary(self, rest):
        
        goodRes = 0
        islamRes = 0
        goodC = 0
        islamC = 0
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni": 
                if self.map[country].is_good():
                    goodC += 1
                    goodRes += self.countryResources(country)
                elif self.map[country].is_fair():
                    goodC += 1
                elif self.map[country].is_poor():
                    islamC += 1
                elif self.map[country].is_islamist_rule():
                    islamC += 1
                    islamRes += self.countryResources(country)
            elif self.map[country].type != "Iran" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        print ""
        if self.ideology == 1:
            print "Jihadist Ideology: Normal"
        elif self.ideology == 2:
            print "Jihadist Ideology: Coherent"
        elif self.ideology == 3:
            print "Jihadist Ideology: Attractive"
        elif self.ideology == 4:
            print "Jihadist Ideology: Potent"
        elif self.ideology == 5:
            print "Jihadist Ideology: Infectious"
        elif self.ideology == 6:
            print "Jihadist Ideology: Virulent"
        print ""
        print "VICTORY"
        print "Good Resources: %d    Islamist Resources: %d" % (goodRes, islamRes)
        print "Good/Fair Countries: %d   Poor/Islamist Countries: %d" % (goodC, islamC)
        print ""
        if worldPos > 0:
            worldPosStr = "Hard"
        elif worldPos < 0:
            worldPosStr = "Soft"
        else:
            worldPosStr = "Even"
        print "GWOT"
        print "US Posture: %s    World Posture: %s %d" % (self.map["United States"].posture, worldPosStr, abs(worldPos))
        print "US Prestige: %d" % self.prestige
        print ""
        print "TROOPS"
        if self.troops >= 10:
            print "Low Intensity: %d troops available" % self.troops
        elif self.troops >= 5:
            print "War: %d troops available" % self.troops
        else:
            print "Overstretch: %d troops available" % self.troops
        print ""
        print "JIHADIST FUNDING"
        print "Funding: %d    Cells Available: %d" % (self.funding, self.cells)
        print ""
        print "EVENTS"
        if len(self.markers) == 0:
            print "Markers: None"
        else:
            print "Markers: %s" % ", ".join(self.markers)
        if len(self.lapsing) == 0:
            print "Lapsing: None"
        else:
            print "Lapsing: %s" % ", ".join(self.lapsing)
        print ""
        
    @staticmethod
    def help_summary():
        print "Display summary of game status.\n"

    def do_sum(self, rest):
        self.do_summary(rest)
        
    def help_sum(self):
        self.help_summary()

    @staticmethod
    def help_adjust():
        print "Adjust game settings - no rule checking applied.\n"

    def help_adj(self):
        self.help_adjust()
        
    def getAdjustFromUser(self):
        while True:
            input_str = self.my_raw_input("Enter 'ideology', 'prestige', 'funding', 'lapsing', 'marker' or country ?: ")
            if input_str == "":
                return ""
            if input_str.lower() == "ideology" or input_str.lower() == "ide" :
                return "ideology"
            if input_str.lower() == "prestige" or input_str.lower() == "pre" :
                return "prestige"
            if input_str.lower() == "funding" or input_str.lower() == "fun" :
                return "funding"
            if input_str.lower() == "lapsing" or input_str.lower() == "lap" :
                return "lapsing"
            if input_str.lower() == "marker" or input_str.lower() == "mar" :
                return "marker"
            possible = []
            for country in self.map:
                if input_str.lower() == country.lower():
                    possible = [country]
                    break
                elif input_str.lower() in country.lower():
                    possible.append(country)
            if len(possible) == 0:
                print "Unrecognized response."
                print ""
            elif len(possible) > 1:
                print "Be more specific", possible
                print ""
            else:
                return possible[0]

    def getAdjustIdeology(self):
        while True:
            print "Ideologies are:"
            print "(1) Normal"
            print "(2) Coherent:   Plot success places 2 Plots"
            print "(3) Attractive: ...and Recruit success places 2 cells"
            print "(4) Potent:     ...and Major Jihad if 3 or more cells than troops"
            print "(5) Infectious: ...and US plays all its cards (not enforced by program)"
            print "(6) Virulent:   ...and Jihad failure does not remove cells"
            input_str = self.my_raw_input("Enter new ideology (1-6): ")
            if input_str == "":
                return ""
            try:
                input_int = int(input_str)
                if input_int < 1 or input_int > 6:
                    print "Invalid prestige value - ", input_int
                else:
                    return input_int
            except:
                print "Invalid ideology value - ", input_str
            
    def adjustIdeology(self):
        print "Adjusting ideology"
        adjustIdeologyResp = self.getAdjustIdeology()
        if adjustIdeologyResp:
            self.ideology = adjustIdeologyResp
        else:
            print "Prestige unchanged"

    def getAdjustPrestige(self):
        while True:
            prestige_str = self.my_raw_input("Enter new prestige (1-12): ")
            if prestige_str == "":
                return ""
            try:
                prestige = int(prestige_str)
                if prestige < 1 or prestige > 12:
                    print "Invalid prestige value -", prestige
                else:
                    return prestige
            except ValueError:
                print "Invalid prestige value -", prestige_str
            
    def adjustPrestige(self):
        print "Adjusting prestige"
        adjustPrestigeResp = self.getAdjustPrestige()
        if adjustPrestigeResp:
            self.changePrestige(adjustPrestigeResp - self.prestige)
        else:
            print "Prestige unchanged"

    def getAdjustFunding(self):
        while True:
            funding_str = self.my_raw_input("Enter new funding (1-9): ")
            if funding_str == "":
                return ""
            try:
                funding = int(funding_str)
                if funding < 1 or funding > 9:
                    print "Invalid funding value -", funding
                else:
                    return funding
            except ValueError:
                print "Invalid funding value -", funding_str
            
    def adjustFunding(self):
        print "Adjusting funding"
        adjustFundResp = self.getAdjustFunding()
        if adjustFundResp:
            self.changeFunding(adjustFundResp - self.funding)
        else:
            print "Funding unchanged"

    def adjustLapsing(self):
        print "Adjusting lapsing event"
        if len(self.lapsing) == 0:
            print "There are no lapsing events"
        else:
            print "Current lapsing events: %s" % ", ".join(self.lapsing)
        print ""
        print "Available lapsing events are:"
        for validEvent in self.validLapsingMarkers:
            print validEvent
        print "Enter a new event to add it to the list or enter an existing event to remove it:"
        while True:
            event = self.my_raw_input("Enter event to be added or removed: ")
            if event == "":
                return ""
            if event in self.lapsing:
                self.lapsing.remove(event)
                print "Removed lapsing event -", event
                break
            elif event in self.validLapsingMarkers:
                self.lapsing.append(event)
                print "Added lapsing event -", event
                break
            else:
                print "Not a valid event"
        if len(self.lapsing) == 0:
            print "There are now no lapsing events"
        else:
            print "Current lapsing events: %s" % ", ".join(self.lapsing)
        print ""
                
    def adjustMarker(self):
        print "Adjusting event markers in play"
        if len(self.markers) == 0:
            print "There are no event markers in play"
        else:
            print "Current events in play: %s" % ", ".join(self.markers)
        print ""
        print "Available global events are:"
        for validEvent in self.validGlobalMarkers:
            print validEvent
        print "Enter a new event to add it to the list or enter an existing event to remove it"
        while True:
            event = self.my_raw_input("Enter event to be added or removed: ")
            if event == "":
                return ""
            if event in self.markers:
                self.markers.remove(event)
                print "Removed event -", event
                break
            elif event in self.validGlobalMarkers:
                self.markers.append(event)
                print "Added event -", event
                break
            else:
                print "Not a valid event"
        if len(self.markers) == 0:
            print "There are now no events in play"
        else:
            print "Current events in play: %s" % ", ".join(self.markers)
        print ""
                
    def adjustCountryGovernance(self, country):
        print "Adjusting governance for -", country
        while True:
            gov_str = self.my_raw_input("Enter governance (0-4) (0 = untested): ")
            if gov_str == "":
                return False
            try:
                gov_num = int(gov_str)
                self.map[country].make_governance(Governances.with_index(gov_num))
                print "Changing governance to", gov_num
                return True
            except ValueError:
                print "Invalid governance value -", gov_str
    
    def adjustCountryAlignment(self, country):
        print "Adjusting alignment for -", country
        while True:
            alignment = self.my_raw_input("Enter alignment ('Ally', 'Neutral', 'Adversary'): ")
            if alignment == "":
                return False
            if alignment == "Adversary":
                print "Changing alignment to Adversary"
                self.map[country].make_adversary()
                return True
            if alignment == "Ally":
                print "Changing alignment to Ally"
                self.map[country].make_ally()
                return True
            if alignment == "Neutral":
                print "Changing alignment to Neutral"
                self.map[country].make_neutral()
                return True
            print "Invalid alignment value -", alignment
    
    def adjustCountryPosture(self, country):
        """Prompts the user to set the posture of the given country (returns true if successful)"""
        print "Adjusting posture for -", country
        while True:
            posture = self.my_raw_input("Enter posture ('Hard', 'Soft', 'Untested'): ")
            if posture == "":  # User aborted
                return False
            if posture.lower() == "hard":
                print "Changing posture to Hard"
                self.map[country].make_hard()
                return True
            if posture.lower() == "soft":
                print "Changing posture to Soft"
                self.map[country].make_soft()
                return True
            if posture.lower() == "untested":
                print "Changing posture to Untested"
                self.map[country].remove_posture()
                return True
            print "Invalid posture value '{}'".format(posture)
            return False

    def adjustCountryTroops(self, country):
        print "Adjusting troops for - ", country
        if 'NATO' in self.map[country].markers:
            print "NATO contributes 2 troops to count, actual troop cubes are ", self.map[country].troopcubes
        while True:
            troop_str = self.my_raw_input("Enter new troop count (0-15): ")
            if troop_str == "":
                return False
            try:
                troops = int(troop_str)
                if troops < 0 or troops > 15:
                    print "Invalid troop cube value -", troops
                else:
                    print "Changing troop cubes to", troops
                    troopChange = troops - self.map[country].troopCubes
                    self.troops -= troopChange
                    self.map[country].troopCubes = troops
                    if self.troops < 0 or self.troops > 15:
                        print "WARNING! Troop track count is now ", self.troops
                    else:
                        print "Troop track count is now ", self.troops
                    return True
            except ValueError:
                print "Invalid troop cube value -", troop_str

    def adjustCountryActive(self, country):
        print "Adjusting active cells for - ", country
        while True:
            cell_str = self.my_raw_input("Enter new active cell count (0-15): ")
            if cell_str == "":
                return False
            try:
                cells = int(cell_str)
                if cells < 0 or cells > 15:
                    print "Invalid active cell value -", cells
                else:
                    print "Changing active cells to ", cells
                    activeChange = cells - self.map[country].activeCells
                    self.cells -= activeChange
                    self.map[country].activeCells = cells
                    if self.cells < 0 or self.cells > 15:
                        print "WARNING! Cell count on funding track is now ", self.cells
                    else:
                        print "Cell count on funding track is now ", self.cells
                    return True
            except ValueError:
                print "Invalid active cell value -", cell_str
    
    def adjustCountrySleeper(self, country):
        print "Adjusting sleeper cells for - ", country
        while True:
            cell_str = self.my_raw_input("Enter new sleeper cell count (0-15): ")
            if cell_str == "":
                return False
            try:
                cells = int(cell_str)
                if cells < 0 or cells > 15:
                    print "Invalid sleeper cell value -", cells
                else:
                    print "Changing sleeper cells to", cells
                    sleeperChange = cells - self.map[country].sleeperCells
                    self.cells -= sleeperChange
                    self.map[country].sleeperCells = cells
                    if self.cells < 0 or self.cells > 15:
                        print "WARNING! Cell count on funding track is now ", self.cells
                    else:
                        print "Cell count on funding track is now ", self.cells
                    return True
            except ValueError:
                print "Invalid sleeper cell value -", cell_str
    
    def adjustCountryCadre(self, country):
        print "Adjusting cadre for - ", country
        while True:
            cadre_str = self.my_raw_input("Enter new cadre count (0-1): ")
            if cadre_str == "":
                return False
            try:
                cadres = int(cadre_str)
                if cadres < 0 or cadres > 1:
                    print "Invalid cadre value -", cadres
                else:
                    print "Changing cadre count to", cadres
                    self.map[country].cadre = cadres
                    return True
            except ValueError:
                print "Invalid cadre value -", cadre_str
    
    def adjustCountryAid(self, country):
        print "Adjusting aid for - ", country
        while True:
            aid_str = self.my_raw_input("Enter new aid count (0-9): ")
            if aid_str == "":
                return False
            try:
                aid = int(aid_str)
                if aid < 0 or aid > 9:
                    print "Invalid aid value -", aid
                else:
                    print "Changing aid count to", aid
                    self.map[country].aid = aid
                    return True
            except:
                print "Invalid aid value -", aid_str
    
    def adjustCountryBesieged(self, country):
        print "Adjusting besieged for - ", country
        while True:
            input = self.my_raw_input("Enter new besieged count (0-1): ")
            if input == "":
                return False
            try:
                input = int(input)
                if input < 0 or input > 1:
                    print "Invalid besieged value - ", input
                else:
                    print "Changing besieged count to ", input
                    self.map[country].besieged = input
                    return True
            except:
                print "Invalid besieged value - ", input
    
    def adjustCountryRegime(self, country):
        print "Adjusting regime change for - ", country
        while True:
            input = self.my_raw_input("Enter new regime change count (0-1): ")
            if input == "":
                return False
            try:
                input = int(input)
                if input < 0 or input > 1:
                    print "Invalid regime change value - ", input
                else:
                    print "Changing regime change count to ", input
                    self.map[country].regimeChange = input
                    return True
            except:
                print "Invalid regime change value - ", input
    
    def adjustCountryPlots(self, country):
        print "Adjusting plots for - ", country
        while True:
            input = self.my_raw_input("Enter new plot count (0-9): ")
            if input == "":
                return False
            try:
                input = int(input)
                if input < 0 or input > 9:
                    print "Invalid plot value - ", input
                else:
                    print "Changing plot count to ", input
                    self.map[country].plots = input
                    return True
            except:
                print "Invalid plot value - ", input
    
    def adjustCountryMarker(self, country):
        print "Adjusting event markers for - ", country
        if len(self.map[country].markers) == 0:
            print "There are no event markers in play"
        else:
            print "Current events in play: %s" % ", ".join(self.map[country].markers)
        print ""
        print "Available country events are:"
        for validEvent in self.validCountryMarkers:
            print validEvent
        print "Enter a new event to add it to the list or enter an existing event to remove it"
        while True:
            input = self.my_raw_input("Enter event to be added or removed: ")
            if input == "":
                return ""
            if input in self.map[country].markers:
                self.map[country].markers.remove(input)
                print "Removed event - ", input
                break
            elif input in self.validCountryMarkers:
                self.map[country].markers.append(input)
                print "Added event - ", input
                break
            else:
                print "Not a valid event"
        if len(self.map[country].markers) == 0:
            print "There are now no events in play"
        else:
            print "Current events in play: %s" % ", ".join(self.map[country].markers)
        print ""
        return True

    def adjustCountry(self, country):
        print "Adjusting country - ", country
        self.map[country].printCountry()
        if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni":
            adjustAttrList = "governance", "alignment", "troops", "active", "sleeper", "cadre", "aid", "besieged", "regime", "plots", "marker"
        elif self.map[country].name == "Philippines":
            adjustAttrList = "posture", "troops", "active", "sleeper", "cadre", "plots", "marker"
        elif self.map[country].type == "Non-Muslim": 
            adjustAttrList = "posture", "active", "sleeper", "cadre", "plots", "marker"
        elif self.map[country].type == "Iran":
            adjustAttrList =  "active", "sleeper", "cadre", "plots", "marker"
        goodAdjustAttr = None
        while not goodAdjustAttr:
            print "Changeable attributes are: %s" % ", ".join(adjustAttrList)
            input = self.my_raw_input("Enter attribute to be changed: ")
            if input == "":
                return ""
            if input in adjustAttrList:
                adjustSuccess = False
                if input == "governance":
                    adjustSuccess = self.adjustCountryGovernance(country)
                elif input == "alignment":
                    adjustSuccess = self.adjustCountryAlignment(country)
                elif input == "posture":
                    adjustSuccess = self.adjustCountryPosture(country)
                elif input == "troops":
                    adjustSuccess = self.adjustCountryTroops(country)
                elif input == "active":
                    adjustSuccess = self.adjustCountryActive(country)
                elif input == "sleeper":
                    adjustSuccess = self.adjustCountrySleeper(country)
                elif input == "cadre":
                    adjustSuccess = self.adjustCountryCadre(country)
                elif input == "aid":
                    adjustSuccess = self.adjustCountryAid(country)
                elif input == "besieged":
                    adjustSuccess = self.adjustCountryBesieged(country)
                elif input == "regime":
                    adjustSuccess = self.adjustCountryRegime(country)
                elif input == "plots":
                    adjustSuccess = self.adjustCountryPlots(country)
                elif input == "marker":
                    adjustSuccess = self.adjustCountryMarker(country)
                if adjustSuccess:
                    self.map[country].printCountry()
                else:
                    print country, "unchanged"
            else:
                print "Invalid attribute - ", input
        
    def do_adjust(self, rest):
        print "Warning! No cross validation of data changes is carried out"
        print "Start adjusting"
        adjustType = self.getAdjustFromUser()
        if adjustType == "":
            print ""
            return
        elif adjustType == "ideology":
            self.adjustIdeology()
        elif adjustType == "prestige":
            self.adjustPrestige()
        elif adjustType == "funding":
            self.adjustFunding()
        elif adjustType == "lapsing":
            self.adjustLapsing()
        elif adjustType == "marker":
            self.adjustMarker()
        else:
            self.adjustCountry(adjustType)
        print ""

    def do_adj(self, rest):
        self.do_adjust(rest)

    def do_history(self,rest):
        
        if rest == 'save':
            f = open('history.txt','w')
            for str in self.history:
                f.write(str + "\r\n")
            f.close()
        
        for str in self.history:
            print str
        print ""

    @staticmethod
    def help_history():
        print "Display Game History.  Type 'history save' to save history to a file called history.txt.\n"

    def do_his(self, rest):
        self.do_history(rest)
        
    def help_his(self):
        self.help_history()

    def do_deploy(self, rest):
        moveFrom = None
        available = 0
        while not moveFrom:
            input = self.getCountryFromUser("From what country (track for Troop Track) (? for list)?: ",  "track", self.listCountriesWithTroops)    
            if input == "":
                print ""
                return
            elif input == "track":
                if self.troops <= 0:
                    print "There are no troops on the Troop Track."
                    print ""
                    return
                else:
                    print "Deploy from Troop Track - %d available" % self.troops
                    print ""
                    available = self.troops
                    moveFrom = input
            else:
                if self.map[input].troops() <= 0:
                    print "There are no troops in %s." % input
                    print ""
                    return
                else:
                    print "Deploy from %s = %d available" % (input, self.map[input].troops())
                    print ""
                    available = self.map[input].troops()
                    moveFrom = input
        moveTo = None
        while not moveTo:
            input = self.getCountryFromUser("To what country (track for Troop Track)  (? for list)?: ",  "track", self.listDeployOptions)    
            if input == "":
                print ""
                return
            elif input == "track":
                print "Deploy troops from %s to Troop Track" % moveFrom
                print ""
                moveTo = input
            else:
                print "Deploy troops from %s to %s" % (moveFrom, input)
                print ""
                moveTo = input
        howMany = 0
        while not howMany:
            input = self.getNumTroopsFromUser("Deploy how many troops (%d available)? " % available, available)
            if input == "":
                print ""
                return
            else:
                howMany = input
        if moveFrom == "track":
            self.troops -= howMany
            troopsLeft = self.troops
        else:
            if self.map[moveFrom].regimeChange:
                if (self.map[moveFrom].troops() - howMany) < (5 + self.map[moveFrom].totalCells(True)):
                    print "You cannot move that many troops from a Regime Change country."
                    print ""
                    return
            self.map[moveFrom].changeTroops(-howMany)
            troopsLeft = self.map[moveFrom].troops()
        if moveTo == "track":
            self.troops += howMany
            troopsNow = self.troops
        else:
            self.map[moveTo].changeTroops(howMany)
            troopsNow = self.map[moveTo].troops()
        self.outputToHistory("* %d troops deployed from %s (%d) to %s (%d)" % (howMany, moveFrom, troopsLeft, moveTo, troopsNow))
        
    @staticmethod
    def help_deploy():
        print "Move Troops\n"

    def do_dep(self, rest):
        self.do_deploy(rest)
        
    def help_dep(self):
        self.help_deploy()      # 20150131PS - fixed method name
        
    def do_disrupt(self, rest):
        where = None
        sleepers = 0
        actives = 0
        while not where:
            input = self.getCountryFromUser("Disrupt what country?  (? for list): ",  "XXX", self.listDisruptableCountries)    
            if input == "":
                print ""
                return
            else:
                if self.map[input].sleeperCells + self.map[input].activeCells <= 0 and self.map[input].cadre <= 0:
                    print "There are no cells or cadre in %s." % input
                    print ""
                elif "FATA" in self.map[input].markers and self.map[input].regimeChange == 0:
                    print "No disrupt allowed due to FATA."
                    print ""
                elif self.map[input].troops() > 0 or self.map[input].type == "Non-Muslim" or self.map[input].is_ally():
                    print ""
                    where = input
                    sleepers = self.map[input].sleeperCells
                    actives = self.map[input].activeCells
                else:
                    print "You can't disrupt there."
                    print ""
        self.handleDisrupt(where)

    @staticmethod
    def help_disrupt():
        print "Disrupt Cells or Cadre.\n"

    def do_dis(self, rest):
        self.do_disrupt(rest)
                
    def help_dis(self):
        self.help_disrupt()
        
    def do_woi(self, rest):
        where = None
        while not where:
            input = self.getCountryFromUser("War of Ideas in what country?  (? for list): ", "XXX", self.listWoICountries)
            if input == "":
                print ""
                return
            else:
                if self.map[input].type == "Non-Muslim" and input != "United States":
                    where = input
                elif self.map[input].is_ally() or self.map[input].is_neutral() or self.map[input].is_ungoverned():
                    where = input
                else:
                    print "Country not eligible for War of Ideas."
                    print ""
        if self.map[where].type == "Non-Muslim" and input != "United States":  # Non-Muslim
            postureRoll = self.getRollFromUser("Enter Posture Roll or r to have program roll: ")
            if postureRoll > 4:
                self.map[where].posture = "Hard"
                self.outputToHistory("* War of Ideas in %s - Posture Hard" % where)
                if self.map["United States"].posture == "Hard":
                    self.prestige += 1
                    if self.prestige > 12:
                        self.prestige = 12
                    self.outputToHistory("US Prestige now %d" % self.prestige)
            else:
                self.map[where].posture = "Soft"
                self.outputToHistory("* War of Ideas in %s - Posture Soft" % where)
                if self.map["United States"].posture == "Soft":
                    self.prestige += 1
                    if self.prestige > 12:
                        self.prestige = 12
                    self.outputToHistory("US Prestige now %d" % self.prestige)
        else:  # Muslim
            self.testCountry(where)
            woiRoll = self.getRollFromUser("Enter WoI roll or r to have program roll: ")
            modRoll = self.modifiedWoIRoll(woiRoll, where)
            self.outputToHistory("Modified Roll: %d" % modRoll)
            self.handleMuslimWoI(modRoll, where)
                
    @staticmethod
    def help_woi():
        print "Conduct War of Ideas operation.\n"
        
    def do_alert(self, rest):
        where = None
        while not where:
            input = self.getCountryFromUser("Alert in what country?  (? for list): ", "XXX", self.listPlotCountries)
            if input == "":
                print ""
                return
            else:
                if self.map[input].plots < 1:
                    print "Country has not plots."
                    print ""
                else:
                    where = input
        self.handleAlert(where)
                    
    @staticmethod
    def help_alert():
        print "Alert an active Plot.\n"

    def do_alr(self, rest):
        self.do_alert(rest)
                
    def help_alr(self):
        self.help_alert()
        
    def do_reassessment(self, rest):
        self.handleReassessment()
                    
    @staticmethod
    def help_reassessment():
        print "Reassessment of US Posture.\n"

    def do_rea(self, rest):
        self.do_reassessment(rest)
                
    def help_rea(self):
        self.help_reassessment()

    def do_regime(self, rest):
        if self.map["United States"].posture == "Soft":
            print "No Regime Change with US Posture Soft"
            print ""
            return
        where = None
        while not where:
            input = self.getCountryFromUser("Regime Change in what country?  (? for list): ", "XXX", self.listIslamistCountries)
            if input == "":
                print ""
                return
            else:
                if (self.map[input].is_islamist_rule()) or (input == "Iraq" and "Iraqi WMD" in self.markers) or (input == "Libya" and "Libyan WMD" in self.markers):
                    where = input
                else:
                    print "Country not Islamist Rule."
                    print ""
        moveFrom = None
        available = 0
        while not moveFrom:
            input = self.getCountryFromUser("Deploy 6+ troops from what country (track for Troop Track) (? for list)?: ",  "track", self.listCountriesWithTroops, 6)    
            if input == "":
                print ""
                return
            elif input == "track":
                if self.troops <= 6:
                    print "There are not enough troops on the Troop Track."
                    print ""
                    return
                else:
                    print "Deploy from Troop Track - %d available" % self.troops
                    print ""
                    available = self.troops
                    moveFrom = input
            else:
                if self.map[input].troops() <= 6:
                    print "There are not enough troops in %s." % input
                    print ""
                    return
                else:
                    print "Deploy from %s = %d available" % (input, self.map[input].troops())
                    print ""
                    available = self.map[input].troops()
                    moveFrom = input
        howMany = 0
        while not howMany:
            input = self.getNumTroopsFromUser("Deploy how many troops (%d available)? " % available, available)
            if input == "":
                print ""
                return
            elif input < 6:
                print "At least 6 troops needed for Regime Change"
            else:
                howMany = input
        govRoll = self.getRollFromUser("Enter Governance roll or r to have program roll: ")
        preFirstRoll = self.getRollFromUser("Enter first die (Raise/Drop) for Prestige roll or r to have program roll: ")
        preSecondRoll = self.getRollFromUser("Enter second die for Prestige roll or r to have program roll: ")
        preThirdRoll = self.getRollFromUser("Enter third die for Prestige roll or r to have program roll: ")
        self.handleRegimeChange(where, moveFrom, howMany, govRoll, (preFirstRoll, preSecondRoll, preThirdRoll))
        
    @staticmethod
    def help_regime():
        print "Regime Change in Islamist Rule Country.\n"
                
    def do_reg(self, rest):
        self.do_regime(rest)
                
    def help_reg(self):
        self.help_regime()
        
    def do_withdraw(self, rest):
        if self.map["United States"].posture == "Hard":
            print "No Withdrawal with US Posture Hard"
            print ""
            return
        moveFrom = None
        available = 0
        while not moveFrom:
            input = self.getCountryFromUser("Withdrawal in what country?  (? for list): ", "XXX", self.listRegimeChangeCountries)
            if input == "":
                print ""
                return
            else:
                if self.map[input].regimeChange > 0:
                    moveFrom = input
                    available = self.map[input].troops()
                else:
                    print "Country not Regime Change."
                    print ""
        moveTo = None
        while not moveTo:
            input = self.getCountryFromUser("To what country (track for Troop Track)  (? for list)?: ",  "track", self.listDeployOptions)    
            if input == "":
                print ""
                return
            elif input == "track":
                print "Withdraw troops from %s to Troop Track" % moveFrom
                print ""
                moveTo = input
            else:
                print "Withdraw troops from %s to %s" % (moveFrom, input)
                print ""
                moveTo = input
        howMany = 0
        while not howMany:
            input = self.getNumTroopsFromUser("Withdraw how many troops (%d available)? " % available, available)
            if input == "":
                print ""
                return
            else:
                howMany = input
        preFirstRoll = self.getRollFromUser("Enter first die (Raise/Drop) for Prestige roll or r to have program roll: ")
        preSecondRoll = self.getRollFromUser("Enter second die for Prestige roll or r to have program roll: ")
        preThirdRoll = self.getRollFromUser("Enter third die for Prestige roll or r to have program roll: ")
        self.handleWithdraw(moveFrom, moveTo, howMany, (preFirstRoll, preSecondRoll, preThirdRoll))

    @staticmethod
    def help_withdraw():
        print "Withdraw Troops from Regime Change Country.\n"
                
    def do_wit(self, rest):
        self.do_withdraw(rest)
                
    def help_wit(self):
        self.help_withdraw()
        
    def do_j(self, rest):
        cardNum = None
        try:
            input = int(rest)
            if input < 1 or input > 120:
                print "Enter j then the card number e.g. j 24"
                print ""
                return
            else:
                cardNum = input
        except:
            print "Enter j then the card number e.g. j 24"
            print ""
            return
        self.SaveUndo()
        self.outputToHistory("", False)
        self.outputToHistory("== Jihadist plays %s - %d Ops ==" % (self.deck[str(cardNum)].name, self.deck[str(cardNum)].ops), True)

        self.aiFlowChartTop(cardNum)
        
    ''' test with timing system
    def do_j(self, rest):
        if self.phase != "Jihadist Action Phase":
            print "It is not the Jihadist Action Phase"
            print ""
            return
        if rest == "p" or rest == "pass":
            self.phase = "US Action Phase"
            self.outputToHistory("== Jihadist player passes turn. ==", True)
            return
        cardNum = None
        try:
            input = int(rest)
            if input < 1 or input > 120:
                print "Enter j then the card number or pass e.g. j 24 or j pass"
                print ""
                return
            else:
                cardNum = input
        except:
            print "Enter j then the card number or pass e.g. j 24 or j pass"
            print ""
            return
        self.jCard += 1
        self.outputToHistory("== Jihadist plays %s. ==" % self.deck[str(cardNum)].name, True)
        self.aiFlowChartTop(cardNum)
        if self.jCard
    '''    

    @staticmethod
    def help_j():
        print "Enter the number of the Jihadist card when it is their card play.\n"

    def do_u(self, rest):
        cardNum = None
        try:
            input = int(rest)
            if input < 1 or input > 120:
                print "Enter u then the card number e.g. u 24"
                print ""
                return
            else:
                cardNum = input
        except:
            print "Enter u then the card number e.g. u 24"
            print ""
            return
        self.SaveUndo()
        self.outputToHistory("", False)
        self.outputToHistory("== US plays %s - %d Ops ==" % (self.deck[str(cardNum)].name, self.deck[str(cardNum)].ops), True)

        if self.deck[str(cardNum)].playable("US", self, True):
            self.outputToHistory("Playable %s Event" % self.deck[str(cardNum)].type, False)
            if cardNum != 120:
                choice = self.getEventOrOpsFromUser("Play card for Event or Ops (enter e or o): ")
            else:
                choice = self.getEventOrOpsFromUser("This event must be played, do you want the Event or Ops to happen first (enter e or o): ")
            if choice == "event":
                self.outputToHistory("Played for Event.", False)
                self.deck[str(cardNum)].playEvent("US", self)
                if cardNum == 120:
                    print "Now, %d Ops available. Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi" % self.deck[str(cardNum)].ops
            elif choice == "ops":
                self.outputToHistory("Played for Ops.", False)
                if cardNum == 120:
                    print "When finished with Ops enter u 120 again to play the event."
                print "%d Ops available. Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi" % self.deck[str(cardNum)].ops
        else:
            if self.deck[str(cardNum)].type == "Jihadist":
                if self.deck[str(cardNum)].playable("Jihadist", self, True):
                    self.outputToHistory("Jihadist Event is playable.", False)
                    playEventFirst = self.getYesNoFromUser("Do you want to play the Jihadist event before using the Ops? (y/n): ")
                    if playEventFirst:
                        self.deck[str(cardNum)].playEvent("Jihadist", self)
                    else:
                        print "Use the Ops now then enter u <card #> again to play the event"
                    print "%d Ops available. Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi" % self.deck[str(cardNum)].ops
                    return
        # Here if it's unplayable by either side.
            self.outputToHistory("Unplayable %s Event" % self.deck[str(cardNum)].type, False)
            print "%d Ops available. Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi" % self.deck[str(cardNum)].ops
                    
    @staticmethod
    def help_u():
        print "Enter the number of the US card when it is your card play.\n"

    def do_plot(self, rest):
        foundPlot = False
        for country in self.map:
            while self.map[country].plots > 0:
                if not foundPlot:
                    self.outputToHistory("", False)
                    self.outputToHistory("[[ Resolving Plots ]]", True)
                foundPlot = True
                print ""
                plotType = self.getPlotTypeFromUser("Enter Plot type from %s: " % country)
                print ""
                isBacklash = False
                if self.backlashInPlay and (self.map[country].type != 'Non-Muslim'):
                    isBacklash = self.getYesNoFromUser("Was this plot selected with backlash (y/n): ")
                postureRoll = 0
                usPrestigeRolls = []
                schCountries = []
                schPostureRolls = []
                govRolls = []
                if country == "United States":
                    if plotType != "WMD":
                        postureRoll = random.randint(1,6)
                        usPrestigeRolls.append(random.randint(1,6))
                        usPrestigeRolls.append(random.randint(1,6))
                        usPrestigeRolls.append(random.randint(1,6))
                elif self.map[country].type != "Non-Muslim":
                    if country != "Iran":
                        numRolls = 0
                        if plotType == "WMD":
                            numRolls = 3
                        else:
                            numRolls = plotType
                        for i in range(numRolls):
                            govRolls.append(random.randint(1,6))
                elif self.map[country].type == "Non-Muslim":
                    postureRoll = random.randint(1,6)
                    if self.map[country].schengen: 
                        schChoices = []
                        for cou in self.map:
                            if cou != country and self.map[cou].schengen:
                                schChoices.append(cou)
                        schCountries.append(random.choice(schChoices))
                        schCountries.append(schCountries[0])
                        while schCountries[0] == schCountries[1]:
                            schCountries[1] = random.choice(schChoices)
                        for i in range(2):
                            schPostureRolls.append(random.randint(1,6))
                self.resolvePlot(country, plotType, postureRoll, usPrestigeRolls, schCountries, schPostureRolls, govRolls, isBacklash)
        if not foundPlot:        
            self.outputToHistory("", False)
            self.outputToHistory("[[ No unblocked plots to resolve ]]", True)
        self.backlashInPlay = False
        
    @staticmethod
    def help_plot():
        print "Use this command after the US Action Phase to resolve any unblocked plots.\n"

    def do_turn(self, rest):
        self.SaveTurn()
        
        self.outputToHistory("* End of Turn.", False)
        if "Pirates" in self.markers and (self.map["Somalia"].is_islamist_rule() or self.map["Yemen"].is_islamist_rule()):
            self.outputToHistory("No funding drop due to Pirates.", False)
        else:
            self.funding -= 1
            if self.funding < 1:
                self.funding = 1
            self.outputToHistory("Jihadist Funding now %d" % self.funding, False)
        anyIR = False
        for country in self.map:
            if self.map[country].is_islamist_rule():
                anyIR = True
                break
        if anyIR:
            self.prestige -= 1
            if self.prestige < 1:
                self.prestige = 1
                self.outputToHistory("Islamist Rule - US Prestige now %d" % self.prestige, False)
        else:
            self.outputToHistory("No Islamist Rule - US Prestige stays at %d" % self.prestige, False)    #20150131PS - added
        worldPos = 0
        for country in self.map:
            if not (self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni") and self.map[country].type != "Iran" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        if (self.map["United States"].posture == "Hard" and worldPos >= 3) or (self.map["United States"].posture == "Soft" and worldPos <= -3):
            self.prestige += 1
            if self.prestige > 12:
                self.prestige = 12
            self.outputToHistory("GWOT World posture is 3 and matches US - US Prestige now %d" % self.prestige, False)
        for event in self.lapsing:
            self.outputToHistory("%s has Lapsed." % event, False)
        self.lapsing = []
        goodRes = 0
        islamRes = 0
        goodC = 0
        islamC = 0
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni": 
                if self.map[country].is_good():
                    goodC += 1
                    goodRes += self.countryResources(country)
                elif self.map[country].is_fair():
                    goodC += 1
                elif self.map[country].is_poor():
                    islamC += 1
                elif self.map[country].is_islamist_rule():
                    islamC += 1
                    islamRes += self.countryResources(country)
        self.outputToHistory("---", False)
        self.outputToHistory("Good Resources   : %d" % goodRes, False)
        self.outputToHistory("Islamist Resources: %d" % islamRes, False)
        self.outputToHistory("---", False)
        self.outputToHistory("Good/Fair Countries   : %d" % goodC, False)
        self.outputToHistory("Poor/Islamist Countries: %d" % islamC, False)
        self.turn += 1
        self.outputToHistory("---", False)
        self.outputToHistory("", False)
        usCards = 0
        jihadistCards = 0
        if self.funding >= 7:
            jihadistCards = 9
        elif self.funding >= 4:
            jihadistCards = 8
        else:
            jihadistCards = 7
        if self.troops >= 10:
            usCards = 9
        elif self.troops >= 5:
            usCards = 8
        else:
            usCards = 7
        self.outputToHistory("Jihadist draws %d cards." % jihadistCards, False)
        self.outputToHistory("US draws %d cards." % usCards, False)
        self.outputToHistory("---", False)
        self.outputToHistory("", False)        
        self.outputToHistory("[[ %d (Turn %s) ]]" % (self.startYear + (self.turn - 1), self.turn), False)
        
    @staticmethod
    def help_turn():
        print "Use this command at the end of the turn.\n"
        
    @staticmethod
    def help_undo():
        print "Rolls back to the last card played.\n"

    def do_undo(self, args):
        self.undo = self.getYesNoFromUser("Undo to last card played? (y/n): ")
    
    @staticmethod
    def help_quit():
        print "Quits game and prompt to save.\n"

    def do_quit(self, args):
        if self.getYesNoFromUser("Save? (y/n): "):
            print "Save suspend file."
            self.Save(SUSPEND_FILE)

        print "Exiting."

    def Save(self, save_file_name):
        save_file = open(save_file_name, 'wb')
        pickle.dump(self, save_file, 2)
        save_file.close()
        
    def SaveUndo(self):
        self.Save(UNDO_FILE)
        
    def SaveTurn(self):
        turnfile = ROLLBACK_FILE + str(self.turn) + ".lwot"
        self.Save(turnfile)
        
    def do_roll(self, args):
        self.do_rollback(args)
    
    def help_roll(self):
        self.help_rollback()
        
    @staticmethod
    def help_rollback():
        print "Roll back to any previous turn in the game.\n"
        
    def do_rollback(self, args):
        self.rollturn = -1
        needTurn = True
        while needTurn:
            try:
                lastturn = self.turn - 1
                input = raw_input("Rollback to which turn valid turns are 0 through " + str(lastturn) + "? Q to cancel rollback: " )
                
                if input == "Q":
                    print "Cancel Rollback"
                    break
                else:
                    input = int(input)
                    if input >= 0 and input <= lastturn:
                        self.rollturn = input
                        needTurn = False
                    else:
                        raise
            except:
                print "Entry error"
                print ""
        
        
def getUserYesNoResponse(prompt):
    good = None
    while not good:
        try:
            input = raw_input(prompt)
            if input.lower() == "y" or input.lower() == "yes":
                return True
            elif input.lower() == "n" or input.lower() == "no":
                return False
            else:
                print "Enter y or n."
                print ""
        except:
            print "Enter y or n."
            print ""


def main():
    print ""
    print "Labyrinth: The War on Terror AI Player"
    print ""
    print "Release", RELEASE
    print ""
    scenario = 0
    ideology = 0
    loadfile = 0
    
    # Starting new session unlink undo save
    if os.path.exists(UNDO_FILE):
        os.remove(UNDO_FILE)
        
    # Starting new session unlink previous turn saves
    for each in os.listdir(os.curdir):
        if "turn." in each and ".lwot" in each:
            os.remove(each)
    
    # Ask user if they want to continue previous game                    
    if os.path.exists(SUSPEND_FILE):
        res = getUserYesNoResponse("Resume suspended game? (y/n): ")
        if res:
            loadfile = 1
    
    if loadfile == 0:
        while scenario == 0:
            try:
                print "Choose Scenario"
                print "(1) Let's Roll!"
                print "(2) You Can Call Me Al"
                print "(3) Anaconda"
                print "(4) Mission Accomplished?"
                input_str = raw_input("Enter choice: ")
                input_int = int(input_str)
                if 1 <= input_int <= 5:
                    scenario = input_int
                    print ""
                else:
                    raise
            except:
                print "Entry error"
                print ""
    
        while ideology == 0:
            try:
                print "Choose Jihadist Ideology"
                print "(1) Normal"
                print "(2) Coherent: Plot success places 2 Plots"
                print "(3) Attractive: ...and Recruit success places 2 cells"
                print "(4) Potent: ...and Major Jihad if 3 or more cells than troops"
                print "(5) Infectious: ...and US plays all its cards (not enforced by program)"
                print "(6) Virulent: ...and Jihad failure does not remove cells"
                input_str = raw_input("Enter choice: ")
                input_int = int(input_str)
                if 1 <= input_int <= 6:
                    ideology = input_int
                    print ""
                else:
                    raise
            except ValueError:
                print "Entry error"
                print ""
        
        app = Labyrinth(scenario, ideology)
        turnfile = ROLLBACK_FILE + "0.lwot"
        app.Save(turnfile)

    else:
        # Load previous game save
        f = open(SUSPEND_FILE,'rb')
        app = pickle.load(f)        
        app.stdout = sys.stdout
        app.undo = False
        f.close()          
        
    
    rollback = True
    while rollback:
    
        app.cmdloop()
        
        # exit out of cmdloop when user quits, want to undo, or rollback - prevents issues dealing with save/reloading within class instance
        if app.undo:
            print "Undo to last turn"
            f = open(UNDO_FILE,'rb')
            
            app = pickle.load(f)
            app.stdout = sys.stdout
            
            f.close()
        elif app.rollturn >= 0:
            print "Rolling back to turn " + str(app.rollturn)
            turnfile = ROLLBACK_FILE + str(app.rollturn) + '.lwot'            
            f = open(turnfile,'rb')
            
            app = pickle.load(f)
            app.stdout = sys.stdout
            
            f.close()
            # rollback invalidates undo save so delete it
            if os.path.exists(UNDO_FILE):
                os.remove(UNDO_FILE)
            
        else:
            rollback = False
            
            
        

if __name__ == "__main__":
    main()
