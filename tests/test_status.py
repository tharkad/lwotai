from lwotai import Labyrinth
from labyrinth_test_case import LabyrinthTestCase


class StatusCommandTest(LabyrinthTestCase):
    """Tests the "status" command"""

    def test_status_of_blank_scenario(self):
        app = Labyrinth(1, 1, LabyrinthTestCase.set_up_blank_test_scenario)
        status = app.do_status(None)
        self.assertEqual(None, status)