from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth
from fakes import FakeRandomizer


class RadicalizationTest(LabyrinthTestCase):
    """Test Radicalization"""

    def test_cell_placement_removes_cadre(self):
        # Set up
        country_name = "Iraq"
        fake_randomizer = FakeRandomizer()
        fake_randomizer.set_choices([country_name])
        app = Labyrinth(1, 1, self.set_up_test_scenario, randomizer=fake_randomizer)
        country = app.map[country_name]
        country.cadre = 1
        sleepers_before = country.sleeperCells

        # Invoke
        app.handleRadicalization(1)

        # Assert
        sleepers_after = country.sleeperCells
        self.assertEqual(sleepers_after, sleepers_before + 1, "Radicalization should place a sleeper")
        self.assertEqual(country.cadre, 0, "Cell placement should have removed cadre")
