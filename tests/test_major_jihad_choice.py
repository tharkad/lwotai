from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class MajorJihadChoice(LabyrinthTestCase):
    """Major Jihad possible?"""
    # For Major Jihad to be possible you need:
    # - A muslim country
    # - Not under Islamist Rule
    # - with at least 5 more cells than troops
    # - At least 2 rolls if the country is poor and not besieged
    # - At least 1 roll if the country is poor and is besieged
    # - At least 3 rolls if the country is fair and not besieged
    # - At least 2 rolls if the country is fair and is besieged
    # - At least 3 rolls if the country is good and is besieged
    # - NOT possible if the country is good and not besieged

    def test_major_jihad_choice(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        self.assertEqual(app.majorJihadChoice(3), False)    # 3 Ops
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Gulf States")    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops
        app.map["Gulf States"].make_fair()
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), False)    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops
        app.map["Gulf States"].make_good()
        self.assertEqual(app.majorJihadChoice(3), False)    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), False)    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops
        app.map["Gulf States"].besieged = 1
        app.map["Gulf States"].make_poor()
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Gulf States")    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), "Gulf States")    # 1 Ops
        app.map["Gulf States"].make_fair()
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Gulf States")    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops
        app.map["Gulf States"].make_good()
        self.assertEqual(app.majorJihadChoice(3), "Gulf States")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), False)    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].sleeperCells = 5
        app.map["Gulf States"].activeCells = 4
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].besieged = 0
        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].sleeperCells = 3
        app.map["Afghanistan"].activeCells = 3
        app.map["Afghanistan"].troopCubes = 1
        app.map["Afghanistan"].besieged = 0

        self.assertEqual(app.majorJihadChoice(3), "Gulf States")  # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Gulf States")  # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)  # 1 Ops

        app.map["Saudi Arabia"].make_poor()
        app.map["Saudi Arabia"].sleeperCells = 5
        app.map["Saudi Arabia"].activeCells = 4
        app.map["Saudi Arabia"].troopCubes = 4
        app.map["Saudi Arabia"].besieged = 0

        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops
        self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])  # 3 Ops

        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].sleeperCells = 5
        app.map["Pakistan"].activeCells = 4
        app.map["Pakistan"].troopCubes = 4
        app.map["Pakistan"].besieged = 0

        self.assertEqual(app.majorJihadChoice(3), "Pakistan")    # 3 Ops
        self.assertEqual(app.majorJihadChoice(2), "Pakistan")    # 2 Ops
        self.assertEqual(app.majorJihadChoice(1), False)    # 1 Ops