from lwotai import Labyrinth
from labyrinth_test_case import LabyrinthTestCase


class RecruitTest(LabyrinthTestCase):
    """Test Recruiting"""

    def test_recruit_choice(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
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

    def test_execute_recruit(self):
        # Normal
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 1, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 1, [2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [2, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 3)
        self.assertEqual(app.cells, 12)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [1, 2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [2, 1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [2, 2, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)    # Coherent
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 1, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 1, [2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 2, [2, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 3)
        self.assertEqual(app.cells, 12)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [1, 2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [2, 1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unusedOps = app.executeRecruit("United States", 3, [2, 2, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        # not enough cells
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [2, 2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [1, 2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 2])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 1
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 3
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 1)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 3
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 2)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 5
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [2, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.cells, 4)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 5
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.cells, 3)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 5
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 3)
        self.assertEqual(app.cells, 2)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 4
        app.funding = 9
        unusedOps = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].sleeperCells, 3)
        self.assertEqual(app.cells, 1)

        # IR RC
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        app.funding = 9
        app.map["Iraq"].make_poor()
        unusedOps = app.executeRecruit("Iraq", 1, [4])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        app.funding = 9
        app.map["Iraq"].make_islamist_rule()
        unusedOps = app.executeRecruit("Iraq", 1, [6])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        app.funding = 9
        app.map["Iraq"].make_fair()
        app.map["Iraq"].regimeChange = 1
        unusedOps = app.executeRecruit("Iraq", 1, [6])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].sleeperCells, 1)
        self.assertEqual(app.cells, 14)