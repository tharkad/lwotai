"""
LWOTai - A Python implementation of the Single-Player AI for Labyrinth: the War on Terror by GMT Games.
Mike Houser, 2011

08112011.1
"""
from lwotai import Country
from lwotai import DieRoller
from lwotai import GOOD
from lwotai import FAIR
from lwotai import POOR
from lwotai import Governance
from lwotai import Governances
from lwotai import Labyrinth
import unittest

class LabyrinthTest(unittest.TestCase):
    """Assertions etc for reuse by test classes in this file"""

    def assertCells(self, app, country, expected_cells, include_sadr = False):
        """Asserts that the given country contains the given number of cells"""
        self.assertEqual(expected_cells, app.map[country].totalCells(include_sadr))

    def assert_new_messages(self, app, message_count_before, expected_messages):
        expected_message_count = len(expected_messages)
        self.assertEquals(len(app.history), message_count_before + expected_message_count)
        new_messages = app.history[-expected_message_count:]
        self.assertEquals(new_messages, expected_messages)


class FakeDieRoller(DieRoller):
    """Allows die rolls to be faked during unit tests"""

    def __init__(self, *results):
        self.__results = list(results)

    def roll(self, times):
        return self.__results

def testScenarioSetup(self):
    self.prestige = 7
    self.troops = 9
    self.funding = 5
    self.cells = 11
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
    self.map["Pakistan"].make_fair()
    self.map["Pakistan"].make_neutral()
    self.map["Pakistan"].troopCubes = 2
    self.map["Pakistan"].activeCells = 4
    self.map["Gulf States"].make_fair()
    self.map["Gulf States"].make_ally()
    self.map["Gulf States"].troopCubes = 4
    self.map["Gulf States"].sleeperCells = 1
    self.map["Gulf States"].activeCells = 4
    self.map["Afghanistan"].make_islamist_rule()
    self.map["Afghanistan"].make_adversary()
    self.map["Afghanistan"].sleeperCells = 4
    self.map["Somalia"].besieged = 1
    self.map["United States"].posture = "Hard"


def test2ScenarioSetup(self):
    self.prestige = 7
    self.troops = 3
    self.funding = 9
    self.cells = 11
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
    self.map["Pakistan"].make_fair()
    self.map["Pakistan"].make_neutral()
    self.map["Pakistan"].troopCubes = 2
    self.map["Pakistan"].activeCells = 4
    self.map["Gulf States"].make_fair()
    self.map["Gulf States"].make_ally()
    self.map["Gulf States"].troopCubes = 2
    self.map["Gulf States"].sleeperCells = 1
    self.map["Gulf States"].activeCells = 4
    self.map["Afghanistan"].make_good()
    self.map["Afghanistan"].make_ally()
    self.map["Afghanistan"].activeCells = 4
    self.map["Afghanistan"].regimeChange = 1
    self.map["Afghanistan"].troopCubes = 6
    self.map["Afghanistan"].aid = 1
    self.map["Afghanistan"].besieged = 0
    self.map["Somalia"].besieged = 1
    self.map["United States"].posture = "Hard"


def test3ScenarioSetup(self):
    self.prestige = 7
    self.troops = 9
    self.funding = 5
    self.cells = 11
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
    self.map["Pakistan"].make_fair()
    self.map["Pakistan"].make_neutral()
    self.map["Pakistan"].troopCubes = 2
    self.map["Pakistan"].activeCells = 4
    self.map["Gulf States"].make_fair()
    self.map["Gulf States"].make_ally()
    self.map["Gulf States"].troopCubes = 4
    self.map["Gulf States"].sleeperCells = 1
    self.map["Gulf States"].activeCells = 4
    self.map["Afghanistan"].make_islamist_rule()
    self.map["Afghanistan"].make_adversary()
    self.map["Afghanistan"].sleeperCells = 4
    self.map["Somalia"].besieged = 1
    self.map["United States"].posture = "Hard"
    self.map["France"].posture = "Hard"
    self.map["France"].cadre = 1
    self.map["Spain"].posture = "Soft"
    self.map["Spain"].sleeperCells = 1
    self.map["Germany"].posture = "Hard"
    self.map["Germany"].activeCells = 1
    self.map["Germany"].sleeperCells = 1


def testBlankScenarioSetup(self):
    self.prestige = 7
    self.troops = 9
    self.funding = 5
    self.cells = 11


class Scenarios(LabyrinthTest):
    """Scenarios"""

    def testScenario4(self):
        app = Labyrinth(4, 1)
        self.assertTrue(app.map["United Kingdom"].posture == "Hard")


class Map(LabyrinthTest):
    """Map"""

    def testDeck(self):
        """Test Map"""
        app = Labyrinth(1, 1, testScenarioSetup)
        for country in app.map:
            for link in app.map[country].links:
                self.assertTrue(app.map[country] in link.links)


class Deck(LabyrinthTest):
    """Deck tests"""

    def testDeck(self):
        """Test Deck"""
        app = Labyrinth(1, 1, testScenarioSetup)
        for i in range(121):
            if i > 0:
                self.assertEqual(i, app.deck[str(i)].number)


class WOIRollModifiers(LabyrinthTest):
    """Test War of Ideas Roll Modifiers"""

    def testPrestige(self):
        """Prestige"""
        app = Labyrinth(1, 1, testScenarioSetup)
        app.prestige = 1
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 1)
        app.prestige = 2
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 1)
        app.prestige = 3
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 1)
        app.prestige = 4
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 2)
        app.prestige = 5
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 2)
        app.prestige = 6
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 2)
        app.prestige = 7
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 3)
        app.prestige = 8
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 3)
        app.prestige = 9
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 3)
        app.prestige = 10
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 4)
        app.prestige = 11
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 4)
        app.prestige = 12
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 4)

    def testAid(self):
        """Aid"""
        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 3)
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 4)

    def testToGood(self):
        """Going to Good"""
        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 3)
        app.map["Gulf States"].make_poor()
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 4)
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].make_neutral()
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 4)

    def testGWOTPenalty(self):
        """GWOT Penalty"""
        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 3)
        app.map["United States"].posture = "Soft"
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 2)
        app.map["Canada"].posture = "Hard"
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 1)
        app.map["France"].posture = "Hard"
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 0)
        app.map["Germany"].posture = "Hard"
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 0)

    def testAdjCountries(self):
        """Adjacent countries Ally Good"""
        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 3)
        app.map['Pakistan'].make_good()
        app.map['Pakistan'].make_neutral()
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 3)
        app.map['Pakistan'].make_ally()
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 4)
        app.map['Iraq'].make_good()
        app.map['Iraq'].make_ally()
        self.assertEqual(app.modifiedWoIRoll(3, "Gulf States"), 4)


class WOIhandler(LabyrinthTest):
    """Test War of Ideas Handler"""

    def testFailRolls(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)
        app.handleMuslimWoI(1, "Gulf States")
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)
        app.handleMuslimWoI(2, "Gulf States")
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)
        app.handleMuslimWoI(3, "Gulf States")
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)
        app.handleMuslimWoI(4, "Gulf States")
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 1)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)
        app.handleMuslimWoI(5, "Gulf States")
        self.assertTrue(app.map["Gulf States"].is_good())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Gulf States"].is_fair())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)
        app.handleMuslimWoI(6, "Gulf States")
        self.assertTrue(app.map["Gulf States"].is_good())
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.map["Gulf States"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 0)
        app.handleMuslimWoI(1, "Pakistan")
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 0)
        app.handleMuslimWoI(2, "Pakistan")
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 0)
        app.handleMuslimWoI(3, "Pakistan")
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 0)
        app.handleMuslimWoI(4, "Pakistan")
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 1)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 0)
        app.handleMuslimWoI(5, "Pakistan")
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_ally())
        self.assertEqual(app.map["Pakistan"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(app.map["Pakistan"].aid, 0)
        app.handleMuslimWoI(6, "Pakistan")
        self.assertTrue(app.map["Pakistan"].is_fair())
        self.assertTrue(app.map["Pakistan"].is_ally())
        self.assertEqual(app.map["Pakistan"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)
        app.handleMuslimWoI(1, "Saudi Arabia")
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)
        app.handleMuslimWoI(2, "Saudi Arabia")
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)
        app.handleMuslimWoI(3, "Saudi Arabia")
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)
        app.handleMuslimWoI(4, "Saudi Arabia")
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 1)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)
        app.handleMuslimWoI(5, "Saudi Arabia")
        self.assertTrue(app.map["Saudi Arabia"].is_fair())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertTrue(app.map["Saudi Arabia"].is_poor())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)
        app.handleMuslimWoI(6, "Saudi Arabia")
        self.assertTrue(app.map["Saudi Arabia"].is_fair())
        self.assertTrue(app.map["Saudi Arabia"].is_ally())
        self.assertEqual(app.map["Saudi Arabia"].aid, 0)


class AlertHandler(LabyrinthTest):
    """Test Alert"""

    def testAlert(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertEqual(app.map["Iraq"].plots, 2)
        app.handleAlert("Iraq")
        self.assertEqual(app.map["Iraq"].plots, 1)
        app.handleAlert("Iraq")
        self.assertEqual(app.map["Iraq"].plots, 0)
        app.handleAlert("Iraq")
        self.assertEqual(app.map["Iraq"].plots, 0)


class ReassessmentHandler(LabyrinthTest):
    """Test Reassessment"""

    def testAlert(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertEqual(app.map["United States"].posture, "Hard")
        app.handleReassessment()
        self.assertEqual(app.map["United States"].posture, "Soft")
        app.handleReassessment()
        self.assertEqual(app.map["United States"].posture, "Hard")


class RegimeChangeHandler(LabyrinthTest):
    """Test Regime Change"""

    def testRegimeChange(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["United States"].posture = "Soft"
        self.assertTrue(app.map["Afghanistan"].is_islamist_rule())
        self.assertTrue(app.map["Afghanistan"].is_adversary())
        self.assertEqual(app.map["Afghanistan"].troops(), 0)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
        self.assertEqual(app.map["Afghanistan"].activeCells, 0)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        govRoll = 4
        prestigeRolls = (3, 2, 5)
        app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_islamist_rule())
        self.assertTrue(app.map["Afghanistan"].is_adversary())
        self.assertEqual(app.map["Afghanistan"].troops(), 0)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
        self.assertEqual(app.map["Afghanistan"].activeCells, 0)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["United States"].posture = "Hard"
        self.assertTrue(app.map["Afghanistan"].is_islamist_rule())
        self.assertTrue(app.map["Afghanistan"].is_adversary())
        self.assertEqual(app.map["Afghanistan"].troops(), 0)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
        self.assertEqual(app.map["Afghanistan"].activeCells, 0)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        govRoll = 4
        prestigeRolls = (3, 2, 5)
        app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_poor())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 6)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
        self.assertEqual(app.map["Afghanistan"].activeCells, 4)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
        self.assertEqual(app.prestige, 5)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["United States"].posture = "Hard"
        self.assertTrue(app.map["Afghanistan"].is_islamist_rule())
        self.assertTrue(app.map["Afghanistan"].is_adversary())
        self.assertEqual(app.map["Afghanistan"].troops(), 0)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
        self.assertEqual(app.map["Afghanistan"].activeCells, 0)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        govRoll = 5
        prestigeRolls = (3, 2, 5)
        app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_fair())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 6)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
        self.assertEqual(app.map["Afghanistan"].activeCells, 4)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
        self.assertEqual(app.prestige, 5)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["United States"].posture = "Hard"
        self.assertTrue(app.map["Afghanistan"].is_islamist_rule())
        self.assertTrue(app.map["Afghanistan"].is_adversary())
        self.assertEqual(app.map["Afghanistan"].troops(), 0)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
        self.assertEqual(app.map["Afghanistan"].activeCells, 0)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        govRoll = 5
        prestigeRolls = (5, 2, 5)
        app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_fair())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 6)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
        self.assertEqual(app.map["Afghanistan"].activeCells, 4)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
        self.assertEqual(app.prestige, 9)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["United States"].posture = "Hard"
        self.assertTrue(app.map["Afghanistan"].is_islamist_rule())
        self.assertTrue(app.map["Afghanistan"].is_adversary())
        self.assertEqual(app.map["Afghanistan"].troops(), 0)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
        self.assertEqual(app.map["Afghanistan"].activeCells, 0)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        govRoll = 5
        prestigeRolls = (2, 6, 5)
        app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_fair())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 6)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
        self.assertEqual(app.map["Afghanistan"].activeCells, 4)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
        self.assertEqual(app.prestige, 2)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["United States"].posture = "Hard"
        self.assertTrue(app.map["Afghanistan"].is_islamist_rule())
        self.assertTrue(app.map["Afghanistan"].is_adversary())
        self.assertEqual(app.map["Afghanistan"].troops(), 0)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
        self.assertEqual(app.map["Afghanistan"].activeCells, 0)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        govRoll = 5
        prestigeRolls = (6, 6, 5)
        app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_fair())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 6)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
        self.assertEqual(app.map["Afghanistan"].activeCells, 4)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
        self.assertEqual(app.prestige, 12)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.troops -= 8
        app.map["Pakistan"].changeTroops(8)
        app.map["United States"].posture = "Hard"
        self.assertTrue(app.map["Afghanistan"].is_islamist_rule())
        self.assertTrue(app.map["Afghanistan"].is_adversary())
        self.assertEqual(app.map["Afghanistan"].troops(), 0)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
        self.assertEqual(app.map["Afghanistan"].activeCells, 0)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 1)
        self.assertEqual(app.map["Pakistan"].troops(), 10)
        govRoll = 5
        prestigeRolls = (6, 6, 5)
        app.handleRegimeChange("Afghanistan", "Pakistan", 7, govRoll, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_fair())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 7)
        self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
        self.assertEqual(app.map["Afghanistan"].activeCells, 4)
        self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
        self.assertEqual(app.prestige, 12)
        self.assertEqual(app.troops, 1)
        self.assertEqual(app.map["Pakistan"].troops(), 3)


class WithdrawHandler(LabyrinthTest):
    """Test Withdraw"""

    def testWithdraw(self):
        app = Labyrinth(1, 1, test2ScenarioSetup)
        app.map["United States"].posture = "Soft"    
        self.assertTrue(app.map["Afghanistan"].is_good())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 6)
        self.assertEqual(app.map["Afghanistan"].aid, 1)
        self.assertEqual(app.map["Afghanistan"].besieged, 0)
        self.assertEqual(app.map["Saudi Arabia"].troops(), 2)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 3)
        prestigeRolls = (5, 2, 5)
        app.handleWithdraw("Afghanistan", "Saudi Arabia", 4, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_good())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 2)
        self.assertEqual(app.map["Afghanistan"].aid, 0)
        self.assertEqual(app.map["Afghanistan"].besieged, 1)
        self.assertEqual(app.map["Saudi Arabia"].troops(), 6)
        self.assertEqual(app.prestige, 9)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, test2ScenarioSetup)
        app.map["United States"].posture = "Soft"    
        self.assertTrue(app.map["Afghanistan"].is_good())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 6)
        self.assertEqual(app.map["Afghanistan"].aid, 1)
        self.assertEqual(app.map["Afghanistan"].besieged, 0)
        self.assertEqual(app.map["Saudi Arabia"].troops(), 2)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 3)
        prestigeRolls = (2, 3, 5)
        app.handleWithdraw("Afghanistan", "track", 5, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_good())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 1)
        self.assertEqual(app.map["Afghanistan"].aid, 0)
        self.assertEqual(app.map["Afghanistan"].besieged, 1)
        self.assertEqual(app.map["Saudi Arabia"].troops(), 2)
        self.assertEqual(app.prestige, 4)
        self.assertEqual(app.troops, 8)


class MajorJihadChoice(LabyrinthTest):
    """Major Jihad possible?"""
    # For Major Jihad to be possible you need:
    # - A muslim country
    # - Not under Islamist Rule
    # - with at least 5 more cells than troops
    # - At least 2 rolls if the country is poor and not besieged
    # - At least 1 roll if the country is poor and is besieged
    # - At least 3 rolls if the country is fair and not besieged
    # - At least 2 rolls if the country is fair and is besieged
    # - At least 3 rolls if the country is good and is besieged
    # - NOT possible if the country is good and not besieged

    def testMajorJihadChoice(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        self.assertEqual(app.majorJihadChoice(3), False)    # 3 Ops
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Gulf States")    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops
        app.map["Gulf States"].make_fair()
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), False)    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops
        app.map["Gulf States"].make_good()
        self.assertEqual(app.majorJihadChoice(3), False)    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), False)    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].make_poor()
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Gulf States")    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), "Gulf States")    # 1 Ops
        app.map["Gulf States"].make_fair()
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Gulf States")    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops
        app.map["Gulf States"].make_good()
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), False)    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].sleeperCells = 3
        app.map["Afghanistan"].activeCells = 3
        app.map["Afghanistan"].troopCubes = 1
        app.map["Afghanistan"].besieged = 0

        self.assertEqual(app.majorJihadChoice(3), "Gulf States")  # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Gulf States")  # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)  # 1 Ops

        app.map["Saudi Arabia"].make_poor()
        app.map["Saudi Arabia"].sleeperCells = 5
        app.map["Saudi Arabia"].activeCells = 4
        app.map["Saudi Arabia"].troopCubes = 4
        app.map["Saudi Arabia"].besieged = 0

        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops

        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].sleeperCells = 5
        app.map["Pakistan"].activeCells = 4
        app.map["Pakistan"].troopCubes = 4
        app.map["Pakistan"].besieged = 0

        self.assertEqual(app.majorJihadChoice(3), "Pakistan")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Pakistan")    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops


class HandleJihad(LabyrinthTest):
    """Test handleJihad"""

    def testHandleJihad(self):
        # Many Cells
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 1)
        self.assertEqual(opsLeft, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 2)
        self.assertEqual(opsLeft, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 3)
        self.assertEqual(opsLeft, 0)

        # 1 cell
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 1)
        self.assertEqual(opsLeft, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 2)
        self.assertEqual(opsLeft, 1)
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 3)
        self.assertEqual(opsLeft, 2)

        # 2 cell
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 1)
        self.assertEqual(opsLeft, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 2)
        self.assertEqual(opsLeft, 0)
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 3)
        self.assertEqual(opsLeft, 1)

        # 3 cell
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 1)
        self.assertEqual(opsLeft, 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 2)
        self.assertEqual(opsLeft, 0)
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        opsLeft = app.handleJihad("Gulf States", 3)
        self.assertEqual(opsLeft, 0)    


