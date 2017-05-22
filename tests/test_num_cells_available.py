from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class NumCellsAvailableTest(LabyrinthTestCase):
    """Test num cells available"""

    def test_num_cells_available(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 9
        app.cells = 15
        self.assertEqual(app.numCellsAvailable(), 15)
        app.cells = 14
        self.assertEqual(app.numCellsAvailable(), 14)
        app.cells = 13
        self.assertEqual(app.numCellsAvailable(), 13)
        app.cells = 12
        self.assertEqual(app.numCellsAvailable(), 12)
        app.cells = 11
        self.assertEqual(app.numCellsAvailable(), 11)
        app.cells = 10
        self.assertEqual(app.numCellsAvailable(), 10)
        app.cells = 9
        self.assertEqual(app.numCellsAvailable(), 9)
        app.cells = 8
        self.assertEqual(app.numCellsAvailable(), 8)
        app.cells = 7
        self.assertEqual(app.numCellsAvailable(), 7)
        app.cells = 6
        self.assertEqual(app.numCellsAvailable(), 6)
        app.cells = 5
        self.assertEqual(app.numCellsAvailable(), 5)
        app.cells = 4
        self.assertEqual(app.numCellsAvailable(), 4)
        app.cells = 3
        self.assertEqual(app.numCellsAvailable(), 3)
        app.cells = 2
        self.assertEqual(app.numCellsAvailable(), 2)
        app.cells = 1
        self.assertEqual(app.numCellsAvailable(), 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 8
        app.cells = 15
        self.assertEqual(app.numCellsAvailable(), 15)
        app.cells = 14
        self.assertEqual(app.numCellsAvailable(), 14)
        app.cells = 13
        self.assertEqual(app.numCellsAvailable(), 13)
        app.cells = 12
        self.assertEqual(app.numCellsAvailable(), 12)
        app.cells = 11
        self.assertEqual(app.numCellsAvailable(), 11)
        app.cells = 10
        self.assertEqual(app.numCellsAvailable(), 10)
        app.cells = 9
        self.assertEqual(app.numCellsAvailable(), 9)
        app.cells = 8
        self.assertEqual(app.numCellsAvailable(), 8)
        app.cells = 7
        self.assertEqual(app.numCellsAvailable(), 7)
        app.cells = 6
        self.assertEqual(app.numCellsAvailable(), 6)
        app.cells = 5
        self.assertEqual(app.numCellsAvailable(), 5)
        app.cells = 4
        self.assertEqual(app.numCellsAvailable(), 4)
        app.cells = 3
        self.assertEqual(app.numCellsAvailable(), 3)
        app.cells = 2
        self.assertEqual(app.numCellsAvailable(), 2)
        app.cells = 1
        self.assertEqual(app.numCellsAvailable(), 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 7
        app.cells = 15
        self.assertEqual(app.numCellsAvailable(), 15)
        app.cells = 14
        self.assertEqual(app.numCellsAvailable(), 14)
        app.cells = 13
        self.assertEqual(app.numCellsAvailable(), 13)
        app.cells = 12
        self.assertEqual(app.numCellsAvailable(), 12)
        app.cells = 11
        self.assertEqual(app.numCellsAvailable(), 11)
        app.cells = 10
        self.assertEqual(app.numCellsAvailable(), 10)
        app.cells = 9
        self.assertEqual(app.numCellsAvailable(), 9)
        app.cells = 8
        self.assertEqual(app.numCellsAvailable(), 8)
        app.cells = 7
        self.assertEqual(app.numCellsAvailable(), 7)
        app.cells = 6
        self.assertEqual(app.numCellsAvailable(), 6)
        app.cells = 5
        self.assertEqual(app.numCellsAvailable(), 5)
        app.cells = 4
        self.assertEqual(app.numCellsAvailable(), 4)
        app.cells = 3
        self.assertEqual(app.numCellsAvailable(), 3)
        app.cells = 2
        self.assertEqual(app.numCellsAvailable(), 2)
        app.cells = 1
        self.assertEqual(app.numCellsAvailable(), 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 6
        app.cells = 15
        self.assertEqual(app.numCellsAvailable(), 10)
        app.cells = 14
        self.assertEqual(app.numCellsAvailable(), 9)
        app.cells = 13
        self.assertEqual(app.numCellsAvailable(), 8)
        app.cells = 12
        self.assertEqual(app.numCellsAvailable(), 7)
        app.cells = 11
        self.assertEqual(app.numCellsAvailable(), 6)
        app.cells = 10
        self.assertEqual(app.numCellsAvailable(), 5)
        app.cells = 9
        self.assertEqual(app.numCellsAvailable(), 4)
        app.cells = 8
        self.assertEqual(app.numCellsAvailable(), 3)
        app.cells = 7
        self.assertEqual(app.numCellsAvailable(), 2)
        app.cells = 6
        self.assertEqual(app.numCellsAvailable(), 1)
        app.cells = 5
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 4
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 3
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 2
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 1
        self.assertEqual(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 5
        app.cells = 15
        self.assertEqual(app.numCellsAvailable(), 10)
        app.cells = 14
        self.assertEqual(app.numCellsAvailable(), 9)
        app.cells = 13
        self.assertEqual(app.numCellsAvailable(), 8)
        app.cells = 12
        self.assertEqual(app.numCellsAvailable(), 7)
        app.cells = 11
        self.assertEqual(app.numCellsAvailable(), 6)
        app.cells = 10
        self.assertEqual(app.numCellsAvailable(), 5)
        app.cells = 9
        self.assertEqual(app.numCellsAvailable(), 4)
        app.cells = 8
        self.assertEqual(app.numCellsAvailable(), 3)
        app.cells = 7
        self.assertEqual(app.numCellsAvailable(), 2)
        app.cells = 6
        self.assertEqual(app.numCellsAvailable(), 1)
        app.cells = 5
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 4
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 3
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 2
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 1
        self.assertEqual(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 4
        app.cells = 15
        self.assertEqual(app.numCellsAvailable(), 10)
        app.cells = 14
        self.assertEqual(app.numCellsAvailable(), 9)
        app.cells = 13
        self.assertEqual(app.numCellsAvailable(), 8)
        app.cells = 12
        self.assertEqual(app.numCellsAvailable(), 7)
        app.cells = 11
        self.assertEqual(app.numCellsAvailable(), 6)
        app.cells = 10
        self.assertEqual(app.numCellsAvailable(), 5)
        app.cells = 9
        self.assertEqual(app.numCellsAvailable(), 4)
        app.cells = 8
        self.assertEqual(app.numCellsAvailable(), 3)
        app.cells = 7
        self.assertEqual(app.numCellsAvailable(), 2)
        app.cells = 6
        self.assertEqual(app.numCellsAvailable(), 1)
        app.cells = 5
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 4
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 3
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 2
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 1
        self.assertEqual(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 3
        app.cells = 15
        self.assertEqual(app.numCellsAvailable(), 5)
        app.cells = 14
        self.assertEqual(app.numCellsAvailable(), 4)
        app.cells = 13
        self.assertEqual(app.numCellsAvailable(), 3)
        app.cells = 12
        self.assertEqual(app.numCellsAvailable(), 2)
        app.cells = 11
        self.assertEqual(app.numCellsAvailable(), 1)
        app.cells = 10
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 9
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 8
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 7
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 6
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 5
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 4
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 3
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 2
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 1
        self.assertEqual(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 2
        app.cells = 15
        self.assertEqual(app.numCellsAvailable(), 5)
        app.cells = 14
        self.assertEqual(app.numCellsAvailable(), 4)
        app.cells = 13
        self.assertEqual(app.numCellsAvailable(), 3)
        app.cells = 12
        self.assertEqual(app.numCellsAvailable(), 2)
        app.cells = 11
        self.assertEqual(app.numCellsAvailable(), 1)
        app.cells = 10
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 9
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 8
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 7
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 6
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 5
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 4
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 3
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 2
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 1
        self.assertEqual(app.numCellsAvailable(), 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 1
        app.cells = 15
        self.assertEqual(app.numCellsAvailable(), 5)
        app.cells = 14
        self.assertEqual(app.numCellsAvailable(), 4)
        app.cells = 13
        self.assertEqual(app.numCellsAvailable(), 3)
        app.cells = 12
        self.assertEqual(app.numCellsAvailable(), 2)
        app.cells = 11
        self.assertEqual(app.numCellsAvailable(), 1)
        app.cells = 10
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 9
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 8
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 7
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 6
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 5
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 4
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 3
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 2
        self.assertEqual(app.numCellsAvailable(), 0)
        app.cells = 1
        self.assertEqual(app.numCellsAvailable(), 0)