import unittest

from mockito import when, mock

from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth, Randomizer
from lwotai import POOR


class Card01(LabyrinthTestCase):
    """Backlash"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["1"].playable("US", app, True))
        app.map["Canada"].plots = 1
        self.assertFalse(app.deck["1"].playable("US", app, True))
        app.map["Iraq"].plots = 1
        self.assertTrue(app.deck["1"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.backlashInPlay)
        app.deck["1"].playEvent("US", app)
        self.assertFalse(app.backlashInPlay)
        app.map["United States"].plots = 1
        app.deck["1"].playEvent("US", app)
        self.assertFalse(app.backlashInPlay)
        app.map["Iraq"].plots = 1
        app.deck["1"].playEvent("US", app)
        self.assertTrue(app.backlashInPlay)


class Card02(LabyrinthTestCase):
    """Biometrics"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["2"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse("Biometrics" in app.lapsing)
        app.deck["2"].playEvent("US", app)
        self.assertTrue("Biometrics" in app.lapsing)
        app.do_turn("")
        self.assertFalse("Biometrics" in app.lapsing)

    def testTravelDestination(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.deck["2"].playEvent("US", app)
        dest = app.travelDestinations(1)
        self.assertTrue("Biometrics" in app.lapsing)
        self.assertEqual(dest, [])
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])

    def testTravelSource(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Gulf States"].make_poor()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.deck["2"].playEvent("US", app)
        dest = app.travelDestinations(1)
        self.assertEqual(dest, [])
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.map["Sudan"].make_islamist_rule()        
        app.map["Sudan"].sleeperCells = 4    
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Iraq"])

    def testTravelToGood(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Gulf States"].make_good()
        app.map["Gulf States"].besieged = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.deck["2"].playEvent("US", app)
        dest = app.travelDestinations(1)
        self.assertEqual(dest, [])
        app.map["Iraq"].sleeperCells = 1
        dest = app.travelDestinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.map["Sudan"].make_islamist_rule()        
        app.map["Sudan"].sleeperCells = 4    
        sources = app.travelSources(dest, 1)
        self.assertEqual(sources, ["Iraq"])
        app.handleTravel(1)


class Card03(LabyrinthTestCase):
    """CTR"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["3"].playable("US", app, True))
        app.do_reassessment("")
        self.assertTrue(app.deck["3"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.do_reassessment("")
        self.assertFalse("CTR" in app.map["Russia"].markers)
        self.assertFalse("CTR" in app.map["Central Asia"].markers)
        app.map["Central Asia"].make_adversary()
        app.deck["3"].playEvent("US", app)
        self.assertTrue("CTR" in app.map["Russia"].markers)
        self.assertFalse("CTR" in app.map["Central Asia"].markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.do_reassessment("")
        self.assertFalse("CTR" in app.map["Russia"].markers)
        self.assertFalse("CTR" in app.map["Central Asia"].markers)
        app.map["Central Asia"].make_neutral()
        app.deck["3"].playEvent("US", app)
        self.assertTrue("CTR" in app.map["Russia"].markers)
        self.assertTrue("CTR" in app.map["Central Asia"].markers)
        print app.map["Russia"].countryStr()
        self.assertTrue("Markers: CTR" in app.map["Russia"].countryStr())
        self.assertTrue("Markers: CTR" in app.map["Central Asia"].countryStr())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.do_reassessment("")
        self.assertFalse("CTR" in app.map["Russia"].markers)
        self.assertFalse("CTR" in app.map["Central Asia"].markers)
        app.map["Central Asia"].make_ally()
        app.deck["3"].playEvent("US", app)
        self.assertTrue("CTR" in app.map["Russia"].markers)
        self.assertTrue("CTR" in app.map["Central Asia"].markers)


class Card04(LabyrinthTestCase):
    """Moro Talks"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["4"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.map["Philippines"].posture == "")
        self.assertTrue(app.funding == 5)
        app.deck["4"].playEvent("US", app)
        self.assertTrue("Moro Talks" in app.markers)
        self.assertTrue(app.map["Philippines"].posture == "Soft" or app.map["Philippines"].posture == "Hard")
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 1
        self.assertTrue(app.map["Philippines"].posture == "")
        self.assertTrue(app.funding == 1)
        app.deck["4"].playEvent("US", app)
        self.assertTrue(app.map["Philippines"].posture == "Soft" or app.map["Philippines"].posture == "Hard")
        self.assertTrue(app.funding == 1)


class Card05(LabyrinthTestCase):
    """NEST"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["5"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse("NEST" in app.markers)
        app.deck["5"].playEvent("US", app)
        self.assertTrue("NEST" in app.markers)


class Card06and07(LabyrinthTestCase):
    """Sanctions"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["6"].playable("US", app, True))
        self.assertFalse(app.deck["7"].playable("US", app, True))
        app.markers.append("Patriot Act")
        self.assertTrue(app.deck["6"].playable("US", app, True))
        self.assertTrue(app.deck["7"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.markers.append("Patriot Act")
        app.deck["6"].playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.markers.append("Patriot Act")
        app.deck["7"].playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 2
        app.markers.append("Patriot Act")
        app.deck["6"].playEvent("US", app)
        self.assertTrue(app.funding == 1)


class Card08and09and10(LabyrinthTestCase):
    """Special Forces"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["8"].playable("US", app, True))
        self.assertFalse(app.deck["9"].playable("US", app, True))
        self.assertFalse(app.deck["10"].playable("US", app, True))
        app.map["Iran"].sleeperCells = 1
        self.assertFalse(app.deck["8"].playable("US", app, True))
        self.assertFalse(app.deck["9"].playable("US", app, True))
        self.assertFalse(app.deck["10"].playable("US", app, True))
        app.map["Iran"].troopCubes = 1
        self.assertTrue(app.deck["8"].playable("US", app, True))
        self.assertTrue(app.deck["9"].playable("US", app, True))
        self.assertTrue(app.deck["10"].playable("US", app, True))
        app.map["Iran"].troopCubes = 0
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["8"].playable("US", app, True))
        self.assertTrue(app.deck["9"].playable("US", app, True))
        self.assertTrue(app.deck["10"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.listCountriesWithCellAndAdjacentTroops()
        app.map["Iran"].sleeperCells = 1
        app.map["Iraq"].troopCubes = 1
        app.listCountriesWithCellAndAdjacentTroops()


class Card11(LabyrinthTestCase):
    """Abbas"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["11"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.funding == 3)
        self.assertTrue("Abbas" in app.markers)
        app.map["Israel"].plots = 1
        app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Syria")
        app.map["Syria"].make_islamist_rule()
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.funding == 3)
        self.assertTrue("Abbas" in app.markers)
        app.map["Israel"].plots = 1
        app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Lebanon")
        app.map["Lebanon"].make_islamist_rule()
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 7)
        self.assertTrue(app.funding == 5)
        self.assertTrue("Abbas" in app.markers)
        app.map["Israel"].plots = 1
        app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 4
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 7)
        self.assertTrue(app.funding == 5)
        self.assertTrue("Abbas" in app.markers)
        app.map["Israel"].plots = 1
        app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 12
        app.funding = 2
        app.deck["11"].playEvent("US", app)
        self.assertTrue(app.prestige == 12)
        self.assertTrue(app.funding == 1)


class Card12(LabyrinthTestCase):
    """Al-Azhar"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["12"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.map["Egypt"].is_ungoverned())
        app.deck["12"].playEvent("US", app)
        self.assertTrue(app.map["Egypt"].is_governed())
        self.assertTrue(app.funding == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.map["Egypt"].is_ungoverned())
        app.map["Pakistan"].make_islamist_rule()
        app.deck["12"].playEvent("US", app)
        self.assertTrue(app.map["Egypt"].is_governed())
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 2
        self.assertTrue(app.map["Egypt"].is_ungoverned())
        app.deck["12"].playEvent("US", app)
        self.assertTrue(app.map["Egypt"].is_governed())
        self.assertTrue(app.funding == 1)


class Card13(LabyrinthTestCase):
    """Anbar Awakening"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["13"].playable("US", app, True))
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["13"].playable("US", app, True))
        app.map["Iraq"].troopCubes = 0
        app.map["Syria"].troopCubes = 1
        self.assertTrue(app.deck["13"].playable("US", app, True))
        app.map["Syria"].troopCubes = 0
        self.assertFalse(app.deck["13"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].troopCubes = 1
        app.deck["13"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].aid > 0)
        self.assertTrue("Anbar Awakening" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Syria"].troopCubes = 1
        app.deck["13"].playEvent("US", app)
        self.assertTrue(app.map["Syria"].aid > 0)
        self.assertTrue("Anbar Awakening" in app.markers)


class Card14(LabyrinthTestCase):
    """Covert Action"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["14"].playable("US", app, True))
        app.map["Iraq"].make_adversary()
        self.assertTrue(app.deck["14"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.listAdversaryCountries()
        app.map["Iran"].make_adversary()
        app.map["Iraq"].make_adversary()
        app.listAdversaryCountries()


class Card15(LabyrinthTestCase):
    """Ethiopia Strikes"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["15"].playable("US", app, True))
        app.map["Somalia"].make_islamist_rule()
        self.assertTrue(app.deck["15"].playable("US", app, True))
        app.map["Somalia"].make_poor()
        self.assertFalse(app.deck["15"].playable("US", app, True))
        app.map["Sudan"].make_islamist_rule()
        self.assertTrue(app.deck["15"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Somalia"].make_islamist_rule()
        app.map["Somalia"].make_adversary()
        app.deck["15"].playEvent("US", app)
        self.assertTrue(app.map["Somalia"].is_poor())
        self.assertTrue(app.map["Somalia"].is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Sudan"].make_islamist_rule()
        app.map["Sudan"].make_adversary()
        app.deck["15"].playEvent("US", app)
        self.assertTrue(app.map["Sudan"].is_poor())
        self.assertTrue(app.map["Sudan"].is_neutral())


class Card16(LabyrinthTestCase):
    """Euro-Islam"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["16"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.executeCardEuroIslam("Hard")
        self.assertTrue(app.map["Benelux"].posture == "Hard")
        self.assertTrue(app.funding == 4)
        app.map["Iraq"].make_islamist_rule()
        app.executeCardEuroIslam("Soft")
        self.assertTrue(app.map["Benelux"].posture == "Soft")
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 1
        app.executeCardEuroIslam("Hard")
        self.assertTrue(app.map["Benelux"].posture == "Hard")
        self.assertTrue(app.funding == 1)


class Card17(LabyrinthTestCase):
    """FSB"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["17"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ['y'])
        app.map["Central Asia"].activeCells = 1
        app.map["Russia"].activeCells = 1
        app.deck["17"].playEvent("US", app)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ['y'])
        app.map["Russia"].activeCells = 1
        app.deck["17"].playEvent("US", app)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ['y'])
        app.map["Central Asia"].sleeperCells = 1
        app.deck["17"].playEvent("US", app)


class Card18(LabyrinthTestCase):
    """Intel Community"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["18"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        history_before = len(app.history)
        app.deck["18"].playEvent("US", app)
        self.assert_new_messages(app, history_before, [
            'Card played for Event.',
            'Examine Jihadist hand. Do not change order of cards.',
            'Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi).',
            'You may now interrupt this action phase to play another card (Use the u command).'
        ])


class Card19(LabyrinthTestCase):
    """Kemalist Republic"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["19"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["19"].playEvent("US", app)
        self.assertTrue(app.map["Turkey"].is_fair())
        self.assertTrue(app.map["Turkey"].is_ally())


class Card20(LabyrinthTestCase):
    """King Abdullah"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["20"].playable("US", app, True))
        self.assertTrue(app.funding == 5)
        self.assertTrue(app.prestige == 7)

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["20"].playEvent("US", app)
        self.assertTrue(app.map["Jordan"].is_fair())
        self.assertTrue(app.map["Jordan"].is_ally())
        self.assertTrue(app.funding == 4)
        self.assertTrue(app.prestige == 8)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 1
        app.prestige = 12
        app.deck["20"].playEvent("US", app)
        self.assertTrue(app.map["Jordan"].is_fair())
        self.assertTrue(app.map["Jordan"].is_ally())
        self.assertTrue(app.funding == 1)
        self.assertTrue(app.prestige == 12)


class Card21(LabyrinthTestCase):
    """Let's Roll"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["21"].playable("US", app, True))
        app.map["Canada"].plots = 1
        self.assertTrue(app.deck["21"].playable("US", app, True))
        app.map["Canada"].plots = 0
        self.assertFalse(app.deck["21"].playable("US", app, True))
        app.map["Saudi Arabia"].make_fair()
        app.map["Saudi Arabia"].plots = 1
        self.assertFalse(app.deck["21"].playable("US", app, True))
        app.map["Saudi Arabia"].make_good()
        self.assertTrue(app.deck["21"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Canada"].plots = 1
        app.map["Spain"].posture = "Soft"
        app.executeCardLetsRoll("Canada", "Spain", "Hard")
        self.assertTrue(app.map["Canada"].plots == 0)
        self.assertTrue(app.map["Spain"].posture == "Hard")

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Saudi Arabi", "Spain", "h"])
        app.map["Spain"].posture = "Soft"
        app.map["Saudi Arabia"].make_good()
        app.map["Saudi Arabia"].plots = 1
        app.deck["21"].playEvent("US", app)
        self.assertTrue(app.map["Spain"].posture == "Hard")
        self.assertTrue(app.map["Saudi Arabia"].plots == 0)


class Card22(LabyrinthTestCase):
    """Mossad and Shin Bet"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["22"].playable("US", app, True))
        app.map["Israel"].sleeperCells = 1
        self.assertTrue(app.deck["22"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["22"].playable("US", app, True))
        app.map["Jordan"].sleeperCells = 1
        self.assertTrue(app.deck["22"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["22"].playable("US", app, True))
        app.map["Lebanon"].sleeperCells = 1
        self.assertTrue(app.deck["22"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Israel"].sleeperCells = 1
        app.map["Israel"].activeCells = 4
        app.map["Jordan"].activeCells = 3
        app.map["Lebanon"].sleeperCells = 2
        app.map["Iraq"].sleeperCells = 2
        app.deck["22"].playEvent("US", app)
        self.assertTrue(app.map["Israel"].sleeperCells == 0)
        self.assertTrue(app.map["Israel"].activeCells == 0)
        self.assertTrue(app.map["Jordan"].sleeperCells == 0)
        self.assertTrue(app.map["Jordan"].activeCells == 0)
        self.assertTrue(app.map["Lebanon"].sleeperCells == 0)
        self.assertTrue(app.map["Lebanon"].activeCells == 0)
        self.assertTrue(app.map["Iraq"].sleeperCells == 2)


class Card23and24and25(LabyrinthTestCase):
    """Predator"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["23"].playable("US", app, True))
        app.map["Israel"].sleeperCells = 1
        self.assertFalse(app.deck["23"].playable("US", app, True))
        app.map["Iran"].sleeperCells = 1
        self.assertFalse(app.deck["23"].playable("US", app, True))
        app.map["Jordan"].sleeperCells = 1
        self.assertTrue(app.deck["23"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["24"].playable("US", app, True))
        app.map["Israel"].sleeperCells = 1
        self.assertFalse(app.deck["24"].playable("US", app, True))
        app.map["Iran"].sleeperCells = 1
        self.assertFalse(app.deck["24"].playable("US", app, True))
        app.map["Jordan"].sleeperCells = 1
        self.assertTrue(app.deck["24"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["25"].playable("US", app, True))
        app.map["Israel"].sleeperCells = 1
        self.assertFalse(app.deck["25"].playable("US", app, True))
        app.map["Iran"].sleeperCells = 1
        self.assertFalse(app.deck["25"].playable("US", app, True))
        app.map["Jordan"].sleeperCells = 1
        self.assertTrue(app.deck["25"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.map["Iraq"].sleeperCells = 2
        app.deck["25"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].sleeperCells == 1)


class Card26(LabyrinthTestCase):
    """Quartet"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["26"].playable("US", app, True))
        app.markers.append("Abbas")
        self.assertTrue(app.deck["26"].playable("US", app, True))
        app.troops = 4
        self.assertFalse(app.deck["26"].playable("US", app, True))
        app.troops = 5
        self.assertTrue(app.deck["26"].playable("US", app, True))
        app.map["Egypt"].make_islamist_rule()
        self.assertFalse(app.deck["26"].playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.markers.append("Abbas")
        app.deck["26"].playEvent("US", app)
        self.assertTrue(app.prestige == 9)
        self.assertTrue(app.funding == 2)


class Card27(LabyrinthTestCase):
    """Saddam Captured"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["27"].playable("US", app, True))
        app.map["Iraq"].troopCubes = 1
        self.assertTrue(app.deck["27"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].troopCubes = 1
        app.deck["27"].playEvent("US", app)
        self.assertTrue("Saddam Captured" in app.markers)
        self.assertTrue(app.map["Iraq"].aid == 1)


class Card28(LabyrinthTestCase):
    """Sharia"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["28"].playable("US", app, True))
        app.map["Iraq"].besieged = 1
        self.assertTrue(app.deck["28"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].besieged = 1
        app.deck["28"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].besieged == 0)


class Card29(LabyrinthTestCase):
    """Tony Blair"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["29"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].posture = "Hard"

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].posture = "Hard"
        app.executeNonMuslimWOI("Spain", 4)
        self.assertTrue(app.map["Spain"].posture == "Soft")
        app.executeNonMuslimWOI("France", 5)
        self.assertTrue(app.map["France"].posture == "Hard")


class Card30(LabyrinthTestCase):
    """UN Nation Building"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["30"].playable("US", app, True))
        app.map["Iraq"].regimeChange = 1
        self.assertTrue(app.deck["30"].playable("US", app, True))
        app.markers.append("Vieira de Mello Slain")
        self.assertFalse(app.deck["30"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["6"])
        app.map["United States"].posture = "Hard"
        app.map["Spain"].posture = "Soft"
        app.map["France"].posture = "Soft"
        app.map["Germany"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        # app.map["Iraq"].regimeChange = 1
        app.map["Pakistan"].regimeChange = 1
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_ally()
        app.deck["30"].playEvent("US", app)
        self.assertTrue(app.map["Pakistan"].aid == 1)
        self.assertTrue(app.map["Pakistan"].is_fair())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq", "6"])
        app.map["United States"].posture = "Hard"
        app.map["Spain"].posture = "Soft"
        app.map["France"].posture = "Soft"
        app.map["Germany"].posture = "Soft"
        app.map["Canada"].posture = "Soft"
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_ally()
        app.map["Pakistan"].regimeChange = 1
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_ally()
        app.deck["30"].playEvent("US", app)
        self.assertTrue(app.map["Pakistan"].aid == 0)
        self.assertTrue(app.map["Pakistan"].is_poor())
        self.assertTrue(app.map["Iraq"].aid == 1)
        self.assertTrue(app.map["Iraq"].is_fair())


class Card31(LabyrinthTestCase):
    """Wiretapping"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["31"].playable("US", app, True))
        app.map["United States"].sleeperCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].activeCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].cadre = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].plots = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["31"].playable("US", app, True))
        app.map["United Kingdom"].sleeperCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United Kingdom"].activeCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United Kingdom"].cadre = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United Kingdom"].plots = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["31"].playable("US", app, True))
        app.map["Canada"].sleeperCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Canada"].activeCells = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Canada"].cadre = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Canada"].plots = 1
        self.assertTrue(app.deck["31"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Canada"].plots = 1
        app.markers.append("Leak-Wiretapping")
        self.assertFalse(app.deck["31"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 1
        app.map["United States"].activeCells = 1
        app.map["United States"].cadre = 1
        app.map["United States"].plots = 1
        app.map["United Kingdom"].sleeperCells = 1
        app.map["United Kingdom"].activeCells = 1
        app.map["United Kingdom"].cadre = 1
        app.map["United Kingdom"].plots = 1
        app.map["Canada"].sleeperCells = 1
        app.map["Canada"].activeCells = 1
        app.map["Canada"].cadre = 1
        app.map["Canada"].plots = 1
        app.deck["31"].playEvent("US", app)
        self.assertTrue("Wiretapping" in app.markers)
        self.assertTrue(app.map["United States"].sleeperCells == 0)
        self.assertTrue(app.map["United States"].activeCells == 0)
        self.assertTrue(app.map["United States"].cadre == 0)
        self.assertTrue(app.map["United States"].plots == 0)
        self.assertTrue(app.map["United Kingdom"].sleeperCells == 0)
        self.assertTrue(app.map["United Kingdom"].activeCells == 0)
        self.assertTrue(app.map["United Kingdom"].cadre == 0)
        self.assertTrue(app.map["United Kingdom"].plots == 0)
        self.assertTrue(app.map["Canada"].sleeperCells == 0)
        self.assertTrue(app.map["Canada"].activeCells == 0)
        self.assertTrue(app.map["Canada"].cadre == 0)
        self.assertTrue(app.map["Canada"].plots == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].sleeperCells = 1
        app.map["United States"].activeCells = 1
        app.map["United States"].cadre = 1
        app.map["United States"].plots = 1
        app.map["Canada"].sleeperCells = 1
        app.map["Canada"].activeCells = 1
        app.map["Canada"].cadre = 1
        app.map["Canada"].plots = 1
        app.deck["31"].playEvent("US", app)
        self.assertTrue("Wiretapping" in app.markers)
        self.assertTrue(app.map["United States"].sleeperCells == 0)
        self.assertTrue(app.map["United States"].activeCells == 0)
        self.assertTrue(app.map["United States"].cadre == 0)
        self.assertTrue(app.map["United States"].plots == 0)
        self.assertTrue(app.map["United Kingdom"].sleeperCells == 0)
        self.assertTrue(app.map["United Kingdom"].activeCells == 0)
        self.assertTrue(app.map["United Kingdom"].cadre == 0)
        self.assertTrue(app.map["United Kingdom"].plots == 0)
        self.assertTrue(app.map["Canada"].sleeperCells == 0)
        self.assertTrue(app.map["Canada"].activeCells == 0)
        self.assertTrue(app.map["Canada"].cadre == 0)
        self.assertTrue(app.map["Canada"].plots == 0)


class Card32(LabyrinthTestCase):
    """Back Channel"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y", "n"])
        app.map["United States"].posture = "Hard"
        self.assertFalse(app.deck["32"].playable("US", app, True))
        app.map["United States"].posture = "Soft"
        self.assertFalse(app.deck["32"].playable("US", app, True))

        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        app.map["Pakistan"].make_adversary()
        print "Say yes"
        self.assertTrue(app.deck["32"].playable("US", app, True))
        print "Say no"
        self.assertFalse(app.deck["32"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y", "y", "Pakistan"])
        app.map["United States"].posture = "Soft"
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        app.map["Pakistan"].make_islamist_rule()
        app.map["Pakistan"].make_adversary()
        self.assertTrue(app.deck["32"].playable("US", app, True))
        aid_before = app.map["Pakistan"].aid
        app.deck["32"].playEvent("US", app)
        aid_after = app.map["Pakistan"].aid
        self.assertTrue(app.map["Iraq"].is_adversary())
        self.assertTrue(app.map["Pakistan"].is_neutral())
        self.assertEqual(aid_after, aid_before + 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "n"])
        app.map["United States"].posture = "Soft"
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        app.map["Pakistan"].make_islamist_rule()
        app.map["Pakistan"].make_adversary()
        self.assertFalse(app.deck["32"].playable("US", app, True))
        app.deck["32"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_adversary())
        self.assertTrue(app.map["Pakistan"].is_adversary())


class Card33(LabyrinthTestCase):
    """Benazir Bhutto"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["33"].playable("US", app, True))
        app.markers.append("Bhutto Shot")
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["33"].playable("US", app, True))
        app.map["Pakistan"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Afghanistan"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["India"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Gulf States"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Indonesia/Malaysia"].make_islamist_rule()
        self.assertFalse(app.deck["33"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Pakistan"].make_poor()
        app.deck["33"].playEvent("US", app)
        self.assertTrue(app.map["Pakistan"].is_fair())

        # no jihad in Pakistan
        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        app.map["Gulf States"].activeCells = 0
        app.map["Gulf States"].sleeperCells = 0
        app.map["Pakistan"].activeCells = 0
        self.assertEqual(app.minorJihadInGoodFairChoice(1), False)
        app.map["Pakistan"].make_fair()
        app.map["Pakistan"].activeCells = 1
        self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Pakistan", 1)])
        app.deck["33"].playEvent("US", app)
        self.assertEqual(app.minorJihadInGoodFairChoice(1), False)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertEqual(app.majorJihadPossible(3), [])
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].activeCells = 5
        self.assertEqual(app.majorJihadPossible(3), ["Pakistan"])
        app.deck["33"].playEvent("US", app)
        self.assertEqual(app.majorJihadPossible(3), [])

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].activeCells = 5
        app.map["Iraq"].make_poor()
        app.map["Iraq"].activeCells = 5
        self.assertEqual(app.majorJihadChoice(3), "Pakistan")
        app.deck["33"].playEvent("US", app)
        self.assertEqual(app.majorJihadPossible(3), ["Iraq"])


class Card34(LabyrinthTestCase):
    """Enhanced Measures"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["34"].playable("US", app, True))
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        self.assertTrue(app.deck["34"].playable("US", app, True))
        app.markers.append("Leak-Enhanced Measures")
        self.assertFalse(app.deck["34"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["United States"].posture = "Soft"
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        self.assertFalse(app.deck["34"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        app.map["Pakistan"].cadre = 1
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].troopCubes = 2
        app.deck["34"].playEvent("US", app)
        self.assertTrue("Enhanced Measures" in app.markers)
        self.assertTrue(app.map["Pakistan"].cadre == 1)
        self.assertTrue(app.map["Iraq"].cadre == 0)


class Card35(LabyrinthTestCase):
    """Hajib"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["35"].playable("US", app, True))
        app.map["Iraq"].make_islamist_rule()
        self.assertFalse(app.deck["35"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["h"])
        app.deck["35"].playEvent("US", app)
        self.assertTrue(app.map["Turkey"].governance_is_better_than(POOR))
        self.assertTrue(app.map["Turkey"].is_governed())
        self.assertTrue(not app.map["Turkey"].is_unaligned())
        print "Say Hard"
        self.assertTrue(app.map["France"].posture == "Hard")
        self.assertTrue(app.funding == 3)


class Card36(LabyrinthTestCase):
    """Indo-Pakistani Talks"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["36"].playable("US", app, True))
        app.map["Pakistan"].make_islamist_rule()
        self.assertFalse(app.deck["36"].playable("US", app, True))
        app.map["Pakistan"].make_poor()
        self.assertFalse(app.deck["36"].playable("US", app, True))
        app.map["Pakistan"].make_fair()
        self.assertTrue(app.deck["36"].playable("US", app, True))
        app.map["Pakistan"].make_good()
        self.assertTrue(app.deck["36"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["s", "1"])
        app.map["Pakistan"].make_fair()
        app.map["Pakistan"].make_adversary()
        app.deck["36"].playEvent("US", app)
        self.assertTrue(app.map["Pakistan"].is_ally())
        self.assertTrue("Indo-Pakistani Talks" in app.markers)
        self.assertTrue(app.map["India"].posture == "Soft")
        app.map["India"].plots = 1
        app.do_plot("")
        self.assertFalse("Indo-Pakistani Talks" in app.markers)


class Card37(LabyrinthTestCase):
    """Iraqi WMD"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["37"].playable("US", app, True))
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_adversary()
        self.assertTrue(app.deck["37"].playable("US", app, True))
        app.map["United States"].posture = "Soft"
        self.assertFalse(app.deck["37"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["37"].playEvent("US", app)
        self.assertTrue("Iraqi WMD" in app.markers)
        app.handleRegimeChange("Iraq", "track", 6, 4, (4, 4, 4))
        self.assertFalse("Iraqi WMD" in app.markers)


class Card38(LabyrinthTestCase):
    """Libyan Desl"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["38"].playable("US", app, True))
        app.map["Libya"].make_poor()
        self.assertFalse(app.deck["38"].playable("US", app, True))
        app.map["Iraq"].make_ally()
        self.assertTrue(app.deck["38"].playable("US", app, True))
        app.map["Iraq"].make_neutral()
        self.assertFalse(app.deck["38"].playable("US", app, True))
        app.map["Syria"].make_ally()
        self.assertTrue(app.deck["38"].playable("US", app, True))
        app.map["Libya"].make_fair()
        self.assertFalse(app.deck["38"].playable("US", app, True))
        app.map["Libya"].make_islamist_rule()
        self.assertFalse(app.deck["38"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["france", "s", "Spain", "h"])
        app.map["Libya"].make_poor()
        app.map["Iraq"].make_ally()
        app.deck["38"].playEvent("US", app)
        self.assertTrue("Libyan Deal" in app.markers)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.map["France"].posture == "Soft")
        self.assertTrue(app.map["Spain"].posture == "Hard")


class Card39(LabyrinthTestCase):
    """Libyan WMD"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["39"].playable("US", app, True))
        app.map["Libya"].make_poor()
        app.map["Libya"].make_adversary()
        self.assertTrue(app.deck["39"].playable("US", app, True))
        app.map["United States"].posture = "Soft"
        self.assertFalse(app.deck["39"].playable("US", app, True))
        app.map["United States"].posture = "Hard"
        self.assertTrue(app.deck["39"].playable("US", app, True))
        app.markers.append("Libyan Deal")
        self.assertFalse(app.deck["39"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["39"].playEvent("US", app)
        self.assertTrue("Libyan WMD" in app.markers)
        app.handleRegimeChange("Libya", "track", 6, 4, (4, 4, 4))
        self.assertFalse("Libyan WMD" in app.markers)


class Card40(LabyrinthTestCase):
    """Mass Turnout"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["40"].playable("US", app, True))
        app.map["Libya"].make_poor()
        app.map["Libya"].make_adversary()
        self.assertFalse(app.deck["40"].playable("US", app, True))
        app.map["Libya"].regimeChange = 1
        self.assertTrue(app.deck["40"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Libya"].make_poor()
        app.map["Libya"].make_adversary()
        app.map["Libya"].regimeChange = 1
        app.deck["40"].playEvent("US", app)
        self.assertTrue(app.map["Libya"].is_fair())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Libya"].make_fair()
        app.map["Libya"].make_adversary()
        app.map["Libya"].regimeChange = 1
        app.map["Libya"].aid = 1
        app.deck["40"].playEvent("US", app)
        self.assertTrue(app.map["Libya"].is_good())
        self.assertTrue(app.map["Libya"].regimeChange == 0)
        self.assertTrue(app.map["Libya"].aid == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.map["Libya"].make_fair()
        app.map["Libya"].make_adversary()
        app.map["Libya"].regimeChange = 1
        app.map["Libya"].aid = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_adversary()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].aid = 1
        app.deck["40"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_good())
        self.assertTrue(app.map["Iraq"].regimeChange == 0)
        self.assertTrue(app.map["Iraq"].aid == 0)


class Card41(LabyrinthTestCase):
    """NATO"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["41"].playable("US", app, True))
        app.map["Libya"].make_poor()
        app.map["Libya"].make_ally()
        app.map["Libya"].regimeChange = 1
        self.assertTrue(app.deck["41"].playable("US", app, True))
        app.map["Canada"].posture = "Soft"
        self.assertTrue(app.deck["41"].playable("US", app, True))
        app.map["Spain"].posture = "Soft"
        self.assertFalse(app.deck["41"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Libya", "track", "3"])
        app.map["Libya"].make_poor()
        app.map["Libya"].make_ally()
        app.map["Libya"].regimeChange = 1
        app.map["Libya"].changeTroops(2)
        app.deck["41"].playEvent("US", app)
        self.assertTrue(app.map["Libya"].aid == 1)
        self.assertTrue(app.map["Libya"].troops() == 4)
        self.assertTrue("NATO" in app.map["Libya"].markers)

        app.map["Libya"].regimeChange = 0
        print "Deploy 3 from Libya to track:"
        app.do_deploy("")
        self.assertTrue(app.map["Libya"].troops() == 0)
        self.assertTrue("NATO" not in app.map["Libya"].markers)        

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.map["Libya"].make_fair()
        app.map["Libya"].make_adversary()
        app.map["Libya"].regimeChange = 1
        app.map["Libya"].aid = 1
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_adversary()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].aid = 0
        app.deck["41"].playEvent("US", app)
        self.assertEqual(app.map["Iraq"].aid, 1)
        self.assertTrue(app.map["Iraq"].troops() == 2)
        self.assertTrue("NATO" in app.map["Iraq"].markers)


class Card42(LabyrinthTestCase):
    """Pakistani Offensive"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["42"].playable("US", app, True))
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_ally()
        self.assertFalse(app.deck["42"].playable("US", app, True))
        app.map["Pakistan"].markers.append("FATA")
        self.assertTrue(app.deck["42"].playable("US", app, True))
        app.map["Pakistan"].make_neutral()
        self.assertFalse(app.deck["42"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_ally()
        app.map["Pakistan"].markers.append("FATA")
        app.deck["42"].playEvent("US", app)
        self.assertTrue("FATA" not in app.map["Pakistan"].markers)


class Card43(LabyrinthTestCase):
    """Patriot Act"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["43"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.isAdjacent("United States", "Canada"))
        self.assertTrue(app.isAdjacent("United States", "United Kingdom"))
        self.assertTrue(app.isAdjacent("United States", "Philippines"))
        for country in app.map:
            if app.map[country].schengen:
                self.assertTrue(app.isAdjacent("United States", country))
        app.deck["43"].playEvent("US", app)
        self.assertTrue("Patriot Act" in app.markers)
        self.assertTrue(app.isAdjacent("United States", "Canada"))
        self.assertFalse(app.isAdjacent("United States", "United Kingdom"))
        self.assertFalse(app.isAdjacent("United States", "Philippines"))
        for country in app.map:
            if app.map[country].schengen:
                self.assertFalse(app.isAdjacent("United States", country))


class Card44(LabyrinthTestCase):
    """Renditions"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["44"].playable("US", app, True))
        app.map["United States"].posture = "Soft"
        self.assertFalse(app.deck["44"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["44"].playable("US", app, True))
        app.markers.append("Leak-Renditions")
        self.assertFalse(app.deck["44"].playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        app.map["Pakistan"].cadre = 1
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].troopCubes = 2
        app.deck["44"].playEvent("US", app)
        self.assertTrue("Renditions" in app.markers)
        self.assertTrue(app.map["Iraq"].cadre == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Pakistan"])
        app.map["Iraq"].cadre = 1
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_neutral()
        app.map["Iraq"].troopCubes = 2
        app.map["Pakistan"].cadre = 1
        app.map["Pakistan"].sleeperCells = 2
        app.map["Pakistan"].make_poor()
        app.map["Pakistan"].make_neutral()
        app.map["Pakistan"].troopCubes = 2
        app.deck["44"].playEvent("US", app)
        self.assertTrue("Renditions" in app.markers)
        self.assertTrue(app.map["Pakistan"].cadre == 1)
        self.assertTrue(app.map["Pakistan"].sleeperCells == 0)


class Card45(LabyrinthTestCase):
    """Safer Now"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].make_islamist_rule()
        app.map["Iraq"].make_adversary()
        self.assertFalse(app.deck["45"].playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].make_good()
        app.map["Iraq"].make_ally()
        self.assertTrue(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].cadre = 1
        self.assertTrue(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].plots = 1
        self.assertFalse(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].plots = 0
        app.map["Iraq"].cadre = 0
        app.map["Iraq"].sleeperCells = 1
        self.assertFalse(app.deck["45"].playable("US", app, True))
        app.map["Iraq"].sleeperCells = 0
        app.map["Iraq"].activeCells = 1
        self.assertFalse(app.deck["45"].playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["4", "Spain", "h"])
        print "Enter 4 for posture role, Spain and Hard"
        app.deck["45"].playEvent("US", app)
        self.assertTrue(app.map["United States"].posture == "Soft")
        self.assertTrue(app.prestige == 10)
        self.assertTrue(app.map["Spain"].posture == "Hard")


class Card46(LabyrinthTestCase):
    """Sistani"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_ally()
        app.map["Iraq"].regimeChange = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Iraq"].cadre = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Iraq"].sleeperCells = 1
        self.assertTrue(app.deck["46"].playable("US", app, True))
        app.map["Iraq"].sleeperCells = 0
        app.map["Iraq"].activeCells = 1
        self.assertTrue(app.deck["46"].playable("US", app, True))    

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Syria"].make_fair()
        app.map["Syria"].make_ally()
        app.map["Syria"].regimeChange = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Syria"].cadre = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Syria"].sleeperCells = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))
        app.map["Syria"].sleeperCells = 0
        app.map["Syria"].activeCells = 1
        self.assertFalse(app.deck["46"].playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_poor()
        app.map["Iraq"].make_ally()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].sleeperCells = 1
        app.deck["46"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_fair())
        app.deck["46"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_good())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_ally()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].sleeperCells = 1
        app.map["Syria"].make_fair()
        app.map["Syria"].make_ally()
        app.map["Syria"].regimeChange = 1
        app.map["Syria"].sleeperCells = 1
        app.deck["46"].playEvent("US", app)
        self.assertTrue(app.map["Iraq"].is_good())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Lebanon"])
        app.map["Iraq"].make_fair()
        app.map["Iraq"].make_ally()
        app.map["Iraq"].regimeChange = 1
        app.map["Iraq"].sleeperCells = 1
        app.map["Lebanon"].make_fair()
        app.map["Lebanon"].make_ally()
        app.map["Lebanon"].regimeChange = 1
        app.map["Lebanon"].sleeperCells = 1
        print "Choose Lebanon"
        app.deck["46"].playEvent("US", app)
        self.assertTrue(app.map["Lebanon"].is_good())


class Card47(LabyrinthTestCase):
    """The door of Itjihad was closed"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["47"].playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["47"].playEvent("US", app)
        self.assertTrue("The door of Itjihad was closed" in app.lapsing)
        self.assertFalse(app.deck["66"].playable("Jihadist", app, False))
        self.assertFalse(app.deck["114"].playable("Jihadist", app, False))
        app.do_turn("")
        self.assertFalse("The door of Itjihad was closed" in app.lapsing)
        self.assertTrue(app.deck["66"].playable("Jihadist", app, False))
        self.assertTrue(app.deck["114"].playable("Jihadist", app, False))


class Card48(LabyrinthTestCase):
    """Adam Gadahn"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "y"])
        app.cells = 0
        self.assertFalse(app.deck["48"].playable("Jihadist", app, False))
        app.cells = 9
        print "Say No"
        self.assertFalse(app.deck["48"].playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck["48"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["48"].putsCell(app))            

    def test_event(self):
        # Set up
        mock_randomizer = mock(Randomizer())
        when(mock_randomizer).roll_d6(3).thenReturn([1, 3, 2])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["120"], randomizer=mock_randomizer)
        self.assertTrue(app.numCellsAvailable() > 0)
        self.assertCells(app, "United States", 0)

        # Invoke
        app.deck["48"].playEvent("Jihadist", app)

        # Check
        self.assertCells(app, "United States", 2)


class Card49(LabyrinthTestCase):
    """Al-Ittihad al-Islami"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["49"].playable("Jihadist", app, False))    
        app.cells = 1
        self.assertTrue(app.deck["49"].playable("Jihadist", app, False))    
        app.cells = 0
        self.assertTrue(app.deck["49"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["49"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["49"].playEvent("Jihadist", app)
        self.assertTrue(app.map["Somalia"].sleeperCells == 1)


class Card50(LabyrinthTestCase):
    """Ansar al-Islam"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["50"].playable("Jihadist", app, False))    
        app.map["Iraq"].make_good()
        self.assertFalse(app.deck["50"].playable("Jihadist", app, False))    
        app.map["Iraq"].make_fair()
        self.assertTrue(app.deck["50"].playable("Jihadist", app, False))    
        app.map["Iraq"].make_poor()
        self.assertTrue(app.deck["50"].playable("Jihadist", app, False))    
        app.map["Iraq"].make_islamist_rule()
        self.assertTrue(app.deck["50"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["50"].putsCell(app))            

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["50"].playEvent("Jihadist", app)
        app.map["Iraq"].make_fair()
        self.assertTrue(app.map["Iraq"].sleeperCells == 1 or app.map["Iran"].sleeperCells == 1)


if __name__ == "__main__":
    unittest.main()   