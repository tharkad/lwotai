from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class ExecuteJihadTest(LabyrinthTestCase):
    """Execute Major Jihad"""
    # A Major jihad needs:
    # - Muslim country not under Islamist Rule
    # - 5 more cells than troops
    # - Then if gov at Poor and not besieged 2 more successes causes Islamist Revolution
    # - Or if gov at Poor and is besieged 1 more success causes Islamist Revolution
    # Jihad does:
    # - Each success worsens gov
    # - Any failure roll sends a cell to the funding track
    # Major failure does:
    # - Three Failure rolls in a Poor country shifts alignment one toward Ally and places Besieged regime
    # A Major jihad does:
    # - All cells go active
    # Islamist Revolution causes:
    # - Gov to Islamist Rule
    # - Alignment to Adversary
    # - Remove Regime Change, Besieged and Aid
    # - Add country's resources to Funding track
    # - If troops in country US Prestige to 1

    # 5 MORE CELLS THAN TROOPS - Major Jihad possible

    def testJihadEnoughCellsPoorGovNotBesieged(self):

        # Poor Gov
        # Not Besieged
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # one removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # to 1 due to troops present

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 2)  # one removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 4
        funding_before = app.funding
        prestige_before = app.prestige
        app.executeJihad("Gulf States", [3, 4, 4])  # 8.4.3.1 Major Jihad Failure
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the two failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)
        self.assertEqual(app.map["Gulf States"].aid, 3)  # one removed by success
        self.assertEqual(app.map["Gulf States"].besieged, 1)
        self.assertTrue(app.map["Gulf States"].is_ally())
        self.assertEqual(app.funding, funding_before)
        self.assertEqual(app.prestige, prestige_before)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])  # Major failure
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_ally())  # major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # to 1 due to troops present

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 7)  # unchanged, no troops

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # to 1 due to troops present

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 7)  # unchanged, no troops

    def testJihadEnoughCellsPoorGovIsBeseiged(self):
        # Poor Gov
        # Besieged
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 4])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 4, 4])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])  # Major Failure in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_ally())  # major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadEnoughCellsFairGovNotBeseiged(self):
        # Fair Gov
        # Not Besieged
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # not Major failure
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # not major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # not major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # to 1 due to troops present

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 7)  # unchanged, no troops

    def testJihadEnoughCellsFairGovIsBeseiged(self):
        # Fair Gov
        # Besieged
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 7)  # unchanged, no troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # Not Major Failure in besieged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadEnoughCellsGoodGovNotBeseiged(self):
        # Good Gov
        # Not Besieged
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # not Major failure
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # not major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # not major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 1])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadEnoughCellsGoodGovIsBeseiged(self):
        # Good Gov
        # Besieged

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 4)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 5)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 1])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_islamist_rule())  # islamist rule
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 9)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 0)  # removed
        self.assertEqual(app.map["Gulf States"].aid, 0)  # removed
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # removed
        self.assertTrue(app.map["Gulf States"].is_adversary())  # due to revolution
        self.assertEqual(app.funding, 8)  # +3 from resources
        self.assertEqual(app.prestige, 1)  # troops

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 2])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 8)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 7)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # not Major Failure in besieged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 6)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # not major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # NOT 5 MORE CELLS THAN TROOPS - Major Jihad NOT possible

    def testJihadNotEnoughCellsPoorGovNotBeseiged(self):
        # Poor Gov
        # Not Besieged
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4, 4])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])  # Not Major failure
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # not major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # not major failure
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3, 4])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3, 4])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 4
        app.executeJihad("Gulf States", [3, 3, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 4
        app.executeJihad("Gulf States", [3, 3, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsPoorGovIsBeseiged(self):
        # Poor Gov
        # Besieged
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # one removed
        self.assertEqual(app.map["Gulf States"].besieged, 1)  #
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  #
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # still
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # two removed by successes
        self.assertEqual(app.map["Gulf States"].besieged, 1)  #
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # one removed by success
        self.assertEqual(app.map["Gulf States"].besieged, 1)  #
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # all cells active
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  #
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 4
        app.executeJihad("Gulf States", [3, 3, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 1)  #
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 4
        app.executeJihad("Gulf States", [3, 3, 4])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 2)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 1)  #
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4, 4])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 1)  #
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])  # no major failure
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  #
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsFairGovNotBesieged(self):
        # Fair Gov
        # Not Besieged
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # worsened
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # gone
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # no Major failure
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov stays 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # No troops
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # Islamist Revolution
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsFairGovIsBeseiged(self):
        # Fair Gov
        # Besieged

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution in besieged
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 3])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 3, 3])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [3, 3, 3])  # no Failure in besieged
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov still 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # major failure
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsGoodGovNotBeseiged(self):
        # Good Gov
        # Not Besieged
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # no Major failure
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 1])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadNotEnoughCellsGoodGovIsBeseiged(self):
        # Good Gov
        # Besieged

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 0
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2])  # Revolution failed
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2])  # Revolution fails in besieged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov still 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 1])  # Can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 3)  # lost no cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 1, 2])  # can't major jihad
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov to 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 2)  # lost one cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [1, 2, 2])  # Revolution fails
        self.assertTrue(app.map["Gulf States"].is_fair())  # gov to 2
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # lost two cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 0)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [2, 2, 2])  # no Major Failure in besieged
        self.assertTrue(app.map["Gulf States"].is_good())  # gov stays 1
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # major jihad not possible
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lost three cells to the to failure rolls
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 1)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        # Sleeper/Active cell testing

    def testJihadOneCell(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # sleeper goes active
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # sleeper goes active
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)  # lose sleeper cell
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadTwoSleeperCells(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # sleeper goes active
        self.assertEqual(app.map["Gulf States"].activeCells, 1)  # sleeper goes active
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)  # lose sleeper cell
        self.assertEqual(app.map["Gulf States"].activeCells, 0)  # lose sleeper cell
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadTwoActiveCells(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadOneSleeperOneActiveCells(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadThreeSleeperCells(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 2)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 2)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 4
        app.executeJihad("Gulf States", [3, 3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 3
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadTwoSleeperOneActiveCells(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 2)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 2)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 4
        app.executeJihad("Gulf States", [3, 3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 2
        app.map["Gulf States"].activeCells = 1
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadOneSleeperTwoActiveCells(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 4
        app.executeJihad("Gulf States", [3, 3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 2
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def testJihadThreeActiveCells(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 4
        app.executeJihad("Gulf States", [3, 3, 3])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 3)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 3
        app.executeJihad("Gulf States", [3, 3, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 2)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 2
        app.executeJihad("Gulf States", [3, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 1)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # reduced by each success
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["Gulf States"].make_neutral()
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 0
        app.map["Gulf States"].activeCells = 3
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].regimeChange = 1
        app.map["Gulf States"].aid = 1
        app.executeJihad("Gulf States", [4, 4, 4])
        self.assertTrue(app.map["Gulf States"].is_poor())  # gov still 3
        self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
        self.assertEqual(app.map["Gulf States"].activeCells, 0)
        self.assertEqual(app.map["Gulf States"].regimeChange, 1)  # still there
        self.assertEqual(app.map["Gulf States"].aid, 1)  # still there
        self.assertEqual(app.map["Gulf States"].besieged, 0)  # need three fails to get a besieged regime
        self.assertTrue(app.map["Gulf States"].is_neutral())  # need three fails to move alignment
        self.assertEqual(app.funding, 5)
        self.assertEqual(app.prestige, 7)

    def test_minor_jihad_worsens_governance_and_removes_aid(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        original_aid = 2
        target_country = app.map["Gulf States"]
        target_country.make_neutral()
        target_country.make_fair()
        target_country.aid = original_aid
        target_country.besieged = 0
        target_country.activeCells = 2
        target_country.sleeperCells = 0
        target_country.regimeChange = 0
        target_country.troopCubes = 0

        # Invoke
        app.executeJihad(target_country.name, [2, 3])  # one success, one failure

        # Assert
        self.assertTrue(target_country.is_poor())
        self.assertEqual(original_aid - 1, target_country.aid)

    def test_failed_major_jihad_still_removes_aid(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        original_aid = 2
        original_sleepers = 6
        target_country = app.map["Gulf States"]
        target_country.make_ally()
        target_country.make_poor()
        target_country.aid = original_aid
        target_country.besieged = 0
        target_country.activeCells = 0
        target_country.sleeperCells = original_sleepers
        target_country.regimeChange = 0
        target_country.troopCubes = 0
        max_success_roll = 3  # for Poor

        # Invoke
        app.executeJihad(target_country.name, [max_success_roll, max_success_roll + 1])  # one success, one failure

        # Assert
        self.assertEqual(0, target_country.sleeperCells)  # all went active
        self.assertEqual(original_sleepers - 1, target_country.activeCells)  # all went active, one lost to failed roll
        self.assertTrue(target_country.is_poor())   # did not worsen
        self.assertEqual(original_aid - 1, target_country.aid)  # but still removed one aid