class ExecuteJihad(LabyrinthTest):
    """Execute Major Jihad"""
    # A Major jihad needs:
    # - Muslim country not under Islamist Rule
    # - 5 more cells than troops
    # - Then if gov at Poor and not besieged 2 more successes causes Islamist Revolution
    # - Or if gov at Poor and is besieged 1 more success causes Islamist Revolution
    # Jihad does:
    # - Each success worsens gov
    # - Any failure roll sends a cell to the funding track
    # Major failure does:
    # - Three Failure rolls in a Poor country shifts alignment one toward Ally and places Besieged regime
    # A Major jihad does:
    # - All cells go active
    # Islamist Revolution causes:
    # - Gov to Islamist Rule
    # - Alignment to Adversary
    # - Remove Regime Change, Beseiged and Aid
    # - Add country's resources to Funding track
    # - If troops in country US Prestige to 1

    # 5 MORE CELLS THAN TROOPS - Major Jihad possible

    def testJihadEnoughCellsPoorGovNotBesieged(self):

        # Poor Gov
        # Not Besieged
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # to 1 due to troops present

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        funding_before = app.funding
        prestige_before = app.prestige
        app.executeJihad("Gulf States", [3, 4, 4])  # 8.4.3.1 Major Jihad Failure
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the two failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)
        self.assertEqual(app.map["Gulf States"].aid, 1)
        self.assertEqual(app.map["Gulf States"].besieged, 1)
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.funding, funding_before)
        self.assertEqual(app.prestige, prestige_before)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])  # Major failure
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_ally())  # major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # to 1 due to troops present

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 7)  # unchanged, no troops

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # to 1 due to troops present

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 7)  # unchanged, no troops

    def testJihadEnoughCellsPoorGovIsBeseiged(self):    
        # Poor Gov
        # Besieged
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4, 4])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])  # Major Failure in besiged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_ally())  # major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadEnoughCellsFairGovNotBeseiged(self):
        # Fair Gov
        # Not Besieged
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # not Major failure
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # not major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # not major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # to 1 due to troops present

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 7)  # unchanged, no troops

    def testJihadEnoughCellsFairGovIsBeseiged(self):
        # Fair Gov
        # Besieged
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 7)  # unchanged, no troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # Not Major Failure in besiged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadEnoughCellsGoodGovNotBeseiged(self):
        # Good Gov
        # Not Besieged
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # not Major failure
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # not major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # not major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 1])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadEnoughCellsGoodGovIsBeseiged(self):
        # Good Gov
        # Besieged

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 1])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 2])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # not Major Failure in besiged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # not major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # NOT 5 MORE CELLS THAN TROOPS - Major Jihad NOT possible

    def testJihadNotEnoughCellsPoorGovNotBeseiged(self):

        # Poor Gov
        # Not Besieged
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])  # Not Major failure
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # not major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # not major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsPoorGovIsBeseiged(self):    
        # Poor Gov
        # Besieged
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # 
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # 
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # 
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # 
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # 
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # 
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # 
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4, 4])  # Revolution in besiged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # 
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])  # no major failure
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # 
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsFairGovNotBeseiged(self):
        # Fair Gov
        # Not Besieged
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # no Major failure
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov stays 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsFairGovIsBeseiged(self):
        # Fair Gov
        # Besieged

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # no Failure in besiged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsGoodGovNotBeseiged(self):
        # Good Gov
        # Not Besieged
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # no Major failure
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 1])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsGoodGovIsBeseiged(self):
        # Good Gov
        # Besieged

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails in besiged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 1])  # Can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 2])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # no Major Failure in besiged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov stays 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # Sleeper/Active cell testing

    def testJihadOneCell(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # sleeper goes active
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # sleeper goes active
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # lose sleeper cell
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadTwoSleeperCells(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # sleeper goes active
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # sleeper goes active
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # lose sleeper cell
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lose sleeper cell
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadTwoActiveCells(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadOneSleeperOneActiveCells(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadThreeSleeperCells(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 2) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1) 
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 2)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadTwoSleeperOneActiveCells(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 2) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1) 
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 2)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadOneSleeperTwoActiveCells(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2) 
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadThreeActiveCells(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 3) 
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)


class MinorJihadChoice(LabyrinthTest):
    """Test minorJihadInGoodFairChoice"""

    def testMinorJihadOneCellOneOps(self):
        # one cell in each country, one ops case

        app = Labyrinth(1, 1, test3ScenarioSetup)
        # only Islamist rule has cells
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(1), False)
        # fair governance
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])
        # good governance
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Saudi Arabia", 1)])
        # 2 good governance
        app.map["Gulf States"].make_good()
        for i in range(10):
            retVal = app.minorJihadInGoodFairChoice(1)
            self.assertTrue((retVal == [("Gulf States", 1)]) or (retVal == [("Saudi Arabia", 1)]))
        # 2 good governance but Jordan has less resources    
        app.map["Saudi Arabia"].make_poor()
        app.map["Jordan"].make_good()
        app.map["Jordan"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])
        # but the other is besieged
        app.map["Jordan"].besieged = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Jordan", 1)])
        # but the other has aid
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])
        # but yet another is Pakistan    
        app.map["Pakistan"].make_good()
        app.map["Pakistan"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Pakistan", 1)])
        # but Pakistan does not win against good if it is fair
        app.map["Pakistan"].make_fair()
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])

    def testMinorJihadOneCellTwoOps(self):
        # one cell in each country, two ops case

        app = Labyrinth(1, 1, test3ScenarioSetup)
        # only Islamist rule has cells
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(2), False)
        # fair governance
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 1)])
        # good governance
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Saudi Arabia", 1), ("Gulf States", 1)])
        # 2 good governance
        app.map["Gulf States"].make_good()
        retVal = app.minorJihadInGoodFairChoice(2)
        self.assertTrue((("Gulf States", 1) in retVal) and (("Saudi Arabia", 1) in retVal) and len(retVal) == 2)
        # 2 good governance but Jordan has less resources    
        app.map["Saudi Arabia"].make_poor()
        app.map["Jordan"].make_good()
        app.map["Jordan"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 1), ("Jordan", 1)])
        # but the other is besieged
        app.map["Jordan"].besieged = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Jordan", 1), ("Gulf States", 1)])
        # but the other has aid
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 1), ("Jordan", 1)])
        # but yet another is Pakistan    
        app.map["Pakistan"].make_good()
        app.map["Pakistan"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Pakistan", 1), ("Gulf States", 1)])
        # but Pakistan does not win against good if it is fair
        app.map["Pakistan"].make_fair()
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 1), ("Jordan", 1)])

    def testMinorJihadOneCellThreeOps(self):
        # one cell in each country, three ops case

        app = Labyrinth(1, 1, test3ScenarioSetup)
        # only Islamist rule has cells
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(3), False)
        # fair governance
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 1)])
        # good governance
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Saudi Arabia", 1), ("Gulf States", 1)])
        # 2 good governance
        app.map["Gulf States"].make_good()
        self.assertTrue((("Gulf States", 1) in app.minorJihadInGoodFairChoice(3)) and
                        (("Saudi Arabia", 1) in app.minorJihadInGoodFairChoice(3))
                        and len(app.minorJihadInGoodFairChoice(3)) == 2)
        # 2 good governance but Jordan has less resources    
        app.map["Saudi Arabia"].make_poor()
        app.map["Jordan"].make_good()
        app.map["Jordan"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 1), ("Jordan", 1)])
        # but the other is besieged
        app.map["Jordan"].besieged = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Jordan", 1), ("Gulf States", 1)])
        # but the other has aid
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 1), ("Jordan", 1)])
        # but yet another is Pakistan    
        app.map["Pakistan"].make_good()
        app.map["Pakistan"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Pakistan", 1), ("Gulf States", 1), ("Jordan", 1)])
        # but Pakistan does not win against good if it is fair
        app.map["Pakistan"].make_fair()
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 1), ("Jordan", 1), ("Pakistan", 1)])

    def testMinorJihadTwoCellOneOps(self):
        # two cells in each country, one ops case

        app = Labyrinth(1, 1, test3ScenarioSetup)
        # only Islamist rule has cells
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(1), False)
        # fair governance
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])
        # good governance
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Saudi Arabia", 1)])
        # 2 good governance
        app.map["Gulf States"].make_good()
        for i in range(10):
            retVal = app.minorJihadInGoodFairChoice(1)
            self.assertTrue(retVal == [("Gulf States", 1)] or retVal == [("Saudi Arabia", 1)])
        # 2 good governance but Jordan has less resources    
        app.map["Saudi Arabia"].make_poor()
        app.map["Jordan"].make_good()
        app.map["Jordan"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])
        # but the other is besieged
        app.map["Jordan"].besieged = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Jordan", 1)])
        # but the other has aid
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])
        # but yet another is Pakistan    
        app.map["Pakistan"].make_good()
        app.map["Pakistan"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Pakistan", 1)])
        # but Pakistan does not win against good if it is fair
        app.map["Pakistan"].make_fair()
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])

    def testMinorJihadTwoCellTwoOps(self):
        # two cell in each country, two ops case

        app = Labyrinth(1, 1, test3ScenarioSetup)
        # only Islamist rule has cells
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(2), False)
        # fair governance
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 2)])
        # good governance
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Saudi Arabia", 2)])
        # 2 good governance
        app.map["Gulf States"].make_good()
        for i in range(10):
            retVal = app.minorJihadInGoodFairChoice(2) 
            self.assertTrue(retVal == [("Gulf States", 2)] or retVal == [("Saudi Arabia", 2)])
        # 2 good governance but Jordan has less resources    
        app.map["Saudi Arabia"].make_poor()
        app.map["Jordan"].make_good()
        app.map["Jordan"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 2)])
        # but the other is besieged
        app.map["Jordan"].besieged = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Jordan", 2)])
        # but the other has aid
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 2)])
        # but yet another is Pakistan    
        app.map["Pakistan"].make_good()
        app.map["Pakistan"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Pakistan", 2)])
        # but Pakistan does not win against good if it is fair
        app.map["Pakistan"].make_fair()
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 2)])

    def testMinorJihadTwoCellThreeOps(self):
        # two cell in each country, three ops case

        app = Labyrinth(1, 1, test3ScenarioSetup)
        # only Islamist rule has cells
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(3), False)
        # fair governance
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 2)])
        # good governance
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Saudi Arabia", 2), ("Gulf States", 1)])
        # 2 good governance
        app.map["Gulf States"].make_good()
        for i in range(10):
            retVal = app.minorJihadInGoodFairChoice(3)
            self.assertTrue(retVal == [("Saudi Arabia", 2), ("Gulf States", 1)] or
                            retVal == [("Gulf States", 2), ("Saudi Arabia", 1)])
        # 2 good governance but Jordan has less resources    
        app.map["Saudi Arabia"].make_poor()
        app.map["Jordan"].make_good()
        app.map["Jordan"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 2), ("Jordan", 1)])
        # but the other is besieged
        app.map["Jordan"].besieged = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Jordan", 2), ("Gulf States", 1)])
        # but the other has aid
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 2), ("Jordan", 1)])
        # but yet another is Pakistan    
        app.map["Pakistan"].make_good()
        app.map["Pakistan"].activeCells = 2
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Pakistan", 2), ("Gulf States", 1)])
        # but Pakistan does not win against good if it is fair
        app.map["Pakistan"].make_fair()
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 2), ("Jordan", 1)])

    def testMinorJihadThreeCellOneOps(self):
        # three cells in each country, one ops case

        app = Labyrinth(1, 1, test3ScenarioSetup)
        # only Islamist rule has cells
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(1), False)
        # fair governance
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])
        # good governance
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Saudi Arabia", 1)])
        # 2 good governance
        app.map["Gulf States"].make_good()
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        # 2 good governance but Jordan has less resources    
        app.map["Saudi Arabia"].make_poor()
        app.map["Jordan"].make_good()
        app.map["Jordan"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])
        # but the other is besieged
        app.map["Jordan"].besieged = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Jordan", 1)])
        # but the other has aid
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])
        # but yet another is Pakistan    
        app.map["Pakistan"].make_good()
        app.map["Pakistan"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Pakistan", 1)])
        # but Pakistan does not win against good if it is fair
        app.map["Pakistan"].make_fair()
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States", 1)])

    def testMinorJihadThreeCellTwoOps(self):
        # three cell in each country, two ops case

        app = Labyrinth(1, 1, test3ScenarioSetup)
        # only Islamist rule has cells
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(2), False)
        # fair governance
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 2)])
        # good governance
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Saudi Arabia", 2)])
        # 2 good governance
        app.map["Gulf States"].make_good()
        for i in range(10):
            retVal = app.minorJihadInGoodFairChoice(2)
            self.assertTrue(retVal == [("Gulf States", 2)] or retVal == [("Saudi Arabia", 2)])
        # 2 good governance but Jordan has less resources    
        app.map["Saudi Arabia"].make_poor()
        app.map["Jordan"].make_good()
        app.map["Jordan"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 2)])
        # but the other is besieged
        app.map["Jordan"].besieged = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Jordan", 2)])
        # but the other has aid
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 2)])
        # but yet another is Pakistan    
        app.map["Pakistan"].make_good()
        app.map["Pakistan"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Pakistan", 2)])
        # but Pakistan does not win against good if it is fair
        app.map["Pakistan"].make_fair()
        self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States", 2)])

    def testMinorJihadThreeCellThreeOps(self):
        # three cell in each country, three ops case

        app = Labyrinth(1, 1, test3ScenarioSetup)
        # only Islamist rule has cells
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(3), False)
        # fair governance
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 3)])
        # good governance
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Saudi Arabia", 3)])
        # 2 good governance
        app.map["Gulf States"].make_good()
        for i in range(10):
            retVal = app.minorJihadInGoodFairChoice(3)
            self.assertTrue((retVal == [("Saudi Arabia", 3)]) or (retVal == [("Gulf States", 3)]))
        # 2 good governance but Jordan has less resources    
        app.map["Saudi Arabia"].make_poor()
        app.map["Jordan"].make_good()
        app.map["Jordan"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 3)])
        # but the other is besieged
        app.map["Jordan"].besieged = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Jordan", 3)])
        # but the other has aid
        app.map["Gulf States"].aid = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 3)])
        # but yet another is Pakistan    
        app.map["Pakistan"].make_good()
        app.map["Pakistan"].activeCells = 3
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Pakistan", 3)])
        # but Pakistan does not win against good if it is fair
        app.map["Pakistan"].make_fair()
        self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States", 3)])


class Recruit(LabyrinthTest):
    """Test Recruiting"""

    def testRecruitChoice(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.recruitChoice(3))
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].activeCells = 1
        self.assertEqual(app.recruitChoice(1), "Gulf States")
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].cadre = 1
        self.assertEqual(app.recruitChoice(1), "Gulf States")
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].cadre = 0
        app.map["Iraq"].make_good()
        app.map["Iraq"].activeCells = 1
        for i in range(10):
            retVal = app.recruitChoice(i)
            self.assertTrue(retVal in ["Iraq", "Gulf States"])
        app.map["Iraq"].activeCells = 0
        app.map["Iraq"].cadre = 1
        self.assertEqual(app.recruitChoice(1), "Gulf States")
        app.map["Iraq"].troopCubes = 2
        self.assertEqual(app.recruitChoice(1), "Iraq")
        app.map["Gulf States"].besieged = 1
        self.assertEqual(app.recruitChoice(1), "Gulf States")
        app.map["Russia"].sleeperCells = 1
        self.assertEqual(app.recruitChoice(1), "Russia")
        app.map["Philippines"].sleeperCells = 1
        self.assertEqual(app.recruitChoice(1), "Philippines")
        app.map["Iraq"].make_islamist_rule()
        app.map["Iraq"].activeCells = 6
        self.assertEqual(app.recruitChoice(1), "Philippines")
        app.map["Iraq"].activeCells = 5
        self.assertEqual(app.recruitChoice(3), "Iraq")
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 5
        self.assertEqual(app.recruitChoice(3), "Iraq")
        app.map["Gulf States"].troopCubes = 6
        self.assertEqual(app.recruitChoice(1), "Gulf States")

    def testExecuteRecruit(self):
        # Normal
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 1, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 1, [2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [2, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 3)
        self.assertEqual(app.cells, 12)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [1, 2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [2, 1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [2, 2, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, testBlankScenarioSetup)    # Coherent
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 1, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 1, [2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [2, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 3)
        self.assertEqual(app.cells, 12)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [1, 2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [2, 1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [2, 2, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        # not enough cells        
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 1
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 2
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [2, 2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 2
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [1, 2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 2
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 2])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 1
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 2
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 3
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 1)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 3
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 2)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 5
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 4)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 5
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 3)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 5
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 3)
        self.assertEqual(app.cells, 2)

        app = Labyrinth(1, 2, testBlankScenarioSetup)
        app.cells = 4
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 3)
        self.assertEqual(app.cells, 1)

        # IR RC
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        app.funding = 9
        app.map["Iraq"].make_poor()
        unusedOps = app.executeRecruit("Iraq", 1, [4])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        app.funding = 9
        app.map["Iraq"].make_islamist_rule()
        unusedOps = app.executeRecruit("Iraq", 1, [6])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 15
        app.funding = 9
        app.map["Iraq"].make_fair()
        app.map["Iraq"].regimeChange = 1
        unusedOps = app.executeRecruit("Iraq", 1, [6])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)


