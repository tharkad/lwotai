from labyrinth_test_case import LabyrinthTestCase
from lwotai import Country
from lwotai import FAIR
from lwotai import Labyrinth


class DisruptTest(LabyrinthTestCase):

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