from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class AlertHandlerTest(LabyrinthTestCase):
    """Test Alert"""

    def test_alert(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        self.assertEqual(app.map["Iraq"].plots, 2)
        app.handleAlert("Iraq")
        self.assertEqual(app.map["Iraq"].plots, 1)
        app.handleAlert("Iraq")
        self.assertEqual(app.map["Iraq"].plots, 0)
        app.handleAlert("Iraq")
        self.assertEqual(app.map["Iraq"].plots, 0)