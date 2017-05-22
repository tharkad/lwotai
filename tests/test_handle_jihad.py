from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class HandleJihadTest(LabyrinthTestCase):
    """Test handleJihad"""

    def test_handle_jihad(self):
        # Many Cells
        app = Labyrinth(1, 1, self.set_up_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_test_scenario)
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

        app = Labyrinth(1, 1, self.set_up_test_scenario)
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
        app = Labyrinth(1, 1, self.set_up_test_scenario)
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