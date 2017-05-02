from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class CountryDistanceTest(LabyrinthTestCase):
    """Test countryDistance"""
    __app = None

    def setUp(self):
        self.__app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

    def assert_distance(self, from_country, to_country, expected_distance):
        self.assertEqual(self.__app.countryDistance(from_country, to_country), expected_distance)

    def test_distance(self):
        self.assert_distance("Iran", "Iran", 0)
        self.assert_distance("Iran", "Iraq", 1)
        self.assert_distance("Iran", "Sudan", 4)
        self.assert_distance("Thailand", "United States", 2)
        self.assert_distance("Russia", "Morocco", 2)