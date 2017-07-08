from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class AdjustCountryPosture(LabyrinthTestCase):
    """Tests the 'adjustCountryPosture' method"""

    def test_accepts_mixed_case_input(self):
        self._assert_adjust_posture("Hard", "Hard")

    def test_accepts_lower_case_input(self):
        self._assert_adjust_posture("hard", "Hard")

    def test_accepts_upper_case_input(self):
        self._assert_adjust_posture("HARD", "Hard")

    def test_set_soft_posture(self):
        self._assert_adjust_posture("soft", "Soft")

    def test_set_untested_posture(self):
        self._assert_adjust_posture("UNTESTED", "")

    def test_set_no_posture(self):
        self._assert_adjust_posture("bad input lalala", "", False)

    def _assert_adjust_posture(self, user_input, expected_posture, expected_successful=True):
        # Set up
        non_muslim_country = "France"  # Only these have a posture
        app = Labyrinth(1, 1, self.set_up_test_scenario, test_user_input=[user_input])
        self.assertEqual(app.map[non_muslim_country].posture, "")  # means "Untested"

        # Invoke
        successful = app.adjustCountryPosture(non_muslim_country)

        # Check
        self.assertEqual(successful, expected_successful)
        self.assertEqual(app.map[non_muslim_country].posture, expected_posture)
