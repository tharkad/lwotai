from labyrinth_test_case import LabyrinthTestCase
from lwotai import Country
from lwotai import FAIR


class CountryImprovementTest(LabyrinthTestCase):

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