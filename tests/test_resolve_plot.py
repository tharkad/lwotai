from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class ResolvePlotTest(LabyrinthTestCase):
    """Resolve _plots"""

    def test_resolve_non_muslim_non_us_plots(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Germany"].plots = 1
        app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Germany"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "Hard")
        self.assertEqual(app.map["Scandinavia"].posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Germany"].plots = 2
        app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Germany"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "Hard")
        self.assertEqual(app.map["Scandinavia"].posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Germany"].plots = 1
        app.resolvePlot("Germany", 2, 5, [], ["Spain", "Scandinavia"], [4, 5], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["Germany"].posture, "Hard")
        self.assertEqual(app.map["Spain"].posture, "Soft")
        self.assertEqual(app.map["Scandinavia"].posture, "Hard")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Canada"].plots = 1
        app.resolvePlot("Canada", 2, 5, [], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["Canada"].posture, "Hard")
        self.assertEqual(app.map["Spain"].posture, "")
        self.assertEqual(app.map["Scandinavia"].posture, "")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Canada"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Russia"].plots = 1
        app.resolvePlot("Russia", 2, 4, [], [], [], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Russia"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "")
        self.assertEqual(app.map["Scandinavia"].posture, "")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Russia"].plots, 0)

        app = Labyrinth(1, "WMD", self.set_up_blank_test_scenario)
        app.map["Germany"].plots = 1
        app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Germany"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "Hard")
        self.assertEqual(app.map["Scandinavia"].posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 0)

        app = Labyrinth(1, "WMD", self.set_up_blank_test_scenario)
        app.funding = 1
        app.map["Germany"].plots = 1
        app.resolvePlot("Germany", 3, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.map["Germany"].posture, "Soft")
        self.assertEqual(app.map["Spain"].posture, "Hard")
        self.assertEqual(app.map["Scandinavia"].posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Germany"].plots, 0)

    def test_resolve_muslim_iran_plots(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_fair()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 1, 0, [], [], [], [3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 1)
        app.resolvePlot("Iraq", 1, 0, [], [], [], [2])
        self.assertEqual(app.funding, 7)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_good()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 1, 2])
        self.assertEqual(app.funding, 7)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_good()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 1, 2])
        self.assertEqual(app.funding, 7)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iran"].plots = 1
        app.resolvePlot("Iran", 3, 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iran"].is_fair())
        self.assertEqual(app.map["Iran"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iran"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.map["Iraq"].troopCubes = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 6)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.map["Iraq"].troopCubes = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 1)
        self.assertEqual(app.map["Iraq"].plots, 0)

    def test_resolve_us_plots(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].plots = 1
        app.map["United States"].posture = "Hard"
        app.resolvePlot("United States", 1, 4, [1, 6, 1], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["United States"].posture, "Soft")
        self.assertEqual(app.prestige, 6)
        self.assertEqual(app.map["United States"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].plots = 1
        app.map["United States"].posture = "Soft"
        app.resolvePlot("United States", 2, 4, [5, 6, 1], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["United States"].posture, "Soft")
        self.assertEqual(app.prestige, 8)
        self.assertEqual(app.map["United States"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].plots = 1
        app.map["United States"].posture = "Soft"
        app.resolvePlot("United States", 3, 5, [5, 6, 4], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.map["United States"].posture, "Hard")
        self.assertEqual(app.prestige, 11)
        self.assertEqual(app.map["United States"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.gameOver)
        app.map["United States"].plots = 1
        app.map["United States"].posture = "Soft"
        app.resolvePlot("United States", "WMD", 0, [], [], [], [])
        self.assertEqual(app.map["United States"].plots, 0)
        self.assertTrue(app.gameOver)

    def test_resolve_muslim_iran_plots_with_backlash(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_fair()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 1, 0, [], [], [], [3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 1)
        app.resolvePlot("Iraq", 1, 0, [], [], [], [2], True)
        self.assertEqual(app.funding, 3)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_good()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 1, 2], True)
        self.assertEqual(app.funding, 3)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_good()
        app.map["Iraq"].aid = 1
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 1, 2], True)
        self.assertEqual(app.funding, 1)
        self.assertTrue(app.map["Iraq"].is_fair())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iran"].plots = 1
        app.resolvePlot("Iran", 3, 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.map["Iran"].is_fair())
        self.assertEqual(app.map["Iran"].aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.map["Iran"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.map["Iraq"].troopCubes = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 6)
        self.assertEqual(app.map["Iraq"].plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 0
        app.map["Iraq"].plots = 1
        app.map["Iraq"].troopCubes = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 1)
        self.assertTrue(app.map["Iraq"].is_poor())
        self.assertEqual(app.map["Iraq"].aid, 0)
        self.assertEqual(app.prestige, 1)
        self.assertEqual(app.map["Iraq"].plots, 0)