class NumCellsAvailable(LabyrinthTest):
    """Test num cells available"""

    def testNumCellsAvaialable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.funding = 9
        self.cells = 15
        self.assertTrue(app.numCellsAvailable(), 15)
        self.cells = 14
        self.assertTrue(app.numCellsAvailable(), 14)
        self.cells = 13
        self.assertTrue(app.numCellsAvailable(), 13)
        self.cells = 12
        self.assertTrue(app.numCellsAvailable(), 12)
        self.cells = 11
        self.assertTrue(app.numCellsAvailable(), 11)
        self.cells = 10
        self.assertTrue(app.numCellsAvailable(), 10)
        self.cells = 9
        self.assertTrue(app.numCellsAvailable(), 9)
        self.cells = 8
        self.assertTrue(app.numCellsAvailable(), 8)
        self.cells = 7
        self.assertTrue(app.numCellsAvailable(), 7)
        self.cells = 6
        self.assertTrue(app.numCellsAvailable(), 6)
        self.cells = 5
        self.assertTrue(app.numCellsAvailable(), 5)
        self.cells = 4
        self.assertTrue(app.numCellsAvailable(), 4)
        self.cells = 3
        self.assertTrue(app.numCellsAvailable(), 3)
        self.cells = 2
        self.assertTrue(app.numCellsAvailable(), 2)
        self.cells = 1
        self.assertTrue(app.numCellsAvailable(), 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.funding = 8
        self.cells = 15
        self.assertTrue(app.numCellsAvailable(), 15)
        self.cells = 14
        self.assertTrue(app.numCellsAvailable(), 14)
        self.cells = 13
        self.assertTrue(app.numCellsAvailable(), 13)
        self.cells = 12
        self.assertTrue(app.numCellsAvailable(), 12)
        self.cells = 11
        self.assertTrue(app.numCellsAvailable(), 11)
        self.cells = 10
        self.assertTrue(app.numCellsAvailable(), 10)
        self.cells = 9
        self.assertTrue(app.numCellsAvailable(), 9)
        self.cells = 8
        self.assertTrue(app.numCellsAvailable(), 8)
        self.cells = 7
        self.assertTrue(app.numCellsAvailable(), 7)
        self.cells = 6
        self.assertTrue(app.numCellsAvailable(), 6)
        self.cells = 5
        self.assertTrue(app.numCellsAvailable(), 5)
        self.cells = 4
        self.assertTrue(app.numCellsAvailable(), 4)
        self.cells = 3
        self.assertTrue(app.numCellsAvailable(), 3)
        self.cells = 2
        self.assertTrue(app.numCellsAvailable(), 2)
        self.cells = 1
        self.assertTrue(app.numCellsAvailable(), 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.funding = 7
        self.cells = 15
        self.assertTrue(app.numCellsAvailable(), 15)
        self.cells = 14
        self.assertTrue(app.numCellsAvailable(), 14)
        self.cells = 13
        self.assertTrue(app.numCellsAvailable(), 13)
        self.cells = 12
        self.assertTrue(app.numCellsAvailable(), 12)
        self.cells = 11
        self.assertTrue(app.numCellsAvailable(), 11)
        self.cells = 10
        self.assertTrue(app.numCellsAvailable(), 10)
        self.cells = 9
        self.assertTrue(app.numCellsAvailable(), 9)
        self.cells = 8
        self.assertTrue(app.numCellsAvailable(), 8)
        self.cells = 7
        self.assertTrue(app.numCellsAvailable(), 7)
        self.cells = 6
        self.assertTrue(app.numCellsAvailable(), 6)
        self.cells = 5
        self.assertTrue(app.numCellsAvailable(), 5)
        self.cells = 4
        self.assertTrue(app.numCellsAvailable(), 4)
        self.cells = 3
        self.assertTrue(app.numCellsAvailable(), 3)
        self.cells = 2
        self.assertTrue(app.numCellsAvailable(), 2)
        self.cells = 1
        self.assertTrue(app.numCellsAvailable(), 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.funding = 6
        self.cells = 15
        self.assertTrue(app.numCellsAvailable(), 10)
        self.cells = 14
        self.assertTrue(app.numCellsAvailable(), 9)
        self.cells = 13
        self.assertTrue(app.numCellsAvailable(), 8)
        self.cells = 12
        self.assertTrue(app.numCellsAvailable(), 7)
        self.cells = 11
        self.assertTrue(app.numCellsAvailable(), 6)
        self.cells = 10
        self.assertTrue(app.numCellsAvailable(), 5)
        self.cells = 9
        self.assertTrue(app.numCellsAvailable(), 4)
        self.cells = 8
        self.assertTrue(app.numCellsAvailable(), 3)
        self.cells = 7
        self.assertTrue(app.numCellsAvailable(), 2)
        self.cells = 6
        self.assertTrue(app.numCellsAvailable(), 1)
        self.cells = 5
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 4
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 3
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 2
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 1
        self.assertTrue(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.funding = 5
        self.cells = 15
        self.assertTrue(app.numCellsAvailable(), 10)
        self.cells = 14
        self.assertTrue(app.numCellsAvailable(), 9)
        self.cells = 13
        self.assertTrue(app.numCellsAvailable(), 8)
        self.cells = 12
        self.assertTrue(app.numCellsAvailable(), 7)
        self.cells = 11
        self.assertTrue(app.numCellsAvailable(), 6)
        self.cells = 10
        self.assertTrue(app.numCellsAvailable(), 5)
        self.cells = 9
        self.assertTrue(app.numCellsAvailable(), 4)
        self.cells = 8
        self.assertTrue(app.numCellsAvailable(), 3)
        self.cells = 7
        self.assertTrue(app.numCellsAvailable(), 2)
        self.cells = 6
        self.assertTrue(app.numCellsAvailable(), 1)
        self.cells = 5
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 4
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 3
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 2
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 1
        self.assertTrue(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.funding = 4
        self.cells = 15
        self.assertTrue(app.numCellsAvailable(), 10)
        self.cells = 14
        self.assertTrue(app.numCellsAvailable(), 9)
        self.cells = 13
        self.assertTrue(app.numCellsAvailable(), 8)
        self.cells = 12
        self.assertTrue(app.numCellsAvailable(), 7)
        self.cells = 11
        self.assertTrue(app.numCellsAvailable(), 6)
        self.cells = 10
        self.assertTrue(app.numCellsAvailable(), 5)
        self.cells = 9
        self.assertTrue(app.numCellsAvailable(), 4)
        self.cells = 8
        self.assertTrue(app.numCellsAvailable(), 3)
        self.cells = 7
        self.assertTrue(app.numCellsAvailable(), 2)
        self.cells = 6
        self.assertTrue(app.numCellsAvailable(), 1)
        self.cells = 5
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 4
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 3
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 2
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 1
        self.assertTrue(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.funding = 3
        self.cells = 15
        self.assertTrue(app.numCellsAvailable(), 5)
        self.cells = 14
        self.assertTrue(app.numCellsAvailable(), 4)
        self.cells = 13
        self.assertTrue(app.numCellsAvailable(), 3)
        self.cells = 12
        self.assertTrue(app.numCellsAvailable(), 2)
        self.cells = 11
        self.assertTrue(app.numCellsAvailable(), 1)
        self.cells = 10
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 9
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 8
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 7
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 6
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 5
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 4
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 3
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 2
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 1
        self.assertTrue(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.funding = 2
        self.cells = 15
        self.assertTrue(app.numCellsAvailable(), 5)
        self.cells = 14
        self.assertTrue(app.numCellsAvailable(), 4)
        self.cells = 13
        self.assertTrue(app.numCellsAvailable(), 3)
        self.cells = 12
        self.assertTrue(app.numCellsAvailable(), 2)
        self.cells = 11
        self.assertTrue(app.numCellsAvailable(), 1)
        self.cells = 10
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 9
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 8
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 7
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 6
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 5
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 4
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 3
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 2
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 1
        self.assertTrue(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.funding = 1
        self.cells = 15
        self.assertTrue(app.numCellsAvailable(), 5)
        self.cells = 14
        self.assertTrue(app.numCellsAvailable(), 4)
        self.cells = 13
        self.assertTrue(app.numCellsAvailable(), 3)
        self.cells = 12
        self.assertTrue(app.numCellsAvailable(), 2)
        self.cells = 11
        self.assertTrue(app.numCellsAvailable(), 1)
        self.cells = 10
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 9
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 8
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 7
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 6
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 5
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 4
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 3
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 2
        self.assertTrue(app.numCellsAvailable(), 0)
        self.cells = 1
        self.assertTrue(app.numCellsAvailable(), 0)


class Travel(LabyrinthTest):
    """Test Travel"""

    def testTravelFirstBox(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].aid = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Gulf States"].aid = 0
        app.map["Gulf States"].regimeChange = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Gulf States"].make_islamist_rule()
        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Afghanistan"])

        app.map["Gulf States"].make_poor()
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 1
        iraqCount = 0
        gulfCount = 0
        for i in range(100):
            dest = app.travelDestinations(1)
            if dest == ["Gulf States"]:
                gulfCount += 1
            elif dest == ["Iraq"]:
                iraqCount += 1
            self.assertTrue(dest == ["Gulf States"] or dest == ["Iraq"])
        self.assertTrue(iraqCount > 0)
        self.assertTrue(gulfCount > 0)

        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].aid = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Pakistan"])

    def testTravelSecondBox(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)

        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].troopCubes = 1
        app.map["Afghanistan"].sleeperCells = 4
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Afghanistan"])

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        dest = app.travelDestinations(2)
        self.assertEqual(dest, ["Gulf States", "Afghanistan"])

    def testTravelThirdBox(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)

        app.map["Jordan"].make_fair()
        app.map["Iraq"].make_poor()
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Jordan"])

        app.map["Gulf States"].make_fair()
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Gulf States"].make_poor()        
        app.map["Algeria/Tunisia"].make_fair()
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Jordan"])

        app.map["Germany"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Algeria/Tunisia"])

    def testTravelForthBox(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)

        app.map["United States"].posture = "Hard"

        app.map["Canada"].posture = "Hard"
        app.map["United Kingdom"].posture = "Hard"
        app.map["Serbia"].posture = "Hard"
        app.map["India"].posture = "Hard"
        app.map["Scandinavia"].posture = "Hard"
        app.map["Eastern Europe"].posture = "Hard"
        app.map["Benelux"].posture = "Hard"
        app.map["Germany"].posture = "Hard"
        app.map["France"].posture = "Hard"
        app.map["Italy"].posture = "Hard"
        app.map["Spain"].posture = "Hard"
        app.map["Russia"].posture = "Hard"
        app.map["Caucasus"].posture = "Hard"
        app.map["China"].posture = "Hard"
        app.map["Kenya/Tanzania"].posture = "Hard"
        app.map["Thailand"].posture = "Hard"
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Philippines"])

    def testTravelMultiple(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        dest = app.travelDestinations(3)

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].troopCubes = 1
        app.map["Afghanistan"].sleeperCells = 4
        dest = app.travelDestinations(2)
        self.assertEqual(dest, ["Gulf States", "Afghanistan"])

        app.map["Jordan"].make_fair()
        app.map["Iraq"].make_poor()
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Gulf States", "Afghanistan", "Jordan"])

        app.map["United States"].posture = "Hard"
        app.map["Canada"].posture = "Hard"
        app.map["United Kingdom"].posture = "Hard"
        app.map["Serbia"].posture = "Hard"
        app.map["India"].posture = "Hard"
        app.map["Scandinavia"].posture = "Hard"
        app.map["Eastern Europe"].posture = "Hard"
        app.map["Benelux"].posture = "Hard"
        app.map["Germany"].posture = "Hard"
        app.map["France"].posture = "Hard"
        app.map["Italy"].posture = "Hard"
        app.map["Spain"].posture = "Hard"
        app.map["Russia"].posture = "Hard"
        app.map["Caucasus"].posture = "Hard"
        app.map["China"].posture = "Hard"
        app.map["Kenya/Tanzania"].posture = "Hard"
        app.map["Thailand"].posture = "Hard"
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Gulf States", "Afghanistan", "Jordan"])

        app.map["Gulf States"].make_islamist_rule()
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Afghanistan", "Jordan", "Philippines"])

        app.map["Kenya/Tanzania"].posture = ""
        phCount = 0
        ktCount = 0
        for i in range(100):
            dest = app.travelDestinations(3)
            if dest == ["Afghanistan", "Jordan", "Philippines"]:
                phCount += 1
            elif dest == ["Afghanistan", "Jordan", "Kenya/Tanzania"]:
                ktCount += 1
            self.assertTrue(dest == ["Afghanistan", "Jordan", "Philippines"] or
                            dest == ["Afghanistan", "Jordan", "Kenya/Tanzania"])
        self.assertTrue(phCount > 0)
        self.assertTrue(ktCount > 0)

        app.map["United States"].posture = "Soft"
        app.map["China"].posture = "Soft"
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Afghanistan", "Jordan", "China"])

        app.map["Benelux"].posture = "Soft"
        chinaCount = 0
        beneluxCount = 0
        for i in range(100):
            dest = app.travelDestinations(3)
            if dest == ["Afghanistan", "Jordan", "China"]:
                chinaCount += 1
            elif dest == ["Afghanistan", "Jordan", "Benelux"]:
                beneluxCount += 1
            self.assertTrue(dest == ["Afghanistan", "Jordan", "China"] or dest == ["Afghanistan", "Jordan", "Benelux"])
        self.assertTrue(chinaCount > 0)
        self.assertTrue(beneluxCount > 0)

    def testTravelFrom(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Lebanon"].make_fair()
        app.map["Lebanon"].activeCells = 1
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Lebanon"])

        app.map["Iraq"].make_fair()
        app.map["Iraq"].activeCells = 1
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Iraq"])

        app.map["Egypt"].make_fair()
        app.map["Egypt"].activeCells = 1
        app.map["Egypt"].regimeChange = 1
        app.map["Egypt"].troopCubes = 2
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Iraq"])
        app.map["Egypt"].activeCells = 3
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Egypt"])

        app.map["Yemen"].make_islamist_rule()
        app.map["Yemen"].activeCells = 3
        app.map["Yemen"].troopCubes = 2
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Egypt"])
        sources = app.travelSources(dest, 2)
        self.assertEqual(sources, ["Yemen"])

        #multi

        app = Labyrinth(1, 1, testBlankScenarioSetup)

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1

        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].troopCubes = 1
        app.map["Afghanistan"].sleeperCells = 4

        app.map["Jordan"].make_fair()
        app.map["Iraq"].make_poor()
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Gulf States", "Afghanistan", "Jordan"])

        app.map["Lebanon"].make_fair()
        app.map["Lebanon"].activeCells = 1

        app.map["Iraq"].make_fair()
        app.map["Iraq"].activeCells = 1

        app.map["Egypt"].make_fair()
        app.map["Egypt"].regimeChange = 1
        app.map["Egypt"].troopCubes = 2
        app.map["Egypt"].activeCells = 3

        app.map["Yemen"].make_islamist_rule()
        app.map["Yemen"].activeCells = 4
        app.map["Yemen"].troopCubes = 2
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Egypt", "Iraq"])

        app.map["Yemen"].activeCells = 5
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Yemen", "Egypt"])

        app.map["Yemen"].activeCells = 6
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Yemen", "Yemen"])

        app.map["Yemen"].activeCells = 4
        sources = app.travelSources(dest, 3)
        app.map["Egypt"].activeCells = 4
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Egypt", "Egypt"])

        app.map["Iraq"].make_fair()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].troopCubes = 2
        app.map["Iraq"].activeCells = 4
        app.map["Egypt"].activeCells = 0
        app.map["Egypt"].sleeperCells = 4
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Iraq", "Iraq"])


class ResolvePlot(LabyrinthTest):
    """Resolve Plots"""

    def testResolveNonMuslimNonUSPlots(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Germany"].plots = 1
        app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Germany"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "Hard")
        self.assertEqual(app.map["Scandinavia"].posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Germany"].plots = 2
        app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Germany"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "Hard")
        self.assertEqual(app.map["Scandinavia"].posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Germany"].plots = 1
        app.resolvePlot("Germany", 2, 5, [], ["Spain", "Scandinavia"], [4, 5], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["Germany"].posture, "Hard")
        self.assertEqual(app.map["Spain"].posture, "Soft")
        self.assertEqual(app.map["Scandinavia"].posture, "Hard")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Canada"].plots = 1
        app.resolvePlot("Canada", 2, 5, [], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["Canada"].posture, "Hard")
        self.assertEqual(app.map["Spain"].posture, "")
        self.assertEqual(app.map["Scandinavia"].posture, "")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Canada"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Russia"].plots = 1
        app.resolvePlot("Russia", 2, 4, [], [], [], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Russia"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "")
        self.assertEqual(app.map["Scandinavia"].posture, "")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Russia"].plots, 0)

        app = Labyrinth(1, "WMD", testBlankScenarioSetup)
        app.map["Germany"].plots = 1
        app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Germany"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "Hard")
        self.assertEqual(app.map["Scandinavia"].posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 0)

        app = Labyrinth(1, "WMD", testBlankScenarioSetup)
        app.funding = 1
        app.map["Germany"].plots = 1
        app.resolvePlot("Germany", 3, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Germany"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "Hard")
        self.assertEqual(app.map["Scandinavia"].posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 0)

    def testResolveMuslimIranPlots(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_fair()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 1, 0, [], [], [], [3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 1)
        app.resolvePlot("Iraq", 1, 0, [], [], [], [2])
        self.assertEqual(app.funding, 7)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_good()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 1, 2])
        self.assertEqual(app.funding, 7)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_good()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 1, 2])
        self.assertEqual(app.funding, 7)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iran"].plots = 1
        app.resolvePlot("Iran", 3, 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iran"].is_fair())
        self.assertEqual(app.map["Iran"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iran"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.map["Iraq"].troopCubes = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 6)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.map["Iraq"].troopCubes = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 1)
        self.assertEqual(app.map["Iraq"].plots, 0)

    def testResolveUSPlots(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].plots = 1
        app.map["United States"].posture = "Hard"
        app.resolvePlot("United States", 1, 4, [1, 6, 1], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["United States"].posture, "Soft")
        self.assertEqual(app.prestige, 6)
        self.assertEqual(app.map["United States"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].plots = 1
        app.map["United States"].posture = "Soft"
        app.resolvePlot("United States", 2, 4, [5, 6, 1], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["United States"].posture, "Soft")
        self.assertEqual(app.prestige, 8)
        self.assertEqual(app.map["United States"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].plots = 1
        app.map["United States"].posture = "Soft"
        app.resolvePlot("United States", 3, 5, [5, 6, 4], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["United States"].posture, "Hard")
        self.assertEqual(app.prestige, 11)
        self.assertEqual(app.map["United States"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.gameOver)
        app.map["United States"].plots = 1
        app.map["United States"].posture = "Soft"
        app.resolvePlot("United States", "WMD", 0, [], [], [], [])
        self.assertEqual(app.map["United States"].plots, 0)
        self.assertTrue(app.gameOver)

    def testResolveMuslimIranPlotsWithBacklash(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_fair()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 1, 0, [], [], [], [3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 1)
        app.resolvePlot("Iraq", 1, 0, [], [], [], [2], True)
        self.assertEqual(app.funding, 3)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_good()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 1, 2], True)
        self.assertEqual(app.funding, 3)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_good()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 1, 2], True)
        self.assertEqual(app.funding, 1)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iran"].plots = 1
        app.resolvePlot("Iran", 3, 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.map["Iran"].is_fair())
        self.assertEqual(app.map["Iran"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iran"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.map["Iraq"].troopCubes = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 6)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.map["Iraq"].troopCubes = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 1)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 1)
        self.assertEqual(app.map["Iraq"].plots, 0)


class PlacePlots(LabyrinthTest):
    """Place Plots"""

    def testPlacePlot(self):
        # no cells
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 1)
        unusedOps = app.executePlot(2, False, [1, 2])
        self.assertEqual(unusedOps, 2)
        unusedOps = app.executePlot(3, True, [1, 2, 3])
        self.assertEqual(unusedOps, 3)

        # 1 cell in US
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 1
        unusedOps = app.executePlot(1, True, [2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 0)

        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 1)
        self.assertEqual(app.map["United States"].plots, 1)

        # 2 cells in us
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 2
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 2
        unusedOps = app.executePlot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 2)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 2
        unusedOps = app.executePlot(2, True, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 2
        unusedOps = app.executePlot(3, True, [1, 2, 3])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 1)

        # 3 cells in us
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.map["United States"].plots, 2)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(2, True, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(2, True, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(3, True, [1, 1, 3])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 3)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 2)

        # Low prestige, no GWOT penalty
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        unusedOps = app.executePlot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].activeCells, 1)
        self.assertEqual(app.map["Iraq"].plots, 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.map["Israel"].sleeperCells = 1
        app.map["United States"].posture = "Soft"
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 0)
        self.assertEqual(app.map["Israel"].sleeperCells, 1)
        self.assertEqual(app.map["Israel"].plots, 0)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].activeCells, 1)
        self.assertEqual(app.map["Iraq"].plots, 1)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 0)
        self.assertEqual(app.map["Israel"].sleeperCells, 1)
        self.assertEqual(app.map["Israel"].plots, 0)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 1)

        # Funding section
        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.funding = 9
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 0
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["Israel"].activeCells, 0)
        self.assertEqual(app.map["Israel"].sleeperCells, 1)
        self.assertEqual(app.map["Israel"].plots, 0)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 0
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 0
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 0
        unusedOps = app.executePlot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 1)
        self.assertEqual(app.map["Iraq"].plots, 0)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 0
        unusedOps = app.executePlot(3, True, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 1)
        self.assertEqual(app.map["Iraq"].plots, 1)

        # High prestige
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 4
        app.markers = ["Abu Sayyaf"]
        app.map["Israel"].sleeperCells = 1
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        app.map["Iraq"].troopCubes = 1
        app.map["Philippines"].sleeperCells = 1
        app.map["Philippines"].troopCubes = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 0)
        self.assertEqual(app.map["Israel"].sleeperCells, 1)
        self.assertEqual(app.map["Israel"].plots, 0)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)
        self.assertEqual(app.map["Philippines"].activeCells, 1)
        self.assertEqual(app.map["Philippines"].sleeperCells, 0)
        self.assertEqual(app.map["Philippines"].plots, 1)

        # priorities box
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.map["Israel"].sleeperCells = 0
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Spain"].sleeperCells = 0
        app.map["Iraq"].make_good()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].aid = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)
        self.assertEqual(app.map["Gulf States"].plots, 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 3
        app.map["Israel"].sleeperCells = 0
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Spain"].sleeperCells = 0
        app.map["Iraq"].make_good()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].aid = 1
        unusedOps = app.executePlot(1, False, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].plots, 1)
        self.assertEqual(app.map["Gulf States"].plots, 0)


