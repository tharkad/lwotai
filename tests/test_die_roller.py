from labyrinth_test_case import LabyrinthTestCase
from lwotai import DieRoller


class DieRollerTest(LabyrinthTestCase):

    def test_rolls_correct_number_of_times(self):
        roller = DieRoller()
        times = 5
        results = roller.roll(times)
        self.assertEqual(len(results), times)

    def test_rolls_are_within_correct_range(self):
        roller = DieRoller()
        results = roller.roll(1000)
        for roll in results:
            self.assertTrue(1 <= roll <= 6)