from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class IsAdjacent(LabyrinthTestCase):
    """Test isAdjacent"""

    def test_is_adjacent(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.isAdjacent("Iran", "Iraq"))
        self.assertTrue(app.isAdjacent("Germany", "Spain"))
        self.assertTrue(app.isAdjacent("Libya", "Italy"))
        self.assertTrue(app.isAdjacent("Benelux", "Russia"))
        self.assertTrue(app.isAdjacent("Lebanon", "France"))
        self.assertFalse(app.isAdjacent("United States", "Lebanon"))