class IsAdjacent(LabyrinthTest):
    """Test isAdjacent"""

    def testIsAdjacent(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.isAdjacent("Iran", "Iraq"))
        self.assertTrue(app.isAdjacent("Germany", "Spain"))
        self.assertTrue(app.isAdjacent("Libya", "Italy"))
        self.assertTrue(app.isAdjacent("Benelux", "Russia"))
        self.assertTrue(app.isAdjacent("Lebanon", "France"))
        self.assertFalse(app.isAdjacent("United States", "Lebanon"))


class CountryResources(LabyrinthTest):
    """Test countryResources"""

    def testCountryResources(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.countryResources("Iraq") == 3)
        self.assertTrue(app.countryResources("Egypt") == 3)
        self.assertTrue(app.countryResources("Syria") == 2)
        self.assertTrue(app.countryResources("Lebanon") == 1)
        app.lapsing.append("Oil Price Spike")
        self.assertTrue(app.countryResources("Iraq") == 4)
        self.assertTrue(app.countryResources("Egypt") == 3)
        self.assertTrue(app.countryResources("Syria") == 2)
        self.assertTrue(app.countryResources("Lebanon") == 1)
        app.lapsing.append("Biometrics")
        app.lapsing.append("Oil Price Spike")
        self.assertTrue(app.countryResources("Iraq") == 5)
        self.assertTrue(app.countryResources("Egypt") == 3)
        self.assertTrue(app.countryResources("Syria") == 2)
        self.assertTrue(app.countryResources("Lebanon") == 1)


class CountryDistance(LabyrinthTest):
    """Test countryDistance"""

    def testIsAdjacent(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.countryDistance("Iran", "Iran") == 0)
        self.assertTrue(app.countryDistance("Iran", "Iraq") == 1)
        self.assertTrue(app.countryDistance("Iran", "Sudan") == 4)
        self.assertTrue(app.countryDistance("Thailand", "United States") == 2)
        self.assertTrue(app.countryDistance("Russia", "Morocco") == 2)


class Card1(LabyrinthTest):
    """Backlash"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["1"].playable("US", app, True))
        app.map["Canada"].plots = 1
        self.assertFalse(app.deck["1"].playable("US", app, True))
        app.map["Iraq"].plots = 1
        self.assertTrue(app.deck["1"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.backlashInPlay)
        app.deck["1"].playEvent("US", app)
        self.assertFalse(app.backlashInPlay)
        app.map["United States"].plots = 1
        app.deck["1"].playEvent("US", app)
        self.assertFalse(app.backlashInPlay)
        app.map["Iraq"].plots = 1
        app.deck["1"].playEvent("US", app)
        self.assertTrue(app.backlashInPlay)


class Card2(LabyrinthTest):
    """Biometrics"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["2"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse("Biometrics" in app.lapsing)
        app.deck["2"].playEvent("US", app)
        self.assertTrue("Biometrics" in app.lapsing)
        app.do_turn("")
        self.assertFalse("Biometrics" in app.lapsing)

    def testTravelDestination(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.deck["2"].playEvent("US", app)
        dest = app.travelDestinations(1)
        self.assertTrue("Biometrics" in app.lapsing)
        self.assertEqual(dest, [])
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

    def testTravelSource(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.deck["2"].playEvent("US", app)
        dest = app.travelDestinations(1)
        self.assertEqual(dest, [])
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.map["Sudan"].make_islamist_rule()        
        app.map["Sudan"].sleeperCells = 4    
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Iraq"])

    def testTravelToGood(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.deck["2"].playEvent("US", app)
        dest = app.travelDestinations(1)
        self.assertEqual(dest, [])
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.map["Sudan"].make_islamist_rule()        
        app.map["Sudan"].sleeperCells = 4    
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Iraq"])
        app.handleTravel(1)


class Card3(LabyrinthTest):
    """CTR"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["3"].playable("US", app, True))
        app.do_reassessment("")
        self.assertTrue(app.deck["3"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.do_reassessment("")
        self.assertFalse("CTR" in app.map["Russia"].markers)
        self.assertFalse("CTR" in app.map["Central Asia"].markers)
        app.map["Central Asia"].make_adversary()
        app.deck["3"].playEvent("US", app)
        self.assertTrue("CTR" in app.map["Russia"].markers)
        self.assertFalse("CTR" in app.map["Central Asia"].markers)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.do_reassessment("")
        self.assertFalse("CTR" in app.map["Russia"].markers)
        self.assertFalse("CTR" in app.map["Central Asia"].markers)
        app.map["Central Asia"].make_neutral()
        app.deck["3"].playEvent("US", app)
        self.assertTrue("CTR" in app.map["Russia"].markers)
        self.assertTrue("CTR" in app.map["Central Asia"].markers)
        print app.map["Russia"].countryStr()
        self.assertTrue("Markers: CTR" in app.map["Russia"].countryStr())
        self.assertTrue("Markers: CTR" in app.map["Central Asia"].countryStr())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.do_reassessment("")
        self.assertFalse("CTR" in app.map["Russia"].markers)
        self.assertFalse("CTR" in app.map["Central Asia"].markers)
        app.map["Central Asia"].make_ally()
        app.deck["3"].playEvent("US", app)
        self.assertTrue("CTR" in app.map["Russia"].markers)
        self.assertTrue("CTR" in app.map["Central Asia"].markers)


class Card4(LabyrinthTest):
    """Moro Talks"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["4"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.map["Philippines"].posture == "")
        self.assertTrue(app.funding == 5)
        app.deck["4"].playEvent("US", app)
        self.assertTrue("Moro Talks" in app.markers)
        self.assertTrue(app.map["Philippines"].posture == "Soft" or app.map["Philippines"].posture == "Hard")
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.funding = 1
        self.assertTrue(app.map["Philippines"].posture == "")
        self.assertTrue(app.funding == 1)
        app.deck["4"].playEvent("US", app)
        self.assertTrue(app.map["Philippines"].posture == "Soft" or app.map["Philippines"].posture == "Hard")
        self.assertTrue(app.funding == 1)


class Card5(LabyrinthTest):
    """NEST"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["5"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse("NEST" in app.markers)
        app.deck["5"].playEvent("US", app)
        self.assertTrue("NEST" in app.markers)


class Card6and7(LabyrinthTest):
    """Sanctions"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["6"].playable("US", app, True))
        self.assertFalse(app.deck["7"].playable("US", app, True))
        app.markers.append("Patriot Act")
        self.assertTrue(app.deck["6"].playable("US", app, True))
        self.assertTrue(app.deck["7"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.markers.append("Patriot Act")
        app.deck["6"].playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.markers.append("Patriot Act")
        app.deck["7"].playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.funding = 2
        app.markers.append("Patriot Act")
        app.deck["6"].playEvent("US", app)
        self.assertTrue(app.funding == 1)


class Card8and9and10(LabyrinthTest):
    """Special Forces"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["8"].playable("US", app, True))
        self.assertFalse(app.deck["9"].playable("US", app, True))
        self.assertFalse(app.deck["10"].playable("US", app, True))
        app.map["Iran"].sleeperCells = 1
        self.assertFalse(app.deck["8"].playable("US", app, True))
        self.assertFalse(app.deck["9"].playable("US", app, True))
        self.assertFalse(app.deck["10"].playable("US", app, True))
        app.map["Iran"].troopCubes = 1
        self.assertTrue(app.deck["8"].playable("US", app, True))
        self.assertTrue(app.deck["9"].playable("US", app, True))
        self.assertTrue(app.deck["10"].playable("US", app, True))
        app.map["Iran"].troopCubes = 0
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["8"].playable("US", app, True))
        self.assertTrue(app.deck["9"].playable("US", app, True))
        self.assertTrue(app.deck["10"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.listCountriesWithCellAndAdjacentTroops()
        app.map["Iran"].sleeperCells = 1
        app.map["Iraq"].troopCubes = 1
        app.listCountriesWithCellAndAdjacentTroops()


class Card11(LabyrinthTest):
    """Abbas"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["11"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.funding == 3)
        self.assertTrue("Abbas" in app.markers)
        app.map["Israel"].plots = 1
        app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Syria")
        app.map["Syria"].make_islamist_rule()
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.funding == 3)
        self.assertTrue("Abbas" in app.markers)
        app.map["Israel"].plots = 1
        app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Lebanon")
        app.map["Lebanon"].make_islamist_rule()
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 7)
        self.assertTrue(app.funding == 5)
        self.assertTrue("Abbas" in app.markers)
        app.map["Israel"].plots = 1
        app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.troops = 4
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 7)
        self.assertTrue(app.funding == 5)
        self.assertTrue("Abbas" in app.markers)
        app.map["Israel"].plots = 1
        app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 12
        app.funding = 2
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 12)
        self.assertTrue(app.funding == 1)


class Card12(LabyrinthTest):
    """Al-Azhar"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["12"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.map["Egypt"].is_ungoverned())
        app.deck["12"].playEvent("US", app)
        self.assertTrue(app.map["Egypt"].is_governed())
        self.assertTrue(app.funding == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.map["Egypt"].is_ungoverned())
        app.map["Pakistan"].make_islamist_rule()
        app.deck["12"].playEvent("US", app)
        self.assertTrue(app.map["Egypt"].is_governed())
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.funding = 2
        self.assertTrue(app.map["Egypt"].is_ungoverned())
        app.deck["12"].playEvent("US", app)
        self.assertTrue(app.map["Egypt"].is_governed())
        self.assertTrue(app.funding == 1)


class Card13(LabyrinthTest):
    """Anbar Awakening"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["13"].playable("US", app, True))
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["13"].playable("US", app, True))
        app.map["Iraq"].troopCubes = 0
        app.map["Syria"].troopCubes = 1
        self.assertTrue(app.deck["13"].playable("US", app, True))
        app.map["Syria"].troopCubes = 0
        self.assertFalse(app.deck["13"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].troopCubes = 1
        app.deck["13"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].aid > 0)
        self.assertTrue("Anbar Awakening" in app.markers)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Syria"].troopCubes = 1
        app.deck["13"].playEvent("US", app)
        self.assertTrue(app.map["Syria"].aid > 0)
        self.assertTrue("Anbar Awakening" in app.markers)


class Card14(LabyrinthTest):
    """Covert Action"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["14"].playable("US", app, True))
        app.map["Iraq"].make_adversary()
        self.assertTrue(app.deck["14"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.listAdversaryCountries()
        app.map["Iran"].make_adversary()
        app.map["Iraq"].make_adversary()
        app.listAdversaryCountries()


class Card15(LabyrinthTest):
    """Ethiopia Strikes"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["15"].playable("US", app, True))
        app.map["Somalia"].make_islamist_rule()
        self.assertTrue(app.deck["15"].playable("US", app, True))
        app.map["Somalia"].make_poor()
        self.assertFalse(app.deck["15"].playable("US", app, True))
        app.map["Sudan"].make_islamist_rule()
        self.assertTrue(app.deck["15"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Somalia"].make_islamist_rule()
        app.map["Somalia"].make_adversary()
        app.deck["15"].playEvent("US", app)
        self.assertTrue(app.map["Somalia"].is_poor())
        self.assertTrue(app.map["Somalia"].is_neutral())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Sudan"].make_islamist_rule()
        app.map["Sudan"].make_adversary()
        app.deck["15"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_poor())
        self.assertTrue(app.map["Sudan"].is_neutral())


class Card16(LabyrinthTest):
    """Euro-Islam"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["16"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.executeCardEuroIslam("Hard")
        self.assertTrue(app.map["Benelux"].posture == "Hard")
        self.assertTrue(app.funding == 4)
        app.map["Iraq"].make_islamist_rule()
        app.executeCardEuroIslam("Soft")
        self.assertTrue(app.map["Benelux"].posture == "Soft")
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.funding = 1
        app.executeCardEuroIslam("Hard")
        self.assertTrue(app.map["Benelux"].posture == "Hard")
        self.assertTrue(app.funding == 1)


class Card17(LabyrinthTest):
    """FSB"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["17"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ['y'])
        app.map["Central Asia"].activeCells = 1
        app.map["Russia"].activeCells = 1
        app.deck["17"].playEvent("US", app)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ['y'])
        app.map["Russia"].activeCells = 1
        app.deck["17"].playEvent("US", app)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ['y'])
        app.map["Central Asia"].sleeperCells = 1
        app.deck["17"].playEvent("US", app)


class Card18(LabyrinthTest):
    """Intel Community"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["18"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        history_before = len(app.history)
        app.deck["18"].playEvent("US", app)
        self.assert_new_messages(app, history_before, [
            'Card played for Event.',
            'Examine Jihadist hand. Do not change order of cards.',
            'Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi).',
            'You may now interrupt this action phase to play another card (Use the u command).'
        ])


class Card19(LabyrinthTest):
    """Kemalist Republic"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["19"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["19"].playEvent("US", app)
        self.assertTrue(app.map["Turkey"].is_fair())
        self.assertTrue(app.map["Turkey"].is_ally())


