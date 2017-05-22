from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class Map(LabyrinthTestCase):

    def testDeck(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        for country in app.map:
            for link in app.map[country].links:
                self.assertTrue(app.map[country] in link.links)