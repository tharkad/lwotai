from mockito import when, mock

from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth, Randomizer


class RadicalizationTest(LabyrinthTestCase):
    """Test Radicalization"""

    def test_cell_placement_removes_cadre(self):
        # Set up
        mock_randomizer = mock(Randomizer())
        app = Labyrinth(1, 1, self.set_up_test_scenario, randomizer=mock_randomizer)
        country_name = "Iraq"
        when(mock_randomizer).pick_one(app.map.keys()).thenReturn(country_name)
        country = app.map[country_name]
        country.cadre = 1
        sleepers_before = country.sleeperCells

        # Invoke
        app.handleRadicalization(1)

        # Assert
        sleepers_after = country.sleeperCells
        self.assertEqual(sleepers_after, sleepers_before + 1, "Radicalization should place a sleeper")
        self.assertEqual(country.cadre, 0, "Cell placement should have removed the cadre")