class Card20(LabyrinthTest):
    """King Abdullah"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["20"].playable("US", app, True))
        self.assertTrue(app.funding == 5)
        self.assertTrue(app.prestige == 7)

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["20"].playEvent("US", app)
        self.assertTrue(app.map["Jordan"].is_fair())
        self.assertTrue(app.map["Jordan"].is_ally())
        self.assertTrue(app.funding == 4)
        self.assertTrue(app.prestige == 8)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.funding = 1
        app.prestige = 12
        app.deck["20"].playEvent("US", app)
        self.assertTrue(app.map["Jordan"].is_fair())
        self.assertTrue(app.map["Jordan"].is_ally())
        self.assertTrue(app.funding == 1)
        self.assertTrue(app.prestige == 12)


class Card21(LabyrinthTest):
    """Let's Roll"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["21"].playable("US", app, True))
        app.map["Canada"].plots = 1
        self.assertTrue(app.deck["21"].playable("US", app, True))
        app.map["Canada"].plots = 0
        self.assertFalse(app.deck["21"].playable("US", app, True))
        app.map["Saudi Arabia"].make_fair()
        app.map["Saudi Arabia"].plots = 1
        self.assertFalse(app.deck["21"].playable("US", app, True))
        app.map["Saudi Arabia"].make_good()
        self.assertTrue(app.deck["21"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Canada"].plots = 1
        app.map["Spain"].posture = "Soft"
        app.executeCardLetsRoll("Canada", "Spain", "Hard")
        self.assertTrue(app.map["Canada"].plots == 0)
        self.assertTrue(app.map["Spain"].posture == "Hard")

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Saudi Arabi", "Spain", "h"])
        app.map["Spain"].posture = "Soft"
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].plots = 1
        app.deck["21"].playEvent("US", app)
        self.assertTrue(app.map["Spain"].posture == "Hard")
        self.assertTrue(app.map["Saudi Arabia"].plots == 0)


class Card22(LabyrinthTest):
    """Mossad and Shin Bet"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["22"].playable("US", app, True))
        app.map["Israel"].sleeperCells = 1
        self.assertTrue(app.deck["22"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["22"].playable("US", app, True))
        app.map["Jordan"].sleeperCells = 1
        self.assertTrue(app.deck["22"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["22"].playable("US", app, True))
        app.map["Lebanon"].sleeperCells = 1
        self.assertTrue(app.deck["22"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Israel"].sleeperCells = 1
        app.map["Israel"].activeCells = 4
        app.map["Jordan"].activeCells = 3
        app.map["Lebanon"].sleeperCells = 2
        app.map["Iraq"].sleeperCells = 2
        app.deck["22"].playEvent("US", app)
        self.assertTrue(app.map["Israel"].sleeperCells == 0)
        self.assertTrue(app.map["Israel"].activeCells == 0)
        self.assertTrue(app.map["Jordan"].sleeperCells == 0)
        self.assertTrue(app.map["Jordan"].activeCells == 0)
        self.assertTrue(app.map["Lebanon"].sleeperCells == 0)
        self.assertTrue(app.map["Lebanon"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].sleeperCells == 2)


class Card23and24and25(LabyrinthTest):
    """Predator"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["23"].playable("US", app, True))
        app.map["Israel"].sleeperCells = 1
        self.assertFalse(app.deck["23"].playable("US", app, True))
        app.map["Iran"].sleeperCells = 1
        self.assertFalse(app.deck["23"].playable("US", app, True))
        app.map["Jordan"].sleeperCells = 1
        self.assertTrue(app.deck["23"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["24"].playable("US", app, True))
        app.map["Israel"].sleeperCells = 1
        self.assertFalse(app.deck["24"].playable("US", app, True))
        app.map["Iran"].sleeperCells = 1
        self.assertFalse(app.deck["24"].playable("US", app, True))
        app.map["Jordan"].sleeperCells = 1
        self.assertTrue(app.deck["24"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["25"].playable("US", app, True))
        app.map["Israel"].sleeperCells = 1
        self.assertFalse(app.deck["25"].playable("US", app, True))
        app.map["Iran"].sleeperCells = 1
        self.assertFalse(app.deck["25"].playable("US", app, True))
        app.map["Jordan"].sleeperCells = 1
        self.assertTrue(app.deck["25"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.map["Iraq"].sleeperCells = 2
        app.deck["25"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)


class Card26(LabyrinthTest):
    """Quartet"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["26"].playable("US", app, True))
        app.markers.append("Abbas")
        self.assertTrue(app.deck["26"].playable("US", app, True))
        app.troops = 4
        self.assertFalse(app.deck["26"].playable("US", app, True))
        app.troops = 5
        self.assertTrue(app.deck["26"].playable("US", app, True))
        app.map["Egypt"].make_islamist_rule()
        self.assertFalse(app.deck["26"].playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.markers.append("Abbas")
        app.deck["26"].playEvent("US", app)
        self.assertTrue(app.prestige == 9)
        self.assertTrue(app.funding == 2)


class Card27(LabyrinthTest):
    """Saddam Captured"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["27"].playable("US", app, True))
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["27"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].troopCubes = 1
        app.deck["27"].playEvent("US", app)
        self.assertTrue("Saddam Captured" in app.markers)
        self.assertTrue(app.map["Iraq"].aid == 1)


class Card28(LabyrinthTest):
    """Sharia"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["28"].playable("US", app, True))
        app.map["Iraq"].besieged = 1
        self.assertTrue(app.deck["28"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].besieged = 1
        app.deck["28"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].besieged == 0)


class Card29(LabyrinthTest):
    """Tony Blair"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["29"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].posture = "Hard"

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].posture = "Hard"
        app.executeNonMuslimWOI("Spain", 4)
        self.assertTrue(app.map["Spain"].posture == "Soft")
        app.executeNonMuslimWOI("France", 5)
        self.assertTrue(app.map["France"].posture == "Hard")


class Card30(LabyrinthTest):
    """UN Nation Building"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["30"].playable("US", app, True))
        app.map["Iraq"].regimeChange = 1
        self.assertTrue(app.deck["30"].playable("US", app, True))
        app.markers.append("Vieira de Mello Slain")
        self.assertFalse(app.deck["30"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["6"])
        app.map["United States"].posture = "Hard"
        app.map["Spain"].posture = "Soft"
        app.map["France"].posture = "Soft"
        app.map["Germany"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        # app.map["Iraq"].regimeChange = 1
        app.map["Pakistan"].regimeChange = 1
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_ally()
        app.deck["30"].playEvent("US", app)
        self.assertTrue(app.map["Pakistan"].aid == 1)
        self.assertTrue(app.map["Pakistan"].is_fair())

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq", "6"])
        app.map["United States"].posture = "Hard"
        app.map["Spain"].posture = "Soft"
        app.map["France"].posture = "Soft"
        app.map["Germany"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_ally()
        app.map["Pakistan"].regimeChange = 1
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_ally()
        app.deck["30"].playEvent("US", app)
        self.assertTrue(app.map["Pakistan"].aid == 0)
        self.assertTrue(app.map["Pakistan"].is_poor())
        self.assertTrue(app.map["Iraq"].aid == 1)
        self.assertTrue(app.map["Iraq"].is_fair())


class Card31(LabyrinthTest):
    """Wiretapping"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["31"].playable("US", app, True))
        app.map["United States"].sleeperCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].activeCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].cadre = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].plots = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["31"].playable("US", app, True))
        app.map["United Kingdom"].sleeperCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United Kingdom"].activeCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United Kingdom"].cadre = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United Kingdom"].plots = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["31"].playable("US", app, True))
        app.map["Canada"].sleeperCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Canada"].activeCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Canada"].cadre = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Canada"].plots = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Canada"].plots = 1
        app.markers.append("Leak-Wiretapping")
        self.assertFalse(app.deck["31"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 1
        app.map["United States"].activeCells = 1
        app.map["United States"].cadre = 1
        app.map["United States"].plots = 1
        app.map["United Kingdom"].sleeperCells = 1
        app.map["United Kingdom"].activeCells = 1
        app.map["United Kingdom"].cadre = 1
        app.map["United Kingdom"].plots = 1
        app.map["Canada"].sleeperCells = 1
        app.map["Canada"].activeCells = 1
        app.map["Canada"].cadre = 1
        app.map["Canada"].plots = 1
        app.deck["31"].playEvent("US", app)
        self.assertTrue("Wiretapping" in app.markers)
        self.assertTrue(app.map["United States"].sleeperCells == 0)
        self.assertTrue(app.map["United States"].activeCells == 0)
        self.assertTrue(app.map["United States"].cadre == 0)
        self.assertTrue(app.map["United States"].plots == 0)
        self.assertTrue(app.map["United Kingdom"].sleeperCells == 0)
        self.assertTrue(app.map["United Kingdom"].activeCells == 0)
        self.assertTrue(app.map["United Kingdom"].cadre == 0)
        self.assertTrue(app.map["United Kingdom"].plots == 0)
        self.assertTrue(app.map["Canada"].sleeperCells == 0)
        self.assertTrue(app.map["Canada"].activeCells == 0)
        self.assertTrue(app.map["Canada"].cadre == 0)
        self.assertTrue(app.map["Canada"].plots == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].sleeperCells = 1
        app.map["United States"].activeCells = 1
        app.map["United States"].cadre = 1
        app.map["United States"].plots = 1
        app.map["Canada"].sleeperCells = 1
        app.map["Canada"].activeCells = 1
        app.map["Canada"].cadre = 1
        app.map["Canada"].plots = 1
        app.deck["31"].playEvent("US", app)
        self.assertTrue("Wiretapping" in app.markers)
        self.assertTrue(app.map["United States"].sleeperCells == 0)
        self.assertTrue(app.map["United States"].activeCells == 0)
        self.assertTrue(app.map["United States"].cadre == 0)
        self.assertTrue(app.map["United States"].plots == 0)
        self.assertTrue(app.map["United Kingdom"].sleeperCells == 0)
        self.assertTrue(app.map["United Kingdom"].activeCells == 0)
        self.assertTrue(app.map["United Kingdom"].cadre == 0)
        self.assertTrue(app.map["United Kingdom"].plots == 0)
        self.assertTrue(app.map["Canada"].sleeperCells == 0)
        self.assertTrue(app.map["Canada"].activeCells == 0)
        self.assertTrue(app.map["Canada"].cadre == 0)
        self.assertTrue(app.map["Canada"].plots == 0)


class Card32(LabyrinthTest):
    """Back Channel"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["y", "n"])
        app.map["United States"].posture = "Hard"
        self.assertFalse(app.deck["32"].playable("US", app, True))
        app.map["United States"].posture = "Soft"
        self.assertFalse(app.deck["32"].playable("US", app, True))

        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        app.map["Pakistan"].make_adversary()
        print "Say yes"
        self.assertTrue(app.deck["32"].playable("US", app, True))
        print "Say no"
        self.assertFalse(app.deck["32"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["y", "y", "Pakistan"])
        app.map["United States"].posture = "Soft"
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        app.map["Pakistan"].make_islamist_rule()
        app.map["Pakistan"].make_adversary()
        self.assertTrue(app.deck["32"].playable("US", app, True))
        aid_before = app.map["Pakistan"].aid
        app.deck["32"].playEvent("US", app)
        aid_after = app.map["Pakistan"].aid
        self.assertTrue(app.map["Iraq"].is_adversary())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(aid_after, aid_before + 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["n", "n"])
        app.map["United States"].posture = "Soft"
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        app.map["Pakistan"].make_islamist_rule()
        app.map["Pakistan"].make_adversary()
        self.assertFalse(app.deck["32"].playable("US", app, True))
        app.deck["32"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_adversary())
        self.assertTrue(app.map["Pakistan"].is_adversary())


class Card33(LabyrinthTest):
    """Benazir Bhutto"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["33"].playable("US", app, True))
        app.markers.append("Bhutto Shot")
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["33"].playable("US", app, True))
        app.map["Pakistan"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Afghanistan"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["India"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Gulf States"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Indonesia/Malaysia"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Pakistan"].make_poor()
        app.deck["33"].playEvent("US", app)
        self.assertTrue(app.map["Pakistan"].is_fair())

        # no jihad in Pakistan
        app = Labyrinth(1, 1, test3ScenarioSetup)
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(1), False)
        app.map["Pakistan"].make_fair()
        app.map["Pakistan"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Pakistan", 1)])
        app.deck["33"].playEvent("US", app)
        self.assertEqual(app.minorJihadInGoodFairChoice(1), False)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertEqual(app.majorJihadPossible(3), [])
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].activeCells = 5
        self.assertEqual(app.majorJihadPossible(3), ["Pakistan"])
        app.deck["33"].playEvent("US", app)
        self.assertEqual(app.majorJihadPossible(3), [])

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].activeCells = 5
        app.map["Iraq"].make_poor()
        app.map["Iraq"].activeCells = 5
        self.assertEqual(app.majorJihadChoice(3), "Pakistan")
        app.deck["33"].playEvent("US", app)
        self.assertEqual(app.majorJihadPossible(3), ["Iraq"])


