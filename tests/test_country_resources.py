from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class CountryResources(LabyrinthTestCase):
    """Test countryResources"""

    def test_country_resources(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.countryResources("Iraq") == 3)
        self.assertTrue(app.countryResources("Egypt") == 3)
        self.assertTrue(app.countryResources("Syria") == 2)
        self.assertTrue(app.countryResources("Lebanon") == 1)
        app.lapsing.append("Oil Price Spike")
        self.assertTrue(app.countryResources("Iraq") == 4)
        self.assertTrue(app.countryResources("Egypt") == 3)
        self.assertTrue(app.countryResources("Syria") == 2)
        self.assertTrue(app.countryResources("Lebanon") == 1)
        app.lapsing.append("Biometrics")
        app.lapsing.append("Oil Price Spike")
        self.assertTrue(app.countryResources("Iraq") == 5)
        self.assertTrue(app.countryResources("Egypt") == 3)
        self.assertTrue(app.countryResources("Syria") == 2)
        self.assertTrue(app.countryResources("Lebanon") == 1)