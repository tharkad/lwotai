import unittest

class LabyrinthTestCase(unittest.TestCase):
    """Assertions, setup functions, etc. for reuse by subclasses"""

    def assertCells(self, app, country, expected_cells, include_sadr = False):
        """Asserts that the given country contains the given number of cells"""
        self.assertEqual(expected_cells, app.map[country].totalCells(include_sadr))

    def assert_new_messages(self, app, message_count_before, expected_messages):
        expected_message_count = len(expected_messages)
        self.assertEquals(len(app.history), message_count_before + expected_message_count)
        new_messages = app.history[-expected_message_count:]
        self.assertEquals(new_messages, expected_messages)

    @staticmethod
    def schengen_countries(app):
        """Returns the Country objects for the Schengen countries"""
        return [app.map[country] for country in app.map if app.map[country].schengen]

    @staticmethod
    def set_up_test_scenario(app):
        app.prestige = 7
        app.troops = 9
        app.funding = 5
        app.cells = 11
        app.map["Libya"].make_poor()
        app.map["Libya"].make_adversary()
        app.map["Syria"].make_fair()
        app.map["Syria"].make_adversary()
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        app.map["Iraq"].plots = 2
        app.map["Saudi Arabia"].make_poor()
        app.map["Saudi Arabia"].make_ally()
        app.map["Saudi Arabia"].troopCubes = 2
        app.map["Pakistan"].make_fair()
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].troopCubes = 2
        app.map["Pakistan"].activeCells = 4
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].make_ally()
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 4
        app.map["Afghanistan"].make_islamist_rule()
        app.map["Afghanistan"].make_adversary()
        app.map["Afghanistan"].sleeperCells = 4
        app.map["Somalia"].besieged = 1
        app.map["United States"].posture = "Hard"

    @staticmethod
    def set_up_test_scenario_2(app):
        app.prestige = 7
        app.troops = 3
        app.funding = 9
        app.cells = 11
        app.map["Libya"].make_poor()
        app.map["Libya"].make_adversary()
        app.map["Syria"].make_fair()
        app.map["Syria"].make_adversary()
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        app.map["Iraq"].plots = 2
        app.map["Saudi Arabia"].make_poor()
        app.map["Saudi Arabia"].make_ally()
        app.map["Saudi Arabia"].troopCubes = 2
        app.map["Pakistan"].make_fair()
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].troopCubes = 2
        app.map["Pakistan"].activeCells = 4
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].make_ally()
        app.map["Gulf States"].troopCubes = 2
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 4
        app.map["Afghanistan"].make_good()
        app.map["Afghanistan"].make_ally()
        app.map["Afghanistan"].activeCells = 4
        app.map["Afghanistan"].regimeChange = 1
        app.map["Afghanistan"].troopCubes = 6
        app.map["Afghanistan"].aid = 1
        app.map["Afghanistan"].besieged = 0
        app.map["Somalia"].besieged = 1
        app.map["United States"].posture = "Hard"

    @staticmethod
    def set_up_test_scenario_3(app):
        app.prestige = 7
        app.troops = 9
        app.funding = 5
        app.cells = 11
        app.map["Libya"].make_poor()
        app.map["Libya"].make_adversary()
        app.map["Syria"].make_fair()
        app.map["Syria"].make_adversary()
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        app.map["Iraq"].plots = 2
        app.map["Saudi Arabia"].make_poor()
        app.map["Saudi Arabia"].make_ally()
        app.map["Saudi Arabia"].troopCubes = 2
        app.map["Pakistan"].make_fair()
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].troopCubes = 2
        app.map["Pakistan"].activeCells = 4
        app.map["Gulf States"].make_fair()
        app.map["Gulf States"].make_ally()
        app.map["Gulf States"].troopCubes = 4
        app.map["Gulf States"].sleeperCells = 1
        app.map["Gulf States"].activeCells = 4
        app.map["Afghanistan"].make_islamist_rule()
        app.map["Afghanistan"].make_adversary()
        app.map["Afghanistan"].sleeperCells = 4
        app.map["Somalia"].besieged = 1
        app.map["United States"].posture = "Hard"
        app.map["France"].posture = "Hard"
        app.map["France"].cadre = 1
        app.map["Spain"].posture = "Soft"
        app.map["Spain"].sleeperCells = 1
        app.map["Germany"].posture = "Hard"
        app.map["Germany"].activeCells = 1
        app.map["Germany"].sleeperCells = 1

    @staticmethod
    def set_up_blank_test_scenario(app):
        app.prestige = 7
        app.troops = 9
        app.funding = 5
        app.cells = 11
