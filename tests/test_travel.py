from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth


class TravelTest(LabyrinthTestCase):
    """Test Travel"""

    def test_travel_first_box(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Gulf States"].besieged = 0
        app.map["Gulf States"].aid = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Gulf States"].aid = 0
        app.map["Gulf States"].regimeChange = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Gulf States"].make_islamist_rule()
        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Afghanistan"])

        app.map["Gulf States"].make_poor()
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Iraq"].make_poor()
        app.map["Iraq"].aid = 1
        iraqCount = 0
        gulfCount = 0
        for i in range(100):
            dest = app.travelDestinations(1)
            if dest == ["Gulf States"]:
                gulfCount += 1
            elif dest == ["Iraq"]:
                iraqCount += 1
            self.assertTrue(dest == ["Gulf States"] or dest == ["Iraq"])
        self.assertTrue(iraqCount > 0)
        self.assertTrue(gulfCount > 0)

        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].aid = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Pakistan"])

    def test_travel_second_box(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].troopCubes = 1
        app.map["Afghanistan"].sleeperCells = 4
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Afghanistan"])

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        dest = app.travelDestinations(2)
        self.assertEqual(dest, ["Gulf States", "Afghanistan"])

    def test_travel_third_box(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.map["Jordan"].make_fair()
        app.map["Iraq"].make_poor()
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Jordan"])

        app.map["Gulf States"].make_fair()
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Gulf States"].make_poor()
        app.map["Algeria/Tunisia"].make_fair()
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Jordan"])

        app.map["Germany"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Algeria/Tunisia"])

    def test_travel_fourth_box(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.map["United States"].posture = "Hard"

        app.map["Canada"].posture = "Hard"
        app.map["United Kingdom"].posture = "Hard"
        app.map["Serbia"].posture = "Hard"
        app.map["India"].posture = "Hard"
        app.map["Scandinavia"].posture = "Hard"
        app.map["Eastern Europe"].posture = "Hard"
        app.map["Benelux"].posture = "Hard"
        app.map["Germany"].posture = "Hard"
        app.map["France"].posture = "Hard"
        app.map["Italy"].posture = "Hard"
        app.map["Spain"].posture = "Hard"
        app.map["Russia"].posture = "Hard"
        app.map["Caucasus"].posture = "Hard"
        app.map["China"].posture = "Hard"
        app.map["Kenya/Tanzania"].posture = "Hard"
        app.map["Thailand"].posture = "Hard"
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Philippines"])

    def test_travel_multiple(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        dest = app.travelDestinations(3)

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].troopCubes = 1
        app.map["Afghanistan"].sleeperCells = 4
        dest = app.travelDestinations(2)
        self.assertEqual(dest, ["Gulf States", "Afghanistan"])

        app.map["Jordan"].make_fair()
        app.map["Iraq"].make_poor()
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Gulf States", "Afghanistan", "Jordan"])

        app.map["United States"].posture = "Hard"
        app.map["Canada"].posture = "Hard"
        app.map["United Kingdom"].posture = "Hard"
        app.map["Serbia"].posture = "Hard"
        app.map["India"].posture = "Hard"
        app.map["Scandinavia"].posture = "Hard"
        app.map["Eastern Europe"].posture = "Hard"
        app.map["Benelux"].posture = "Hard"
        app.map["Germany"].posture = "Hard"
        app.map["France"].posture = "Hard"
        app.map["Italy"].posture = "Hard"
        app.map["Spain"].posture = "Hard"
        app.map["Russia"].posture = "Hard"
        app.map["Caucasus"].posture = "Hard"
        app.map["China"].posture = "Hard"
        app.map["Kenya/Tanzania"].posture = "Hard"
        app.map["Thailand"].posture = "Hard"
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Gulf States", "Afghanistan", "Jordan"])

        app.map["Gulf States"].make_islamist_rule()
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Afghanistan", "Jordan", "Philippines"])

        app.map["Kenya/Tanzania"].posture = ""
        phCount = 0
        ktCount = 0
        for i in range(100):
            dest = app.travelDestinations(3)
            if dest == ["Afghanistan", "Jordan", "Philippines"]:
                phCount += 1
            elif dest == ["Afghanistan", "Jordan", "Kenya/Tanzania"]:
                ktCount += 1
            self.assertTrue(dest == ["Afghanistan", "Jordan", "Philippines"] or
                            dest == ["Afghanistan", "Jordan", "Kenya/Tanzania"])
        self.assertTrue(phCount > 0)
        self.assertTrue(ktCount > 0)

        app.map["United States"].posture = "Soft"
        app.map["China"].posture = "Soft"
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Afghanistan", "Jordan", "China"])

        app.map["Benelux"].posture = "Soft"
        chinaCount = 0
        beneluxCount = 0
        for i in range(100):
            dest = app.travelDestinations(3)
            if dest == ["Afghanistan", "Jordan", "China"]:
                chinaCount += 1
            elif dest == ["Afghanistan", "Jordan", "Benelux"]:
                beneluxCount += 1
            self.assertTrue(dest == ["Afghanistan", "Jordan", "China"] or dest == ["Afghanistan", "Jordan", "Benelux"])
        self.assertTrue(chinaCount > 0)
        self.assertTrue(beneluxCount > 0)

    def test_travel_from(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.map["Lebanon"].make_fair()
        app.map["Lebanon"].activeCells = 1
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Lebanon"])

        app.map["Iraq"].make_fair()
        app.map["Iraq"].activeCells = 1
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Iraq"])

        app.map["Egypt"].make_fair()
        app.map["Egypt"].activeCells = 1
        app.map["Egypt"].regimeChange = 1
        app.map["Egypt"].troopCubes = 2
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Iraq"])
        app.map["Egypt"].activeCells = 3
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Egypt"])

        app.map["Yemen"].make_islamist_rule()
        app.map["Yemen"].activeCells = 3
        app.map["Yemen"].troopCubes = 2
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Egypt"])
        sources = app.travelSources(dest, 2)
        self.assertEqual(sources, ["Yemen"])

        #multi

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1

        app.map["Afghanistan"].make_poor()
        app.map["Afghanistan"].troopCubes = 1
        app.map["Afghanistan"].sleeperCells = 4

        app.map["Jordan"].make_fair()
        app.map["Iraq"].make_poor()
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(3)
        self.assertEqual(dest, ["Gulf States", "Afghanistan", "Jordan"])

        app.map["Lebanon"].make_fair()
        app.map["Lebanon"].activeCells = 1

        app.map["Iraq"].make_fair()
        app.map["Iraq"].activeCells = 1

        app.map["Egypt"].make_fair()
        app.map["Egypt"].regimeChange = 1
        app.map["Egypt"].troopCubes = 2
        app.map["Egypt"].activeCells = 3

        app.map["Yemen"].make_islamist_rule()
        app.map["Yemen"].activeCells = 4
        app.map["Yemen"].troopCubes = 2
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Egypt", "Iraq"])

        app.map["Yemen"].activeCells = 5
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Yemen", "Egypt"])

        app.map["Yemen"].activeCells = 6
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Yemen", "Yemen"])

        app.map["Yemen"].activeCells = 4
        sources = app.travelSources(dest, 3)
        app.map["Egypt"].activeCells = 4
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Egypt", "Egypt"])

        app.map["Iraq"].make_fair()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].troopCubes = 2
        app.map["Iraq"].activeCells = 4
        app.map["Egypt"].activeCells = 0
        app.map["Egypt"].sleeperCells = 4
        sources = app.travelSources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Iraq", "Iraq"])