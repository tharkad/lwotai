from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth

class ScenarioTest(LabyrinthTestCase):
    """Scenarios"""

    def test_scenario_4(self):
        app = Labyrinth(4, 1)
        self.assertTrue(app.map["United Kingdom"].posture == "Hard")