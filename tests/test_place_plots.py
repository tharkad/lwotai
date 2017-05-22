from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class PlacePlotsTest(LabyrinthTestCase):
    """Place Plots"""

    def test_place_plot(self):
        # no cells
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 1)
        unusedOps = app.executePlot(2, False, [1, 2])
        self.assertEqual(unusedOps, 2)
        unusedOps = app.executePlot(3, True, [1, 2, 3])
        self.assertEqual(unusedOps, 3)

        # 1 cell in US
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 1
        unusedOps = app.executePlot(1, True, [2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 0)

        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 1)
        self.assertEqual(app.map["United States"].plots, 1)

        # 2 cells in us
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 2
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 2
        unusedOps = app.executePlot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 2
        unusedOps = app.executePlot(2, True, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 2
        unusedOps = app.executePlot(3, True, [1, 2, 3])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 1)

        # 3 cells in us
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 1)
        self.assertEqual(app.map["United States"].sleeperCells, 2)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.map["United States"].plots, 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(2, True, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(2, True, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 2)
        self.assertEqual(app.map["United States"].sleeperCells, 1)
        self.assertEqual(app.map["United States"].plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 3
        unusedOps = app.executePlot(3, True, [1, 1, 3])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["United States"].activeCells, 3)
        self.assertEqual(app.map["United States"].sleeperCells, 0)
        self.assertEqual(app.map["United States"].plots, 2)

        # Low prestige, no GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        unusedOps = app.executePlot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].activeCells, 1)
        self.assertEqual(app.map["Iraq"].plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.map["Israel"].sleeperCells = 1
        app.map["United States"].posture = "Soft"
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 0)
        self.assertEqual(app.map["Israel"].sleeperCells, 1)
        self.assertEqual(app.map["Israel"].plots, 0)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].activeCells, 1)
        self.assertEqual(app.map["Iraq"].plots, 1)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 0)
        self.assertEqual(app.map["Israel"].sleeperCells, 1)
        self.assertEqual(app.map["Israel"].plots, 0)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 1)

        # Funding section
        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 9
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 0
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.map["Israel"].activeCells, 0)
        self.assertEqual(app.map["Israel"].sleeperCells, 1)
        self.assertEqual(app.map["Israel"].plots, 0)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 0
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 0
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 0
        unusedOps = app.executePlot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 1)
        self.assertEqual(app.map["Iraq"].plots, 0)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.map["Israel"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 0
        unusedOps = app.executePlot(3, True, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 1)
        self.assertEqual(app.map["Israel"].sleeperCells, 0)
        self.assertEqual(app.map["Israel"].plots, 1)
        self.assertEqual(app.map["Canada"].plots, 1)
        self.assertEqual(app.map["Iraq"].plots, 1)

        # High prestige
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 4
        app.markers = ["Abu Sayyaf"]
        app.map["Israel"].sleeperCells = 1
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        app.map["Iraq"].troopCubes = 1
        app.map["Philippines"].sleeperCells = 1
        app.map["Philippines"].troopCubes = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Israel"].activeCells, 0)
        self.assertEqual(app.map["Israel"].sleeperCells, 1)
        self.assertEqual(app.map["Israel"].plots, 0)
        self.assertEqual(app.map["Canada"].plots, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)
        self.assertEqual(app.map["Philippines"].activeCells, 1)
        self.assertEqual(app.map["Philippines"].sleeperCells, 0)
        self.assertEqual(app.map["Philippines"].plots, 1)

        # priorities box
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.map["Israel"].sleeperCells = 0
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Spain"].sleeperCells = 0
        app.map["Iraq"].make_good()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].aid = 1
        unusedOps = app.executePlot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].plots, 0)
        self.assertEqual(app.map["Gulf States"].plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.map["Israel"].sleeperCells = 0
        app.map["Canada"].posture = "Soft"
        app.map["Canada"].sleeperCells = 1
        app.map["Spain"].posture = "Soft"
        app.map["Spain"].sleeperCells = 0
        app.map["Iraq"].make_good()
        app.map["Iraq"].sleeperCells = 1
        app.map["Iraq"].aid = 1
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].aid = 1
        unusedOps = app.executePlot(1, False, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.map["Iraq"].plots, 1)
        self.assertEqual(app.map["Gulf States"].plots, 0)