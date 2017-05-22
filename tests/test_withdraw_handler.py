from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class WithdrawHandlerTest(LabyrinthTestCase):
    """Test Withdraw"""

    def test_withdraw(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario_2)
        app.map["United States"].posture = "Soft"
        self.assertTrue(app.map["Afghanistan"].is_good())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 6)
        self.assertEqual(app.map["Afghanistan"].aid, 1)
        self.assertEqual(app.map["Afghanistan"].besieged, 0)
        self.assertEqual(app.map["Saudi Arabia"].troops(), 2)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 3)
        prestigeRolls = (5, 2, 5)
        app.handleWithdraw("Afghanistan", "Saudi Arabia", 4, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_good())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 2)
        self.assertEqual(app.map["Afghanistan"].aid, 0)
        self.assertEqual(app.map["Afghanistan"].besieged, 1)
        self.assertEqual(app.map["Saudi Arabia"].troops(), 6)
        self.assertEqual(app.prestige, 9)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, self.set_up_test_scenario_2)
        app.map["United States"].posture = "Soft"
        self.assertTrue(app.map["Afghanistan"].is_good())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 6)
        self.assertEqual(app.map["Afghanistan"].aid, 1)
        self.assertEqual(app.map["Afghanistan"].besieged, 0)
        self.assertEqual(app.map["Saudi Arabia"].troops(), 2)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 3)
        prestigeRolls = (2, 3, 5)
        app.handleWithdraw("Afghanistan", "track", 5, prestigeRolls)
        self.assertTrue(app.map["Afghanistan"].is_good())
        self.assertTrue(app.map["Afghanistan"].is_ally())
        self.assertEqual(app.map["Afghanistan"].troops(), 1)
        self.assertEqual(app.map["Afghanistan"].aid, 0)
        self.assertEqual(app.map["Afghanistan"].besieged, 1)
        self.assertEqual(app.map["Saudi Arabia"].troops(), 2)
        self.assertEqual(app.prestige, 4)
        self.assertEqual(app.troops, 8)