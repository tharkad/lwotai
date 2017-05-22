from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class NamesOfCountriesMatchingPredicateTest(LabyrinthTestCase):

    def test_schengen_countries(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_test_scenario)

        # Invoke
        schengen_countries = app.names_of_countries(lambda c: c.schengen)

        # Check
        self.assertEqual(schengen_countries,
                         ['France', 'Italy', 'Germany', 'Spain', 'Scandinavia', 'Eastern Europe', 'Benelux'])