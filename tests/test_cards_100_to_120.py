import unittest

from fakes import FakeDieRoller
from labyrinth_test_case import LabyrinthTestCase
from lwotai import GOOD
from lwotai import Labyrinth
from lwotai import POOR


class Card100(LabyrinthTestCase):
    """His Ut-Tahrir"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["100"].playable("US", app, True))
        self.assertTrue(app.deck["100"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["100"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["100"].playEvent("US", app)
        self.assertTrue(app.funding == 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["100"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 4
        app.deck["100"].playEvent("US", app)
        self.assertTrue(app.funding == 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 4
        app.deck["100"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 10
        app.deck["100"].playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 10
        app.deck["100"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 3)


class Card101(LabyrinthTestCase):
    """Kosovo"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["101"].playable("US", app, True))
        self.assertTrue(app.deck["101"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["101"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["101"].playEvent("US", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.map["Serbia"].posture == "Soft")

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].posture = "Soft"
        app.deck["101"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.map["Serbia"].posture == "Hard")


class Card102(LabyrinthTestCase):
    """Former Soviet Union"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["102"].playable("US", app, True))
        self.assertTrue(app.deck["102"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["102"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["102"].playEvent("US", app)
        self.assertTrue(app.map["Central Asia"].is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Central Asia")
        app.map["Central Asia"].make_good()
        app.map["Central Asia"].make_ally()
        app.deck["102"].playEvent("Jihadist", app)
        self.assertFalse(app.map["Central Asia"].is_good())
        self.assertTrue(app.map["Central Asia"].is_neutral())


class Card103(LabyrinthTestCase):
    """Hizballah"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["103"].playable("US", app, True))
        self.assertTrue(app.deck["103"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["103"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["103"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["103"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Lebanon"].is_poor())
        self.assertTrue(app.map["Lebanon"].is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Lebanon")
        app.map["Lebanon"].make_good()
        app.map["Lebanon"].make_ally()
        app.map["Jordan"].make_good()
        app.map["Jordan"].make_ally()
        app.deck["103"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Lebanon"].is_poor())
        self.assertTrue(app.map["Lebanon"].is_neutral())

        # no countries
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.deck["103"].playEvent("US", app)

        # one country
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.testCountry("Gulf States")
        app.map["Gulf States"].sleeperCells = 1
        app.deck["103"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)


class Card104(LabyrinthTestCase):
    """Iran"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["104"].playable("US", app, True))
        self.assertTrue(app.deck["104"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["104"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["104"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Yemen"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.testCountry("Yemen")
        app.map["Yemen"].sleeperCells = 1
        app.deck["104"].playEvent("US", app)
        self.assertTrue(app.map["Yemen"].sleeperCells == 0)

        app.deck["104"].playEvent("Jihadist", app)


class Card105(LabyrinthTestCase):
    """Iran"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["105"].playable("US", app, True))
        self.assertTrue(app.deck["105"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["105"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["105"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Yemen"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.testCountry("Yemen")
        app.map["Yemen"].sleeperCells = 1
        app.deck["105"].playEvent("US", app)
        self.assertTrue(app.map["Yemen"].sleeperCells == 0)

        app.deck["105"].playEvent("Jihadist", app)


class Card106(LabyrinthTestCase):
    """Jaysh al-Mahdi"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["106"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 3
        app.map["Iraq"].troopCubes = 1
        app.deck["106"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 2
        app.map["Iraq"].troopCubes = 1
        app.deck["106"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].troopCubes = 1
        app.deck["106"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Lebanon"])
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 2
        app.map["Iraq"].troopCubes = 1
        app.map["Lebanon"].sleeperCells = 2
        app.map["Lebanon"].troopCubes = 1
        print "Choose Lebanon"
        app.deck["106"].playEvent("US", app)
        self.assertTrue(app.map["Lebanon"].sleeperCells == 0)

        print "HERE"
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 2
        app.map["Iraq"].troopCubes = 1
        app.deck["106"].playEvent("Jihadist", app)


class Card107(LabyrinthTestCase):
    """Kurdistan"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["107"].playable("US", app, True))
        self.assertTrue(app.deck["107"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["107"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.deck["107"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].aid == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["107"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Turkey"].is_poor())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].make_good()
        app.deck["107"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Turkey"].governance_is_worse_than(GOOD))
        self.assertTrue(app.map["Iraq"].is_fair())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].make_fair()
        app.testCountry("Turkey")
        app.map["Turkey"].make_fair()
        app.map["Turkey"].aid = 1
        app.deck["107"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Turkey"].is_poor())
        self.assertTrue(app.map["Iraq"].is_fair())


class Card108(LabyrinthTestCase):
    """Musharraf"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["108"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 1
        app.map["Pakistan"].make_good()
        app.deck["108"].playEvent("US", app)
        self.assertCells(app, "Pakistan", 0, True)
        self.assertTrue(app.map["Pakistan"].is_poor())
        self.assertTrue(app.map["Pakistan"].is_ally())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 3
        app.map["Pakistan"].make_islamist_rule()
        app.map["Pakistan"].make_adversary()
        app.deck["108"].playEvent("Jihadist", app)
        self.assertCells(app, "Pakistan", 2, True)
        self.assertTrue(app.map["Pakistan"].is_poor())
        self.assertTrue(app.map["Pakistan"].is_ally())


class Card109(LabyrinthTestCase):
    """Tora Bora"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["109"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 2
        app.map["Pakistan"].regimeChange = 1
        app.deck["109"].playEvent("US", app)
        self.assertCells(app, "Pakistan", 0, True)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Pakistan")
        app.map["Pakistan"].sleeperCells = 2
        app.map["Pakistan"].regimeChange = 1
        app.deck["109"].playEvent("Jihadist", app)
        self.assertCells(app, "Pakistan", 0, True)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
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


class Card110(LabyrinthTestCase):
    """Zarqawi"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["110"].playable("US", app, True))
        self.assertFalse(app.deck["110"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["110"].playable("US", app, True))
        self.assertTrue(app.deck["110"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["110"].playable("US", app, True))
        self.assertFalse(app.deck["110"].playable("Jihadist", app, False))
        app.testCountry("Syria")
        app.map["Syria"].troopCubes = 1
        self.assertTrue(app.deck["110"].playable("US", app, True))
        self.assertTrue(app.deck["110"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["110"].playable("US", app, True))
        self.assertFalse(app.deck["110"].playable("Jihadist", app, False))
        app.testCountry("Lebanon")
        app.map["Lebanon"].troopCubes = 1
        self.assertTrue(app.deck["110"].playable("US", app, True))
        self.assertTrue(app.deck["110"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["110"].playable("US", app, True))
        self.assertFalse(app.deck["110"].playable("Jihadist", app, False))
        app.testCountry("Jordan")
        app.map["Jordan"].troopCubes = 1
        self.assertTrue(app.deck["110"].playable("US", app, True))
        self.assertTrue(app.deck["110"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["110"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].troopCubes = 2
        app.deck["110"].playEvent("US", app)
        self.assertTrue(app.prestige == 10)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].troopCubes = 2
        app.deck["110"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].totalCells(True) == 3)
        self.assertTrue(app.map["Iraq"].plots == 1)


class Card111(LabyrinthTestCase):
    """Zawahiri"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["111"].playable("US", app, True))
        self.assertTrue(app.deck["111"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        self.assertFalse(app.deck["111"].playable("US", app, True))
        self.assertTrue(app.deck["111"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Pakistan")
        app.map["Pakistan"].markers.append("FATA")
        self.assertFalse(app.deck["111"].playable("US", app, True))
        self.assertTrue(app.deck["111"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Pakistan")
        app.markers.append("Al-Anbar")
        self.assertFalse(app.deck["111"].playable("US", app, True))
        self.assertTrue(app.deck["111"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["111"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["111"].playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["111"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        app.deck["111"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 4)


class Card112(LabyrinthTestCase):
    """Bin Ladin"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["112"].playable("US", app, True))
        self.assertTrue(app.deck["112"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        self.assertFalse(app.deck["112"].playable("US", app, True))
        self.assertTrue(app.deck["112"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Pakistan")
        app.map["Pakistan"].markers.append("FATA")
        self.assertFalse(app.deck["112"].playable("US", app, True))
        self.assertTrue(app.deck["112"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Pakistan")
        app.markers.append("Al-Anbar")
        self.assertFalse(app.deck["112"].playable("US", app, True))
        self.assertTrue(app.deck["112"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["112"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["112"].playEvent("US", app)
        self.assertTrue(app.funding == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["112"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        app.deck["112"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 3)


class Card113(LabyrinthTestCase):
    """Darfur"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["113"].playable("US", app, True))
        self.assertTrue(app.deck["113"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["113"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["113"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].aid == 1)
        self.assertTrue(app.map["Sudan"].is_ally())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Sudan")
        app.map["Sudan"].make_adversary()
        app.deck["113"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].aid == 1)
        self.assertTrue(app.map["Sudan"].is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 6
        app.deck["113"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].besieged == 1)
        self.assertTrue(app.map["Sudan"].is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 6
        app.testCountry("Sudan")
        app.map["Sudan"].make_ally()
        app.deck["113"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].besieged == 1)
        self.assertTrue(app.map["Sudan"].is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["113"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].aid == 1)
        self.assertTrue(app.map["Sudan"].is_ally())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Sudan")
        app.map["Sudan"].make_adversary()
        app.deck["113"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].aid == 1)
        self.assertTrue(app.map["Sudan"].is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 6
        app.deck["113"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].besieged == 1)
        self.assertTrue(app.map["Sudan"].is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 6
        app.testCountry("Sudan")
        app.map["Sudan"].make_ally()
        app.deck["113"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Sudan"].is_governed())
        self.assertTrue(app.map["Sudan"].besieged == 1)
        self.assertTrue(app.map["Sudan"].is_neutral())


class Card114(LabyrinthTestCase):
    """GTMO"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["114"].playable("US", app, True))
        self.assertTrue(app.deck["114"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["114"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["114"].playEvent("US", app)
        self.assertTrue("GTMO" in app.lapsing)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["114"].playEvent("Jihadist", app)
        self.assertTrue("GTMO" in app.lapsing)
        self.assertTrue(app.prestige != 7)


class Card115(LabyrinthTestCase):
    """Hambali"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["115"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Philippines")
        app.map["Philippines"].sleeperCells = 1
        app.map["Philippines"].posture = "Hard"
        app.deck["115"].playEvent("US", app)
        self.assertTrue(app.map["Philippines"].sleeperCells == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Indonesia/Malaysia"])
        app.testCountry("Indonesia/Malaysia")
        app.map["Indonesia/Malaysia"].sleeperCells = 1
        app.map["Indonesia/Malaysia"].make_ally()
        app.testCountry("Philippines")
        app.map["Philippines"].sleeperCells = 1
        app.map["Philippines"].posture = "Hard"
        print "Choose Indonesia/Malaysia"
        app.deck["115"].playEvent("US", app)
        self.assertTrue(app.map["Indonesia/Malaysia"].sleeperCells == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Indonesia/Malaysia")
        app.map["Indonesia/Malaysia"].sleeperCells = 1
        app.map["Indonesia/Malaysia"].make_ally()
        app.deck["115"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Indonesia/Malaysia"].plots == 1)


class Card116(LabyrinthTestCase):
    """KSM"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["116"].playable("Jihadist", app, False))
        self.assertFalse(app.deck["116"].playable("US", app, True))
        app.testCountry("Iraq")
        app.map["Iraq"].make_ally()
        app.map["Iraq"].plots = 1
        self.assertTrue(app.deck["116"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["116"].playable("Jihadist", app, False))
        self.assertFalse(app.deck["116"].playable("US", app, True))
        app.testCountry("Canada")
        app.map["Canada"].plots = 1
        self.assertTrue(app.deck["116"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["116"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].sleeperCells = 1
        app.deck["116"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.map["Iraq"].make_islamist_rule()
        app.map["Iraq"].sleeperCells = 1
        app.deck["116"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)
        self.assertTrue(app.map["Iraq"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].plots == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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


class Card117(LabyrinthTestCase):
    """Oil Price Spike"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["117"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["117"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["117"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["117"].playEvent("US", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y"])
        app.deck["117"].playEvent("Jihadist", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 4)
        app.deck["117"].playEvent("US", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 5)


class Card118(LabyrinthTestCase):
    """Oil Price Spike"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["118"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["118"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["118"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["118"].playEvent("US", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y"])
        app.deck["118"].playEvent("Jihadist", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 4)
        app.deck["118"].playEvent("US", app)
        self.assertTrue(app.countryResources("Saudi Arabia") == 5)


class Card119(LabyrinthTestCase):
    """Saleh"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["119"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["119"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["119"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["119"].playEvent("US", app)
        self.assertTrue(app.map["Yemen"].is_governed())
        self.assertTrue(app.map["Yemen"].is_ally())
        self.assertTrue(app.map["Yemen"].aid == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Yemen"].make_islamist_rule()
        app.map["Yemen"].make_neutral()
        app.deck["119"].playEvent("US", app)
        self.assertTrue(app.map["Yemen"].is_governed())
        self.assertTrue(app.map["Yemen"].is_neutral())
        self.assertTrue(app.map["Yemen"].aid == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["119"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Yemen"].is_governed())
        self.assertTrue(app.map["Yemen"].is_adversary())
        self.assertTrue(app.map["Yemen"].besieged == 1)


class Card120(LabyrinthTestCase):
    """US Election"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["120"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["120"].playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["120"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.executeCardUSElection(5)
        self.assertTrue(app.prestige == 8)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.executeCardUSElection(4)
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["120"].playEvent("US", app)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["120"].playEvent("US", app)
        self.assertTrue(app.prestige != 7)


if __name__ == "__main__":
    unittest.main()   