class Card34(LabyrinthTest):
    """Enhanced Measures"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["34"].playable("US", app, True))
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        self.assertTrue(app.deck["34"].playable("US", app, True))
        app.markers.append("Leak-Enhanced Measures")
        self.assertFalse(app.deck["34"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].posture = "Soft"
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        self.assertFalse(app.deck["34"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        app.map["Pakistan"].cadre = 1
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].troopCubes = 2
        app.deck["34"].playEvent("US", app)
        self.assertTrue("Enhanced Measures" in app.markers)
        self.assertTrue(app.map["Pakistan"].cadre == 1)
        self.assertTrue(app.map["Iraq"].cadre == 0)


class Card35(LabyrinthTest):
    """Hajib"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["35"].playable("US", app, True))
        app.map["Iraq"].make_islamist_rule()
        self.assertFalse(app.deck["35"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["h"])
        app.deck["35"].playEvent("US", app)
        self.assertTrue(app.map["Turkey"].governance_is_better_than(POOR))
        self.assertTrue(app.map["Turkey"].is_governed())
        self.assertTrue(not app.map["Turkey"].is_unaligned())
        print "Say Hard"
        self.assertTrue(app.map["France"].posture == "Hard")
        self.assertTrue(app.funding == 3)


class Card36(LabyrinthTest):
    """Indo-Pakistani Talks"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["36"].playable("US", app, True))
        app.map["Pakistan"].make_islamist_rule()
        self.assertFalse(app.deck["36"].playable("US", app, True))
        app.map["Pakistan"].make_poor()
        self.assertFalse(app.deck["36"].playable("US", app, True))
        app.map["Pakistan"].make_fair()
        self.assertTrue(app.deck["36"].playable("US", app, True))
        app.map["Pakistan"].make_good()
        self.assertTrue(app.deck["36"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["s", "1"])
        app.map["Pakistan"].make_fair()
        app.map["Pakistan"].make_adversary()
        app.deck["36"].playEvent("US", app)
        self.assertTrue(app.map["Pakistan"].is_ally())
        self.assertTrue("Indo-Pakistani Talks" in app.markers)
        self.assertTrue(app.map["India"].posture == "Soft")
        app.map["India"].plots = 1
        app.do_plot("")
        self.assertFalse("Indo-Pakistani Talks" in app.markers)


class Card37(LabyrinthTest):
    """Iraqi WMD"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["37"].playable("US", app, True))
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        self.assertTrue(app.deck["37"].playable("US", app, True))
        app.map["United States"].posture = "Soft"
        self.assertFalse(app.deck["37"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["37"].playEvent("US", app)
        self.assertTrue("Iraqi WMD" in app.markers)
        app.handleRegimeChange("Iraq", "track", 6, 4, (4, 4, 4))
        self.assertFalse("Iraqi WMD" in app.markers)


class Card38(LabyrinthTest):
    """Libyan Desl"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["38"].playable("US", app, True))
        app.map["Libya"].make_poor()
        self.assertFalse(app.deck["38"].playable("US", app, True))
        app.map["Iraq"].make_ally()
        self.assertTrue(app.deck["38"].playable("US", app, True))
        app.map["Iraq"].make_neutral()
        self.assertFalse(app.deck["38"].playable("US", app, True))
        app.map["Syria"].make_ally()
        self.assertTrue(app.deck["38"].playable("US", app, True))
        app.map["Libya"].make_fair()
        self.assertFalse(app.deck["38"].playable("US", app, True))
        app.map["Libya"].make_islamist_rule()
        self.assertFalse(app.deck["38"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["france", "s", "Spain", "h"])
        app.map["Libya"].make_poor()
        app.map["Iraq"].make_ally()
        app.deck["38"].playEvent("US", app)
        self.assertTrue("Libyan Deal" in app.markers)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.map["France"].posture == "Soft")
        self.assertTrue(app.map["Spain"].posture == "Hard")


class Card39(LabyrinthTest):
    """Libyan WMD"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["39"].playable("US", app, True))
        app.map["Libya"].make_poor()
        app.map["Libya"].make_adversary()
        self.assertTrue(app.deck["39"].playable("US", app, True))
        app.map["United States"].posture = "Soft"
        self.assertFalse(app.deck["39"].playable("US", app, True))
        app.map["United States"].posture = "Hard"
        self.assertTrue(app.deck["39"].playable("US", app, True))
        app.markers.append("Libyan Deal")
        self.assertFalse(app.deck["39"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["39"].playEvent("US", app)
        self.assertTrue("Libyan WMD" in app.markers)
        app.handleRegimeChange("Libya", "track", 6, 4, (4, 4, 4))
        self.assertFalse("Libyan WMD" in app.markers)


class Card40(LabyrinthTest):
    """Mass Turnout"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["40"].playable("US", app, True))
        app.map["Libya"].make_poor()
        app.map["Libya"].make_adversary()
        self.assertFalse(app.deck["40"].playable("US", app, True))
        app.map["Libya"].regimeChange = 1
        self.assertTrue(app.deck["40"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Libya"].make_poor()
        app.map["Libya"].make_adversary()
        app.map["Libya"].regimeChange = 1
        app.deck["40"].playEvent("US", app)
        self.assertTrue(app.map["Libya"].is_fair())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Libya"].make_fair()
        app.map["Libya"].make_adversary()
        app.map["Libya"].regimeChange = 1
        app.map["Libya"].aid = 1
        app.deck["40"].playEvent("US", app)
        self.assertTrue(app.map["Libya"].is_good())
        self.assertTrue(app.map["Libya"].regimeChange == 0)
        self.assertTrue(app.map["Libya"].aid == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.map["Libya"].make_fair()
        app.map["Libya"].make_adversary()
        app.map["Libya"].regimeChange = 1
        app.map["Libya"].aid = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_adversary()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].aid = 1
        app.deck["40"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_good())
        self.assertTrue(app.map["Iraq"].regimeChange == 0)
        self.assertTrue(app.map["Iraq"].aid == 0)


class Card41(LabyrinthTest):
    """NATO"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["41"].playable("US", app, True))
        app.map["Libya"].make_poor()
        app.map["Libya"].make_ally()
        app.map["Libya"].regimeChange = 1
        self.assertTrue(app.deck["41"].playable("US", app, True))
        app.map["Canada"].posture = "Soft"
        self.assertTrue(app.deck["41"].playable("US", app, True))
        app.map["Spain"].posture = "Soft"
        self.assertFalse(app.deck["41"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Libya", "track", "3"])
        app.map["Libya"].make_poor()
        app.map["Libya"].make_ally()
        app.map["Libya"].regimeChange = 1
        app.map["Libya"].changeTroops(2)
        app.deck["41"].playEvent("US", app)
        self.assertTrue(app.map["Libya"].aid == 1)
        self.assertTrue(app.map["Libya"].troops() == 4)
        self.assertTrue("NATO" in app.map["Libya"].markers)

        app.map["Libya"].regimeChange = 0
        print "Deploy 3 from Libya to track:"
        app.do_deploy("")
        self.assertTrue(app.map["Libya"].troops() == 0)
        self.assertTrue("NATO" not in app.map["Libya"].markers)        

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.map["Libya"].make_fair()
        app.map["Libya"].make_adversary()
        app.map["Libya"].regimeChange = 1
        app.map["Libya"].aid = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_adversary()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].aid = 0
        app.deck["41"].playEvent("US", app)
        self.assertEqual(app.map["Iraq"].aid, 1)
        self.assertTrue(app.map["Iraq"].troops() == 2)
        self.assertTrue("NATO" in app.map["Iraq"].markers)


class Card42(LabyrinthTest):
    """Pakistani Offensive"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["42"].playable("US", app, True))
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_ally()
        self.assertFalse(app.deck["42"].playable("US", app, True))
        app.map["Pakistan"].markers.append("FATA")
        self.assertTrue(app.deck["42"].playable("US", app, True))
        app.map["Pakistan"].make_neutral()
        self.assertFalse(app.deck["42"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_ally()
        app.map["Pakistan"].markers.append("FATA")
        app.deck["42"].playEvent("US", app)
        self.assertTrue("FATA" not in app.map["Pakistan"].markers)


class Card43(LabyrinthTest):
    """Patriot Act"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["43"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.isAdjacent("United States", "Canada"))
        self.assertTrue(app.isAdjacent("United States", "United Kingdom"))
        self.assertTrue(app.isAdjacent("United States", "Philippines"))
        for country in app.map:
            if app.map[country].schengen:
                self.assertTrue(app.isAdjacent("United States", country))
        app.deck["43"].playEvent("US", app)
        self.assertTrue("Patriot Act" in app.markers)
        self.assertTrue(app.isAdjacent("United States", "Canada"))
        self.assertFalse(app.isAdjacent("United States", "United Kingdom"))
        self.assertFalse(app.isAdjacent("United States", "Philippines"))
        for country in app.map:
            if app.map[country].schengen:
                self.assertFalse(app.isAdjacent("United States", country))


class Card44(LabyrinthTest):
    """Renditions"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["44"].playable("US", app, True))
        app.map["United States"].posture = "Soft"
        self.assertFalse(app.deck["44"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["44"].playable("US", app, True))
        app.markers.append("Leak-Renditions")
        self.assertFalse(app.deck["44"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        app.map["Pakistan"].cadre = 1
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].troopCubes = 2
        app.deck["44"].playEvent("US", app)
        self.assertTrue("Renditions" in app.markers)
        self.assertTrue(app.map["Iraq"].cadre == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Pakistan"])
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        app.map["Pakistan"].cadre = 1
        app.map["Pakistan"].sleeperCells = 2
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].troopCubes = 2
        app.deck["44"].playEvent("US", app)
        self.assertTrue("Renditions" in app.markers)
        self.assertTrue(app.map["Pakistan"].cadre == 1)
        self.assertTrue(app.map["Pakistan"].sleeperCells == 0)


class Card45(LabyrinthTest):
    """Safer Now"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].make_islamist_rule()
        app.map["Iraq"].make_adversary()
        self.assertFalse(app.deck["45"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].make_good()
        app.map["Iraq"].make_ally()
        self.assertTrue(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].cadre = 1
        self.assertTrue(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].plots = 1
        self.assertFalse(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].plots = 0
        app.map["Iraq"].cadre = 0
        app.map["Iraq"].sleeperCells = 1
        self.assertFalse(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].sleeperCells = 0
        app.map["Iraq"].activeCells = 1
        self.assertFalse(app.deck["45"].playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["4", "Spain", "h"])
        print "Enter 4 for posture role, Spain and Hard"
        app.deck["45"].playEvent("US", app)
        self.assertTrue(app.map["United States"].posture == "Soft")
        self.assertTrue(app.prestige == 10)
        self.assertTrue(app.map["Spain"].posture == "Hard")


class Card46(LabyrinthTest):
    """Sistani"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_ally()
        app.map["Iraq"].regimeChange = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Iraq"].cadre = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Iraq"].sleeperCells = 1
        self.assertTrue(app.deck["46"].playable("US", app, True))
        app.map["Iraq"].sleeperCells = 0
        app.map["Iraq"].activeCells = 1
        self.assertTrue(app.deck["46"].playable("US", app, True))    

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Syria"].make_fair()
        app.map["Syria"].make_ally()
        app.map["Syria"].regimeChange = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Syria"].cadre = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Syria"].sleeperCells = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Syria"].sleeperCells = 0
        app.map["Syria"].activeCells = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_ally()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].sleeperCells = 1
        app.deck["46"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_fair())
        app.deck["46"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_good())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_ally()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].sleeperCells = 1
        app.map["Syria"].make_fair()
        app.map["Syria"].make_ally()
        app.map["Syria"].regimeChange = 1
        app.map["Syria"].sleeperCells = 1
        app.deck["46"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_good())

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Lebanon"])
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_ally()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].sleeperCells = 1
        app.map["Lebanon"].make_fair()
        app.map["Lebanon"].make_ally()
        app.map["Lebanon"].regimeChange = 1
        app.map["Lebanon"].sleeperCells = 1
        print "Choose Lebanon"
        app.deck["46"].playEvent("US", app)
        self.assertTrue(app.map["Lebanon"].is_good())


class Card47(LabyrinthTest):
    """The door of Itjihad was closed"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["47"].playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["47"].playEvent("US", app)
        self.assertTrue("The door of Itjihad was closed" in app.lapsing)
        self.assertFalse(app.deck["66"].playable("Jihadist", app, False))
        self.assertFalse(app.deck["114"].playable("Jihadist", app, False))
        app.do_turn("")
        self.assertFalse("The door of Itjihad was closed" in app.lapsing)
        self.assertTrue(app.deck["66"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["114"].playable("Jihadist", app, False))


class Card48(LabyrinthTest):
    """Adam Gadahn"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["n", "y"])
        app.cells = 0
        self.assertFalse(app.deck["48"].playable("Jihadist", app, False))
        app.cells = 9
        print "Say No"
        self.assertFalse(app.deck["48"].playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck["48"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["48"].putsCell(app))            

    def test_event(self):
        die_roller = FakeDieRoller(1, 3, 2)
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["120"])
        self.assertTrue(app.numCellsAvailable() > 0)
        self.assertCells(app, "United States", 0)
        app.deck["48"].playEvent("Jihadist", app, die_roller)
        self.assertCells(app, "United States", 2)


class Card49(LabyrinthTest):
    """Al-Ittihad al-Islami"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["49"].playable("Jihadist", app, False))    
        app.cells = 1
        self.assertTrue(app.deck["49"].playable("Jihadist", app, False))    
        app.cells = 0
        self.assertTrue(app.deck["49"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["49"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["49"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Somalia"].sleeperCells == 1)


class Card50(LabyrinthTest):
    """Ansar al-Islam"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["50"].playable("Jihadist", app, False))    
        app.map["Iraq"].make_good()
        self.assertFalse(app.deck["50"].playable("Jihadist", app, False))    
        app.map["Iraq"].make_fair()
        self.assertTrue(app.deck["50"].playable("Jihadist", app, False))    
        app.map["Iraq"].make_poor()
        self.assertTrue(app.deck["50"].playable("Jihadist", app, False))    
        app.map["Iraq"].make_islamist_rule()
        self.assertTrue(app.deck["50"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["50"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["50"].playEvent("Jihadist", app)
        app.map["Iraq"].make_fair()
        self.assertTrue(app.map["Iraq"].sleeperCells == 1 or app.map["Iran"].sleeperCells == 1)


class Card51(LabyrinthTest):
    """FREs"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["51"].playable("Jihadist", app, False))    
        app.map["Iraq"].changeTroops(1)
        self.assertTrue(app.deck["51"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["51"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].changeTroops(1)
        app.deck["51"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.markers.append("Saddam Captured")
        app.testCountry("Iraq")
        app.map["Iraq"].changeTroops(1)
        app.deck["51"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 2)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 3
        app.testCountry("Iraq")
        app.map["Iraq"].changeTroops(1)
        app.deck["51"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 3)


class Card52(LabyrinthTest):
    """IEDs"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["52"].playable("Jihadist", app, False))    
        app.testCountry("Iraq")
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].sleeperCells = 1
        self.assertTrue(app.deck["52"].playable("Jihadist", app, False))        

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["52"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["52"].playEvent("Jihadist", app)


class Card53(LabyrinthTest):
    """Madrassas"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["n", "y"])
        print "Say No"
        self.assertFalse(app.deck["53"].playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck["53"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["53"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup, ["1"])
        app.deck["53"].playEvent("Jihadist", app)


class Card54(LabyrinthTest):
    """Moqtada al-Sadr"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["54"].playable("Jihadist", app, False))
        app.map["Iraq"].changeTroops(1)
        self.assertTrue(app.deck["54"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["54"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.deck["54"].playEvent("Jihadist", app)
        self.assertTrue("Sadr" in app.map["Iraq"].markers)


class Card55(LabyrinthTest):
    """Uyghur Jihad"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["55"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["55"].putsCell(app))            

    def test_event(self):
        for i in range(100):
            app = Labyrinth(1, 1, testBlankScenarioSetup)
            app.deck["55"].playEvent("Jihadist", app)
            self.assertTrue(app.map["China"].posture != "")
            if app.map["China"].posture == "Soft":
                self.assertTrue(app.map["China"].sleeperCells == 1)
            else:
                self.assertTrue(app.map["Central Asia"].is_governed())
                self.assertTrue(app.map["Central Asia"].sleeperCells == 1)


class Card56(LabyrinthTest):
    """Vieira de Mello Slain"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["56"].playable("Jihadist", app, False))    
        app.testCountry("Iraq")
        app.map["Iraq"].regimeChange = 1
        self.assertFalse(app.deck["56"].playable("Jihadist", app, False))    
        app.map["Iraq"].sleeperCells = 1
        self.assertTrue(app.deck["56"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["56"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["56"].playEvent("Jihadist", app)
        self.assertTrue("Vieira de Mello Slain" in app.markers)
        self.assertTrue(app.prestige == 6)


class Card57(LabyrinthTest):
    """Abu Sayyaf"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["57"].playable("Jihadist", app, False))    
        app.markers.append("Moro Talks")
        self.assertFalse(app.deck["57"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["57"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["57"].playEvent("Jihadist", app)
        self.assertTrue("Abu Sayyaf" in app.markers)
        self.assertTrue(app.map["Philippines"].is_governed())
        self.assertTrue(app.map["Philippines"].sleeperCells == 1)
        app.map["Philippines"].sleeperCells = 3
        app.placePlots("Philippines", 0, [1, 5, 1])
        self.assertTrue(app.prestige == 5)


class Card58(LabyrinthTest):
    """Al-Anbar"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["58"].playable("Jihadist", app, False))    
        app.markers.append("Anbar Awakening")
        self.assertFalse(app.deck["58"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["58"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["58"].playEvent("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 3
        app.map["Iraq"].troopCubes = 3
        app.handleDisrupt("Iraq")
        self.assertTrue(app.map["Iraq"].sleeperCells == 2)
        self.assertTrue(app.map["Iraq"].activeCells == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["58"].playEvent("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        app.testCountry("Syria")
        app.map["Syria"].sleeperCells = 3
        app.map["Syria"].troopCubes = 3
        app.handleDisrupt("Syria")
        self.assertTrue(app.map["Syria"].sleeperCells == 2)
        self.assertTrue(app.map["Syria"].activeCells == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["58"].playEvent("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        app.testCountry("Afghanistan")
        app.map["Afghanistan"].sleeperCells = 3
        app.map["Afghanistan"].troopCubes = 3
        app.handleDisrupt("Afghanistan")
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 1)
        self.assertTrue(app.map["Afghanistan"].activeCells == 2)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["58"].playEvent("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        app.testCountry("Iraq")
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].troopCubes = 3
        app.handleDisrupt("Iraq")
        self.assertTrue(app.map["Iraq"].cadre == 1)


class Card59(LabyrinthTest):
    """Amerithrax"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["59"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["59"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["59"].playEvent("Jihadist", app)


class Card60(LabyrinthTest):
    """Bhutto Shot"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["60"].playable("Jihadist", app, False))
        app.map["Pakistan"].sleeperCells = 1
        self.assertTrue(app.deck["60"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["60"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["60"].playEvent("Jihadist", app)
        self.assertTrue("Bhutto Shot" in app.markers)


class Card61(LabyrinthTest):
    """Detainee Release"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.lapsing.append("GTMO")
        self.assertFalse(app.deck["61"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.markers.append("Renditions")
        self.assertFalse(app.deck["61"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["n", "y"])
        print "Say No"
        self.assertFalse(app.deck["61"].playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck["61"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["61"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.testCountry("Iraq")
        app.deck["61"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)


class Card62(LabyrinthTest):
    """Ex-KGB"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["62"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["62"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Russia"].markers.append("CTR")
        app.map["Caucasus"].posture = "Hard"
        app.map["Spain"].posture = "Soft"
        app.map["Germany"].posture = "Soft"
        app.deck["62"].playEvent("Jihadist", app)
        self.assertTrue("CTR" not in app.map["Russia"].markers)
        self.assertTrue(app.map["Caucasus"].posture == "Hard")
        self.assertTrue(app.map["Central Asia"].is_ungoverned())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Caucasus"].posture = "Hard"
        app.map["Spain"].posture = "Soft"
        app.map["Germany"].posture = "Soft"
        app.deck["62"].playEvent("Jihadist", app)
        self.assertTrue("CTR" not in app.map["Russia"].markers)
        self.assertTrue(app.map["Caucasus"].posture == "Soft")
        self.assertTrue(app.map["Central Asia"].is_ungoverned())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Caucasus"].posture = "Hard"
        app.map["Spain"].posture = "Hard"
        app.deck["62"].playEvent("Jihadist", app)
        self.assertTrue("CTR" not in app.map["Russia"].markers)
        self.assertTrue(app.map["Caucasus"].posture == "Hard")
        self.assertTrue(app.map["Central Asia"].is_governed())
        self.assertTrue(app.map["Central Asia"].is_adversary())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Caucasus"].posture = "Hard"
        app.map["Spain"].posture = "Hard"
        app.testCountry("Central Asia")
        app.map["Central Asia"].make_ally()
        app.deck["62"].playEvent("Jihadist", app)
        self.assertTrue("CTR" not in app.map["Russia"].markers)
        self.assertTrue(app.map["Caucasus"].posture == "Hard")
        self.assertTrue(app.map["Central Asia"].is_governed())
        self.assertTrue(app.map["Central Asia"].is_neutral())


class Card63(LabyrinthTest):
    """Gaza War"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["63"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["63"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["63"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 6)
        self.assertTrue(app.prestige == 6)


class Card64(LabyrinthTest):
    """Hariri Killed"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["64"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["64"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Syria"].make_good()
        app.map["Syria"].make_ally()
        app.deck["64"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Lebanon"].is_governed())
        self.assertTrue(app.map["Syria"].is_fair())
        self.assertTrue(app.map["Syria"].is_adversary())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Syria"].make_fair()
        app.map["Syria"].make_ally()
        app.deck["64"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Lebanon"].is_governed())
        self.assertTrue(app.map["Syria"].is_poor())
        self.assertTrue(app.map["Syria"].is_adversary())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Syria"].make_poor()
        app.map["Syria"].make_ally()
        app.deck["64"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Lebanon"].is_governed())
        self.assertTrue(app.map["Syria"].is_poor())
        self.assertTrue(app.map["Syria"].is_adversary())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Syria"].make_islamist_rule()
        app.map["Syria"].make_ally()
        app.deck["64"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Lebanon"].is_governed())
        self.assertTrue(app.map["Syria"].is_islamist_rule())
        self.assertTrue(app.map["Syria"].is_adversary())


class Card65(LabyrinthTest):
    """HEU"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["65"].playable("Jihadist", app, False))
        app.testCountry("Russia")
        app.map["Russia"].sleeperCells = 1
        self.assertTrue(app.deck["65"].playable("Jihadist", app, False))
        app.map["Russia"].markers.append("CTR")
        self.assertFalse(app.deck["65"].playable("Jihadist", app, False))
        app.testCountry("Central Asia")
        app.map["Central Asia"].sleeperCells = 1
        self.assertTrue(app.deck["65"].playable("Jihadist", app, False))
        app.map["Central Asia"].markers.append("CTR")
        self.assertFalse(app.deck["65"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["65"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Russia")
        app.map["Russia"].sleeperCells = 1
        app.executeCardHEU("Russia", 1)
        self.assertTrue(app.map["Russia"].sleeperCells == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Russia")
        app.map["Russia"].sleeperCells = 1
        app.executeCardHEU("Russia", 3)
        self.assertTrue(app.map["Russia"].sleeperCells == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Central Asia")
        app.map["Central Asia"].sleeperCells = 1
        app.executeCardHEU("Central Asia", 1)
        self.assertTrue(app.map["Central Asia"].sleeperCells == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Central Asia")
        app.map["Central Asia"].sleeperCells = 1
        app.executeCardHEU("Central Asia", 4)
        self.assertTrue(app.map["Central Asia"].sleeperCells == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Russia"].sleeperCells = 1
        app.deck["65"].playEvent("Jihadist", app)


class Card66(LabyrinthTest):
    """Homegrown"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["66"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["66"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["66"].playEvent("Jihadist", app)
        self.assertTrue(app.map["United Kingdom"].posture != "")
        self.assertTrue(app.map["United Kingdom"].sleeperCells == 1)


class Card67(LabyrinthTest):
    """Islamic Jihad Union"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["67"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["67"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["67"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Central Asia"].sleeperCells == 1)
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 1
        app.deck["67"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Central Asia"].sleeperCells == 1)
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 0)


class Card68(LabyrinthTest):
    """Jemaah Islamiya"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["68"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["68"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["68"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Indonesia/Malaysia"].sleeperCells == 2)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 1
        app.deck["68"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Indonesia/Malaysia"].sleeperCells == 1)


class Card69(LabyrinthTest):
    """Kazakh Strain"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Central Asia")
        app.map["Central Asia"].sleeperCells = 1
        self.assertTrue(app.deck["69"].playable("Jihadist", app, False))
        app.map["Central Asia"].markers.append("CTR")
        self.assertFalse(app.deck["69"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["69"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Central Asia")
        app.map["Central Asia"].sleeperCells = 1
        app.executeCardHEU("Central Asia", 1)
        self.assertTrue(app.map["Central Asia"].sleeperCells == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Central Asia")
        app.map["Central Asia"].sleeperCells = 1
        app.executeCardHEU("Central Asia", 4)
        self.assertTrue(app.map["Central Asia"].sleeperCells == 0)

        app.deck["69"].playEvent("Jihadist", app)


class Card70(LabyrinthTest):
    """Lashkar-e-Tayyiba"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["70"].playable("Jihadist", app, False))
        app.markers.append("Indo-Pakistani Talks")
        self.assertFalse(app.deck["70"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["70"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["70"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Pakistan"].sleeperCells == 1)
        self.assertTrue(app.map["India"].sleeperCells == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 1
        app.deck["70"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Pakistan"].sleeperCells == 1)
        self.assertTrue(app.map["India"].sleeperCells == 0)


class Card71(LabyrinthTest):
    """Kazakh Strain"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Russia")
        app.map["Russia"].sleeperCells = 1
        self.assertTrue(app.deck["71"].playable("Jihadist", app, False))
        app.map["Russia"].markers.append("CTR")
        self.assertFalse(app.deck["71"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["71"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Russia")
        app.map["Russia"].sleeperCells = 1
        app.executeCardHEU("Russia", 1)
        self.assertTrue(app.map["Russia"].sleeperCells == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Russia")
        app.map["Russia"].sleeperCells = 1
        app.executeCardHEU("Russia", 4)
        self.assertTrue(app.map["Russia"].sleeperCells == 0)

        app.deck["71"].playEvent("Jihadist", app)


class Card72(LabyrinthTest):
    """Opium"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["72"].playable("Jihadist", app, False))
        app.map["Afghanistan"].sleeperCells = 1
        self.assertTrue(app.deck["72"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["72"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 14
        app.testCountry("Afghanistan")
        app.map["Afghanistan"].sleeperCells = 1
        app.deck["72"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 14
        app.testCountry("Afghanistan")
        app.map["Afghanistan"].sleeperCells = 1
        app.map["Afghanistan"].make_islamist_rule()
        app.deck["72"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 15)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 2
        app.testCountry("Afghanistan")
        app.map["Afghanistan"].sleeperCells = 1
        app.deck["72"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 3)


class Card73(LabyrinthTest):
    """Pirates"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["73"].playable("Jihadist", app, False))
        app.map["Somalia"].make_islamist_rule()
        self.assertTrue(app.deck["73"].playable("Jihadist", app, False))
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["73"].playable("Jihadist", app, False))
        app.map["Yemen"].make_islamist_rule()
        self.assertTrue(app.deck["73"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["73"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["73"].playEvent("Jihadist", app)
        self.assertTrue("Pirates" in app.markers)
        app.do_turn("")
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Somalia"].make_islamist_rule()
        app.deck["73"].playEvent("Jihadist", app)
        app.do_turn("")
        self.assertTrue(app.funding == 5)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Yemen"].make_islamist_rule()
        app.deck["73"].playEvent("Jihadist", app)
        app.do_turn("")
        self.assertTrue(app.funding == 5)


class Card74(LabyrinthTest):
    """Schengen Visas"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["74"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["74"].putsCell(app))

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.deck["74"].playEvent("Jihadist", app)


class Card75(LabyrinthTest):
    """Schroeder & Chirac"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["75"].playable("Jihadist", app, False))
        app.map["United States"].posture = "Soft"
        self.assertFalse(app.deck["75"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["75"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.deck["75"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Germany"].posture == "Soft")
        self.assertTrue(app.map["France"].posture == "Soft")
        self.assertTrue(app.prestige == 6)


class Card76(LabyrinthTest):
    """Abu Ghurayb"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["76"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        app.map["Iraq"].regimeChange = 1
        self.assertFalse(app.deck["76"].playable("Jihadist", app, False))
        app.map["Iraq"].sleeperCells = 1
        self.assertTrue(app.deck["76"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["76"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].sleeperCells = 1         
        app.deck["76"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 5)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].sleeperCells = 1     
        app.testCountry("Pakistan")
        app.testCountry("Lebanon")
        app.map["Lebanon"].make_ally()
        app.deck["76"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Lebanon"].is_neutral())
        self.assertTrue(app.prestige == 5)


class Card77(LabyrinthTest):
    """Al Jazeera"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Saudi Arabia")
        app.map["Saudi Arabia"].troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Jordan")
        app.map["Jordan"].troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Gulf States")
        app.map["Gulf States"].troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Yemen")
        app.map["Yemen"].troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["77"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Yemen")
        app.map["Yemen"].troopCubes = 1
        app.deck["77"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Yemen"].is_adversary())


class Card78(LabyrinthTest):
    """Axis of Evil"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["78"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["78"].putsCell(app))            

    def test_event(self):
        for i in range(100):
            app = Labyrinth(1, 1, testBlankScenarioSetup)
            app.map["United States"].posture = "Soft"
            app.deck["78"].playEvent("Jihadist", app)
            self.assertTrue(app.map["United States"].posture == "Hard")
            self.assertTrue(app.prestige != 7)


class Card79(LabyrinthTest):
    """Clean Operatives"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["79"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["79"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.deck["79"].playEvent("Jihadist", app)
        self.assertTrue(app.map["United States"].sleeperCells == 2)


class Card80(LabyrinthTest):
    """FATA"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["80"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["80"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.deck["80"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Pakistan"].sleeperCells == 1)
        self.assertTrue("FATA" in app.map["Pakistan"].markers)


class Card81(LabyrinthTest):
    """Foreign Fighters"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["81"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        self.assertFalse(app.deck["81"].playable("Jihadist", app, False))
        app.map["Iraq"].regimeChange = 1
        self.assertTrue(app.deck["81"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["81"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].regimeChange = 1
        app.deck["81"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 5)
        self.assertTrue(app.map["Iraq"].besieged == 1)
        self.assertTrue(app.map["Iraq"].aid == 0)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].aid = 1
        app.deck["81"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 5)
        self.assertTrue(app.map["Iraq"].besieged == 0)
        self.assertTrue(app.map["Iraq"].aid == 0)


class Card82(LabyrinthTest):
    """Jihadist Videos"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["82"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["82"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.deck["82"].playEvent("Jihadist", app)


class Card83(LabyrinthTest):
    """Kashmir"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["83"].playable("Jihadist", app, False))
        app.markers.append("Indo-Pakistani Talks")
        self.assertFalse(app.deck["83"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["83"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.testCountry("Pakistan")
        app.deck["83"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Pakistan"].is_adversary())
        self.assertTrue(app.map["Pakistan"].sleeperCells == 1)


class Card84(LabyrinthTest):
    """Leak"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["84"].playable("Jihadist", app, False))
        app.markers.append("Enhanced Measures")
        self.assertTrue(app.deck["84"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["84"].playable("Jihadist", app, False))
        app.markers.append("Renditions")
        self.assertTrue(app.deck["84"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["84"].playable("Jihadist", app, False))
        app.markers.append("Wiretapping")
        self.assertTrue(app.deck["84"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["84"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.markers.append("Enhanced Measures")
        app.deck["84"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Enhanced Measures" in app.markers)
        self.assertTrue("Enhanced Measures" not in app.markers)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.markers.append("Renditions")
        app.deck["84"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Renditions" in app.markers)
        self.assertTrue("Renditions" not in app.markers)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.markers.append("Wiretapping")
        app.deck["84"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Wiretapping" in app.markers)
        self.assertTrue("Wiretapping" not in app.markers)
        self.assertTrue(app.prestige != 7)


class Card85(LabyrinthTest):
    """Leak"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["85"].playable("Jihadist", app, False))
        app.markers.append("Enhanced Measures")
        self.assertTrue(app.deck["85"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["85"].playable("Jihadist", app, False))
        app.markers.append("Renditions")
        self.assertTrue(app.deck["85"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["85"].playable("Jihadist", app, False))
        app.markers.append("Wiretapping")
        self.assertTrue(app.deck["85"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["85"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.markers.append("Enhanced Measures")
        app.deck["85"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Enhanced Measures" in app.markers)
        self.assertTrue("Enhanced Measures" not in app.markers)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.markers.append("Renditions")
        app.deck["85"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Renditions" in app.markers)
        self.assertTrue("Renditions" not in app.markers)

        app = Labyrinth(1, 1, testScenarioSetup)
        app.markers.append("Wiretapping")
        app.deck["85"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Wiretapping" in app.markers)
        self.assertTrue("Wiretapping" not in app.markers)
        self.assertTrue(app.prestige != 7)


class Card86(LabyrinthTest):
    """Lebanon War"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["86"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["86"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testScenarioSetup)
        app.deck["86"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 6)


class Card87(LabyrinthTest):
    """Martyrdom Operation"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["87"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        self.assertFalse(app.deck["87"].playable("Jihadist", app, False))
        app.map["Iraq"].sleeperCells = 1
        self.assertFalse(app.deck["87"].playable("Jihadist", app, False))
        app.map["Iraq"].make_poor()
        self.assertTrue(app.deck["87"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["87"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["87"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 2)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.map["United States"].sleeperCells = 1
        app.deck["87"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 0)
        self.assertTrue(app.map["United States"].sleeperCells == 0)
        self.assertTrue(app.map["United States"].activeCells == 0)
        self.assertTrue(app.map["United States"].plots == 2)


class Card88(LabyrinthTest):
    """Martyrdom Operation"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["88"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        self.assertFalse(app.deck["88"].playable("Jihadist", app, False))
        app.map["Iraq"].sleeperCells = 1
        self.assertFalse(app.deck["88"].playable("Jihadist", app, False))
        app.map["Iraq"].make_poor()
        self.assertTrue(app.deck["88"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["88"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["88"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 2)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.map["United States"].sleeperCells = 1
        app.deck["88"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 0)
        self.assertTrue(app.map["United States"].sleeperCells == 0)
        self.assertTrue(app.map["United States"].activeCells == 0)
        self.assertTrue(app.map["United States"].plots == 2)


class Card89(LabyrinthTest):
    """Martyrdom Operation"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["89"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        self.assertFalse(app.deck["89"].playable("Jihadist", app, False))
        app.map["Iraq"].sleeperCells = 1
        self.assertFalse(app.deck["89"].playable("Jihadist", app, False))
        app.map["Iraq"].make_poor()
        self.assertTrue(app.deck["89"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["89"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["89"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 2)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.map["United States"].sleeperCells = 1
        app.deck["89"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 0)
        self.assertTrue(app.map["United States"].sleeperCells == 0)
        self.assertTrue(app.map["United States"].activeCells == 0)
        self.assertTrue(app.map["United States"].plots == 2)


class Card90(LabyrinthTest):
    """Quagmire"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))
        app.prestige = 6
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        app.map["Iraq"].regimeChange = 1
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))
        app.map["Iraq"].sleeperCells = 1
        self.assertTrue(app.deck["90"].playable("Jihadist", app, False))
        app.prestige = 7
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))
        app.prestige = 6
        app.map["Iraq"].regimeChange = 0
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["90"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.deck["90"].playEvent("Jihadist", app)
        self.assertTrue(app.map["United States"].posture == "Soft")


class Card91(LabyrinthTest):
    """Regional al-Qaeda"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["91"].playable("Jihadist", app, False))
        for country in app.map:
            if app.map[country].type == "Suni" or app.map[country].type == "Shia-Mix":
                app.testCountry(country)
        self.assertFalse(app.deck["91"].playable("Jihadist", app, False))
        app.map["Iraq"].make_ungoverned()
        app.map["Iraq"].alignment = ""
        self.assertFalse(app.deck["91"].playable("Jihadist", app, False))
        app.map["Lebanon"].make_ungoverned()
        app.map["Lebanon"].alignment = ""
        self.assertTrue(app.deck["91"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["91"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        for country in app.map:
            if app.map[country].type == "Suni" or app.map[country].type == "Shia-Mix":
                app.testCountry(country)
        app.map["Iraq"].make_ungoverned()
        app.map["Iraq"].alignment = ""
        app.map["Lebanon"].make_ungoverned()
        app.map["Lebanon"].alignment = ""
        app.deck["91"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].is_governed())
        self.assertTrue(app.map["Iraq"].is_aligned())
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        self.assertTrue(app.map["Lebanon"].is_governed())
        self.assertTrue(app.map["Lebanon"].is_aligned())
        self.assertTrue(app.map["Lebanon"].sleeperCells == 1)


class Card92(LabyrinthTest):
    """Saddam"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["92"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        self.assertFalse(app.deck["92"].playable("Jihadist", app, False))
        app.map["Iraq"].make_poor()    
        self.assertFalse(app.deck["92"].playable("Jihadist", app, False))
        app.map["Iraq"].make_adversary()
        self.assertTrue(app.deck["92"].playable("Jihadist", app, False))
        app.markers.append("Saddam Captured")
        self.assertFalse(app.deck["92"].playable("Jihadist", app, False))        

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["92"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["92"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 9)         


class Card93(LabyrinthTest):
    """Taliban"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["93"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["93"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Afghanistan")
        app.testCountry("Pakistan")
        app.deck["93"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Afghanistan"].besieged == 1)         
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 1)         
        self.assertTrue(app.map["Pakistan"].sleeperCells == 1)         
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Afghanistan")
        app.testCountry("Pakistan")
        app.map["Afghanistan"].make_islamist_rule()
        app.deck["93"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Afghanistan"].besieged == 1)         
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 1)         
        self.assertTrue(app.map["Pakistan"].sleeperCells == 1)         
        self.assertTrue(app.prestige == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Afghanistan")
        app.testCountry("Pakistan")
        app.map["Pakistan"].make_islamist_rule()
        app.deck["93"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Afghanistan"].besieged == 1)         
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 1)         
        self.assertTrue(app.map["Pakistan"].sleeperCells == 1)         
        self.assertTrue(app.prestige == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.cells = 1
        app.testCountry("Afghanistan")
        app.testCountry("Pakistan")
        app.deck["93"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Afghanistan"].besieged == 1)         
        self.assertTrue(app.map["Afghanistan"].sleeperCells == 1)         
        self.assertTrue(app.map["Pakistan"].sleeperCells == 0)         
        self.assertTrue(app.prestige == 6)


class Card94(LabyrinthTest):
    """The door of Itjihad was closed"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["n", "y"])
        print "Say No"
        self.assertFalse(app.deck["94"].playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck["94"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["94"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        print "Choose Iraq"
        app.testCountry("Iraq")
        app.map["Iraq"].make_fair()
        app.deck["94"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].is_poor())


class Card95(LabyrinthTest):
    """Wahhabism"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["95"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["95"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Saudi Arabia"].make_poor()
        app.deck["95"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 8)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Saudi Arabia"].make_fair()
        app.deck["95"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 7)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Saudi Arabia")
        app.map["Saudi Arabia"].make_islamist_rule()
        app.deck["95"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 9)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Saudi Arabia")
        app.map["Saudi Arabia"].make_islamist_rule()
        app.funding = 2
        app.deck["95"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 9)


class Card96(LabyrinthTest):
    """Danish Cartoons"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["96"].playable("US", app, True))
        self.assertTrue(app.deck["96"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["96"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["s", "h"])
        app.deck["96"].playEvent("US", app)
        self.assertTrue(app.map["Scandinavia"].posture == "Soft")
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        app.deck["96"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Scandinavia"].posture == "Hard")


class Card97(LabyrinthTest):
    """Fatwa"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["y", "n"])
        print "Say Yes"
        self.assertTrue(app.deck["97"].playable("US", app, True))
        print "Say No"
        self.assertFalse(app.deck["97"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["97"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["97"].playEvent("US", app)
        app.deck["97"].playEvent("Jihadist", app)


class Card98(LabyrinthTest):
    """Gaza Withdrawl"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["98"].playable("US", app, True))
        self.assertTrue(app.deck["98"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["98"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["98"].playEvent("US", app)
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["98"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Israel"].sleeperCells == 1)
        self.assertTrue(app.cells == 10)


class Card99(LabyrinthTest):
    """HAMAS Elected"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["99"].playable("US", app, True))
        self.assertTrue(app.deck["99"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["99"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["99"].playEvent("US", app)
        self.assertTrue(app.funding == 4)
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["99"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 4)
        self.assertTrue(app.prestige == 6)


class CardHundred(LabyrinthTest):
    """His Ut-Tahrir"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["100"].playable("US", app, True))
        self.assertTrue(app.deck["100"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["100"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["100"].playEvent("US", app)
        self.assertTrue(app.funding == 5)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["100"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 5)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.troops = 4
        app.deck["100"].playEvent("US", app)
        self.assertTrue(app.funding == 7)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.troops = 4
        app.deck["100"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 7)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.troops = 10
        app.deck["100"].playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.troops = 10
        app.deck["100"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 3)


class CardHundredOne(LabyrinthTest):
    """Kosovo"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["101"].playable("US", app, True))
        self.assertTrue(app.deck["101"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["101"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["101"].playEvent("US", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.map["Serbia"].posture == "Soft")

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["United States"].posture = "Soft"
        app.deck["101"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.map["Serbia"].posture == "Hard")


class CardHundredTwo(LabyrinthTest):
    """Former Soviet Union"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["102"].playable("US", app, True))
        self.assertTrue(app.deck["102"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["102"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["102"].playEvent("US", app)
        self.assertTrue(app.map["Central Asia"].is_neutral())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Central Asia")
        app.map["Central Asia"].make_good()
        app.map["Central Asia"].make_ally()
        app.deck["102"].playEvent("Jihadist", app)
        self.assertFalse(app.map["Central Asia"].is_good())
        self.assertTrue(app.map["Central Asia"].is_neutral())


class CardHundredThree(LabyrinthTest):
    """Hizballah"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["103"].playable("US", app, True))
        self.assertTrue(app.deck["103"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["103"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["103"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["103"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Lebanon"].is_poor())
        self.assertTrue(app.map["Lebanon"].is_neutral())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Lebanon")
        app.map["Lebanon"].make_good()
        app.map["Lebanon"].make_ally()
        app.map["Jordan"].make_good()
        app.map["Jordan"].make_ally()
        app.deck["103"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Lebanon"].is_poor())
        self.assertTrue(app.map["Lebanon"].is_neutral())

        # no countries
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.deck["103"].playEvent("US", app)

        # one country
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.testCountry("Gulf States")
        app.map["Gulf States"].sleeperCells = 1
        app.deck["103"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)


class CardHundredFour(LabyrinthTest):
    """Iran"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["104"].playable("US", app, True))
        self.assertTrue(app.deck["104"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["104"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["104"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Yemen"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.testCountry("Yemen")
        app.map["Yemen"].sleeperCells = 1
        app.deck["104"].playEvent("US", app)
        self.assertTrue(app.map["Yemen"].sleeperCells == 0)

        app.deck["104"].playEvent("Jihadist", app)


class CardHundredFive(LabyrinthTest):
    """Iran"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["105"].playable("US", app, True))
        self.assertTrue(app.deck["105"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["105"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["105"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Yemen"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.testCountry("Yemen")
        app.map["Yemen"].sleeperCells = 1
        app.deck["105"].playEvent("US", app)
        self.assertTrue(app.map["Yemen"].sleeperCells == 0)

        app.deck["105"].playEvent("Jihadist", app)


class CardHundredSix(LabyrinthTest):
    """Jaysh al-Mahdi"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["106"].playable("US", app, True))
        self.assertFalse(app.deck["106"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        self.assertFalse(app.deck["106"].playable("US", app, True))
        self.assertFalse(app.deck["106"].playable("Jihadist", app, False))
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["106"].playable("US", app, True))
        self.assertTrue(app.deck["106"].playable("Jihadist", app, False))
        app.map["Iraq"].sleeperCells = 0
        self.assertFalse(app.deck["106"].playable("US", app, True))
        self.assertFalse(app.deck["106"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["106"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 3
        app.map["Iraq"].troopCubes = 1
        app.deck["106"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 2
        app.map["Iraq"].troopCubes = 1
        app.deck["106"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].troopCubes = 1
        app.deck["106"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Lebanon"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 2
        app.map["Iraq"].troopCubes = 1
        app.map["Lebanon"].sleeperCells = 2
        app.map["Lebanon"].troopCubes = 1
        print "Choose Lebanon"
        app.deck["106"].playEvent("US", app)
        self.assertTrue(app.map["Lebanon"].sleeperCells == 0)

        print "HERE"
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 2
        app.map["Iraq"].troopCubes = 1
        app.deck["106"].playEvent("Jihadist", app)


class CardHundredSeven(LabyrinthTest):
    """Kurdistan"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["107"].playable("US", app, True))
        self.assertTrue(app.deck["107"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["107"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.deck["107"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].aid == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["107"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Turkey"].is_poor())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].make_good()
        app.deck["107"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Turkey"].governance_is_worse_than(GOOD))
        self.assertTrue(app.map["Iraq"].is_fair())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].make_fair()
        app.testCountry("Turkey")
        app.map["Turkey"].make_fair()
        app.map["Turkey"].aid = 1
        app.deck["107"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Turkey"].is_poor())
        self.assertTrue(app.map["Iraq"].is_fair())


class CardHundredEight(LabyrinthTest):
    """Musharraf"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["108"].playable("US", app, True))
        self.assertFalse(app.deck["108"].playable("Jihadist", app, False))
        app.testCountry("Pakistan")
        app.map["Pakistan"].activeCells = 1
        self.assertTrue(app.deck["108"].playable("US", app, True))
        self.assertTrue(app.deck["108"].playable("Jihadist", app, False))
        app.markers.append("Benazir Bhutto")
        self.assertFalse(app.deck["108"].playable("US", app, True))
        self.assertFalse(app.deck["108"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["108"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 1
        app.map["Pakistan"].make_good()
        app.deck["108"].playEvent("US", app)
        self.assertCells(app, "Pakistan", 0, True)
        self.assertTrue(app.map["Pakistan"].is_poor())
        self.assertTrue(app.map["Pakistan"].is_ally())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 3
        app.map["Pakistan"].make_islamist_rule()
        app.map["Pakistan"].make_adversary()
        app.deck["108"].playEvent("Jihadist", app)
        self.assertCells(app, "Pakistan", 2, True)
        self.assertTrue(app.map["Pakistan"].is_poor())
        self.assertTrue(app.map["Pakistan"].is_ally())


class CardHundredNine(LabyrinthTest):
    """Tora Bora"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["109"].playable("US", app, True))
        self.assertFalse(app.deck["109"].playable("Jihadist", app, False))
        app.testCountry("Pakistan")
        app.map["Pakistan"].activeCells = 2
        self.assertFalse(app.deck["109"].playable("US", app, True))
        self.assertFalse(app.deck["109"].playable("Jihadist", app, False))
        app.map["Pakistan"].regimeChange = 1
        self.assertTrue(app.deck["109"].playable("US", app, True))
        self.assertTrue(app.deck["109"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["109"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 2
        app.map["Pakistan"].regimeChange = 1
        app.deck["109"].playEvent("US", app)
        self.assertCells(app, "Pakistan", 0, True)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 2
        app.map["Pakistan"].regimeChange = 1
        app.deck["109"].playEvent("Jihadist", app)
        self.assertCells(app, "Pakistan", 0, True)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 2
        app.map["Pakistan"].regimeChange = 1
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 2
        app.map["Iraq"].regimeChange = 1
        print "Choose Iraq"
        app.deck["109"].playEvent("US", app)
        self.assertCells(app, "Iraq", 0, True)
        self.assertTrue(app.prestige != 7)


class CardHundredTen(LabyrinthTest):
    """Zarqawi"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["110"].playable("US", app, True))
        self.assertFalse(app.deck["110"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["110"].playable("US", app, True))
        self.assertTrue(app.deck["110"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["110"].playable("US", app, True))
        self.assertFalse(app.deck["110"].playable("Jihadist", app, False))
        app.testCountry("Syria")
        app.map["Syria"].troopCubes = 1
        self.assertTrue(app.deck["110"].playable("US", app, True))
        self.assertTrue(app.deck["110"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["110"].playable("US", app, True))
        self.assertFalse(app.deck["110"].playable("Jihadist", app, False))
        app.testCountry("Lebanon")
        app.map["Lebanon"].troopCubes = 1
        self.assertTrue(app.deck["110"].playable("US", app, True))
        self.assertTrue(app.deck["110"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["110"].playable("US", app, True))
        self.assertFalse(app.deck["110"].playable("Jihadist", app, False))
        app.testCountry("Jordan")
        app.map["Jordan"].troopCubes = 1
        self.assertTrue(app.deck["110"].playable("US", app, True))
        self.assertTrue(app.deck["110"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["110"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].troopCubes = 2
        app.deck["110"].playEvent("US", app)
        self.assertTrue(app.prestige == 10)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].troopCubes = 2
        app.deck["110"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].totalCells(True) == 3)
        self.assertTrue(app.map["Iraq"].plots == 1)


class CardHundredEleven(LabyrinthTest):
    """Zawahiri"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["111"].playable("US", app, True))
        self.assertTrue(app.deck["111"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        self.assertFalse(app.deck["111"].playable("US", app, True))
        self.assertTrue(app.deck["111"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Pakistan")
        app.map["Pakistan"].markers.append("FATA")
        self.assertFalse(app.deck["111"].playable("US", app, True))
        self.assertTrue(app.deck["111"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Pakistan")
        app.markers.append("Al-Anbar")
        self.assertFalse(app.deck["111"].playable("US", app, True))
        self.assertTrue(app.deck["111"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["111"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["111"].playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["111"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        app.deck["111"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 4)


class CardHundredTwelve(LabyrinthTest):
    """Bin Ladin"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["112"].playable("US", app, True))
        self.assertTrue(app.deck["112"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        self.assertFalse(app.deck["112"].playable("US", app, True))
        self.assertTrue(app.deck["112"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Pakistan")
        app.map["Pakistan"].markers.append("FATA")
        self.assertFalse(app.deck["112"].playable("US", app, True))
        self.assertTrue(app.deck["112"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Pakistan")
        app.markers.append("Al-Anbar")
        self.assertFalse(app.deck["112"].playable("US", app, True))
        self.assertTrue(app.deck["112"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["112"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["112"].playEvent("US", app)
        self.assertTrue(app.funding == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["112"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 5)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        app.deck["112"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 3)


class CardHundredThirteen(LabyrinthTest):
    """Darfur"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["113"].playable("US", app, True))
        self.assertTrue(app.deck["113"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["113"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["113"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].aid == 1)
        self.assertTrue(app.map["Sudan"].is_ally())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Sudan")
        app.map["Sudan"].make_adversary()
        app.deck["113"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].aid == 1)
        self.assertTrue(app.map["Sudan"].is_neutral())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 6
        app.deck["113"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].besieged == 1)
        self.assertTrue(app.map["Sudan"].is_adversary())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 6
        app.testCountry("Sudan")
        app.map["Sudan"].make_ally()
        app.deck["113"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].besieged == 1)
        self.assertTrue(app.map["Sudan"].is_neutral())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["113"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].aid == 1)
        self.assertTrue(app.map["Sudan"].is_ally())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Sudan")
        app.map["Sudan"].make_adversary()
        app.deck["113"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].aid == 1)
        self.assertTrue(app.map["Sudan"].is_neutral())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 6
        app.deck["113"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].besieged == 1)
        self.assertTrue(app.map["Sudan"].is_adversary())

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.prestige = 6
        app.testCountry("Sudan")
        app.map["Sudan"].make_ally()
        app.deck["113"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].besieged == 1)
        self.assertTrue(app.map["Sudan"].is_neutral())


class CardHundredFourteen(LabyrinthTest):
    """GTMO"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["114"].playable("US", app, True))
        self.assertTrue(app.deck["114"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["114"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["114"].playEvent("US", app)
        self.assertTrue("GTMO" in app.lapsing)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["114"].playEvent("Jihadist", app)
        self.assertTrue("GTMO" in app.lapsing)
        self.assertTrue(app.prestige != 7)


class CardHundredFifteen(LabyrinthTest):
    """Hambali"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.testCountry("Indonesia/Malaysia")
        app.map["Indonesia/Malaysia"].sleeperCells = 1
        app.map["Indonesia/Malaysia"].make_ally()
        self.assertTrue(app.deck["115"].playable("US", app, True))
        self.assertTrue(app.deck["115"].playable("Jihadist", app, False))
        app.map["Indonesia/Malaysia"].sleeperCells = 0
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.map["Indonesia/Malaysia"].sleeperCells = 1
        app.map["Indonesia/Malaysia"].make_neutral()
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 1
        app.map["Pakistan"].make_ally()
        self.assertTrue(app.deck["115"].playable("US", app, True))
        self.assertTrue(app.deck["115"].playable("Jihadist", app, False))
        app.map["Pakistan"].sleeperCells = 0
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.map["Pakistan"].sleeperCells = 1
        app.map["Pakistan"].make_neutral()
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.testCountry("India")
        app.map["India"].sleeperCells = 1
        app.map["India"].posture = "Hard"
        self.assertTrue(app.deck["115"].playable("US", app, True))
        self.assertTrue(app.deck["115"].playable("Jihadist", app, False))
        app.map["India"].sleeperCells = 0
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.map["India"].sleeperCells = 1
        app.map["India"].posture = "Soft"
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.testCountry("Thailand")
        app.map["Thailand"].sleeperCells = 1
        app.map["Thailand"].posture = "Hard"
        self.assertTrue(app.deck["115"].playable("US", app, True))
        self.assertTrue(app.deck["115"].playable("Jihadist", app, False))
        app.map["Thailand"].sleeperCells = 0
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.map["Thailand"].sleeperCells = 1
        app.map["Thailand"].posture = "Soft"
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.testCountry("Philippines")
        app.map["Philippines"].sleeperCells = 1
        app.map["Philippines"].posture = "Hard"
        self.assertTrue(app.deck["115"].playable("US", app, True))
        self.assertTrue(app.deck["115"].playable("Jihadist", app, False))
        app.map["Philippines"].sleeperCells = 0
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))
        app.map["Philippines"].sleeperCells = 1
        app.map["Philippines"].posture = "Soft"
        self.assertFalse(app.deck["115"].playable("US", app, True))
        self.assertFalse(app.deck["115"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["115"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Philippines")
        app.map["Philippines"].sleeperCells = 1
        app.map["Philippines"].posture = "Hard"
        app.deck["115"].playEvent("US", app)
        self.assertTrue(app.map["Philippines"].sleeperCells == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["Indonesia/Malaysia"])
        app.testCountry("Indonesia/Malaysia")
        app.map["Indonesia/Malaysia"].sleeperCells = 1
        app.map["Indonesia/Malaysia"].make_ally()
        app.testCountry("Philippines")
        app.map["Philippines"].sleeperCells = 1
        app.map["Philippines"].posture = "Hard"
        print "Choose Indonesia/Malaysia"
        app.deck["115"].playEvent("US", app)
        self.assertTrue(app.map["Indonesia/Malaysia"].sleeperCells == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Indonesia/Malaysia")
        app.map["Indonesia/Malaysia"].sleeperCells = 1
        app.map["Indonesia/Malaysia"].make_ally()
        app.deck["115"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Indonesia/Malaysia"].plots == 1)


class CardHundredSixteen(LabyrinthTest):
    """KSM"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["116"].playable("Jihadist", app, False))
        self.assertFalse(app.deck["116"].playable("US", app, True))
        app.testCountry("Iraq")
        app.map["Iraq"].make_ally()
        app.map["Iraq"].plots = 1
        self.assertTrue(app.deck["116"].playable("US", app, True))

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["116"].playable("Jihadist", app, False))
        self.assertFalse(app.deck["116"].playable("US", app, True))
        app.testCountry("Canada")
        app.map["Canada"].plots = 1
        self.assertTrue(app.deck["116"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["116"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].make_ally()
        app.map["Iraq"].plots = 2
        app.testCountry("Pakistan")
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].plots = 2
        app.testCountry("Canada")
        app.map["Canada"].plots = 1
        app.deck["116"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].plots == 0)
        self.assertTrue(app.map["Pakistan"].plots == 2)
        self.assertTrue(app.map["Canada"].plots == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["116"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        app.map["Iraq"].sleeperCells = 1
        app.deck["116"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.map["United States"].sleeperCells = 1
        app.deck["116"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 0)
        self.assertTrue(app.map["United States"].sleeperCells == 1)
        self.assertTrue(app.map["United States"].activeCells == 0)
        self.assertTrue(app.map["United States"].plots == 1)


class CardHundredSeventeen(LabyrinthTest):
    """Oil Price Spike"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["117"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["117"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["117"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["117"].playEvent("US", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["y"])
        app.deck["117"].playEvent("Jihadist", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 4)
        app.deck["117"].playEvent("US", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 5)


class CardHundredEightteen(LabyrinthTest):
    """Oil Price Spike"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["118"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["118"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["118"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["118"].playEvent("US", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 4)

        app = Labyrinth(1, 1, testBlankScenarioSetup, ["y"])
        app.deck["118"].playEvent("Jihadist", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 4)
        app.deck["118"].playEvent("US", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 5)


class CardHundredNineteen(LabyrinthTest):
    """Saleh"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["119"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["119"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["119"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["119"].playEvent("US", app)
        self.assertTrue(app.map["Yemen"].is_governed())
        self.assertTrue(app.map["Yemen"].is_ally())
        self.assertTrue(app.map["Yemen"].aid == 1)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.map["Yemen"].make_islamist_rule()
        app.map["Yemen"].make_neutral()
        app.deck["119"].playEvent("US", app)
        self.assertTrue(app.map["Yemen"].is_governed())
        self.assertTrue(app.map["Yemen"].is_neutral())
        self.assertTrue(app.map["Yemen"].aid == 0)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["119"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Yemen"].is_governed())
        self.assertTrue(app.map["Yemen"].is_adversary())
        self.assertTrue(app.map["Yemen"].besieged == 1)


class CardHundredTwenty(LabyrinthTest):
    """US Election"""

    def test_playable(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertTrue(app.deck["120"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["120"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        self.assertFalse(app.deck["120"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.executeCardUSElection(5)
        self.assertTrue(app.prestige == 8)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.executeCardUSElection(4)
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["120"].playEvent("US", app)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, testBlankScenarioSetup)
        app.deck["120"].playEvent("US", app)
        self.assertTrue(app.prestige != 7)


class TestGovernanceClass(LabyrinthTest):

    def test_with_good_index(self):
        gov = Governances.with_index(2)
        self.assertEquals(FAIR, gov)

    def test_with_too_high_index(self):
        try:
            Governances.with_index(5)
            self.fail("Should have raised a ValueError")
        except ValueError as e:
            self.assertEquals("Invalid governance value - 5", e.message)

    def test_str(self):
        gov = Governance("Anarchy", 5, -2)
        self.assertEquals("Anarchy", str(gov))

    def test_repr(self):
        gov = Governance("Anarchy", 5, -2)
        self.assertEquals('Governance("Anarchy", 5, -2)', repr(gov))

    def test_equality(self):
        name = "some name"
        max_roll = 3
        gov1 = Governance(name, max_roll, 0)
        gov2 = Governance(name, max_roll, 0)
        self.assertEquals(gov1, gov2)

    def test_inequality_by_name(self):
        gov1 = Governance("name 1", 0, 1)
        gov2 = Governance("name 2", 0, 1)
        self.assertNotEqual(gov1, gov2)

    def test_inequality_by_max_roll(self):
        gov1 = Governance("name 1", 1, 2)
        gov2 = Governance("name 1", 2, 2)
        self.assertNotEqual(gov1, gov2)

    def test_successful_roll(self):
        max_roll = 4
        gov = Governance("some name", max_roll, 0)
        for roll in range(1, max_roll + 1):
            self.assertTrue(gov.is_success(roll))
        for roll in range(max_roll + 1, max_roll + 2):
            self.assertFalse(gov.is_success(roll))

    def test_instances_are_hashable(self):
        gov = Governance("anything", 0, 0)
        hash(gov)


class TestCountry(LabyrinthTest):

    def test_improve_country_from_fair_to_good(self):
        # Set up
        country = Country(None, "Somewhere", "Sunni", None, FAIR, False, 0, 0, 0, 0, False, 2)
        country.aid = 4
        country.besieged = 1
        country.regimeChange = 1

        # Invoke
        country.improve_governance()

        # Assert
        self.assertTrue(country.is_good())
        self.assertEqual(0, country.aid)
        self.assertEqual(0, country.besieged)
        self.assertEqual(0, country.regimeChange)


class DieRollerTest(LabyrinthTest):

    def test_rolls_correct_number_of_times(self):
        roller = DieRoller()
        times = 5
        results = roller.roll(times)
        self.assertEqual(len(results), times)

    def test_rolls_are_within_correct_range(self):
        roller = DieRoller()
        results = roller.roll(1000)
        for roll in results:
            self.assertTrue(1 <= roll <= 6)


class Disrupt(LabyrinthTest):

    def test_cannot_disrupt_in_neutral_muslim_country_with_no_troops(self):
        # Set up
        country = Country(None, "Somewhere", "Shia-Mix", None, FAIR, False, 0, 0, 0, 0, False, 0)
        country.cadre = 1
        country.make_neutral()
        country.troopCubes = 0

        # Invoke & assert
        self.assertFalse(country.is_disruptable())

    def test_cannot_disrupt_in_neutral_muslim_country_with_one_troop(self):
        # Set up
        country = Country(None, "Somewhere", "Shia-Mix", None, FAIR, False, 0, 0, 0, 0, False, 0)
        country.cadre = 1
        country.make_neutral()
        country.troopCubes = 1

        # Invoke & assert
        self.assertFalse(country.is_disruptable())

    def test_can_disrupt_in_neutral_muslim_country_with_two_troops(self):
        # Set up
        country = Country(None, "Somewhere", "Shia-Mix", None, FAIR, False, 0, 0, 0, 0, False, 0)
        country.cadre = 1
        country.make_neutral()
        country.troopCubes = 2

        # Invoke & assert
        self.assertTrue(country.is_disruptable())

    def test_can_disrupt_in_allied_muslim_country_with_no_troops(self):
        # Set up
        country = Country(None, "Somewhere", "Shia-Mix", None, FAIR, False, 0, 0, 0, 0, False, 0)
        country.cadre = 1
        country.make_ally()
        country.troopCubes = 0

        # Invoke & assert
        self.assertTrue(country.is_disruptable())

    def test_can_disrupt_in_non_muslim_country_with_no_troops(self):
        # Set up
        country = Country(None, "Somewhere", "Non-Muslim", None, FAIR, False, 0, 0, 0, 0, False, 0)
        country.cadre = 1
        country.troopCubes = 0

        # Invoke & assert
        self.assertTrue(country.is_disruptable())

    def test_num_disruptable(self):
        # Set up
        app = Labyrinth(1, 1)
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].make_ally()
        app.map["Jordan"].sleeperCells = 1
        app.map["Jordan"].troopCubes = 2
        app.map["Libya"].sleeperCells = 1
        app.map["Libya"].troopCubes = 1 # Should not be enough

        # Invoke & assert
        self.assertEqual(app.num_disruptable(), 3)

if __name__ == "__main__":
    unittest.main()   