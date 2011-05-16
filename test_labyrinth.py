'''
LWOTai - A Python implementation of the Single-Player AI for Labyrinth: the War on Terror by GMT Games.
Mike Houser, 2011
'''
from labyrinth import Labyrinth
import unittest

def testScenarioSetup(self):
	self.prestige = 7
	self.troops = 9
	self.funding = 5
	self.cells = 11
	self.map["Libya"].governance = 3
	self.map["Libya"].alignment = "Adversary"
	self.map["Syria"].governance = 2
	self.map["Syria"].alignment = "Adversary"
	self.map["Iraq"].governance = 3
	self.map["Iraq"].alignment = "Adversary"
	self.map["Iraq"].plots = 2	
	self.map["Saudi Arabia"].governance = 3
	self.map["Saudi Arabia"].alignment = "Ally"
	self.map["Saudi Arabia"].troopCubes = 2
	self.map["Pakistan"].governance = 2
	self.map["Pakistan"].alignment = "Neutral"
	self.map["Pakistan"].troopCubes = 2
	self.map["Pakistan"].activeCells = 4
	self.map["Gulf States"].governance = 2
	self.map["Gulf States"].alignment = "Ally"
	self.map["Gulf States"].troopCubes = 4
	self.map["Gulf States"].sleeperCells = 1
	self.map["Gulf States"].activeCells = 4
	self.map["Afghanistan"].governance = 4
	self.map["Afghanistan"].alignment = "Adversary"
	self.map["Afghanistan"].sleeperCells = 4
	self.map["Somalia"].besieged = 1
	self.map["United States"].posture = "Hard"

def test2ScenarioSetup(self):
	self.prestige = 7
	self.troops = 3
	self.funding = 9
	self.cells = 11
	self.map["Libya"].governance = 3
	self.map["Libya"].alignment = "Adversary"
	self.map["Syria"].governance = 2
	self.map["Syria"].alignment = "Adversary"
	self.map["Iraq"].governance = 3
	self.map["Iraq"].alignment = "Adversary"
	self.map["Iraq"].plots = 2	
	self.map["Saudi Arabia"].governance = 3
	self.map["Saudi Arabia"].alignment = "Ally"
	self.map["Saudi Arabia"].troopCubes = 2
	self.map["Pakistan"].governance = 2
	self.map["Pakistan"].alignment = "Neutral"
	self.map["Pakistan"].troopCubes = 2
	self.map["Pakistan"].activeCells = 4
	self.map["Gulf States"].governance = 2
	self.map["Gulf States"].alignment = "Ally"
	self.map["Gulf States"].troopCubes = 2
	self.map["Gulf States"].sleeperCells = 1
	self.map["Gulf States"].activeCells = 4
	self.map["Afghanistan"].governance = 1
	self.map["Afghanistan"].alignment = "Ally"
	self.map["Afghanistan"].activeCells = 4
	self.map["Afghanistan"].regimeChange = 1
	self.map["Afghanistan"].troopCubes = 6
	self.map["Afghanistan"].aid = 1
	self.map["Afghanistan"].besieged = 0
	self.map["Somalia"].besieged = 1
	self.map["United States"].posture = "Hard"

def test3ScenarioSetup(self):
	self.prestige = 7
	self.troops = 9
	self.funding = 5
	self.cells = 11
	self.map["Libya"].governance = 3
	self.map["Libya"].alignment = "Adversary"
	self.map["Syria"].governance = 2
	self.map["Syria"].alignment = "Adversary"
	self.map["Iraq"].governance = 3
	self.map["Iraq"].alignment = "Adversary"
	self.map["Iraq"].plots = 2	
	self.map["Saudi Arabia"].governance = 3
	self.map["Saudi Arabia"].alignment = "Ally"
	self.map["Saudi Arabia"].troopCubes = 2
	self.map["Pakistan"].governance = 2
	self.map["Pakistan"].alignment = "Neutral"
	self.map["Pakistan"].troopCubes = 2
	self.map["Pakistan"].activeCells = 4
	self.map["Gulf States"].governance = 2
	self.map["Gulf States"].alignment = "Ally"
	self.map["Gulf States"].troopCubes = 4
	self.map["Gulf States"].sleeperCells = 1
	self.map["Gulf States"].activeCells = 4
	self.map["Afghanistan"].governance = 4
	self.map["Afghanistan"].alignment = "Adversary"
	self.map["Afghanistan"].sleeperCells = 4
	self.map["Somalia"].besieged = 1
	self.map["United States"].posture = "Hard"
	self.map["France"].posture = "Hard"
	self.map["France"].cadre = 1
	self.map["Spain"].posture = "Soft"
	self.map["Spain"].sleeperCells = 1
	self.map["Germany"].posture = "Hard"
	self.map["Germany"].activeCells = 1
	self.map["Germany"].sleeperCells = 1
	
def testBlankScenarioSetup(self):
	self.prestige = 7
	self.troops = 9
	self.funding = 5
	self.cells = 11

class Map(unittest.TestCase):
	'''Map'''
		
	def testDeck(self):
		'''Test Map'''
		app = Labyrinth(1, 1, testScenarioSetup)
		for country in app.map:
			for link in app.map[country].links:
				self.assertTrue(app.map[country] in link.links)

class Deck(unittest.TestCase):
	'''Deck tests'''
		
	def testDeck(self):
		'''Test Deck'''
		app = Labyrinth(1, 1, testScenarioSetup)
		for i in range(121):
			if i > 0:
				self.assertEqual(i, app.deck[str(i)].number)

class WOIRollModifiers(unittest.TestCase):
	'''Test War of Ideas Roll Modifires'''
		
	def testPrestige(self):
		'''Prestige'''
		app = Labyrinth(1, 1, testScenarioSetup)
		app.prestige = 1
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 1)
		app.prestige = 2
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 1)
		app.prestige = 3
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 1)
		app.prestige = 4
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 2)
		app.prestige = 5
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 2)
		app.prestige = 6
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 2)
		app.prestige = 7
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 3)
		app.prestige = 8
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 3)
		app.prestige = 9
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 3)
		app.prestige = 10
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 4)
		app.prestige = 11
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 4)
		app.prestige = 12
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 4)

	def testAid(self):
		'''Aid'''
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 3)
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 4)
		
	def testToGood(self):
		'''Going to Good'''
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 3)
		app.map["Gulf States"].governance = 3
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 4)
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].alignment = "Neutral"
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 4)

	def testGWOTPenalty(self):
		'''GWOT Penalty'''
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 3)
		app.map["United States"].posture = "Soft"
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 2)
		app.map["Canada"].posture = "Hard"
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 1)
		app.map["France"].posture = "Hard"
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 0)
		app.map["Germany"].posture = "Hard"
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 0)
		
	def testAdjCountries(self):
		'''Adjacent countries Ally Good'''
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 3)
		app.map['Pakistan'].governance = 1
		app.map['Pakistan'].alignment = "Neutral"
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 3)
		app.map['Pakistan'].alignment = "Ally"
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 4)
		app.map['Iraq'].governance = 1
		app.map['Iraq'].alignment = "Ally"
		self.assertEqual(app.modifiedWoIRoll(3,"Gulf States"), 4)

class WOIhandler(unittest.TestCase):
	'''Test War of Ideas Handler'''

	def testFailRolls(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
		app.handleMuslimWoI(1, "Gulf States")
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
		app.handleMuslimWoI(2, "Gulf States")
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)

		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
		app.handleMuslimWoI(3, "Gulf States")
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
		app.handleMuslimWoI(4, "Gulf States")
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 1)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
		app.handleMuslimWoI(5, "Gulf States")
		self.assertEqual(app.map["Gulf States"].governance, 1)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Gulf States"].governance, 2)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
		app.handleMuslimWoI(6, "Gulf States")
		self.assertEqual(app.map["Gulf States"].governance, 1)
		self.assertEqual(app.map["Gulf States"].alignment, "Ally")
		self.assertEqual(app.map["Gulf States"].aid, 0)
#///
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 0)
		app.handleMuslimWoI(1, "Pakistan")
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 0)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 0)
		app.handleMuslimWoI(2, "Pakistan")
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 0)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 0)
		app.handleMuslimWoI(3, "Pakistan")
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 0)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 0)
		app.handleMuslimWoI(4, "Pakistan")
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 1)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 0)
		app.handleMuslimWoI(5, "Pakistan")
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Ally")
		self.assertEqual(app.map["Pakistan"].aid, 0)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Neutral")
		self.assertEqual(app.map["Pakistan"].aid, 0)
		app.handleMuslimWoI(6, "Pakistan")
		self.assertEqual(app.map["Pakistan"].governance, 2)
		self.assertEqual(app.map["Pakistan"].alignment, "Ally")
		self.assertEqual(app.map["Pakistan"].aid, 0)
#///
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
		app.handleMuslimWoI(1, "Saudi Arabia")
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
		app.handleMuslimWoI(2, "Saudi Arabia")
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
		app.handleMuslimWoI(3, "Saudi Arabia")
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
		app.handleMuslimWoI(4, "Saudi Arabia")
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 1)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
		app.handleMuslimWoI(5, "Saudi Arabia")
		self.assertEqual(app.map["Saudi Arabia"].governance, 2)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Saudi Arabia"].governance, 3)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
		app.handleMuslimWoI(6, "Saudi Arabia")
		self.assertEqual(app.map["Saudi Arabia"].governance, 2)
		self.assertEqual(app.map["Saudi Arabia"].alignment, "Ally")
		self.assertEqual(app.map["Saudi Arabia"].aid, 0)
	
class alertHandler(unittest.TestCase):
	'''Test Alert'''
	
	def testAlert(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["Iraq"].plots, 2)
		app.handleAlert("Iraq")
		self.assertEqual(app.map["Iraq"].plots, 1)
		app.handleAlert("Iraq")
		self.assertEqual(app.map["Iraq"].plots, 0)
		app.handleAlert("Iraq")
		self.assertEqual(app.map["Iraq"].plots, 0)

class reassessmentHandler(unittest.TestCase):
	'''Test Reassessment'''
	
	def testAlert(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.map["United States"].posture, "Hard")
		app.handleReassessment()
		self.assertEqual(app.map["United States"].posture, "Soft")
		app.handleReassessment()
		self.assertEqual(app.map["United States"].posture, "Hard")

class regimeChangeHandler(unittest.TestCase):
	'''Test Regime Change'''
	
	def testRegimeChange(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Soft"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops(), 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 9)
		govRoll = 4
		prestigeRolls = (3,2,5)
		app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops(), 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 9)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops(), 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 9)
		govRoll = 4
		prestigeRolls = (3,2,5)
		app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 3)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 5)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops(), 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 9)
		govRoll = 5
		prestigeRolls = (3,2,5)
		app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 2)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 5)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops(), 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 9)
		govRoll = 5
		prestigeRolls = (5,2,5)
		app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 2)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 9)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops(), 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 9)
		govRoll = 5
		prestigeRolls = (2,6,5)
		app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 2)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 2)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops(), 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 9)
		govRoll = 5
		prestigeRolls = (6,6,5)
		app.handleRegimeChange("Afghanistan", "track", 6, govRoll, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 2)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 12)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.troops -= 8
		app.map["Pakistan"].changeTroops(8)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops(), 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 1)
		self.assertEqual(app.map["Pakistan"].troops(), 10)
		govRoll = 5
		prestigeRolls = (6,6,5)
		app.handleRegimeChange("Afghanistan", "Pakistan", 7, govRoll, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 2)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 7)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 12)
		self.assertEqual(app.troops, 1)
		self.assertEqual(app.map["Pakistan"].troops(), 3)

class withdrawHandler(unittest.TestCase):
	'''Test Withdraw'''
	
	def testWithdraw(self):
		app = Labyrinth(1, 1, test2ScenarioSetup)
		app.map["United States"].posture = "Soft"	
		self.assertEqual(app.map["Afghanistan"].governance, 1)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 6)
		self.assertEqual(app.map["Afghanistan"].aid, 1)
		self.assertEqual(app.map["Afghanistan"].besieged, 0)
		self.assertEqual(app.map["Saudi Arabia"].troops(), 2)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 3)
		prestigeRolls = (5,2,5)
		app.handleWithdraw("Afghanistan", "Saudi Arabia", 4, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 1)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 2)
		self.assertEqual(app.map["Afghanistan"].aid, 0)
		self.assertEqual(app.map["Afghanistan"].besieged, 1)
		self.assertEqual(app.map["Saudi Arabia"].troops(), 6)
		self.assertEqual(app.prestige, 9)
		self.assertEqual(app.troops, 3)

		app = Labyrinth(1, 1, test2ScenarioSetup)
		app.map["United States"].posture = "Soft"	
		self.assertEqual(app.map["Afghanistan"].governance, 1)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 6)
		self.assertEqual(app.map["Afghanistan"].aid, 1)
		self.assertEqual(app.map["Afghanistan"].besieged, 0)
		self.assertEqual(app.map["Saudi Arabia"].troops(), 2)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 3)
		prestigeRolls = (2,3,5)
		app.handleWithdraw("Afghanistan", "track", 5, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 1)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops(), 1)
		self.assertEqual(app.map["Afghanistan"].aid, 0)
		self.assertEqual(app.map["Afghanistan"].besieged, 1)
		self.assertEqual(app.map["Saudi Arabia"].troops(), 2)
		self.assertEqual(app.prestige, 4)
		self.assertEqual(app.troops, 8)

class majorJihadChoice(unittest.TestCase):
	'''Major Jihad possible?'''
	# For Major Jihad to be possible you need:
	# - A muslim country
	# - Not under Islamic Rule
	# - with at least 5 more cells than troops
	# - At least 2 rolls if the country is poor and not besieged
	# - At least 1 roll if the country is poor and is besieged
	# - At least 3 rolls if the country is fair and not besieged
	# - At least 2 rolls if the country is fair and is besieged
	# - At least 3 rolls if the country is good and is besieged
	# - NOT possible if the country is good and not besieged
	
	def testMajorJihadChoice(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		self.assertEqual(app.majorJihadChoice(3), False)	# 3 Ops
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		self.assertEqual(app.majorJihadChoice(3), "Gulf States")	# 3 Ops
		self.assertEqual(app.majorJihadChoice(2), "Gulf States")	# 2 Ops
		self.assertEqual(app.majorJihadChoice(1), False)	# 1 Ops
		app.map["Gulf States"].governance = 2
		self.assertEqual(app.majorJihadChoice(3), "Gulf States")	# 3 Ops
		self.assertEqual(app.majorJihadChoice(2), False)	# 2 Ops
		self.assertEqual(app.majorJihadChoice(1), False)	# 1 Ops
		app.map["Gulf States"].governance = 1
		self.assertEqual(app.majorJihadChoice(3), False)	# 3 Ops
		self.assertEqual(app.majorJihadChoice(2), False)	# 2 Ops
		self.assertEqual(app.majorJihadChoice(1), False)	# 1 Ops
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].governance = 3
		self.assertEqual(app.majorJihadChoice(3), "Gulf States")	# 3 Ops
		self.assertEqual(app.majorJihadChoice(2), "Gulf States")	# 2 Ops
		self.assertEqual(app.majorJihadChoice(1), "Gulf States")	# 1 Ops
		app.map["Gulf States"].governance = 2
		self.assertEqual(app.majorJihadChoice(3), "Gulf States")	# 3 Ops
		self.assertEqual(app.majorJihadChoice(2), "Gulf States")	# 2 Ops
		self.assertEqual(app.majorJihadChoice(1), False)	# 1 Ops
		app.map["Gulf States"].governance = 1
		self.assertEqual(app.majorJihadChoice(3), "Gulf States")	# 3 Ops
		self.assertEqual(app.majorJihadChoice(2), False)	# 2 Ops
		self.assertEqual(app.majorJihadChoice(1), False)	# 1 Ops

		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Afghanistan"].governance = 3
		app.map["Afghanistan"].sleeperCells = 3
		app.map["Afghanistan"].activeCells = 3
		app.map["Afghanistan"].troopCubes = 1
		app.map["Afghanistan"].besieged = 0

		self.assertEqual(app.majorJihadChoice(3), "Gulf States")	# 3 Ops
		self.assertEqual(app.majorJihadChoice(2), "Gulf States")	# 2 Ops
		self.assertEqual(app.majorJihadChoice(1), False)	# 1 Ops
		
		app.map["Saudi Arabia"].governance = 3
		app.map["Saudi Arabia"].sleeperCells = 5
		app.map["Saudi Arabia"].activeCells = 4
		app.map["Saudi Arabia"].troopCubes = 4
		app.map["Saudi Arabia"].besieged = 0

		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops
		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops
		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops
		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops
		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops
		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops
		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops
		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops
		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops
		self.assertTrue(app.majorJihadChoice(3) in ["Gulf States", "Saudi Arabia"])	# 3 Ops

		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].sleeperCells = 5
		app.map["Pakistan"].activeCells = 4
		app.map["Pakistan"].troopCubes = 4
		app.map["Pakistan"].besieged = 0

		self.assertEqual(app.majorJihadChoice(3), "Pakistan")	# 3 Ops
		self.assertEqual(app.majorJihadChoice(2), "Pakistan")	# 2 Ops
		self.assertEqual(app.majorJihadChoice(1), False)	# 1 Ops
		
class handleJihad(unittest.TestCase):
	'''Test handleJihad'''
	
	def testHandleJihad(self):
	# Many Cells
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 1)
		self.assertEqual(opsLeft, 0)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 2)
		self.assertEqual(opsLeft, 0)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 3)
		self.assertEqual(opsLeft, 0)
	
	# 1 cell
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 1)
		self.assertEqual(opsLeft, 0)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 2)
		self.assertEqual(opsLeft, 1)
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 3)
		self.assertEqual(opsLeft, 2)
		
	# 2 cell
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 1)
		self.assertEqual(opsLeft, 0)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 2)
		self.assertEqual(opsLeft, 0)
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 3)
		self.assertEqual(opsLeft, 1)
		
	# 3 cell
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 1)
		self.assertEqual(opsLeft, 0)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 2)
		self.assertEqual(opsLeft, 0)
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		opsLeft = app.handleJihad("Gulf States", 3)
		self.assertEqual(opsLeft, 0)	
		
class executeJihad(unittest.TestCase):
	'''Execute Major Jihad'''
	# A Major jihad needs:
	# - Muslim country not under Islamic Rule
	# - 5 more cells than troops
	# - Then if gov at Poor and not besieged 2 more successes causes Islamic Revolution
	# - Or if gov at Poor and is besieged 1 more success causses Islamic Revolution
	# Jihad does:
	# - Each success worsens gov
	# - Any failure roll sends a cell to the funding track
	# Major failure does:
	# - Three Failure rolls in a Poor country shifts alignment one toward Ally and places Besieged regime
	# A Major jihad does:
	# - All cells go active
	# Islamic Revolution causes:
	# - Gov to Islamic Rule
	# - Alignment to Adversary
	# - Remove Regime Change, Beseiged and Aid
	# - Add country's resources to Funding track
	# - If troops in country US Prestige to 1
	
# 5 MORE CELLS THAN TROOPS - Major Jihad possible

	def testJihadEnoughCellsPoorGovNotBeseiged(self):

# Poor Gov
# Not Besieged
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 4) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3]) # Islamic Revolution
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # to 1 due to troops present

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 7) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4,4]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 7) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
				
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4,4]) # Major failure
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 6) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # major failure
		self.assertEqual(app.map["Gulf States"].alignment, "Ally") # major failure
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4]) # Islamic 		Revolution
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # to 1 due to troops present
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4]) # Islamic Revolution
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 7) # unchanged, no troops

	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # Islamic Revolution
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # to 1 due to troops present
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # Islamic Revolution
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 7) # unchanged, no troops

	def testJihadEnoughCellsPoorGovIsBeseiged(self):	
# Poor Gov
# Besieged
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # troops
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # troops

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # troops
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 7) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # troops
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # troops
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4,4]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 7) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # troops
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4,4]) # Major Failure in besiged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 6) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # major failure
		self.assertEqual(app.map["Gulf States"].alignment, "Ally") # major failure
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadEnoughCellsFairGovNotBeseiged(self):
# Fair Gov
# Not Besieged
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 4) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 4) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,3,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 7) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
				
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # not Major failure
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 6) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # not major failure
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # not major failure
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,3]) # Islamic Revolution
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	# troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # Islamic Revolution
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # to 1 due to troops present
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # Islamic Revolution
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 7) # unchanged, no troops
		
	def testJihadEnoughCellsFairGovIsBeseiged(self):
# Fair Gov
# Besieged

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 4) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2]) # Revolution in besieged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 7) # unchanged, no troops

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,3]) # Revolution failed
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 7) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # troops
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,3]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # troops
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,3,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 7) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # Not Major Failure in besiged
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 6) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # major failure
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # major failure
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadEnoughCellsGoodGovNotBeseiged(self):
# Good Gov
# Not Besieged
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 4) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 4) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
				
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # not Major failure
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # not major failure
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # not major failure
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2,2]) # Revolution failed
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1,1]) # Revolution failed
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 4) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadEnoughCellsGoodGovIsBeseiged(self):
# Good Gov
# Besieged

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 4) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 4) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2]) # Revolution failed
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 5) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1,1]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 4) # islamic rule
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 9) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 0) # removed
		self.assertEqual(app.map["Gulf States"].aid, 0) # removed
		self.assertEqual(app.map["Gulf States"].besieged, 0) # removed
		self.assertEqual(app.map["Gulf States"].alignment, "Adversary") # due to revolution
		self.assertEqual(app.funding, 8) # +3 from resources
		self.assertEqual(app.prestige, 1) # troops
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1,2]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 8) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 7) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 5
		app.map["Gulf States"].activeCells = 4
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # not Major Failure in besiged
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 6) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # major failure
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # not major failure
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
# NOT 5 MORE CELLS THAN TROOPS - Major Jihad NOT possible

	def testJihadNotEnoughCellsPoorGovNotBeseiged(self):

# Poor Gov
# Not Besieged
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3]) # Islamic Revolution
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4,4]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
				
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4,4]) # Not Major failure
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 0) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # not major failure
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # not major failure
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadNotEnoughCellsPoorGovIsBeseiged(self):	
# Poor Gov
# Besieged
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # 
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # 
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # 
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # 
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # all cells active
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # 
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # 
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # 
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4,4]) # Revolution in besiged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # 
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4,4]) # no major failure
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 0) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # 
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadNotEnoughCellsFairGovNotBeseiged(self):
# Fair Gov
# Not Besieged
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,3,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
				
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # no Major failure
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov stays 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 0) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,3]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	# troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	# No troops
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # Islamic Revolution
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
	def testJihadNotEnoughCellsFairGovIsBeseiged(self):
# Fair Gov
# Besieged

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2]) # Revolution in besieged
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,3]) # Revolution failed
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,3]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,3,3]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3]) # no Failure in besiged
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov still 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 0) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # major failure
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadNotEnoughCellsGoodGovNotBeseiged(self):
# Good Gov
# Not Besieged
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
				
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # no Major failure
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 0) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2,2]) # Revolution failed
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1,1]) # Revolution failed
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadNotEnoughCellsGoodGovIsBeseiged(self):
# Good Gov
# Besieged

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 0
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2]) # Revolution failed
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2]) # Revolution fails in besiged
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov still 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1,1]) # Can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 3) # lost no cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,1,2]) # can't major jihad
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov to 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 2) # lost one cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [1,2,2]) # Revolution fails
		self.assertEqual(app.map["Gulf States"].governance, 2) # gov to 2
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # lost two cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)
		
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 1
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [2,2,2]) # no Major Failure in besiged
		self.assertEqual(app.map["Gulf States"].governance, 1) # gov stays 1
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # major jihad not possible
		self.assertEqual(app.map["Gulf States"].activeCells, 0) # lost three cells to the to failure rolls
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 1) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

# Sleeper/Active cell testing

	def testJihadOneCell(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # sleeper goes active
		self.assertEqual(app.map["Gulf States"].activeCells, 1) #  sleeper goes active
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) # lose sleeper cell
		self.assertEqual(app.map["Gulf States"].activeCells, 0) # 
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadTwoSleeperCells(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # sleeper goes active
		self.assertEqual(app.map["Gulf States"].activeCells, 1) # sleeper goes active
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) # lose sleeper cell
		self.assertEqual(app.map["Gulf States"].activeCells, 0) # lose sleeper cell
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadTwoActiveCells(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadOneSleeperOneActiveCells(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadThreeSleeperCells(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 3
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 2) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1) 
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 3
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 2)
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 3
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 3
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 3
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 3
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 3)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 3
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 3
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 3
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadTwoSleeperOneActiveCells(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 2) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1) 
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 2)
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 3)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 2
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadOneSleeperTwoActiveCells(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2) 
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1)
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 1) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 3)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].activeCells = 2
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

	def testJihadThreeActiveCells(self):
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 3) 
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0)
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 3)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,3])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 3)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,3,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 2)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [3,4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 1)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["Gulf States"].alignment = "Neutral"
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].sleeperCells = 0
		app.map["Gulf States"].activeCells = 3
		app.map["Gulf States"].troopCubes = 4
		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].aid = 1
		app.executeJihad("Gulf States", [4,4,4])
		self.assertEqual(app.map["Gulf States"].governance, 3) # gov still 3
		self.assertEqual(app.map["Gulf States"].sleeperCells, 0) 
		self.assertEqual(app.map["Gulf States"].activeCells, 0)
		self.assertEqual(app.map["Gulf States"].regimeChange, 1) # still there
		self.assertEqual(app.map["Gulf States"].aid, 1) # still there
		self.assertEqual(app.map["Gulf States"].besieged, 0) # need three fails to get a besieged regime
		self.assertEqual(app.map["Gulf States"].alignment, "Neutral") # need three fails to move alingment
		self.assertEqual(app.funding, 5)
		self.assertEqual(app.prestige, 7)

class minorJihadChoice(unittest.TestCase):
	'''Test minorJihadInGoodFairChoice'''

	def testMinorJihadOneCellOneOps(self):
# one cell in each country, one ops case	

		app = Labyrinth(1, 1, test3ScenarioSetup)
	# only Islamic rule has cells	
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(1), False)
	# fair governance
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])
	# good governance
		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Saudi Arabia",1)])
	# 2 good governance
		app.map["Gulf States"].governance = 1
		for i in range(10):
			retVal = app.minorJihadInGoodFairChoice(1)
			self.assertTrue((retVal == [("Gulf States",1)]) or (retVal == [("Saudi Arabia",1)]))
	# 2 good governance but Jordan has less resources	
		app.map["Saudi Arabia"].governance = 3
		app.map["Jordan"].governance = 1
		app.map["Jordan"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])
	# but the other is besieged
		app.map["Jordan"].besieged = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Jordan",1)])
	# but the other has aid
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])
	# but yet another is Pakistan	
		app.map["Pakistan"].governance = 1
		app.map["Pakistan"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Pakistan",1)])
	# but Pakistan does not win against good if it is fair
		app.map["Pakistan"].governance = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])

	def testMinorJihadOneCellTwoOps(self):
# one cell in each country, two ops case	

		app = Labyrinth(1, 1, test3ScenarioSetup)
	# only Islamic rule has cells	
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(2), False)
	# fair governance
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",1)])
	# good governance
		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Saudi Arabia",1),("Gulf States",1)])
	# 2 good governance
		app.map["Gulf States"].governance = 1
		retVal = app.minorJihadInGoodFairChoice(2)
		self.assertTrue((("Gulf States",1) in retVal) and (("Saudi Arabia",1) in retVal) and len(retVal) == 2)
	# 2 good governance but Jordan has less resources	
		app.map["Saudi Arabia"].governance = 3
		app.map["Jordan"].governance = 1
		app.map["Jordan"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",1),("Jordan",1)])
	# but the other is besieged
		app.map["Jordan"].besieged = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Jordan",1),("Gulf States",1)])
	# but the other has aid
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",1),("Jordan",1)])
	# but yet another is Pakistan	
		app.map["Pakistan"].governance = 1
		app.map["Pakistan"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Pakistan",1),("Gulf States",1)])
	# but Pakistan does not win against good if it is fair
		app.map["Pakistan"].governance = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",1),("Jordan",1)])

	def testMinorJihadOneCellThreeOps(self):
# one cell in each country, three ops case	

		app = Labyrinth(1, 1, test3ScenarioSetup)
	# only Islamic rule has cells	
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(3), False)
	# fair governance
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",1)])
	# good governance
		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Saudi Arabia",1),("Gulf States",1)])
	# 2 good governance
		app.map["Gulf States"].governance = 1
		self.assertTrue((("Gulf States",1) in app.minorJihadInGoodFairChoice(3)) and (("Saudi Arabia",1) in app.minorJihadInGoodFairChoice(3)) and len(app.minorJihadInGoodFairChoice(3)) == 2)
	# 2 good governance but Jordan has less resources	
		app.map["Saudi Arabia"].governance = 3
		app.map["Jordan"].governance = 1
		app.map["Jordan"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",1),("Jordan",1)])
	# but the other is besieged
		app.map["Jordan"].besieged = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Jordan",1),("Gulf States",1)])
	# but the other has aid
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",1),("Jordan",1)])
	# but yet another is Pakistan	
		app.map["Pakistan"].governance = 1
		app.map["Pakistan"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Pakistan",1),("Gulf States",1),("Jordan",1)])
	# but Pakistan does not win against good if it is fair
		app.map["Pakistan"].governance = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",1),("Jordan",1),("Pakistan",1)])

	def testMinorJihadTwoCellOneOps(self):
# two cells in each country, one ops case	

		app = Labyrinth(1, 1, test3ScenarioSetup)
	# only Islamic rule has cells	
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(1), False)
	# fair governance
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])
	# good governance
		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Saudi Arabia",1)])
	# 2 good governance
		app.map["Gulf States"].governance = 1
		for i in range(10):
			retVal = app.minorJihadInGoodFairChoice(1)
			self.assertTrue(retVal == [("Gulf States",1)] or retVal == [("Saudi Arabia",1)])
	# 2 good governance but Jordan has less resources	
		app.map["Saudi Arabia"].governance = 3
		app.map["Jordan"].governance = 1
		app.map["Jordan"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])
	# but the other is besieged
		app.map["Jordan"].besieged = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Jordan",1)])
	# but the other has aid
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])
	# but yet another is Pakistan	
		app.map["Pakistan"].governance = 1
		app.map["Pakistan"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Pakistan",1)])
	# but Pakistan does not win against good if it is fair
		app.map["Pakistan"].governance = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])

	def testMinorJihadTwoCellTwoOps(self):
# two cell in each country, two ops case	

		app = Labyrinth(1, 1, test3ScenarioSetup)
	# only Islamic rule has cells	
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(2), False)
	# fair governance
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",2)])
	# good governance
		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Saudi Arabia",2)])
	# 2 good governance
		app.map["Gulf States"].governance = 1
		for i in range(10):
			retVal = app.minorJihadInGoodFairChoice(2) 
			self.assertTrue(retVal == [("Gulf States",2)] or retVal == [("Saudi Arabia",2)])
	# 2 good governance but Jordan has less resources	
		app.map["Saudi Arabia"].governance = 3
		app.map["Jordan"].governance = 1
		app.map["Jordan"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",2)])
	# but the other is besieged
		app.map["Jordan"].besieged = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Jordan",2)])
	# but the other has aid
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",2)])
	# but yet another is Pakistan	
		app.map["Pakistan"].governance = 1
		app.map["Pakistan"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Pakistan",2)])
	# but Pakistan does not win against good if it is fair
		app.map["Pakistan"].governance = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",2)])

	def testMinorJihadTwoCellThreeOps(self):
# two cell in each country, three ops case	

		app = Labyrinth(1, 1, test3ScenarioSetup)
	# only Islamic rule has cells	
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(3), False)
	# fair governance
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",2)])
	# good governance
		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Saudi Arabia",2),("Gulf States",1)])
	# 2 good governance
		app.map["Gulf States"].governance = 1
		for i in range(10):
			retVal = app.minorJihadInGoodFairChoice(3)
			self.assertTrue(retVal == [("Saudi Arabia",2),("Gulf States",1)] or retVal == [("Gulf States",2),("Saudi Arabia",1)])
	# 2 good governance but Jordan has less resources	
		app.map["Saudi Arabia"].governance = 3
		app.map["Jordan"].governance = 1
		app.map["Jordan"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",2),("Jordan",1)])
	# but the other is besieged
		app.map["Jordan"].besieged = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Jordan",2),("Gulf States",1)])
	# but the other has aid
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",2),("Jordan",1)])
	# but yet another is Pakistan	
		app.map["Pakistan"].governance = 1
		app.map["Pakistan"].activeCells = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Pakistan",2),("Gulf States",1)])
	# but Pakistan does not win against good if it is fair
		app.map["Pakistan"].governance = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",2),("Jordan",1)])

	def testMinorJihadThreeCellOneOps(self):
# three cells in each country, one ops case	

		app = Labyrinth(1, 1, test3ScenarioSetup)
	# only Islamic rule has cells	
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(1), False)
	# fair governance
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])
	# good governance
		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Saudi Arabia",1)])
	# 2 good governance
		app.map["Gulf States"].governance = 1
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
		self.assertTrue(app.minorJihadInGoodFairChoice(1) in [[("Gulf States",1)],[("Saudi Arabia",1)]])
	# 2 good governance but Jordan has less resources	
		app.map["Saudi Arabia"].governance = 3
		app.map["Jordan"].governance = 1
		app.map["Jordan"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])
	# but the other is besieged
		app.map["Jordan"].besieged = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Jordan",1)])
	# but the other has aid
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])
	# but yet another is Pakistan	
		app.map["Pakistan"].governance = 1
		app.map["Pakistan"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Pakistan",1)])
	# but Pakistan does not win against good if it is fair
		app.map["Pakistan"].governance = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Gulf States",1)])

	def testMinorJihadThreeCellTwoOps(self):
# three cell in each country, two ops case	

		app = Labyrinth(1, 1, test3ScenarioSetup)
	# only Islamic rule has cells	
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(2), False)
	# fair governance
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",2)])
	# good governance
		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Saudi Arabia",2)])
	# 2 good governance
		app.map["Gulf States"].governance = 1
		for i in range(10):
			retVal = app.minorJihadInGoodFairChoice(2)
			self.assertTrue(retVal == [("Gulf States",2)] or retVal == [("Saudi Arabia",2)])
	# 2 good governance but Jordan has less resources	
		app.map["Saudi Arabia"].governance = 3
		app.map["Jordan"].governance = 1
		app.map["Jordan"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",2)])
	# but the other is besieged
		app.map["Jordan"].besieged = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Jordan",2)])
	# but the other has aid
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",2)])
	# but yet another is Pakistan	
		app.map["Pakistan"].governance = 1
		app.map["Pakistan"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Pakistan",2)])
	# but Pakistan does not win against good if it is fair
		app.map["Pakistan"].governance = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(2), [("Gulf States",2)])

	def testMinorJihadThreeCellThreeOps(self):
# three cell in each country, three ops case	

		app = Labyrinth(1, 1, test3ScenarioSetup)
	# only Islamic rule has cells	
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(3), False)
	# fair governance
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",3)])
	# good governance
		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Saudi Arabia",3)])
	# 2 good governance
		app.map["Gulf States"].governance = 1
		for i in range(10):
			retVal = app.minorJihadInGoodFairChoice(3)
			self.assertTrue((retVal == [("Saudi Arabia",3)]) or (retVal == [("Gulf States",3)]))
	# 2 good governance but Jordan has less resources	
		app.map["Saudi Arabia"].governance = 3
		app.map["Jordan"].governance = 1
		app.map["Jordan"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",3)])
	# but the other is besieged
		app.map["Jordan"].besieged = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Jordan",3)])
	# but the other has aid
		app.map["Gulf States"].aid = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",3)])
	# but yet another is Pakistan	
		app.map["Pakistan"].governance = 1
		app.map["Pakistan"].activeCells = 3
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Pakistan",3)])
	# but Pakistan does not win against good if it is fair
		app.map["Pakistan"].governance = 2
		self.assertEqual(app.minorJihadInGoodFairChoice(3), [("Gulf States",3)])
		
class recruit(unittest.TestCase):
	'''Test Recruiting'''
	
	def testRecruitChoice(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.recruitChoice())
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].activeCells = 1
		self.assertEqual(app.recruitChoice(), "Gulf States")
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].cadre = 1
		self.assertEqual(app.recruitChoice(), "Gulf States")
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].cadre = 0
		app.map["Iraq"].governance = 1
		app.map["Iraq"].activeCells = 1
		for i in range(10):
			retVal = app.recruitChoice()
			self.assertTrue(retVal in ["Iraq", "Gulf States"])
		app.map["Iraq"].activeCells = 0
		app.map["Iraq"].cadre = 1
		self.assertEqual(app.recruitChoice(), "Gulf States")
		app.map["Iraq"].troopCubes = 2
		self.assertEqual(app.recruitChoice(), "Iraq")
		app.map["Gulf States"].besieged = 1
		self.assertEqual(app.recruitChoice(), "Gulf States")
		app.map["Russia"].sleeperCells = 1
		self.assertEqual(app.recruitChoice(), "Russia")
		app.map["Philippines"].sleeperCells = 1
		self.assertEqual(app.recruitChoice(), "Philippines")
		app.map["Iraq"].governance = 4
		app.map["Iraq"].activeCells = 6
		self.assertEqual(app.recruitChoice(), "Philippines")
		app.map["Iraq"].activeCells = 5
		self.assertEqual(app.recruitChoice(), "Iraq")
		app.map["Gulf States"].regimeChange = 1
		app.map["Gulf States"].activeCells = 1
		app.map["Gulf States"].troopCubes = 5
		self.assertEqual(app.recruitChoice(), "Iraq")
		app.map["Gulf States"].troopCubes = 6
		self.assertEqual(app.recruitChoice(), "Gulf States")
		
	def testExecuteRecruit(self):
	# Normal
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 1, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.cells, 14)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 1, [2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.cells, 15)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 2, [1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 13)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 2, [1,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.cells, 14)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 2, [2,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.cells, 15)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 3, [1,1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 3)
		self.assertEqual(app.cells, 12)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 3, [1,2,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 13)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 3, [2,1,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.cells, 14)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 3, [2,2,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.cells, 15)

	# Attractive
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 1, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 13)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 1, [2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.cells, 15)

		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 2, [1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 4)
		self.assertEqual(app.cells, 11)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 2, [1,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 13)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 2, [2,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.cells, 15)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 3, [1,1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 6)
		self.assertEqual(app.cells, 9)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 3, [1,2,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 4)
		self.assertEqual(app.cells, 11)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 3, [2,1,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 13)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 15
		unusedOps = app.executeRecruit("United States", 3, [2,2,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.cells, 15)
		
	# not enough cells		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 1
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 2, [1,1])
		self.assertEqual(unusedOps, 1)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.cells, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 2
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 3, [2,2,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.cells, 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 2
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 3, [1,2,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 2
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 3, [1,1,2])
		self.assertEqual(unusedOps, 1)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 0)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 1
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 2, [1,1])
		self.assertEqual(unusedOps, 1)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.cells, 0)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 2
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 2, [1,1])
		self.assertEqual(unusedOps, 1)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 0)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 3
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 2, [1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 3)
		self.assertEqual(app.cells, 0)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 3
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 2, [2,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 1)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 5
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 2, [2,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.cells, 3)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 5
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 2, [1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 4)
		self.assertEqual(app.cells, 1)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 5
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 3, [1,1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].sleeperCells, 5)
		self.assertEqual(app.cells, 0)
		
		app = Labyrinth(1, 2, testBlankScenarioSetup)
		app.cells = 4
		app.funding = 9
		unusedOps = app.executeRecruit("United States", 3, [1,1,1])
		self.assertEqual(unusedOps, 1)
		self.assertEqual(app.map["United States"].sleeperCells, 4)
		self.assertEqual(app.cells, 0)

	# IR RC
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		app.funding = 9
		app.map["Iraq"].governance = 3
		unusedOps = app.executeRecruit("Iraq", 1, [4])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Iraq"].sleeperCells, 0)
		self.assertEqual(app.cells, 15)
				
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		app.funding = 9
		app.map["Iraq"].governance = 4
		unusedOps = app.executeRecruit("Iraq", 1, [6])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Iraq"].sleeperCells, 1)
		self.assertEqual(app.cells, 14)
				
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.cells = 15
		app.funding = 9
		app.map["Iraq"].governance = 2
		app.map["Iraq"].regimeChange = 1
		unusedOps = app.executeRecruit("Iraq", 1, [6])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Iraq"].sleeperCells, 1)
		self.assertEqual(app.cells, 14)
				
class numCellsAvaialbe(unittest.TestCase):
	'''Test num cells available'''
	
	def testNumCellsAvaialable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.funding = 9
		self.cells = 15
		self.assertTrue(app.numCellsAvailable(), 15)
		self.cells = 14
		self.assertTrue(app.numCellsAvailable(), 14)
		self.cells = 13
		self.assertTrue(app.numCellsAvailable(), 13)
		self.cells = 12
		self.assertTrue(app.numCellsAvailable(), 12)
		self.cells = 11
		self.assertTrue(app.numCellsAvailable(), 11)
		self.cells = 10
		self.assertTrue(app.numCellsAvailable(), 10)
		self.cells = 9
		self.assertTrue(app.numCellsAvailable(), 9)
		self.cells = 8
		self.assertTrue(app.numCellsAvailable(), 8)
		self.cells = 7
		self.assertTrue(app.numCellsAvailable(), 7)
		self.cells = 6
		self.assertTrue(app.numCellsAvailable(), 6)
		self.cells = 5
		self.assertTrue(app.numCellsAvailable(), 5)
		self.cells = 4
		self.assertTrue(app.numCellsAvailable(), 4)
		self.cells = 3
		self.assertTrue(app.numCellsAvailable(), 3)
		self.cells = 2
		self.assertTrue(app.numCellsAvailable(), 2)
		self.cells = 1
		self.assertTrue(app.numCellsAvailable(), 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.funding = 8
		self.cells = 15
		self.assertTrue(app.numCellsAvailable(), 15)
		self.cells = 14
		self.assertTrue(app.numCellsAvailable(), 14)
		self.cells = 13
		self.assertTrue(app.numCellsAvailable(), 13)
		self.cells = 12
		self.assertTrue(app.numCellsAvailable(), 12)
		self.cells = 11
		self.assertTrue(app.numCellsAvailable(), 11)
		self.cells = 10
		self.assertTrue(app.numCellsAvailable(), 10)
		self.cells = 9
		self.assertTrue(app.numCellsAvailable(), 9)
		self.cells = 8
		self.assertTrue(app.numCellsAvailable(), 8)
		self.cells = 7
		self.assertTrue(app.numCellsAvailable(), 7)
		self.cells = 6
		self.assertTrue(app.numCellsAvailable(), 6)
		self.cells = 5
		self.assertTrue(app.numCellsAvailable(), 5)
		self.cells = 4
		self.assertTrue(app.numCellsAvailable(), 4)
		self.cells = 3
		self.assertTrue(app.numCellsAvailable(), 3)
		self.cells = 2
		self.assertTrue(app.numCellsAvailable(), 2)
		self.cells = 1
		self.assertTrue(app.numCellsAvailable(), 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.funding = 7
		self.cells = 15
		self.assertTrue(app.numCellsAvailable(), 15)
		self.cells = 14
		self.assertTrue(app.numCellsAvailable(), 14)
		self.cells = 13
		self.assertTrue(app.numCellsAvailable(), 13)
		self.cells = 12
		self.assertTrue(app.numCellsAvailable(), 12)
		self.cells = 11
		self.assertTrue(app.numCellsAvailable(), 11)
		self.cells = 10
		self.assertTrue(app.numCellsAvailable(), 10)
		self.cells = 9
		self.assertTrue(app.numCellsAvailable(), 9)
		self.cells = 8
		self.assertTrue(app.numCellsAvailable(), 8)
		self.cells = 7
		self.assertTrue(app.numCellsAvailable(), 7)
		self.cells = 6
		self.assertTrue(app.numCellsAvailable(), 6)
		self.cells = 5
		self.assertTrue(app.numCellsAvailable(), 5)
		self.cells = 4
		self.assertTrue(app.numCellsAvailable(), 4)
		self.cells = 3
		self.assertTrue(app.numCellsAvailable(), 3)
		self.cells = 2
		self.assertTrue(app.numCellsAvailable(), 2)
		self.cells = 1
		self.assertTrue(app.numCellsAvailable(), 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.funding = 6
		self.cells = 15
		self.assertTrue(app.numCellsAvailable(), 10)
		self.cells = 14
		self.assertTrue(app.numCellsAvailable(), 9)
		self.cells = 13
		self.assertTrue(app.numCellsAvailable(), 8)
		self.cells = 12
		self.assertTrue(app.numCellsAvailable(), 7)
		self.cells = 11
		self.assertTrue(app.numCellsAvailable(), 6)
		self.cells = 10
		self.assertTrue(app.numCellsAvailable(), 5)
		self.cells = 9
		self.assertTrue(app.numCellsAvailable(), 4)
		self.cells = 8
		self.assertTrue(app.numCellsAvailable(), 3)
		self.cells = 7
		self.assertTrue(app.numCellsAvailable(), 2)
		self.cells = 6
		self.assertTrue(app.numCellsAvailable(), 1)
		self.cells = 5
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 4
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 3
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 2
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 1
		self.assertTrue(app.numCellsAvailable(), 0)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.funding = 5
		self.cells = 15
		self.assertTrue(app.numCellsAvailable(), 10)
		self.cells = 14
		self.assertTrue(app.numCellsAvailable(), 9)
		self.cells = 13
		self.assertTrue(app.numCellsAvailable(), 8)
		self.cells = 12
		self.assertTrue(app.numCellsAvailable(), 7)
		self.cells = 11
		self.assertTrue(app.numCellsAvailable(), 6)
		self.cells = 10
		self.assertTrue(app.numCellsAvailable(), 5)
		self.cells = 9
		self.assertTrue(app.numCellsAvailable(), 4)
		self.cells = 8
		self.assertTrue(app.numCellsAvailable(), 3)
		self.cells = 7
		self.assertTrue(app.numCellsAvailable(), 2)
		self.cells = 6
		self.assertTrue(app.numCellsAvailable(), 1)
		self.cells = 5
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 4
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 3
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 2
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 1
		self.assertTrue(app.numCellsAvailable(), 0)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.funding = 4
		self.cells = 15
		self.assertTrue(app.numCellsAvailable(), 10)
		self.cells = 14
		self.assertTrue(app.numCellsAvailable(), 9)
		self.cells = 13
		self.assertTrue(app.numCellsAvailable(), 8)
		self.cells = 12
		self.assertTrue(app.numCellsAvailable(), 7)
		self.cells = 11
		self.assertTrue(app.numCellsAvailable(), 6)
		self.cells = 10
		self.assertTrue(app.numCellsAvailable(), 5)
		self.cells = 9
		self.assertTrue(app.numCellsAvailable(), 4)
		self.cells = 8
		self.assertTrue(app.numCellsAvailable(), 3)
		self.cells = 7
		self.assertTrue(app.numCellsAvailable(), 2)
		self.cells = 6
		self.assertTrue(app.numCellsAvailable(), 1)
		self.cells = 5
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 4
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 3
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 2
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 1
		self.assertTrue(app.numCellsAvailable(), 0)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.funding = 3
		self.cells = 15
		self.assertTrue(app.numCellsAvailable(), 5)
		self.cells = 14
		self.assertTrue(app.numCellsAvailable(), 4)
		self.cells = 13
		self.assertTrue(app.numCellsAvailable(), 3)
		self.cells = 12
		self.assertTrue(app.numCellsAvailable(), 2)
		self.cells = 11
		self.assertTrue(app.numCellsAvailable(), 1)
		self.cells = 10
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 9
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 8
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 7
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 6
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 5
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 4
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 3
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 2
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 1
		self.assertTrue(app.numCellsAvailable(), 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.funding = 2
		self.cells = 15
		self.assertTrue(app.numCellsAvailable(), 5)
		self.cells = 14
		self.assertTrue(app.numCellsAvailable(), 4)
		self.cells = 13
		self.assertTrue(app.numCellsAvailable(), 3)
		self.cells = 12
		self.assertTrue(app.numCellsAvailable(), 2)
		self.cells = 11
		self.assertTrue(app.numCellsAvailable(), 1)
		self.cells = 10
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 9
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 8
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 7
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 6
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 5
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 4
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 3
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 2
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 1
		self.assertTrue(app.numCellsAvailable(), 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.funding = 1
		self.cells = 15
		self.assertTrue(app.numCellsAvailable(), 5)
		self.cells = 14
		self.assertTrue(app.numCellsAvailable(), 4)
		self.cells = 13
		self.assertTrue(app.numCellsAvailable(), 3)
		self.cells = 12
		self.assertTrue(app.numCellsAvailable(), 2)
		self.cells = 11
		self.assertTrue(app.numCellsAvailable(), 1)
		self.cells = 10
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 9
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 8
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 7
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 6
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 5
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 4
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 3
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 2
		self.assertTrue(app.numCellsAvailable(), 0)
		self.cells = 1
		self.assertTrue(app.numCellsAvailable(), 0)
		
class travel(unittest.TestCase):
	'''Test Travel'''

	def testTravelFirstBox(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)

		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].besieged = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])

		app.map["Gulf States"].besieged = 0
		app.map["Gulf States"].aid = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])

		app.map["Gulf States"].aid = 0
		app.map["Gulf States"].regimeChange = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])

		app.map["Gulf States"].governance = 4
		app.map["Afghanistan"].governance = 3
		app.map["Afghanistan"].besieged = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Afghanistan"])

		app.map["Gulf States"].governance = 3
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])

		app.map["Iraq"].governance = 3
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
			
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].aid = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Pakistan"])
		
	def testTravelSecondBox(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)

		app.map["Afghanistan"].governance = 3
		app.map["Afghanistan"].troopCubes = 1
		app.map["Afghanistan"].sleeperCells = 4
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Afghanistan"])

		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].besieged = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])

		dest = app.travelDestinations(2)
		self.assertEqual(dest,["Gulf States","Afghanistan"])
		
	def testTravelThirdBox(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)

		app.map["Jordan"].governance = 2
		app.map["Iraq"].governance = 3
		app.map["Iraq"].sleeperCells = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Jordan"])

		app.map["Gulf States"].governance = 2
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])
		
		app.map["Gulf States"].governance = 3		
		app.map["Algeria/Tunisia"].governance = 2
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Jordan"])
		
		app.map["Germany"].sleeperCells = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Algeria/Tunisia"])
		
	def testTravelForthBox(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		
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
		#app.map["Philippines"]
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Philippines"])
	
	def testTravelMultiple(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		dest = app.travelDestinations(3)
		
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].besieged = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])
		
		app.map["Afghanistan"].governance = 3
		app.map["Afghanistan"].troopCubes = 1
		app.map["Afghanistan"].sleeperCells = 4
		dest = app.travelDestinations(2)
		self.assertEqual(dest,["Gulf States", "Afghanistan"])

		app.map["Jordan"].governance = 2
		app.map["Iraq"].governance = 3
		app.map["Iraq"].sleeperCells = 1
		dest = app.travelDestinations(3)
		self.assertEqual(dest,["Gulf States", "Afghanistan", "Jordan"])

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
		#app.map["Philippines"]
		dest = app.travelDestinations(3)
		self.assertEqual(dest,["Gulf States", "Afghanistan", "Jordan"])

		app.map["Gulf States"].governance = 4
		dest = app.travelDestinations(3)
		self.assertEqual(dest,["Afghanistan", "Jordan", "Philippines"])
		
		app.map["Kenya/Tanzania"].posture = ""
		phCount = 0
		ktCount = 0
		for i in range(100):
			dest = app.travelDestinations(3)
			if dest == ["Afghanistan", "Jordan", "Philippines"]:
				phCount += 1
			elif dest == ["Afghanistan", "Jordan", "Kenya/Tanzania"]:
				ktCount += 1
			self.assertTrue(dest == ["Afghanistan", "Jordan", "Philippines"] or dest == ["Afghanistan", "Jordan", "Kenya/Tanzania"])
		self.assertTrue(phCount > 0)
		self.assertTrue(ktCount > 0)

		app.map["United States"].posture = "Soft"
		app.map["China"].posture = "Soft"
		dest = app.travelDestinations(3)
		self.assertEqual(dest,["Afghanistan", "Jordan", "China"])
		
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
		
	def testTravelFrom(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)

		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].besieged = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])
		
		app.map["Lebanon"].governance = 2
		app.map["Lebanon"].activeCells = 1
		sources = app.travelSources(dest, 1)
		self.assertEqual(sources,["Lebanon"])

		app.map["Iraq"].governance = 2
		app.map["Iraq"].activeCells = 1
		sources = app.travelSources(dest, 1)
		self.assertEqual(sources,["Iraq"])
		
		app.map["Egypt"].governance = 2
		app.map["Egypt"].activeCells = 1
		app.map["Egypt"].regimeChange = 1
		app.map["Egypt"].troopCubes = 2
		sources = app.travelSources(dest, 1)
		self.assertEqual(sources,["Iraq"])
		app.map["Egypt"].activeCells = 3
		sources = app.travelSources(dest, 1)
		self.assertEqual(sources,["Egypt"])
		
		app.map["Yemen"].governance = 4
		app.map["Yemen"].activeCells = 3
		app.map["Yemen"].troopCubes = 2
		sources = app.travelSources(dest, 3)
		self.assertEqual(sources,["Egypt"])
		sources = app.travelSources(dest, 2)
		self.assertEqual(sources,["Yemen"])
		
	#multi	

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].besieged = 1
		
		app.map["Afghanistan"].governance = 3
		app.map["Afghanistan"].troopCubes = 1
		app.map["Afghanistan"].sleeperCells = 4

		app.map["Jordan"].governance = 2
		app.map["Iraq"].governance = 3
		app.map["Iraq"].sleeperCells = 1
		dest = app.travelDestinations(3)
		self.assertEqual(dest,["Gulf States", "Afghanistan", "Jordan"])

		app.map["Lebanon"].governance = 2
		app.map["Lebanon"].activeCells = 1

		app.map["Iraq"].governance = 2
		app.map["Iraq"].activeCells = 1
		
		app.map["Egypt"].governance = 2
		app.map["Egypt"].regimeChange = 1
		app.map["Egypt"].troopCubes = 2
		app.map["Egypt"].activeCells = 3
		
		app.map["Yemen"].governance = 4
		app.map["Yemen"].activeCells = 4
		app.map["Yemen"].troopCubes = 2
		sources = app.travelSources(dest, 3)
		self.assertEqual(sources,["Yemen", "Egypt", "Iraq"])
		
		app.map["Yemen"].activeCells = 5
		sources = app.travelSources(dest, 3)
		self.assertEqual(sources,["Yemen", "Yemen", "Egypt"])

		app.map["Yemen"].activeCells = 6
		sources = app.travelSources(dest, 3)
		self.assertEqual(sources,["Yemen", "Yemen", "Yemen"])

		app.map["Yemen"].activeCells = 4
		sources = app.travelSources(dest, 3)
		app.map["Egypt"].activeCells = 4
		sources = app.travelSources(dest, 3)
		self.assertEqual(sources,["Yemen", "Egypt", "Egypt"])

		app.map["Iraq"].governance = 2
		app.map["Iraq"].regimeChange = 1
		app.map["Iraq"].troopCubes = 2
		app.map["Iraq"].activeCells = 4
		app.map["Egypt"].activeCells = 0
		app.map["Egypt"].sleeperCells = 4
		sources = app.travelSources(dest, 3)
		self.assertEqual(sources,["Yemen", "Iraq", "Iraq"])

class resolvePlot(unittest.TestCase):
	'''Resolve Plots'''
	
	def testResolveNonMuslimNonUSPlots(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Germany"].plots = 1
		app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5,4], [])
		self.assertEqual(app.funding, 7)
		self.assertEqual(app.map["Germany"].posture, "Soft")
		self.assertEqual(app.map["Spain"].posture, "Hard")
		self.assertEqual(app.map["Scandinavia"].posture, "Soft")
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Germany"].plots, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Germany"].plots = 2
		app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5,4], [])
		self.assertEqual(app.funding, 7)
		self.assertEqual(app.map["Germany"].posture, "Soft")
		self.assertEqual(app.map["Spain"].posture, "Hard")
		self.assertEqual(app.map["Scandinavia"].posture, "Soft")
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Germany"].plots, 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Germany"].plots = 1
		app.resolvePlot("Germany", 2, 5, [], ["Spain", "Scandinavia"], [4,5], [])
		self.assertEqual(app.funding, 9)
		self.assertEqual(app.map["Germany"].posture, "Hard")
		self.assertEqual(app.map["Spain"].posture, "Soft")
		self.assertEqual(app.map["Scandinavia"].posture, "Hard")
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Germany"].plots, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Canada"].plots = 1
		app.resolvePlot("Canada", 2, 5, [], [], [], [])
		self.assertEqual(app.funding, 9)
		self.assertEqual(app.map["Canada"].posture, "Hard")
		self.assertEqual(app.map["Spain"].posture, "")
		self.assertEqual(app.map["Scandinavia"].posture, "")
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Canada"].plots, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Russia"].plots = 1
		app.resolvePlot("Russia", 2, 4, [], [], [], [])
		self.assertEqual(app.funding, 7)
		self.assertEqual(app.map["Russia"].posture, "Soft")
		self.assertEqual(app.map["Spain"].posture, "")
		self.assertEqual(app.map["Scandinavia"].posture, "")
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Russia"].plots, 0)
		
		app = Labyrinth(1, "WMD", testBlankScenarioSetup)
		app.map["Germany"].plots = 1
		app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5,4], [])
		self.assertEqual(app.funding, 7)
		self.assertEqual(app.map["Germany"].posture, "Soft")
		self.assertEqual(app.map["Spain"].posture, "Hard")
		self.assertEqual(app.map["Scandinavia"].posture, "Soft")
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Germany"].plots, 0)
		
		app = Labyrinth(1, "WMD", testBlankScenarioSetup)
		app.funding = 1
		app.map["Germany"].plots = 1
		app.resolvePlot("Germany", 3, 4, [], ["Spain", "Scandinavia"], [5,4], [])
		self.assertEqual(app.funding, 7)
		self.assertEqual(app.map["Germany"].posture, "Soft")
		self.assertEqual(app.map["Spain"].posture, "Hard")
		self.assertEqual(app.map["Scandinavia"].posture, "Soft")
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Germany"].plots, 0)
		
	def testResolveMuslimIranPlots(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 2
		app.map["Iraq"].aid = 1
		app.map["Iraq"].plots = 1
		app.resolvePlot("Iraq", 1, 0, [], [], [], [3])
		self.assertEqual(app.funding, 6)
		self.assertEqual(app.map["Iraq"].governance, 2)
		self.assertEqual(app.map["Iraq"].aid, 1)
		app.resolvePlot("Iraq", 1, 0, [], [], [], [2])
		self.assertEqual(app.funding, 7)
		self.assertEqual(app.map["Iraq"].governance, 3)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iraq"].plots, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 1
		app.map["Iraq"].aid = 1
		app.map["Iraq"].plots = 1
		app.resolvePlot("Iraq", 3, 0, [], [], [], [3,1,2])
		self.assertEqual(app.funding, 7)
		self.assertEqual(app.map["Iraq"].governance, 2)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 1
		app.map["Iraq"].aid = 1
		app.map["Iraq"].plots = 1
		app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3,1,2])
		self.assertEqual(app.funding, 7)
		self.assertEqual(app.map["Iraq"].governance, 2)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 3
		app.map["Iraq"].aid = 0
		app.map["Iraq"].plots = 1
		app.resolvePlot("Iraq", 3, 0, [], [], [], [3,3,3])
		self.assertEqual(app.funding, 6)
		self.assertEqual(app.map["Iraq"].governance, 3)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iran"].plots = 1
		app.resolvePlot("Iran", 3, 0, [], [], [], [3,3,3])
		self.assertEqual(app.funding, 6)
		self.assertEqual(app.map["Iran"].governance, 2)
		self.assertEqual(app.map["Iran"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iran"].plots, 0)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 3
		app.map["Iraq"].aid = 0
		app.map["Iraq"].plots = 1
		app.map["Iraq"].troopCubes = 1
		app.resolvePlot("Iraq", 3, 0, [], [], [], [3,3,3])
		self.assertEqual(app.funding, 6)
		self.assertEqual(app.map["Iraq"].governance, 3)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 6)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 3
		app.map["Iraq"].aid = 0
		app.map["Iraq"].plots = 1
		app.map["Iraq"].troopCubes = 1
		app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3,3,3])
		self.assertEqual(app.funding, 6)
		self.assertEqual(app.map["Iraq"].governance, 3)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 1)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
	def testResolveUSPlots(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].plots = 1
		app.map["United States"].posture = "Hard"
		app.resolvePlot("United States", 1, 4, [1,6,1], [], [], [])
		self.assertEqual(app.funding, 9)
		self.assertEqual(app.map["United States"].posture, "Soft")
		self.assertEqual(app.prestige, 6)
		self.assertEqual(app.map["United States"].plots, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].plots = 1
		app.map["United States"].posture = "Soft"
		app.resolvePlot("United States", 2, 4, [5,6,1], [], [], [])
		self.assertEqual(app.funding, 9)
		self.assertEqual(app.map["United States"].posture, "Soft")
		self.assertEqual(app.prestige, 8)
		self.assertEqual(app.map["United States"].plots, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].plots = 1
		app.map["United States"].posture = "Soft"
		app.resolvePlot("United States", 3, 5, [5,6,4], [], [], [])
		self.assertEqual(app.funding, 9)
		self.assertEqual(app.map["United States"].posture, "Hard")
		self.assertEqual(app.prestige, 11)
		self.assertEqual(app.map["United States"].plots, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.gameOver)
		app.map["United States"].plots = 1
		app.map["United States"].posture = "Soft"
		app.resolvePlot("United States", "WMD", 0, [], [], [], [])
		self.assertEqual(app.map["United States"].plots, 0)
		self.assertTrue(app.gameOver)

	def testResolveMuslimIranPlotsWithBacklash(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 2
		app.map["Iraq"].aid = 1
		app.map["Iraq"].plots = 1
		app.resolvePlot("Iraq", 1, 0, [], [], [], [3], True)
		self.assertEqual(app.funding, 4)
		self.assertEqual(app.map["Iraq"].governance, 2)
		self.assertEqual(app.map["Iraq"].aid, 1)
		app.resolvePlot("Iraq", 1, 0, [], [], [], [2], True)
		self.assertEqual(app.funding, 3)
		self.assertEqual(app.map["Iraq"].governance, 3)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iraq"].plots, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 1
		app.map["Iraq"].aid = 1
		app.map["Iraq"].plots = 1
		app.resolvePlot("Iraq", 3, 0, [], [], [], [3,1,2], True)
		self.assertEqual(app.funding, 3)
		self.assertEqual(app.map["Iraq"].governance, 2)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 1
		app.map["Iraq"].aid = 1
		app.map["Iraq"].plots = 1
		app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3,1,2], True)
		self.assertEqual(app.funding, 1)
		self.assertEqual(app.map["Iraq"].governance, 2)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 3
		app.map["Iraq"].aid = 0
		app.map["Iraq"].plots = 1
		app.resolvePlot("Iraq", 3, 0, [], [], [], [3,3,3], True)
		self.assertEqual(app.funding, 4)
		self.assertEqual(app.map["Iraq"].governance, 3)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iran"].plots = 1
		app.resolvePlot("Iran", 3, 0, [], [], [], [3,3,3], True)
		self.assertEqual(app.funding, 4)
		self.assertEqual(app.map["Iran"].governance, 2)
		self.assertEqual(app.map["Iran"].aid, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.map["Iran"].plots, 0)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 3
		app.map["Iraq"].aid = 0
		app.map["Iraq"].plots = 1
		app.map["Iraq"].troopCubes = 1
		app.resolvePlot("Iraq", 3, 0, [], [], [], [3,3,3], True)
		self.assertEqual(app.funding, 4)
		self.assertEqual(app.map["Iraq"].governance, 3)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 6)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].governance = 3
		app.map["Iraq"].aid = 0
		app.map["Iraq"].plots = 1
		app.map["Iraq"].troopCubes = 1
		app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3,3,3], True)
		self.assertEqual(app.funding, 1)
		self.assertEqual(app.map["Iraq"].governance, 3)
		self.assertEqual(app.map["Iraq"].aid, 0)
		self.assertEqual(app.prestige, 1)
		self.assertEqual(app.map["Iraq"].plots, 0)

class placePlots(unittest.TestCase):
	'''Place Plots'''
	
	def testPlacePlot(self):
	# no cells
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 1)
		unusedOps = app.executePlot(2, False, [1,2])
		self.assertEqual(unusedOps, 2)
		unusedOps = app.executePlot(3, True, [1,2,3])
		self.assertEqual(unusedOps, 3)
	
	# 1 cell in US
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 1
		unusedOps = app.executePlot(1, True, [2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 1)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.map["United States"].plots, 0)

		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 1)
		self.assertEqual(app.map["United States"].plots, 1)
	
	# 2 cells in us
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 2
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 1)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.map["United States"].plots, 1)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 2
		unusedOps = app.executePlot(2, True, [1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 2)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.map["United States"].plots, 2)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 2
		unusedOps = app.executePlot(2, True, [1,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 2)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.map["United States"].plots, 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 2
		unusedOps = app.executePlot(3, True, [1,2,3])
		self.assertEqual(unusedOps, 1)
		self.assertEqual(app.map["United States"].activeCells, 2)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.map["United States"].plots, 1)
		
	# 3 cells in us
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 3
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 1)
		self.assertEqual(app.map["United States"].sleeperCells, 2)
		self.assertEqual(app.map["United States"].plots, 1)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 3
		unusedOps = app.executePlot(2, True, [1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 2)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.map["United States"].plots, 2)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 3
		unusedOps = app.executePlot(2, True, [1,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 2)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.map["United States"].plots, 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 3
		unusedOps = app.executePlot(2, True, [1,2])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 2)
		self.assertEqual(app.map["United States"].sleeperCells, 1)
		self.assertEqual(app.map["United States"].plots, 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].sleeperCells = 3
		unusedOps = app.executePlot(3, True, [1,1,3])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["United States"].activeCells, 3)
		self.assertEqual(app.map["United States"].sleeperCells, 0)
		self.assertEqual(app.map["United States"].plots, 2)
	
	# Low prestige, no GWOT penalty
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.funding = 8
		app.map["Israel"].sleeperCells = 1
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 1
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 1
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Israel"].activeCells, 1)
		self.assertEqual(app.map["Israel"].sleeperCells, 0)
		self.assertEqual(app.map["Israel"].plots, 1)
		self.assertEqual(app.map["Canada"].plots, 0)
		self.assertEqual(app.map["Iraq"].plots, 0)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.funding = 8
		app.map["Israel"].sleeperCells = 1
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 1
		app.map["Iraq"].governance = 2
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 1
		unusedOps = app.executePlot(2, True, [1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Israel"].activeCells, 1)
		self.assertEqual(app.map["Israel"].sleeperCells, 0)
		self.assertEqual(app.map["Israel"].plots, 1)
		self.assertEqual(app.map["Canada"].plots, 0)
		self.assertEqual(app.map["Iraq"].activeCells, 1)
		self.assertEqual(app.map["Iraq"].plots, 1)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.map["Israel"].sleeperCells = 1
		app.map["United States"].posture = "Soft"
		app.map["Iraq"].governance = 2
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 1
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Israel"].activeCells, 0)
		self.assertEqual(app.map["Israel"].sleeperCells, 1)
		self.assertEqual(app.map["Israel"].plots, 0)
		self.assertEqual(app.map["Canada"].plots, 0)
		self.assertEqual(app.map["Iraq"].activeCells, 1)
		self.assertEqual(app.map["Iraq"].plots, 1)
		
	# Low prestige, yes GWOT penalty
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.map["Israel"].sleeperCells = 1
		app.map["Spain"].posture = "Soft"
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 1
		app.map["Iraq"].governance = 2
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 1
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Israel"].activeCells, 0)
		self.assertEqual(app.map["Israel"].sleeperCells, 1)
		self.assertEqual(app.map["Israel"].plots, 0)
		self.assertEqual(app.map["Canada"].plots, 0)
		self.assertEqual(app.map["Iraq"].plots, 1)
		
	# Funding section
		# Low prestige, yes GWOT penalty
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.funding = 9
		app.map["Israel"].sleeperCells = 1
		app.map["Spain"].posture = "Soft"
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 1
		app.map["Iraq"].governance = 2
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 0
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 1)
		self.assertEqual(app.map["Israel"].activeCells, 0)
		self.assertEqual(app.map["Israel"].sleeperCells, 1)
		self.assertEqual(app.map["Israel"].plots, 0)
		self.assertEqual(app.map["Canada"].plots, 0)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		# Low prestige, yes GWOT penalty
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.funding = 8
		app.map["Israel"].sleeperCells = 1
		app.map["Spain"].posture = "Soft"
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 0
		app.map["Iraq"].governance = 2
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 0
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Israel"].activeCells, 1)
		self.assertEqual(app.map["Israel"].sleeperCells, 0)
		self.assertEqual(app.map["Israel"].plots, 1)
		self.assertEqual(app.map["Canada"].plots, 0)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		# Low prestige, yes GWOT penalty
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.funding = 8
		app.map["Israel"].sleeperCells = 1
		app.map["Spain"].posture = "Soft"
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 1
		app.map["Iraq"].governance = 2
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 0
		unusedOps = app.executePlot(2, True, [1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Israel"].activeCells, 1)
		self.assertEqual(app.map["Israel"].sleeperCells, 0)
		self.assertEqual(app.map["Israel"].plots, 1)
		self.assertEqual(app.map["Canada"].plots, 1)
		self.assertEqual(app.map["Iraq"].plots, 0)
	
		# Low prestige, yes GWOT penalty
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.funding = 8
		app.map["Israel"].sleeperCells = 1
		app.map["Spain"].posture = "Soft"
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 1
		app.map["Iraq"].governance = 2
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 0
		unusedOps = app.executePlot(3, True, [1,1,1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Israel"].activeCells, 1)
		self.assertEqual(app.map["Israel"].sleeperCells, 0)
		self.assertEqual(app.map["Israel"].plots, 1)
		self.assertEqual(app.map["Canada"].plots, 1)
		self.assertEqual(app.map["Iraq"].plots, 1)
		
	# High prestige
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 4
		app.markers = ["Abu Sayyaf"]
		app.map["Israel"].sleeperCells = 1
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 1
		app.map["Iraq"].governance = 2
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 1
		app.map["Iraq"].troopCubes = 1
		app.map["Philippines"].sleeperCells = 1
		app.map["Philippines"].troopCubes = 1
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Israel"].activeCells, 0)
		self.assertEqual(app.map["Israel"].sleeperCells, 1)
		self.assertEqual(app.map["Israel"].plots, 0)
		self.assertEqual(app.map["Canada"].plots, 0)
		self.assertEqual(app.map["Iraq"].plots, 0)
		self.assertEqual(app.map["Philippines"].activeCells, 1)
		self.assertEqual(app.map["Philippines"].sleeperCells, 0)
		self.assertEqual(app.map["Philippines"].plots, 1)
		
	# priorities box
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.map["Israel"].sleeperCells = 0
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 1
		app.map["Spain"].posture = "Soft"
		app.map["Spain"].sleeperCells = 0
		app.map["Iraq"].governance = 1
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 1
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].aid = 1
		unusedOps = app.executePlot(1, True, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Iraq"].plots, 0)
		self.assertEqual(app.map["Gulf States"].plots, 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 3
		app.map["Israel"].sleeperCells = 0
		app.map["Canada"].posture = "Soft"
		app.map["Canada"].sleeperCells = 1
		app.map["Spain"].posture = "Soft"
		app.map["Spain"].sleeperCells = 0
		app.map["Iraq"].governance = 1
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].aid = 1
		app.map["Gulf States"].governance = 2
		app.map["Gulf States"].sleeperCells = 1
		app.map["Gulf States"].aid = 1
		unusedOps = app.executePlot(1, False, [1])
		self.assertEqual(unusedOps, 0)
		self.assertEqual(app.map["Iraq"].plots, 1)
		self.assertEqual(app.map["Gulf States"].plots, 0)
		
class isAdjacent(unittest.TestCase):
	'''Test isAdjacent'''
	
	def testIsAdjacent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.isAdjacent("Iran","Iraq"))
		self.assertTrue(app.isAdjacent("Germany","Spain"))
		self.assertTrue(app.isAdjacent("Libya","Italy"))
		self.assertTrue(app.isAdjacent("Benelux","Russia"))
		self.assertTrue(app.isAdjacent("Lebanon","France"))
		self.assertFalse(app.isAdjacent("United States","Lebanon"))

class countryResources(unittest.TestCase):
	'''Test countryResources'''
	
	def testCountryResources(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
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

class countryDistance(unittest.TestCase):
	'''Test countryDistance'''
	
	def testIsAdjacent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.countryDistance("Iran","Iran") == 0)
		self.assertTrue(app.countryDistance("Iran","Iraq") == 1)
		self.assertTrue(app.countryDistance("Iran","Sudan") == 4)
		self.assertTrue(app.countryDistance("Thailand","United States") == 2)
		self.assertTrue(app.countryDistance("Russia","Morocco") == 2)
		
class card1(unittest.TestCase):
	'''Backlash'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["1"].playable("US", app))
		app.map["Canada"].plots = 1
		self.assertFalse(app.deck["1"].playable("US", app))
		app.map["Iraq"].plots = 1
		self.assertTrue(app.deck["1"].playable("US", app))
		
	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.backlashInPlay)
		app.deck["1"].playEvent("US", app)
		self.assertFalse(app.backlashInPlay)
		app.map["United States"].plots = 1
		app.deck["1"].playEvent("US", app)
		self.assertFalse(app.backlashInPlay)
		app.map["Iraq"].plots = 1
		app.deck["1"].playEvent("US", app)
		self.assertTrue(app.backlashInPlay)
		
class card2(unittest.TestCase):
	'''Biometrics'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["2"].playable("US", app))
		
	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse("Biometrics" in app.lapsing)
		app.deck["2"].playEvent("US", app)
		self.assertTrue("Biometrics" in app.lapsing)
		app.do_turn("")
		self.assertFalse("Biometrics" in app.lapsing)
		
	def testTravelDestination(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].besieged = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])
		app.deck["2"].playEvent("US", app)
		dest = app.travelDestinations(1)
		self.assertTrue("Biometrics" in app.lapsing)
		self.assertEqual(dest,[])
		app.map["Iraq"].sleeperCells = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])
		
	def testTravelSource(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].besieged = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])
		app.deck["2"].playEvent("US", app)
		dest = app.travelDestinations(1)
		self.assertEqual(dest,[])
		app.map["Iraq"].sleeperCells = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])
		app.map["Sudan"].governance = 4		
		app.map["Sudan"].sleeperCells = 4	
		sources = app.travelSources(dest, 1)
		self.assertEqual(sources,["Iraq"])
		
	def testTravelToGood(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Gulf States"].governance = 1
		app.map["Gulf States"].besieged = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])
		app.deck["2"].playEvent("US", app)
		dest = app.travelDestinations(1)
		self.assertEqual(dest,[])
		app.map["Iraq"].sleeperCells = 1
		dest = app.travelDestinations(1)
		self.assertEqual(dest,["Gulf States"])
		app.map["Sudan"].governance = 4		
		app.map["Sudan"].sleeperCells = 4	
		sources = app.travelSources(dest, 1)
		self.assertEqual(sources,["Iraq"])
		app.handleTravel(1)

class card3(unittest.TestCase):
	'''CRT'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["3"].playable("US", app))
		app.do_reassessment("")
		self.assertTrue(app.deck["3"].playable("US", app))

	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.do_reassessment("")
		self.assertFalse("CRT" in app.map["Russia"].markers)
		self.assertFalse("CRT" in app.map["Central Asia"].markers)
		app.map["Central Asia"].alignment = "Adversary"
		app.deck["3"].playEvent("US", app)
		self.assertTrue("CRT" in app.map["Russia"].markers)
		self.assertFalse("CRT" in app.map["Central Asia"].markers)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.do_reassessment("")
		self.assertFalse("CRT" in app.map["Russia"].markers)
		self.assertFalse("CRT" in app.map["Central Asia"].markers)
		app.map["Central Asia"].alignment = "Neutral"
		app.deck["3"].playEvent("US", app)
		self.assertTrue("CRT" in app.map["Russia"].markers)
		self.assertTrue("CRT" in app.map["Central Asia"].markers)
		print app.map["Russia"].countryStr()
		self.assertTrue("Markers: CRT" in app.map["Russia"].countryStr())
		self.assertTrue("Markers: CRT" in app.map["Central Asia"].countryStr())
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.do_reassessment("")
		self.assertFalse("CRT" in app.map["Russia"].markers)
		self.assertFalse("CRT" in app.map["Central Asia"].markers)
		app.map["Central Asia"].alignment = "Ally"
		app.deck["3"].playEvent("US", app)
		self.assertTrue("CRT" in app.map["Russia"].markers)
		self.assertTrue("CRT" in app.map["Central Asia"].markers)

class card4(unittest.TestCase):
	'''Moro Talks'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["4"].playable("US", app))

	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.map["Philippines"].posture == "")
		self.assertTrue(app.funding == 5)
		app.deck["4"].playEvent("US", app)
		self.assertTrue("Moro Talks" in app.markers)
		self.assertTrue(app.map["Philippines"].posture == "Soft" or app.map["Philippines"].posture == "Hard")
		self.assertTrue(app.funding == 4)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.funding = 1
		self.assertTrue(app.map["Philippines"].posture == "")
		self.assertTrue(app.funding == 1)
		app.deck["4"].playEvent("US", app)
		self.assertTrue(app.map["Philippines"].posture == "Soft" or app.map["Philippines"].posture == "Hard")
		self.assertTrue(app.funding == 1)

class card5(unittest.TestCase):
	'''NEST'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["5"].playable("US", app))
		
	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse("NEST" in app.markers)
		app.deck["5"].playEvent("US", app)
		self.assertTrue("NEST" in app.markers)
		
class card6and7(unittest.TestCase):
	'''Sanctions'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["6"].playable("US", app))
		self.assertFalse(app.deck["7"].playable("US", app))
		app.markers.append("Patriot Act")
		self.assertTrue(app.deck["6"].playable("US", app))
		self.assertTrue(app.deck["7"].playable("US", app))

	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.markers.append("Patriot Act")
		app.deck["6"].playEvent("US", app)
		self.assertTrue(app.funding == 3)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.markers.append("Patriot Act")
		app.deck["7"].playEvent("US", app)
		self.assertTrue(app.funding == 3)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.funding = 2
		app.markers.append("Patriot Act")
		app.deck["6"].playEvent("US", app)
		self.assertTrue(app.funding == 1)
		
class card8and9and10(unittest.TestCase):
	'''Special Forces'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["8"].playable("US", app))
		self.assertFalse(app.deck["9"].playable("US", app))
		self.assertFalse(app.deck["10"].playable("US", app))
		app.map["Iran"].sleeperCells = 1
		self.assertFalse(app.deck["8"].playable("US", app))
		self.assertFalse(app.deck["9"].playable("US", app))
		self.assertFalse(app.deck["10"].playable("US", app))
		app.map["Iran"].troopCubes = 1
		self.assertTrue(app.deck["8"].playable("US", app))
		self.assertTrue(app.deck["9"].playable("US", app))
		self.assertTrue(app.deck["10"].playable("US", app))
		app.map["Iran"].troopCubes = 0
		app.map["Iraq"].troopCubes = 1
		self.assertTrue(app.deck["8"].playable("US", app))
		self.assertTrue(app.deck["9"].playable("US", app))
		self.assertTrue(app.deck["10"].playable("US", app))
		
	def testPlayEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.listCountriesWithCellAndAdjacentTroops()
		app.map["Iran"].sleeperCells = 1
		app.map["Iraq"].troopCubes = 1
		app.listCountriesWithCellAndAdjacentTroops()

class card11(unittest.TestCase):
	'''Abbas'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["11"].playable("US", app))

	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["11"].playEvent("US", app)
		self.assertTrue(app.prestige == 8)
		self.assertTrue(app.funding == 3)
		self.assertTrue("Abbas" in app.markers)
		app.map["Israel"].plots = 1
		app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
		self.assertFalse("Abbas" in app.markers)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Syria")
		app.map["Syria"].governance = 4
		app.deck["11"].playEvent("US", app)
		self.assertTrue(app.prestige == 8)
		self.assertTrue(app.funding == 3)
		self.assertTrue("Abbas" in app.markers)
		app.map["Israel"].plots = 1
		app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
		self.assertFalse("Abbas" in app.markers)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Lebanon")
		app.map["Lebanon"].governance = 4
		app.deck["11"].playEvent("US", app)
		self.assertTrue(app.prestige == 7)
		self.assertTrue(app.funding == 5)
		self.assertTrue("Abbas" in app.markers)
		app.map["Israel"].plots = 1
		app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
		self.assertFalse("Abbas" in app.markers)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.troops = 4
		app.deck["11"].playEvent("US", app)
		self.assertTrue(app.prestige == 7)
		self.assertTrue(app.funding == 5)
		self.assertTrue("Abbas" in app.markers)
		app.map["Israel"].plots = 1
		app.resolvePlot("Israel", 1, [1], [], [], [], [], False)
		self.assertFalse("Abbas" in app.markers)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.prestige = 12
		app.funding = 2
		app.deck["11"].playEvent("US", app)
		self.assertTrue(app.prestige == 12)
		self.assertTrue(app.funding == 1)

class card12(unittest.TestCase):
	'''Al-Azhar'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["12"].playable("US", app))

	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.map["Egypt"].governance == 0)
		app.deck["12"].playEvent("US", app)
		self.assertTrue(app.map["Egypt"].governance != 0)
		self.assertTrue(app.funding == 1)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.map["Egypt"].governance == 0)
		app.map["Pakistan"].governance = 4
		app.deck["12"].playEvent("US", app)
		self.assertTrue(app.map["Egypt"].governance != 0)
		self.assertTrue(app.funding == 3)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.funding = 2
		self.assertTrue(app.map["Egypt"].governance == 0)
		app.deck["12"].playEvent("US", app)
		self.assertTrue(app.map["Egypt"].governance != 0)
		self.assertTrue(app.funding == 1)
		
class card13(unittest.TestCase):
	'''Anbar Awakening'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["13"].playable("US", app))
		app.map["Iraq"].troopCubes = 1
		self.assertTrue(app.deck["13"].playable("US", app))
		app.map["Iraq"].troopCubes = 0
		app.map["Syria"].troopCubes = 1
		self.assertTrue(app.deck["13"].playable("US", app))
		app.map["Syria"].troopCubes = 0
		self.assertFalse(app.deck["13"].playable("US", app))

	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].troopCubes = 1
		app.deck["13"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].aid > 0)
		self.assertTrue("Anbar Awakening" in app.markers)
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Syria"].troopCubes = 1
		app.deck["13"].playEvent("US", app)
		self.assertTrue(app.map["Syria"].aid > 0)
		self.assertTrue("Anbar Awakening" in app.markers)
						
class card14(unittest.TestCase):
	'''Covert Action'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["14"].playable("US", app))
		app.map["Iraq"].alignment = "Adversary"
		self.assertTrue(app.deck["14"].playable("US", app))

	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.listAdversaryCountries()
		app.map["Iran"].alignment = "Adversary"
		app.map["Iraq"].alignment = "Adversary"
		app.listAdversaryCountries()

class card15(unittest.TestCase):
	'''Ethiopia Strikes'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["15"].playable("US", app))
		app.map["Somalia"].governance = 4
		self.assertTrue(app.deck["15"].playable("US", app))
		app.map["Somalia"].governance = 3
		self.assertFalse(app.deck["15"].playable("US", app))
		app.map["Sudan"].governance = 4
		self.assertTrue(app.deck["15"].playable("US", app))

	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Somalia"].governance = 4
		app.map["Somalia"].alignment = "Adversary"
		app.deck["15"].playEvent("US", app)
		self.assertTrue(app.map["Somalia"].governance == 3)
		self.assertTrue(app.map["Somalia"].alignment == "Neutral")
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Sudan"].governance = 4
		app.map["Sudan"].alignment = "Adversary"
		app.deck["15"].playEvent("US", app)
		self.assertTrue(app.map["Sudan"].governance == 3)
		self.assertTrue(app.map["Sudan"].alignment == "Neutral")

class card16(unittest.TestCase):
	'''Euro-Islam'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["16"].playable("US", app))

	def testEvent(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.executeCardEuroIslam("Hard")
		self.assertTrue(app.map["Benelux"].posture == "Hard")
		self.assertTrue(app.funding == 4)
		app.map["Iraq"].governance = 4
		app.executeCardEuroIslam("Soft")
		self.assertTrue(app.map["Benelux"].posture == "Soft")
		self.assertTrue(app.funding == 4)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.funding = 1
		app.executeCardEuroIslam("Hard")
		self.assertTrue(app.map["Benelux"].posture == "Hard")
		self.assertTrue(app.funding == 1)

class card17(unittest.TestCase):
	'''FSB'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["17"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ['y'])
		app.map["Central Asia"].activeCells = 1
		app.map["Russia"].activeCells = 1
		app.deck["17"].playEvent("US", app)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup, ['y'])
		app.map["Russia"].activeCells = 1
		app.deck["17"].playEvent("US", app)
	
		app = Labyrinth(1, 1, testBlankScenarioSetup, ['y'])
		app.map["Central Asia"].sleeperCells = 1
		app.deck["17"].playEvent("US", app)

class card18(unittest.TestCase):
	'''Intel Community'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["18"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["18"].playEvent("US", app)
	
class card19(unittest.TestCase):
	'''Kemalist Republic'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["19"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["19"].playEvent("US", app)
		self.assertTrue(app.map["Turkey"].governance == 2)
		self.assertTrue(app.map["Turkey"].alignment == "Ally")
	
class card20(unittest.TestCase):
	'''King Abdullah'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["20"].playable("US", app))
		self.assertTrue(app.funding == 5)
		self.assertTrue(app.prestige == 7)

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["20"].playEvent("US", app)
		self.assertTrue(app.map["Jordan"].governance == 2)
		self.assertTrue(app.map["Jordan"].alignment == "Ally")
		self.assertTrue(app.funding == 4)
		self.assertTrue(app.prestige == 8)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.funding = 1
 		app.prestige = 12
		app.deck["20"].playEvent("US", app)
		self.assertTrue(app.map["Jordan"].governance == 2)
		self.assertTrue(app.map["Jordan"].alignment == "Ally")
		self.assertTrue(app.funding == 1)
		self.assertTrue(app.prestige == 12)

class card21(unittest.TestCase):
	'''Let's Roll'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["21"].playable("US", app))
		app.map["Canada"].plots = 1
		self.assertTrue(app.deck["21"].playable("US", app))
		app.map["Canada"].plots = 0
		self.assertFalse(app.deck["21"].playable("US", app))
		app.map["Saudi Arabia"].governance = 2
		app.map["Saudi Arabia"].plots = 1
		self.assertFalse(app.deck["21"].playable("US", app))
		app.map["Saudi Arabia"].governance = 1
		self.assertTrue(app.deck["21"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Canada"].plots = 1
		app.map["Spain"].posture = "Soft"
		app.executeCardLetsRoll("Canada", "Spain", "Hard")
		self.assertTrue(app.map["Canada"].plots == 0)
		self.assertTrue(app.map["Spain"].posture == "Hard")

 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Saudi Arabi", "Spain","h"])
		app.map["Spain"].posture = "Soft"
 		app.map["Saudi Arabia"].governance = 1
		app.map["Saudi Arabia"].plots = 1
		app.deck["21"].playEvent("US", app)
 		self.assertTrue(app.map["Spain"].posture == "Hard")
		self.assertTrue(app.map["Saudi Arabia"].plots == 0)

class card22(unittest.TestCase):
	'''Mossad and Shin Bet'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["22"].playable("US", app))
		app.map["Israel"].sleeperCells = 1
		self.assertTrue(app.deck["22"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["22"].playable("US", app))
		app.map["Jordan"].sleeperCells = 1
		self.assertTrue(app.deck["22"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["22"].playable("US", app))
		app.map["Lebanon"].sleeperCells = 1
		self.assertTrue(app.deck["22"].playable("US", app))
		
	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
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

class card23and24and25(unittest.TestCase):
	'''Predator'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["23"].playable("US", app))
		app.map["Israel"].sleeperCells = 1
		self.assertFalse(app.deck["23"].playable("US", app))
		app.map["Iran"].sleeperCells = 1
		self.assertFalse(app.deck["23"].playable("US", app))
		app.map["Jordan"].sleeperCells = 1
		self.assertTrue(app.deck["23"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["24"].playable("US", app))
		app.map["Israel"].sleeperCells = 1
		self.assertFalse(app.deck["24"].playable("US", app))
		app.map["Iran"].sleeperCells = 1
		self.assertFalse(app.deck["24"].playable("US", app))
		app.map["Jordan"].sleeperCells = 1
		self.assertTrue(app.deck["24"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["25"].playable("US", app))
		app.map["Israel"].sleeperCells = 1
		self.assertFalse(app.deck["25"].playable("US", app))
		app.map["Iran"].sleeperCells = 1
		self.assertFalse(app.deck["25"].playable("US", app))
		app.map["Jordan"].sleeperCells = 1
		self.assertTrue(app.deck["25"].playable("US", app))
		
	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
		app.map["Iraq"].sleeperCells = 2
		app.deck["25"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].sleeperCells == 1)

class card26(unittest.TestCase):
	'''Quartet'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["26"].playable("US", app))
		app.markers.append("Abbas")
		self.assertTrue(app.deck["26"].playable("US", app))
		app.troops = 4
		self.assertFalse(app.deck["26"].playable("US", app))
		app.troops = 5
		self.assertTrue(app.deck["26"].playable("US", app))
		app.map["Egypt"].governance = 4
		self.assertFalse(app.deck["26"].playable("US", app))	
		
	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.markers.append("Abbas")
		app.deck["26"].playEvent("US", app)
		self.assertTrue(app.prestige == 9)
		self.assertTrue(app.funding == 2)
 		
class card27(unittest.TestCase):
	'''Saddam Captured'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["27"].playable("US", app))
		app.map["Iraq"].troopCubes = 1
		self.assertTrue(app.deck["27"].playable("US", app))
		
	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].troopCubes = 1
		app.deck["27"].playEvent("US", app)
		self.assertTrue("Saddam Captured" in app.markers)
		self.assertTrue(app.map["Iraq"].aid == 1)
		
class card28(unittest.TestCase):
	'''Sharia'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["28"].playable("US", app))
		app.map["Iraq"].besieged = 1
		self.assertTrue(app.deck["28"].playable("US", app))
		
	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].besieged = 1
		app.deck["28"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].besieged == 0)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Iraq"].besieged = 1
		app.map["Pakistan"].besieged = 1
		#app.deck["28"].playEvent("US", app)
		
class card29(unittest.TestCase):
	'''Tony Blair'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["29"].playable("US", app))
		
	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["United States"].posture = "Hard"
		#app.deck["29"].playEvent("US", app)
		#self.assertTrue(app.map["United Kingdom"].posture == "Hard")
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["United States"].posture = "Hard"
		app.executeNonMuslimWOI("Spain", 4)
		self.assertTrue(app.map["Spain"].posture == "Soft")
		app.executeNonMuslimWOI("France", 5)
		self.assertTrue(app.map["France"].posture == "Hard")
		#app.deck["29"].playEvent("US", app)

class card30(unittest.TestCase):
	'''UN Nation Building'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["30"].playable("US", app))
		app.map["Iraq"].regimeChange = 1
		self.assertTrue(app.deck["30"].playable("US", app))
		app.markers.append("Vieira de Mello Slain")
		self.assertFalse(app.deck["30"].playable("US", app))
		
	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["6"])
 		app.map["United States"].posture = "Hard"
 		app.map["Spain"].posture = "Soft"
 		app.map["France"].posture = "Soft"
 		app.map["Germany"].posture = "Soft"
 		app.map["Canada"].posture = "Soft"
		#app.map["Iraq"].regimeChange = 1
		app.map["Pakistan"].regimeChange = 1
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].alignment = "Ally"
		app.deck["30"].playEvent("US", app)
		self.assertTrue(app.map["Pakistan"].aid == 1)
		self.assertTrue(app.map["Pakistan"].governance == 2)

 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq", "6"])
 		app.map["United States"].posture = "Hard"
 		app.map["Spain"].posture = "Soft"
 		app.map["France"].posture = "Soft"
 		app.map["Germany"].posture = "Soft"
 		app.map["Canada"].posture = "Soft"
		app.map["Iraq"].regimeChange = 1
		app.map["Iraq"].governance = 3
		app.map["Iraq"].alignment = "Ally"
		app.map["Pakistan"].regimeChange = 1
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].alignment = "Ally"
		app.deck["30"].playEvent("US", app)
		self.assertTrue(app.map["Pakistan"].aid == 0)
		self.assertTrue(app.map["Pakistan"].governance == 3)
		self.assertTrue(app.map["Iraq"].aid == 1)
		self.assertTrue(app.map["Iraq"].governance == 2)

class card31(unittest.TestCase):
	'''Wiretapping'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["31"].playable("US", app))
		app.map["United States"].sleeperCells = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].activeCells = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].cadre = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].plots = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["31"].playable("US", app))
		app.map["United Kingdom"].sleeperCells = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United Kingdom"].activeCells = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United Kingdom"].cadre = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United Kingdom"].plots = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["31"].playable("US", app))
		app.map["Canada"].sleeperCells = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Canada"].activeCells = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Canada"].cadre = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Canada"].plots = 1
		self.assertTrue(app.deck["31"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Canada"].plots = 1
		app.markers.append("Leak-Wiretapping")
		self.assertFalse(app.deck["31"].playable("US", app))
		
	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
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

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
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

class card32(unittest.TestCase):
	'''Back Channel'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup, ["y","n"])
 		app.map["United States"].posture = "Hard"
		self.assertFalse(app.deck["32"].playable("US", app))
 		app.map["United States"].posture = "Soft"
		self.assertFalse(app.deck["32"].playable("US", app))

 		app.map["Iraq"].governance = 3
 		app.map["Iraq"].alignment = "Adversary"
 		app.map["Pakistan"].alignment = "Adversary"
 		print "Say yes"
		self.assertTrue(app.deck["32"].playable("US", app))
 		print "Say no"
		self.assertFalse(app.deck["32"].playable("US", app))
 		
	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["y","y","Pakistan"])
 		app.map["United States"].posture = "Soft"
 		app.map["Iraq"].governance = 3
 		app.map["Iraq"].alignment = "Adversary"
 		app.map["Pakistan"].governance = 4
 		app.map["Pakistan"].alignment = "Adversary"
 		app.deck["32"].playable("US", app)
 		app.deck["32"].playEvent("US", app)
 		self.assertTrue(app.map["Iraq"].alignment == "Adversary")
 		self.assertTrue(app.map["Pakistan"].alignment == "Neutral")

 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["n", "n"])
 		app.map["United States"].posture = "Soft"
 		app.map["Iraq"].governance = 3
 		app.map["Iraq"].alignment = "Adversary"
 		app.map["Pakistan"].governance = 4
 		app.map["Pakistan"].alignment = "Adversary"
 		app.deck["32"].playable("US", app)
 		app.deck["32"].playEvent("US", app)
 		self.assertTrue(app.map["Iraq"].alignment == "Adversary")
 		self.assertTrue(app.map["Pakistan"].alignment == "Adversary")

class card33(unittest.TestCase):
	'''Benazir Bhutto'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["33"].playable("US", app))
		app.markers.append("Bhutto Shot")
		self.assertFalse(app.deck["33"].playable("US", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["33"].playable("US", app))
 		app.map["Pakistan"].governance = 4
		self.assertFalse(app.deck["33"].playable("US", app))

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Afghanistan"].governance = 4
		self.assertFalse(app.deck["33"].playable("US", app))

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["India"].governance = 4
		self.assertFalse(app.deck["33"].playable("US", app))

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Gulf States"].governance = 4
		self.assertFalse(app.deck["33"].playable("US", app))

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Indonesia/Malaysia"].governance = 4
		self.assertFalse(app.deck["33"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Pakistan"].governance = 3
 		app.deck["33"].playEvent("US", app)
 		self.assertTrue(app.map["Pakistan"].governance == 2)

# no jihad in Pakistan
		app = Labyrinth(1, 1, test3ScenarioSetup)
		app.map["Gulf States"].activeCells = 0
		app.map["Gulf States"].sleeperCells = 0
		app.map["Pakistan"].activeCells = 0
		self.assertEqual(app.minorJihadInGoodFairChoice(1), False)
		app.map["Pakistan"].governance = 2
		app.map["Pakistan"].activeCells = 1
		self.assertEqual(app.minorJihadInGoodFairChoice(1), [("Pakistan",1)])
  		app.deck["33"].playEvent("US", app)
		self.assertEqual(app.minorJihadInGoodFairChoice(1), False)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertEqual(app.majorJihadPossible(3), [])
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].activeCells = 5
		self.assertEqual(app.majorJihadPossible(3), ["Pakistan"])
  		app.deck["33"].playEvent("US", app)
		self.assertEqual(app.majorJihadPossible(3), [])
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].activeCells = 5
		app.map["Iraq"].governance = 3
		app.map["Iraq"].activeCells = 5
		self.assertEqual(app.majorJihadChoice(3), "Pakistan")
  		app.deck["33"].playEvent("US", app)
		self.assertEqual(app.majorJihadPossible(3), ["Iraq"])

class card34(unittest.TestCase):
	'''Enhanced Measures'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["34"].playable("US", app))
		app.map["Iraq"].cadre = 1
		app.map["Iraq"].governance = 3
		app.map["Iraq"].alignment = "Neutral"
		app.map["Iraq"].troopCubes = 2
		self.assertTrue(app.deck["34"].playable("US", app))
		app.markers.append("Leak-Enhanced Measures")
		self.assertFalse(app.deck["34"].playable("US", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["United States"].posture = "Soft"
		app.map["Iraq"].cadre = 1
		app.map["Iraq"].governance = 3
		app.map["Iraq"].alignment = "Neutral"
		app.map["Iraq"].troopCubes = 2
		self.assertFalse(app.deck["34"].playable("US", app))
		
	def testEvent(self):
  		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
		app.map["Iraq"].cadre = 1
		app.map["Iraq"].governance = 3
		app.map["Iraq"].alignment = "Neutral"
		app.map["Iraq"].troopCubes = 2
		app.map["Pakistan"].cadre = 1
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].alignment = "Neutral"
		app.map["Pakistan"].troopCubes = 2
 		app.deck["34"].playEvent("US", app)
		self.assertTrue("Enhanced Measures" in app.markers)
		self.assertTrue(app.map["Pakistan"].cadre == 1)
		self.assertTrue(app.map["Iraq"].cadre == 0)
		
class card35(unittest.TestCase):
	'''Hajib'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["35"].playable("US", app))
		app.map["Iraq"].governance = 4
		self.assertFalse(app.deck["35"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["h"])
 		app.deck["35"].playEvent("US", app)
 		self.assertTrue(app.map["Turkey"].governance <= 2)
 		self.assertTrue(app.map["Turkey"].governance != 0)
 		self.assertTrue(app.map["Turkey"].alignment != "")
		print "Say Hard"
 		self.assertTrue(app.map["France"].posture == "Hard")
		self.assertTrue(app.funding == 3)

class card36(unittest.TestCase):
	'''Indo-Pakistani Talks'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["36"].playable("US", app))
		app.map["Pakistan"].governance = 4
		self.assertFalse(app.deck["36"].playable("US", app))
		app.map["Pakistan"].governance = 3
		self.assertFalse(app.deck["36"].playable("US", app))
		app.map["Pakistan"].governance = 2
		self.assertTrue(app.deck["36"].playable("US", app))
		app.map["Pakistan"].governance = 1
		self.assertTrue(app.deck["36"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["s","1"])
		app.map["Pakistan"].governance = 2
		app.map["Pakistan"].alignment = "Adversary"
  		app.deck["36"].playEvent("US", app)
  		self.assertTrue(app.map["Pakistan"].alignment == "Ally")
  		self.assertTrue("Indo-Pakistani Talks" in app.markers)
  		self.assertTrue(app.map["India"].posture == "Soft")
  		app.map["India"].plots = 1
  		app.do_plot("")
   		self.assertFalse("Indo-Pakistani Talks" in app.markers)
 		
class card37(unittest.TestCase):
	'''Iraqi WMD'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["37"].playable("US", app))
		app.map["Iraq"].governance = 3
		app.map["Iraq"].alignment = "Adversary"
		self.assertTrue(app.deck["37"].playable("US", app))
		app.map["United States"].posture = "Soft"
		self.assertFalse(app.deck["37"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
   		app.deck["37"].playEvent("US", app)
   		self.assertTrue("Iraqi WMD" in app.markers)
   		app.handleRegimeChange("Iraq", "track", 6, 4, (4, 4, 4))
   		self.assertFalse("Iraqi WMD" in app.markers)

class card38(unittest.TestCase):
	'''Libyan Desl'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["38"].playable("US", app))
		app.map["Libya"].governance = 3
		self.assertFalse(app.deck["38"].playable("US", app))
		app.map["Iraq"].alignment = "Ally"
		self.assertTrue(app.deck["38"].playable("US", app))
		app.map["Iraq"].alignment = "Neutral"
		self.assertFalse(app.deck["38"].playable("US", app))
		app.map["Syria"].alignment = "Ally"
		self.assertTrue(app.deck["38"].playable("US", app))
		app.map["Libya"].governance = 2
		self.assertFalse(app.deck["38"].playable("US", app))
		app.map["Libya"].governance = 4
		self.assertFalse(app.deck["38"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup,["france", "s", "Spain", "h"])
		app.map["Libya"].governance = 3
		app.map["Iraq"].alignment = "Ally"
		app.deck["38"].playEvent("US", app)
		self.assertTrue("Libyan Deal" in app.markers)
		self.assertTrue(app.prestige == 8)
		self.assertTrue(app.map["France"].posture == "Soft")
		self.assertTrue(app.map["Spain"].posture == "Hard")

class card39(unittest.TestCase):
	'''Libyan WMD'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["39"].playable("US", app))
		app.map["Libya"].governance = 3
		app.map["Libya"].alignment = "Adversary"
		self.assertTrue(app.deck["39"].playable("US", app))
		app.map["United States"].posture = "Soft"
		self.assertFalse(app.deck["39"].playable("US", app))
		app.map["United States"].posture = "Hard"
		self.assertTrue(app.deck["39"].playable("US", app))
		app.markers.append("Libyan Deal")
		self.assertFalse(app.deck["39"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
   		app.deck["39"].playEvent("US", app)
   		self.assertTrue("Libyan WMD" in app.markers)
   		app.handleRegimeChange("Libya", "track", 6, 4, (4, 4, 4))
   		self.assertFalse("Libyan WMD" in app.markers)

class card40(unittest.TestCase):
	'''Mass Turnout'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["40"].playable("US", app))
		app.map["Libya"].governance = 3
		app.map["Libya"].alignment = "Adversary"
		self.assertFalse(app.deck["40"].playable("US", app))
		app.map["Libya"].regimeChange = 1
		self.assertTrue(app.deck["40"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Libya"].governance = 3
		app.map["Libya"].alignment = "Adversary"
		app.map["Libya"].regimeChange = 1
   		app.deck["40"].playEvent("US", app)
		self.assertTrue(app.map["Libya"].governance == 2)
   		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Libya"].governance = 2
		app.map["Libya"].alignment = "Adversary"
		app.map["Libya"].regimeChange = 1
		app.map["Libya"].aid = 1
   		app.deck["40"].playEvent("US", app)
		self.assertTrue(app.map["Libya"].governance == 1)
		self.assertTrue(app.map["Libya"].regimeChange == 0)
		self.assertTrue(app.map["Libya"].aid == 0)
  		
 		app = Labyrinth(1, 1, testBlankScenarioSetup,["Iraq"])
  		app.map["Libya"].governance = 2
		app.map["Libya"].alignment = "Adversary"
		app.map["Libya"].regimeChange = 1
		app.map["Libya"].aid = 1
  		app.map["Iraq"].governance = 2
		app.map["Iraq"].alignment = "Adversary"
		app.map["Iraq"].regimeChange = 1
		app.map["Iraq"].aid = 1
   		app.deck["40"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].governance == 1)
		self.assertTrue(app.map["Iraq"].regimeChange == 0)
		self.assertTrue(app.map["Iraq"].aid == 0)
  		
class card41(unittest.TestCase):
	'''NATO'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["41"].playable("US", app))
		app.map["Libya"].governance = 3
		app.map["Libya"].alignment = "Ally"
		app.map["Libya"].regimeChange = 1
		self.assertTrue(app.deck["41"].playable("US", app))
		app.map["Canada"].posture = "Soft"
		self.assertTrue(app.deck["41"].playable("US", app))
		app.map["Spain"].posture = "Soft"
		self.assertFalse(app.deck["41"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Libya", "track", "3"])
 		app.map["Libya"].governance = 3
		app.map["Libya"].alignment = "Ally"
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
   		
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
  		app.map["Libya"].governance = 2
		app.map["Libya"].alignment = "Adversary"
		app.map["Libya"].regimeChange = 1
		app.map["Libya"].aid = 1
  		app.map["Iraq"].governance = 2
		app.map["Iraq"].alignment = "Adversary"
		app.map["Iraq"].regimeChange = 1
		app.map["Iraq"].aid = 1
   		app.deck["41"].playEvent("US", app)
 		self.assertTrue(app.map["Iraq"].aid == 1)
		self.assertTrue(app.map["Iraq"].troops() == 2)
		self.assertTrue("NATO" in app.map["Iraq"].markers)
 		
class card42(unittest.TestCase):
	'''Pakistani Offensive'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["42"].playable("US", app))
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].alignment = "Ally"
		self.assertFalse(app.deck["42"].playable("US", app))
		app.map["Pakistan"].markers.append("FATA")
		self.assertTrue(app.deck["42"].playable("US", app))
		app.map["Pakistan"].alignment = "Neutral"
		self.assertFalse(app.deck["42"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].alignment = "Ally"
		app.map["Pakistan"].markers.append("FATA")
   		app.deck["42"].playEvent("US", app)
		self.assertTrue("FATA" not in app.map["Pakistan"].markers)

class card43(unittest.TestCase):
	'''Patriot Act'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["43"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
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

class card44(unittest.TestCase):
	'''Renditions'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["44"].playable("US", app))
		app.map["United States"].posture = "Soft"
		self.assertFalse(app.deck["44"].playable("US", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["44"].playable("US", app))
		app.markers.append("Leak-Renditions")
		self.assertFalse(app.deck["44"].playable("US", app))

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
		app.map["Iraq"].cadre = 1
		app.map["Iraq"].governance = 3
		app.map["Iraq"].alignment = "Neutral"
		app.map["Iraq"].troopCubes = 2
		app.map["Pakistan"].cadre = 1
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].alignment = "Neutral"
		app.map["Pakistan"].troopCubes = 2
 		app.deck["44"].playEvent("US", app)
		self.assertTrue("Renditions" in app.markers)
		self.assertTrue(app.map["Iraq"].cadre == 0)
	
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Pakistan"])
		app.map["Iraq"].cadre = 1
		app.map["Iraq"].governance = 3
		app.map["Iraq"].alignment = "Neutral"
		app.map["Iraq"].troopCubes = 2
		app.map["Pakistan"].cadre = 1
		app.map["Pakistan"].sleeperCells = 2
		app.map["Pakistan"].governance = 3
		app.map["Pakistan"].alignment = "Neutral"
		app.map["Pakistan"].troopCubes = 2
 		app.deck["44"].playEvent("US", app)
		self.assertTrue("Renditions" in app.markers)
		self.assertTrue(app.map["Pakistan"].cadre == 1)
		self.assertTrue(app.map["Pakistan"].sleeperCells == 0)
	
class card45(unittest.TestCase):
	'''Safer Now'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["45"].playable("US", app))
 		app.map["Iraq"].governance = 4
 		app.map["Iraq"].alignment = "Adversary"
		self.assertFalse(app.deck["45"].playable("US", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["45"].playable("US", app))
 		app.map["Iraq"].governance = 1
 		app.map["Iraq"].alignment = "Ally"
		self.assertTrue(app.deck["45"].playable("US", app))
 		app.map["Iraq"].cadre = 1
		self.assertTrue(app.deck["45"].playable("US", app))
 		app.map["Iraq"].plots = 1
		self.assertFalse(app.deck["45"].playable("US", app))
 		app.map["Iraq"].plots = 0
 		app.map["Iraq"].cadre = 0
 		app.map["Iraq"].sleeperCells = 1
		self.assertFalse(app.deck["45"].playable("US", app))
 		app.map["Iraq"].sleeperCells = 0
 		app.map["Iraq"].activeCells = 1
		self.assertFalse(app.deck["45"].playable("US", app))	

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["4", "Spain", "h"])
 		print "Enter 4 for posture role, Spain and Hard"
 		app.deck["45"].playEvent("US", app)
		self.assertTrue(app.map["United States"].posture == "Soft")
		self.assertTrue(app.prestige == 10)
		self.assertTrue(app.map["Spain"].posture == "Hard")

class card46(unittest.TestCase):
	'''Sistani'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["46"].playable("US", app))
 		app.map["Iraq"].governance = 2
 		app.map["Iraq"].alignment = "Ally"
 		app.map["Iraq"].regimeChange = 1
		self.assertFalse(app.deck["46"].playable("US", app))
 		app.map["Iraq"].cadre = 1
		self.assertFalse(app.deck["46"].playable("US", app))
 		app.map["Iraq"].sleeperCells = 1
		self.assertTrue(app.deck["46"].playable("US", app))
 		app.map["Iraq"].sleeperCells = 0
 		app.map["Iraq"].activeCells = 1
		self.assertTrue(app.deck["46"].playable("US", app))	

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["46"].playable("US", app))
 		app.map["Syria"].governance = 2
 		app.map["Syria"].alignment = "Ally"
 		app.map["Syria"].regimeChange = 1
		self.assertFalse(app.deck["46"].playable("US", app))
 		app.map["Syria"].cadre = 1
		self.assertFalse(app.deck["46"].playable("US", app))
 		app.map["Syria"].sleeperCells = 1
		self.assertFalse(app.deck["46"].playable("US", app))
 		app.map["Syria"].sleeperCells = 0
 		app.map["Syria"].activeCells = 1
		self.assertFalse(app.deck["46"].playable("US", app))	

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Iraq"].governance = 3
 		app.map["Iraq"].alignment = "Ally"
 		app.map["Iraq"].regimeChange = 1
 		app.map["Iraq"].sleeperCells = 1
  		app.deck["46"].playEvent("US", app)
  		self.assertTrue(app.map["Iraq"].governance == 2)
  		app.deck["46"].playEvent("US", app)
  		self.assertTrue(app.map["Iraq"].governance == 1)
  		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Iraq"].governance = 2
 		app.map["Iraq"].alignment = "Ally"
 		app.map["Iraq"].regimeChange = 1
 		app.map["Iraq"].sleeperCells = 1
 		app.map["Syria"].governance = 2
 		app.map["Syria"].alignment = "Ally"
 		app.map["Syria"].regimeChange = 1
 		app.map["Syria"].sleeperCells = 1
  		app.deck["46"].playEvent("US", app)
  		self.assertTrue(app.map["Iraq"].governance == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Lebanon"])
 		app.map["Iraq"].governance = 2
 		app.map["Iraq"].alignment = "Ally"
 		app.map["Iraq"].regimeChange = 1
 		app.map["Iraq"].sleeperCells = 1
 		app.map["Lebanon"].governance = 2
 		app.map["Lebanon"].alignment = "Ally"
 		app.map["Lebanon"].regimeChange = 1
 		app.map["Lebanon"].sleeperCells = 1
 		print "Choose Lebanon"
  		app.deck["46"].playEvent("US", app)
  		self.assertTrue(app.map["Lebanon"].governance == 1)

class card47(unittest.TestCase):
	'''The door of Itjihad was closed'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["47"].playable("US", app))	

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["47"].playEvent("US", app)
		self.assertTrue("The door of Itjihad was closed" in app.lapsing)
		self.assertFalse(app.deck["66"].playable("Jihadist", app))	
		self.assertFalse(app.deck["114"].playable("Jihadist", app))	
		app.do_turn("")
		self.assertFalse("The door of Itjihad was closed" in app.lapsing)
		self.assertTrue(app.deck["66"].playable("Jihadist", app))	
		self.assertTrue(app.deck["114"].playable("Jihadist", app))	

class card48(unittest.TestCase):
	'''Adam Gadahn'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup, ["n","y"])
		print "Say No"
		self.assertFalse(app.deck["48"].playable("Jihadist", app))
		print "Say Yes"
		self.assertTrue(app.deck["48"].playable("Jihadist", app))
		app.cells = 4
		self.assertFalse(app.deck["48"].playable("Jihadist", app))		
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["48"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
# 		app.deck["48"].playEvent("Jihadist", app)
		
class card49(unittest.TestCase):
	'''Al-Ittihad al-Islami'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["49"].playable("Jihadist", app))	
		app.cells = 1
		self.assertTrue(app.deck["49"].playable("Jihadist", app))	
		app.cells = 0
		self.assertTrue(app.deck["49"].playable("Jihadist", app))	

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["49"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.deck["49"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Somalia"].sleeperCells == 1)
		
class card50(unittest.TestCase):
	'''Ansar al-Islam'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["50"].playable("Jihadist", app))	
		app.map["Iraq"].governance = 1
		self.assertFalse(app.deck["50"].playable("Jihadist", app))	
		app.map["Iraq"].governance = 2
		self.assertTrue(app.deck["50"].playable("Jihadist", app))	
		app.map["Iraq"].governance = 3
		self.assertTrue(app.deck["50"].playable("Jihadist", app))	
		app.map["Iraq"].governance = 4
		self.assertTrue(app.deck["50"].playable("Jihadist", app))	

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["50"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.deck["50"].playEvent("Jihadist", app)
		app.map["Iraq"].governance = 2
 		self.assertTrue(app.map["Iraq"].sleeperCells == 1 or app.map["Iran"].sleeperCells == 1 )
		
class card51(unittest.TestCase):
	'''FREs'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["51"].playable("Jihadist", app))	
		app.map["Iraq"].changeTroops(1)
		self.assertTrue(app.deck["51"].playable("Jihadist", app))	

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["51"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].changeTroops(1)
 		app.deck["51"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 4)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.markers.append("Saddam Captured")
		app.testCountry("Iraq")
		app.map["Iraq"].changeTroops(1)
 		app.deck["51"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 2)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.cells = 3
		app.testCountry("Iraq")
		app.map["Iraq"].changeTroops(1)
 		app.deck["51"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 3)
		
class card52(unittest.TestCase):
	'''IEDs'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["52"].playable("Jihadist", app))	
		app.testCountry("Iraq")
		app.map["Iraq"].regimeChange = 1
		app.map["Iraq"].sleeperCells = 1
		self.assertTrue(app.deck["52"].playable("Jihadist", app))		

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["52"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.deck["52"].playEvent("Jihadist", app)
		
class card53(unittest.TestCase):
	'''Madrassas'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup, ["n","y"])
		print "Say No"
		self.assertFalse(app.deck["53"].playable("Jihadist", app))
		print "Say Yes"
		self.assertTrue(app.deck["53"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["53"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup, ["1"])
 		app.deck["53"].playEvent("Jihadist", app)
		
class card54(unittest.TestCase):
	'''Moqtada al-Sadr'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["54"].playable("Jihadist", app))
		app.map["Iraq"].changeTroops(1)
		self.assertTrue(app.deck["54"].playable("Jihadist", app))	
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["54"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
 		app.deck["54"].playEvent("Jihadist", app)
 		self.assertTrue("Sadr" in app.map["Iraq"].markers)
		
class card55(unittest.TestCase):
	'''Uyghur Jihad'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["55"].playable("Jihadist", app))	
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["55"].putsCell(app))			

	def testEvent(self):
 		for i in range(100):
 			app = Labyrinth(1, 1, testBlankScenarioSetup)
			app.deck["55"].playEvent("Jihadist", app)
			self.assertTrue(app.map["China"].posture != "")
			if app.map["China"].posture == "Soft":
				self.assertTrue(app.map["China"].sleeperCells == 1)
			else:
				self.assertTrue(app.map["Central Asia"].governance != 0)
				self.assertTrue(app.map["Central Asia"].sleeperCells == 1)
 			
class card56(unittest.TestCase):
	'''Vieira de Mello Slain'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["56"].playable("Jihadist", app))	
		app.testCountry("Iraq")
		app.map["Iraq"].regimeChange = 1
		self.assertFalse(app.deck["56"].playable("Jihadist", app))	
		app.map["Iraq"].sleeperCells = 1
		self.assertTrue(app.deck["56"].playable("Jihadist", app))	
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["56"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["56"].playEvent("Jihadist", app)
		self.assertTrue("Vieira de Mello Slain" in app.markers)
		self.assertTrue(app.prestige == 6)
		
class card57(unittest.TestCase):
	'''Abu Sayyaf'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["57"].playable("Jihadist", app))	
		app.markers.append("Moro Talks")
		self.assertFalse(app.deck["57"].playable("Jihadist", app))	
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["57"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["57"].playEvent("Jihadist", app)
		self.assertTrue("Abu Sayyaf" in app.markers)
		self.assertTrue(app.map["Philippines"].governance != 0)
		self.assertTrue(app.map["Philippines"].sleeperCells == 1)
		app.map["Philippines"].sleeperCells = 3
		app.placePlots("Philippines", 0, [1,5,1])
		self.assertTrue(app.prestige == 5)
		
class card58(unittest.TestCase):
	'''Al-Anbar'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["58"].playable("Jihadist", app))	
		app.markers.append("Anbar Awakening")
		self.assertFalse(app.deck["58"].playable("Jihadist", app))	
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["58"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["58"].playEvent("Jihadist", app)
		self.assertTrue("Al-Anbar" in app.markers)
		self.assertTrue(app.map["Iraq"].sleeperCells == 1)
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 3
		app.map["Iraq"].troopCubes = 3
		app.handleDisrupt("Iraq")
		self.assertTrue(app.map["Iraq"].sleeperCells == 2)
		self.assertTrue(app.map["Iraq"].activeCells == 1)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["58"].playEvent("Jihadist", app)
		self.assertTrue("Al-Anbar" in app.markers)
		app.testCountry("Syria")
		app.map["Syria"].sleeperCells = 3
		app.map["Syria"].troopCubes = 3
		app.handleDisrupt("Syria")
		self.assertTrue(app.map["Syria"].sleeperCells == 2)
		self.assertTrue(app.map["Syria"].activeCells == 1)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["58"].playEvent("Jihadist", app)
		self.assertTrue("Al-Anbar" in app.markers)
		app.testCountry("Afghanistan")
		app.map["Afghanistan"].sleeperCells = 3
		app.map["Afghanistan"].troopCubes = 3
		app.handleDisrupt("Afghanistan")
		self.assertTrue(app.map["Afghanistan"].sleeperCells == 1)
		self.assertTrue(app.map["Afghanistan"].activeCells == 2)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["58"].playEvent("Jihadist", app)
		self.assertTrue("Al-Anbar" in app.markers)
		app.testCountry("Iraq")
		app.map["Iraq"].cadre = 1
		app.map["Iraq"].troopCubes = 3
		app.handleDisrupt("Iraq")
		self.assertTrue(app.map["Iraq"].cadre == 1)
				
class card59(unittest.TestCase):
	'''Amerithrax'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["59"].playable("Jihadist", app))	
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["59"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["59"].playEvent("Jihadist", app)

class card60(unittest.TestCase):
	'''Bhutto Shot'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["60"].playable("Jihadist", app))
		app.map["Pakistan"].sleeperCells = 1
		self.assertTrue(app.deck["60"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["60"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["60"].playEvent("Jihadist", app)
		self.assertTrue("Bhutto Shot" in app.markers)

class card61(unittest.TestCase):
	'''Detainee Release'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.lapsing.append("GTMO")
		self.assertFalse(app.deck["61"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.markers.append("Renditions")
		self.assertFalse(app.deck["61"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup, ["n","y"])
		print "Say No"
		self.assertFalse(app.deck["61"].playable("Jihadist", app))
		print "Say Yes"
		self.assertTrue(app.deck["61"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["61"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
 		app.testCountry("Iraq")
 		app.deck["61"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 1)

class card62(unittest.TestCase):
	'''Ex-KGB'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["62"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["62"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Russia"].markers.append("CTR")
 		app.map["Caucasus"].posture = "Hard"
 		app.map["Spain"].posture = "Soft"
 		app.map["Germany"].posture = "Soft"
		app.deck["62"].playEvent("Jihadist", app)
		self.assertTrue("CTR" not in app.map["Russia"].markers)
		self.assertTrue(app.map["Caucasus"].posture == "Hard")
		self.assertTrue(app.map["Central Asia"].governance == 0)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Caucasus"].posture = "Hard"
 		app.map["Spain"].posture = "Soft"
 		app.map["Germany"].posture = "Soft"
		app.deck["62"].playEvent("Jihadist", app)
		self.assertTrue("CTR" not in app.map["Russia"].markers)
		self.assertTrue(app.map["Caucasus"].posture == "Soft")
		self.assertTrue(app.map["Central Asia"].governance == 0)

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Caucasus"].posture = "Hard"
		app.map["Spain"].posture = "Hard"
		app.deck["62"].playEvent("Jihadist", app)
		self.assertTrue("CTR" not in app.map["Russia"].markers)
		self.assertTrue(app.map["Caucasus"].posture == "Hard")
		self.assertTrue(app.map["Central Asia"].governance != 0)
		self.assertTrue(app.map["Central Asia"].alignment == "Adversary")

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Caucasus"].posture = "Hard"
		app.map["Spain"].posture = "Hard"
		app.testCountry("Central Asia")
		app.map["Central Asia"].alignment = "Ally"
		app.deck["62"].playEvent("Jihadist", app)
		self.assertTrue("CTR" not in app.map["Russia"].markers)
		self.assertTrue(app.map["Caucasus"].posture == "Hard")
		self.assertTrue(app.map["Central Asia"].governance != 0)
		self.assertTrue(app.map["Central Asia"].alignment == "Neutral")

class card63(unittest.TestCase):
	'''Gaza War'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["63"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["63"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.deck["63"].playEvent("Jihadist", app)
 		self.assertTrue(app.funding == 6)
 		self.assertTrue(app.prestige == 6)

class card64(unittest.TestCase):
	'''Hariri Killed'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["64"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["64"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Syria"].governance = 1
 		app.map["Syria"].alignment = "Ally"
 		app.deck["64"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Lebanon"].governance != 0)
 		self.assertTrue(app.map["Syria"].governance == 2)
 		self.assertTrue(app.map["Syria"].alignment == "Adversary")

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Syria"].governance = 2
 		app.map["Syria"].alignment = "Ally"
 		app.deck["64"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Lebanon"].governance != 0)
 		self.assertTrue(app.map["Syria"].governance == 3)
 		self.assertTrue(app.map["Syria"].alignment == "Adversary")

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Syria"].governance = 3
 		app.map["Syria"].alignment = "Ally"
 		app.deck["64"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Lebanon"].governance != 0)
 		self.assertTrue(app.map["Syria"].governance == 3)
 		self.assertTrue(app.map["Syria"].alignment == "Adversary")

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Syria"].governance = 4
 		app.map["Syria"].alignment = "Ally"
 		app.deck["64"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Lebanon"].governance != 0)
 		self.assertTrue(app.map["Syria"].governance == 4)
 		self.assertTrue(app.map["Syria"].alignment == "Adversary")

class card65(unittest.TestCase):
	'''HEU'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["65"].playable("Jihadist", app))
 		app.testCountry("Russia")
 		app.map["Russia"].sleeperCells = 1
 		self.assertTrue(app.deck["65"].playable("Jihadist", app))
 		app.map["Russia"].markers.append("CTR")
 		self.assertFalse(app.deck["65"].playable("Jihadist", app))
 		app.testCountry("Central Asia")
  		app.map["Central Asia"].sleeperCells = 1
 		self.assertTrue(app.deck["65"].playable("Jihadist", app))
 		app.map["Central Asia"].markers.append("CTR")
 		self.assertFalse(app.deck["65"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["65"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Russia")
 		app.map["Russia"].sleeperCells = 1
		app.executeCardHEU("Russia",1)
		self.assertTrue(app.map["Russia"].sleeperCells == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Russia")
 		app.map["Russia"].sleeperCells = 1
		app.executeCardHEU("Russia",3)
		self.assertTrue(app.map["Russia"].sleeperCells == 0)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Central Asia")
 		app.map["Central Asia"].sleeperCells = 1
		app.executeCardHEU("Central Asia",1)
		self.assertTrue(app.map["Central Asia"].sleeperCells == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Central Asia")
 		app.map["Central Asia"].sleeperCells = 1
		app.executeCardHEU("Central Asia",4)
		self.assertTrue(app.map["Central Asia"].sleeperCells == 0)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["Russia"].sleeperCells = 1
 		app.deck["65"].playEvent("Jihadist", app)

class card66(unittest.TestCase):
	'''Homegrown'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["66"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["66"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.deck["66"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["United Kingdom"].posture != "")
 		self.assertTrue(app.map["United Kingdom"].sleeperCells == 1)

class card67(unittest.TestCase):
	'''Islamic Jihad Union'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["67"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["67"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.deck["67"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Central Asia"].sleeperCells == 1)
 		self.assertTrue(app.map["Afghanistan"].sleeperCells == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.cells = 1
 		app.deck["67"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Central Asia"].sleeperCells == 1)
 		self.assertTrue(app.map["Afghanistan"].sleeperCells == 0)

class card68(unittest.TestCase):
	'''Jemaah Islamiya'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["68"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["68"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.deck["68"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Indonesia/Malaysia"].sleeperCells == 2)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.cells = 1
 		app.deck["68"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Indonesia/Malaysia"].sleeperCells == 1)

class card69(unittest.TestCase):
	'''Kazakh Strain'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Central Asia")
  		app.map["Central Asia"].sleeperCells = 1
 		self.assertTrue(app.deck["69"].playable("Jihadist", app))
 		app.map["Central Asia"].markers.append("CTR")
 		self.assertFalse(app.deck["69"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["69"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Central Asia")
 		app.map["Central Asia"].sleeperCells = 1
		app.executeCardHEU("Central Asia",1)
		self.assertTrue(app.map["Central Asia"].sleeperCells == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Central Asia")
 		app.map["Central Asia"].sleeperCells = 1
		app.executeCardHEU("Central Asia",4)
		self.assertTrue(app.map["Central Asia"].sleeperCells == 0)

 		app.deck["69"].playEvent("Jihadist", app)

class card70(unittest.TestCase):
	'''Lashkar-e-Tayyiba'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["70"].playable("Jihadist", app))
 		app.markers.append("Indo-Pakistani Talks")
 		self.assertFalse(app.deck["70"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["70"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.deck["70"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Pakistan"].sleeperCells == 1)
 		self.assertTrue(app.map["India"].sleeperCells == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.cells = 1
 		app.deck["70"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Pakistan"].sleeperCells == 1)
 		self.assertTrue(app.map["India"].sleeperCells == 0)

class card71(unittest.TestCase):
	'''Kazakh Strain'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Russia")
  		app.map["Russia"].sleeperCells = 1
 		self.assertTrue(app.deck["71"].playable("Jihadist", app))
 		app.map["Russia"].markers.append("CTR")
 		self.assertFalse(app.deck["71"].playable("Jihadist", app))
		
	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["71"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Russia")
 		app.map["Russia"].sleeperCells = 1
		app.executeCardHEU("Russia",1)
		self.assertTrue(app.map["Russia"].sleeperCells == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Russia")
 		app.map["Russia"].sleeperCells = 1
		app.executeCardHEU("Russia",4)
		self.assertTrue(app.map["Russia"].sleeperCells == 0)

 		app.deck["71"].playEvent("Jihadist", app)

class card72(unittest.TestCase):
	'''Opium'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["72"].playable("Jihadist", app))
		app.map["Afghanistan"].sleeperCells = 1
 		self.assertTrue(app.deck["72"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["72"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.cells = 14
 		app.testCountry("Afghanistan")
		app.map["Afghanistan"].sleeperCells = 1
 		app.deck["72"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Afghanistan"].sleeperCells == 4)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.cells = 14
 		app.testCountry("Afghanistan")
		app.map["Afghanistan"].sleeperCells = 1
		app.map["Afghanistan"].governance = 4
 		app.deck["72"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Afghanistan"].sleeperCells == 15)
 		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.cells = 2
 		app.testCountry("Afghanistan")
		app.map["Afghanistan"].sleeperCells = 1
 		app.deck["72"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Afghanistan"].sleeperCells == 3)


class card73(unittest.TestCase):
	'''Pirates'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["73"].playable("Jihadist", app))
		app.map["Somalia"].governance = 4
 		self.assertTrue(app.deck["73"].playable("Jihadist", app))
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["73"].playable("Jihadist", app))
		app.map["Yemen"].governance = 4
 		self.assertTrue(app.deck["73"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["73"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.deck["73"].playEvent("Jihadist", app)
 		self.assertTrue("Pirates" in app.markers)
 		app.do_turn("")
 		self.assertTrue(app.funding == 4)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Somalia"].governance = 4
 		app.deck["73"].playEvent("Jihadist", app)
 		app.do_turn("")
 		self.assertTrue(app.funding == 5)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Yemen"].governance = 4
 		app.deck["73"].playEvent("Jihadist", app)
 		app.do_turn("")
 		self.assertTrue(app.funding == 5)

class card74(unittest.TestCase):
	'''Schengen Visas'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["74"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["74"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
 		app.deck["74"].playEvent("Jihadist", app)

class card75(unittest.TestCase):
	'''Schroeder & Chirac'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["75"].playable("Jihadist", app))
 		app.map["United States"].posture = "Soft"
 		self.assertFalse(app.deck["75"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["75"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
 		app.deck["75"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Germany"].posture == "Soft")
 		self.assertTrue(app.map["France"].posture == "Soft")
 		self.assertTrue(app.prestige == 6)

class card76(unittest.TestCase):
	'''Abu Ghurayb'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["76"].playable("Jihadist", app))
 		app.testCountry("Iraq")
 		app.map["Iraq"].regimeChange = 1
 		self.assertFalse(app.deck["76"].playable("Jihadist", app))
		app.map["Iraq"].sleeperCells = 1
 		self.assertTrue(app.deck["76"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["76"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
 		app.map["Iraq"].regimeChange = 1
		app.map["Iraq"].sleeperCells = 1 		
 		app.deck["76"].playEvent("Jihadist", app)
 		self.assertTrue(app.prestige == 5)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
 		app.map["Iraq"].regimeChange = 1
		app.map["Iraq"].sleeperCells = 1 	
		app.testCountry("Pakistan")
		app.testCountry("Lebanon")
		app.map["Lebanon"].alignment = "Ally"
 		app.deck["76"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Lebanon"].alignment == "Neutral")
 		self.assertTrue(app.prestige == 5)

class card77(unittest.TestCase):
	'''Al Jazeera'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["77"].playable("Jihadist", app))
 		app.testCountry("Saudi Arabia")
 		app.map["Saudi Arabia"].troopCubes = 1
 		self.assertTrue(app.deck["77"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["77"].playable("Jihadist", app))
 		app.testCountry("Jordan")
 		app.map["Jordan"].troopCubes = 1
 		self.assertTrue(app.deck["77"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["77"].playable("Jihadist", app))
 		app.testCountry("Iraq")
 		app.map["Iraq"].troopCubes = 1
 		self.assertTrue(app.deck["77"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["77"].playable("Jihadist", app))
 		app.testCountry("Gulf States")
 		app.map["Gulf States"].troopCubes = 1
 		self.assertTrue(app.deck["77"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["77"].playable("Jihadist", app))
 		app.testCountry("Yemen")
 		app.map["Yemen"].troopCubes = 1
 		self.assertTrue(app.deck["77"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["77"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Yemen")
 		app.map["Yemen"].troopCubes = 1
 		app.deck["77"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Yemen"].alignment == "Adversary")

class card78(unittest.TestCase):
	'''Axis of Evil'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["78"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["78"].putsCell(app))			

	def testEvent(self):
 		for i in range(100):
			app = Labyrinth(1, 1, testBlankScenarioSetup)
			app.map["United States"].posture = "Soft"
			app.deck["78"].playEvent("Jihadist", app)
			self.assertTrue(app.map["United States"].posture == "Hard")
			self.assertTrue(app.prestige != 7)

class card79(unittest.TestCase):
	'''Clean Operatives'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["79"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["79"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
 		app.deck["79"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["United States"].sleeperCells == 2)

class card80(unittest.TestCase):
	'''FATA'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertTrue(app.deck["80"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["80"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
 		app.deck["80"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Pakistan"].sleeperCells == 1)
 		self.assertTrue("FATA" in app.map["Pakistan"].markers)

class card81(unittest.TestCase):
	'''Foreign Fighters'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		self.assertFalse(app.deck["81"].playable("Jihadist", app))
 		app.testCountry("Iraq")
  		self.assertFalse(app.deck["81"].playable("Jihadist", app))
		app.map["Iraq"].regimeChange = 1
		self.assertTrue(app.deck["81"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["81"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
 		app.testCountry("Iraq")
 		app.map["Iraq"].regimeChange = 1
		app.deck["81"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 5)
 		self.assertTrue(app.map["Iraq"].besieged == 1)
 		self.assertTrue(app.map["Iraq"].aid == 0)

 		app = Labyrinth(1, 1, testScenarioSetup)
 		app.testCountry("Iraq")
 		app.map["Iraq"].regimeChange = 1
 		app.map["Iraq"].aid = 1
		app.deck["81"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 5)
 		self.assertTrue(app.map["Iraq"].besieged == 0)
 		self.assertTrue(app.map["Iraq"].aid == 0)

class card82(unittest.TestCase):
	'''Jihadist Videos'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["82"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["82"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
		app.deck["82"].playEvent("Jihadist", app)

class card83(unittest.TestCase):
	'''Kashmir'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["83"].playable("Jihadist", app))
		app.markers.append("Indo-Pakistani Talks")
		self.assertFalse(app.deck["83"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["83"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
 		app.testCountry("Pakistan")
		app.deck["83"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Pakistan"].alignment == "Adversary")
 		self.assertTrue(app.map["Pakistan"].sleeperCells == 1)

class card84(unittest.TestCase):
	'''Leak'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["84"].playable("Jihadist", app))
		app.markers.append("Enhanced Measures")
		self.assertTrue(app.deck["84"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["84"].playable("Jihadist", app))
		app.markers.append("Reditions")
		self.assertTrue(app.deck["84"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["84"].playable("Jihadist", app))
		app.markers.append("Wiretapping")
		self.assertTrue(app.deck["84"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["84"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
		app.markers.append("Enhanced Measures")
		app.deck["84"].playEvent("Jihadist", app)
 		self.assertTrue("Leak-Enhanced Measures" in app.markers)
 		self.assertTrue("Enhanced Measures" not in app.markers)

 		app = Labyrinth(1, 1, testScenarioSetup)
		app.markers.append("Reditions")
		app.deck["84"].playEvent("Jihadist", app)
 		self.assertTrue("Leak-Reditions" in app.markers)
 		self.assertTrue("Reditions" not in app.markers)

 		app = Labyrinth(1, 1, testScenarioSetup)
		app.markers.append("Wiretapping")
		app.deck["84"].playEvent("Jihadist", app)
 		self.assertTrue("Leak-Wiretapping" in app.markers)
 		self.assertTrue("Wiretapping" not in app.markers)
 		self.assertTrue(app.prestige != 7)
 		
class card85(unittest.TestCase):
	'''Leak'''
	
	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["85"].playable("Jihadist", app))
		app.markers.append("Enhanced Measures")
		self.assertTrue(app.deck["85"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["85"].playable("Jihadist", app))
		app.markers.append("Reditions")
		self.assertTrue(app.deck["85"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["85"].playable("Jihadist", app))
		app.markers.append("Wiretapping")
		self.assertTrue(app.deck["85"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["85"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
		app.markers.append("Enhanced Measures")
		app.deck["85"].playEvent("Jihadist", app)
 		self.assertTrue("Leak-Enhanced Measures" in app.markers)
 		self.assertTrue("Enhanced Measures" not in app.markers)

 		app = Labyrinth(1, 1, testScenarioSetup)
		app.markers.append("Reditions")
		app.deck["85"].playEvent("Jihadist", app)
 		self.assertTrue("Leak-Reditions" in app.markers)
 		self.assertTrue("Reditions" not in app.markers)

 		app = Labyrinth(1, 1, testScenarioSetup)
		app.markers.append("Wiretapping")
		app.deck["85"].playEvent("Jihadist", app)
 		self.assertTrue("Leak-Wiretapping" in app.markers)
 		self.assertTrue("Wiretapping" not in app.markers)
 		self.assertTrue(app.prestige != 7)

class card86(unittest.TestCase):
	'''Lebanon War'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["86"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["86"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testScenarioSetup)
		app.deck["86"].playEvent("Jihadist", app)
 		self.assertTrue(app.prestige == 6)

class card87(unittest.TestCase):
	'''Martyrdom Operation'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["87"].playable("Jihadist", app))
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 4
		self.assertFalse(app.deck["87"].playable("Jihadist", app))
		app.map["Iraq"].sleeperCells = 1
		self.assertFalse(app.deck["87"].playable("Jihadist", app))
		app.map["Iraq"].governance = 3
		self.assertTrue(app.deck["87"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["87"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		app.deck["87"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 0)
 		self.assertTrue(app.map["Iraq"].activeCells == 0)
 		self.assertTrue(app.map["Iraq"].plots == 2)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		app.map["United States"].sleeperCells = 1
		app.deck["87"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 1)
 		self.assertTrue(app.map["Iraq"].activeCells == 0)
 		self.assertTrue(app.map["Iraq"].plots == 0)
 		self.assertTrue(app.map["United States"].sleeperCells == 0)
 		self.assertTrue(app.map["United States"].activeCells == 0)
 		self.assertTrue(app.map["United States"].plots == 2)

class card88(unittest.TestCase):
	'''Martyrdom Operation'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["88"].playable("Jihadist", app))
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 4
		self.assertFalse(app.deck["88"].playable("Jihadist", app))
		app.map["Iraq"].sleeperCells = 1
		self.assertFalse(app.deck["88"].playable("Jihadist", app))
		app.map["Iraq"].governance = 3
		self.assertTrue(app.deck["88"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["88"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		app.deck["88"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 0)
 		self.assertTrue(app.map["Iraq"].activeCells == 0)
 		self.assertTrue(app.map["Iraq"].plots == 2)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		app.map["United States"].sleeperCells = 1
		app.deck["88"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 1)
 		self.assertTrue(app.map["Iraq"].activeCells == 0)
 		self.assertTrue(app.map["Iraq"].plots == 0)
 		self.assertTrue(app.map["United States"].sleeperCells == 0)
 		self.assertTrue(app.map["United States"].activeCells == 0)
 		self.assertTrue(app.map["United States"].plots == 2)

class card89(unittest.TestCase):
	'''Martyrdom Operation'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["89"].playable("Jihadist", app))
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 4
		self.assertFalse(app.deck["89"].playable("Jihadist", app))
		app.map["Iraq"].sleeperCells = 1
		self.assertFalse(app.deck["89"].playable("Jihadist", app))
		app.map["Iraq"].governance = 3
		self.assertTrue(app.deck["89"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["89"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		app.deck["89"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 0)
 		self.assertTrue(app.map["Iraq"].activeCells == 0)
 		self.assertTrue(app.map["Iraq"].plots == 2)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		app.map["United States"].sleeperCells = 1
		app.deck["89"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 1)
 		self.assertTrue(app.map["Iraq"].activeCells == 0)
 		self.assertTrue(app.map["Iraq"].plots == 0)
 		self.assertTrue(app.map["United States"].sleeperCells == 0)
 		self.assertTrue(app.map["United States"].activeCells == 0)
 		self.assertTrue(app.map["United States"].plots == 2)

class card90(unittest.TestCase):
	'''Quagmire'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["90"].playable("Jihadist", app))
		app.prestige = 6
		self.assertFalse(app.deck["90"].playable("Jihadist", app))
		app.testCountry("Iraq")
		app.map["Iraq"].regimeChange = 1
		self.assertFalse(app.deck["90"].playable("Jihadist", app))
		app.map["Iraq"].sleeperCells = 1
		self.assertTrue(app.deck["90"].playable("Jihadist", app))
		app.prestige = 7
		self.assertFalse(app.deck["90"].playable("Jihadist", app))
		app.prestige = 6
		app.map["Iraq"].regimeChange = 0
		self.assertFalse(app.deck["90"].playable("Jihadist", app))	

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["90"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.deck["90"].playEvent("Jihadist", app)
		self.assertTrue(app.map["United States"].posture == "Soft")
 		
class card91(unittest.TestCase):
	'''Regional al-Qaeda'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["91"].playable("Jihadist", app))
		for country in app.map:
			if app.map[country].type == "Suni" or app.map[country].type == "Shia-Mix":
				app.testCountry(country)
		self.assertFalse(app.deck["91"].playable("Jihadist", app))
		app.map["Iraq"].governance = 0
		app.map["Iraq"].alignment = ""
		self.assertFalse(app.deck["91"].playable("Jihadist", app))
		app.map["Lebanon"].governance = 0
		app.map["Lebanon"].alignment = ""
		self.assertTrue(app.deck["91"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["91"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		for country in app.map:
			if app.map[country].type == "Suni" or app.map[country].type == "Shia-Mix":
				app.testCountry(country)
		app.map["Iraq"].governance = 0
		app.map["Iraq"].alignment = ""
		app.map["Lebanon"].governance = 0
		app.map["Lebanon"].alignment = ""
		app.deck["91"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Iraq"].governance != 0)
		self.assertTrue(app.map["Iraq"].alignment != "")
		self.assertTrue(app.map["Iraq"].sleeperCells == 1)
		self.assertTrue(app.map["Lebanon"].governance != 0)
		self.assertTrue(app.map["Lebanon"].alignment != "")
		self.assertTrue(app.map["Lebanon"].sleeperCells == 1)
 		
class card92(unittest.TestCase):
	'''Saddam'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["92"].playable("Jihadist", app))
		app.testCountry("Iraq")
		self.assertFalse(app.deck["92"].playable("Jihadist", app))
		app.map["Iraq"].governance = 3	
		self.assertFalse(app.deck["92"].playable("Jihadist", app))
		app.map["Iraq"].alignment = "Adversary"
		self.assertTrue(app.deck["92"].playable("Jihadist", app))
		app.markers.append("Saddam Captured")
		self.assertFalse(app.deck["92"].playable("Jihadist", app))		

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["92"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["92"].playEvent("Jihadist", app)
		self.assertTrue(app.funding == 9) 		

class card93(unittest.TestCase):
	'''Taliban'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["93"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["93"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Afghanistan")
		app.testCountry("Pakistan")
		app.deck["93"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Afghanistan"].besieged == 1) 		
		self.assertTrue(app.map["Afghanistan"].sleeperCells == 1) 		
		self.assertTrue(app.map["Pakistan"].sleeperCells == 1) 		
		self.assertTrue(app.prestige == 6)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Afghanistan")
		app.testCountry("Pakistan")
		app.map["Afghanistan"].governance = 4
		app.deck["93"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Afghanistan"].besieged == 1) 		
		self.assertTrue(app.map["Afghanistan"].sleeperCells == 1) 		
		self.assertTrue(app.map["Pakistan"].sleeperCells == 1) 		
		self.assertTrue(app.prestige == 4)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Afghanistan")
		app.testCountry("Pakistan")
		app.map["Pakistan"].governance = 4
		app.deck["93"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Afghanistan"].besieged == 1) 		
		self.assertTrue(app.map["Afghanistan"].sleeperCells == 1) 		
		self.assertTrue(app.map["Pakistan"].sleeperCells == 1) 		
		self.assertTrue(app.prestige == 4)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.cells = 1
		app.testCountry("Afghanistan")
		app.testCountry("Pakistan")
		app.deck["93"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Afghanistan"].besieged == 1) 		
		self.assertTrue(app.map["Afghanistan"].sleeperCells == 1) 		
		self.assertTrue(app.map["Pakistan"].sleeperCells == 0) 		
		self.assertTrue(app.prestige == 6)

class card94(unittest.TestCase):
	'''The door of Itjihad was closed'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup, ["n","y"])
		print "Say No"
		self.assertFalse(app.deck["94"].playable("Jihadist", app))
		print "Say Yes"
		self.assertTrue(app.deck["94"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["94"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
		print "Choose Iraq"
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 2
		app.deck["94"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Iraq"].governance == 3)

class card95(unittest.TestCase):
	'''Wahhabism'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["95"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["95"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["95"].playEvent("Jihadist", app)
		self.assertTrue(app.funding == 8)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Saudi Arabia")
 		app.map["Saudi Arabia"].governance = 4
		app.deck["95"].playEvent("Jihadist", app)
		self.assertTrue(app.funding == 9)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.lapsing.append("Oil Price Spike")
		app.deck["95"].playEvent("Jihadist", app)
		self.assertTrue(app.funding == 9)

class card96(unittest.TestCase):
	'''Danish Cartoons'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["96"].playable("US", app))
		self.assertTrue(app.deck["96"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["96"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup,["s","h"])
		app.deck["96"].playEvent("US", app)
		self.assertTrue(app.map["Scandinavia"].posture == "Soft")
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 4
		app.deck["96"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Scandinavia"].posture == "Hard")

class card97(unittest.TestCase):
	'''Fatwa'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup, ["y","n"])
		print "Say Yes"
		self.assertTrue(app.deck["97"].playable("US", app))
		print "Say No"
		self.assertFalse(app.deck["97"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["97"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["97"].playEvent("US", app)
		app.deck["97"].playEvent("Jihadist", app)

class card98(unittest.TestCase):
	'''Gaza Withdrawl'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["98"].playable("US", app))
		self.assertTrue(app.deck["98"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["98"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["98"].playEvent("US", app)
		self.assertTrue(app.funding == 4)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["98"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Israel"].sleeperCells == 1)
		self.assertTrue(app.cells == 10)

class card99(unittest.TestCase):
	'''HAMAS Elected'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["99"].playable("US", app))
		self.assertTrue(app.deck["99"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["99"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["99"].playEvent("US", app)
		self.assertTrue(app.funding == 4)
		self.assertTrue(app.prestige == 6)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["99"].playEvent("Jihadist", app)
		self.assertTrue(app.funding == 4)
		self.assertTrue(app.prestige == 6)

class cardHundred(unittest.TestCase):
	'''His Ut-Tahrir'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["100"].playable("US", app))
		self.assertTrue(app.deck["100"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["100"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["100"].playEvent("US", app)
		self.assertTrue(app.funding == 5)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["100"].playEvent("Jihadist", app)
		self.assertTrue(app.funding == 5)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.troops = 4
		app.deck["100"].playEvent("US", app)
		self.assertTrue(app.funding == 7)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.troops = 4
		app.deck["100"].playEvent("Jihadist", app)
		self.assertTrue(app.funding == 7)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.troops = 10
		app.deck["100"].playEvent("US", app)
		self.assertTrue(app.funding == 3)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.troops = 10
		app.deck["100"].playEvent("Jihadist", app)
		self.assertTrue(app.funding == 3)
		
class cardHundredOne(unittest.TestCase):
	'''Kosovo'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["101"].playable("US", app))
		self.assertTrue(app.deck["101"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["101"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["101"].playEvent("US", app)
		self.assertTrue(app.prestige == 8)
		self.assertTrue(app.map["Serbia"].posture == "Soft")
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.map["United States"].posture = "Soft"
		app.deck["101"].playEvent("Jihadist", app)
		self.assertTrue(app.prestige == 8)
		self.assertTrue(app.map["Serbia"].posture == "Hard")
		
class cardHundredTwo(unittest.TestCase):
	'''Former Soviet Union'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["102"].playable("US", app))
		self.assertTrue(app.deck["102"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["102"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["102"].playEvent("US", app)
		self.assertTrue(app.map["Central Asia"].alignment == "Neutral")
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Central Asia")
 		app.map["Central Asia"].governance = 1
 		app.map["Central Asia"].alignment = "Ally"
		app.deck["102"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Central Asia"].governance != 1)
		self.assertTrue(app.map["Central Asia"].alignment == "Neutral")
		
class cardHundredThree(unittest.TestCase):
	'''Hizballah'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["103"].playable("US", app))
		self.assertTrue(app.deck["103"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["103"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
 		app.map["Iraq"].sleeperCells = 1
		app.deck["103"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].sleeperCells == 0)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["103"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Lebanon"].governance == 3)
		self.assertTrue(app.map["Lebanon"].alignment == "Neutral")

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Lebanon")
 		app.map["Lebanon"].governance = 1
 		app.map["Lebanon"].alignment = "Ally"
 		app.map["Jordan"].governance = 1
 		app.map["Jordan"].alignment = "Ally"
		app.deck["103"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Lebanon"].governance == 3)
		self.assertTrue(app.map["Lebanon"].alignment == "Neutral")
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
 		app.testCountry("Iraq")
 		app.map["Iraq"].sleeperCells = 1
 		app.testCountry("Gulf States")
 		app.map["Gulf States"].sleeperCells = 1
		app.deck["103"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].sleeperCells == 0)
		
class cardHundredFour(unittest.TestCase):
	'''Iran'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["104"].playable("US", app))
		self.assertTrue(app.deck["104"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["104"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
 		app.testCountry("Iraq")
 		app.map["Iraq"].sleeperCells = 1
		app.deck["104"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].sleeperCells == 0)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Yemen"])
 		app.testCountry("Iraq")
 		app.map["Iraq"].sleeperCells = 1
 		app.testCountry("Yemen")
 		app.map["Yemen"].sleeperCells = 1
		app.deck["104"].playEvent("US", app)
		self.assertTrue(app.map["Yemen"].sleeperCells == 0)
		
		app.deck["104"].playEvent("Jihadist", app)
		
class cardHundredFive(unittest.TestCase):
	'''Iran'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["105"].playable("US", app))
		self.assertTrue(app.deck["105"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["105"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
 		app.testCountry("Iraq")
 		app.map["Iraq"].sleeperCells = 1
		app.deck["105"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].sleeperCells == 0)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Yemen"])
 		app.testCountry("Iraq")
 		app.map["Iraq"].sleeperCells = 1
 		app.testCountry("Yemen")
 		app.map["Yemen"].sleeperCells = 1
		app.deck["105"].playEvent("US", app)
		self.assertTrue(app.map["Yemen"].sleeperCells == 0)
		
		app.deck["105"].playEvent("Jihadist", app)
		
class cardHundredSix(unittest.TestCase):
	'''Jaysh al-Mahdi'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["106"].playable("US", app))
		self.assertFalse(app.deck["106"].playable("Jihadist", app))
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		self.assertFalse(app.deck["106"].playable("US", app))
		self.assertFalse(app.deck["106"].playable("Jihadist", app))
		app.map["Iraq"].troopCubes = 1
		self.assertTrue(app.deck["106"].playable("US", app))
		self.assertTrue(app.deck["106"].playable("Jihadist", app))
		app.map["Iraq"].sleeperCells = 0
		self.assertFalse(app.deck["106"].playable("US", app))
		self.assertFalse(app.deck["106"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["106"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 3
		app.map["Iraq"].troopCubes = 1
		app.deck["106"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].sleeperCells == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 2
		app.map["Iraq"].troopCubes = 1
		app.deck["106"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].sleeperCells == 0)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		app.map["Iraq"].troopCubes = 1
		app.deck["106"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].sleeperCells == 0)

 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Lebanon"])
 		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 2
		app.map["Iraq"].troopCubes = 1
		app.map["Lebanon"].sleeperCells = 2
		app.map["Lebanon"].troopCubes = 1
		print "Choose Lebanon"
		app.deck["106"].playEvent("US", app)
		self.assertTrue(app.map["Lebanon"].sleeperCells == 0)
		
 		print "HERE"
		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
		app.map["Iraq"].governance = 2
		app.map["Iraq"].sleeperCells = 2
		app.map["Iraq"].troopCubes = 1
		app.deck["106"].playEvent("Jihadist", app)
		
class cardHundredSeven(unittest.TestCase):
	'''Kurdistan'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["107"].playable("US", app))
		self.assertTrue(app.deck["107"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["107"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
		app.deck["107"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].aid == 1)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["107"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Turkey"].governance == 3)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
		app.map["Iraq"].governance = 1
		app.deck["107"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Turkey"].governance > 1)
		self.assertTrue(app.map["Iraq"].governance == 2)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Iraq")
		app.map["Iraq"].governance = 2
 		app.testCountry("Turkey")
		app.map["Turkey"].governance = 2
		app.map["Turkey"].aid = 1
		app.deck["107"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Turkey"].governance == 3)
		self.assertTrue(app.map["Iraq"].governance == 2)

class cardHundredEight(unittest.TestCase):
	'''Musharraf'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["108"].playable("US", app))
		self.assertFalse(app.deck["108"].playable("Jihadist", app))
		app.testCountry("Pakistan")
		app.map["Pakistan"].activeCells = 1
		self.assertTrue(app.deck["108"].playable("US", app))
		self.assertTrue(app.deck["108"].playable("Jihadist", app))
		app.markers.append("Benazir Bhutto")
		self.assertFalse(app.deck["108"].playable("US", app))
		self.assertFalse(app.deck["108"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["108"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Pakistan")
		app.map["Pakistan"].sleeperCells = 1
		app.map["Pakistan"].governance = 1
		app.deck["108"].playEvent("US", app)
		self.assertTrue(app.map["Pakistan"].totalCells(True) == 0)
		self.assertTrue(app.map["Pakistan"].governance == 3)
		self.assertTrue(app.map["Pakistan"].alignment == "Ally")
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Pakistan")
		app.map["Pakistan"].sleeperCells = 3
		app.map["Pakistan"].governance = 4
		app.map["Pakistan"].alignment = "Adversary"
		app.deck["108"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Pakistan"].totalCells(True) == 2)
		self.assertTrue(app.map["Pakistan"].governance == 3)
		self.assertTrue(app.map["Pakistan"].alignment == "Ally")
		
class cardHundredNine(unittest.TestCase):
	'''Tora Bora'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["109"].playable("US", app))
		self.assertFalse(app.deck["109"].playable("Jihadist", app))
		app.testCountry("Pakistan")
		app.map["Pakistan"].activeCells = 2
		self.assertFalse(app.deck["109"].playable("US", app))
		self.assertFalse(app.deck["109"].playable("Jihadist", app))
		app.map["Pakistan"].regimeChange = 1
		self.assertTrue(app.deck["109"].playable("US", app))
		self.assertTrue(app.deck["109"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["109"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Pakistan")
		app.map["Pakistan"].sleeperCells = 2
		app.map["Pakistan"].regimeChange = 1
		app.deck["109"].playEvent("US", app)
		self.assertTrue(app.map["Pakistan"].totalCells(True) == 0)
		self.assertTrue(app.prestige != 7)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Pakistan")
		app.map["Pakistan"].sleeperCells = 2
		app.map["Pakistan"].regimeChange = 1
		app.deck["109"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Pakistan"].totalCells(True) == 0)
		self.assertTrue(app.prestige != 7)

 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Iraq"])
		app.testCountry("Pakistan")
		app.map["Pakistan"].sleeperCells = 2
		app.map["Pakistan"].regimeChange = 1
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 2
		app.map["Iraq"].regimeChange = 1
		print "Choose Iraq"
		app.deck["109"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].totalCells(True) == 0)
		self.assertTrue(app.prestige != 7)
		
class cardHundredTen(unittest.TestCase):
	'''Zarqawi'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["110"].playable("US", app))
		self.assertFalse(app.deck["110"].playable("Jihadist", app))
		app.testCountry("Iraq")
		app.map["Iraq"].troopCubes = 1
		self.assertTrue(app.deck["110"].playable("US", app))
		self.assertTrue(app.deck["110"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["110"].playable("US", app))
		self.assertFalse(app.deck["110"].playable("Jihadist", app))
		app.testCountry("Syria")
		app.map["Syria"].troopCubes = 1
		self.assertTrue(app.deck["110"].playable("US", app))
		self.assertTrue(app.deck["110"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["110"].playable("US", app))
		self.assertFalse(app.deck["110"].playable("Jihadist", app))
		app.testCountry("Lebanon")
		app.map["Lebanon"].troopCubes = 1
		self.assertTrue(app.deck["110"].playable("US", app))
		self.assertTrue(app.deck["110"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["110"].playable("US", app))
		self.assertFalse(app.deck["110"].playable("Jihadist", app))
		app.testCountry("Jordan")
		app.map["Jordan"].troopCubes = 1
		self.assertTrue(app.deck["110"].playable("US", app))
		self.assertTrue(app.deck["110"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["110"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].troopCubes = 2
		app.deck["110"].playEvent("US", app)
		self.assertTrue(app.prestige == 10)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].troopCubes = 2
		app.deck["110"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Iraq"].totalCells(True) == 3)
		self.assertTrue(app.map["Iraq"].plots == 1)

class cardHundredEleven(unittest.TestCase):
	'''Zawahiri'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["111"].playable("US", app))
		self.assertTrue(app.deck["111"].playable("Jihadist", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 4
		self.assertFalse(app.deck["111"].playable("US", app))
		self.assertTrue(app.deck["111"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Pakistan")
		app.map["Pakistan"].markers.append("FATA")
		self.assertFalse(app.deck["111"].playable("US", app))
		self.assertTrue(app.deck["111"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Pakistan")
		app.markers.append("Al-Anbar")
		self.assertFalse(app.deck["111"].playable("US", app))
		self.assertTrue(app.deck["111"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["111"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["111"].playEvent("US", app)
		self.assertTrue(app.funding == 3)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["111"].playEvent("Jihadist", app)
		self.assertTrue(app.prestige == 6)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 4
		app.deck["111"].playEvent("Jihadist", app)
		self.assertTrue(app.prestige == 4)

class cardHundredTwelve(unittest.TestCase):
	'''Bin Ladin'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["112"].playable("US", app))
		self.assertTrue(app.deck["112"].playable("Jihadist", app))
		
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 4
		self.assertFalse(app.deck["112"].playable("US", app))
		self.assertTrue(app.deck["112"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Pakistan")
		app.map["Pakistan"].markers.append("FATA")
		self.assertFalse(app.deck["112"].playable("US", app))
		self.assertTrue(app.deck["112"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Pakistan")
		app.markers.append("Al-Anbar")
		self.assertFalse(app.deck["112"].playable("US", app))
		self.assertTrue(app.deck["112"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["112"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["112"].playEvent("US", app)
		self.assertTrue(app.funding == 1)
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["112"].playEvent("Jihadist", app)
		self.assertTrue(app.prestige == 5)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 4
		app.deck["112"].playEvent("Jihadist", app)
		self.assertTrue(app.prestige == 3)

class cardHundredThirteen(unittest.TestCase):
	'''Darfur'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["113"].playable("US", app))
		self.assertTrue(app.deck["113"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["113"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["113"].playEvent("US", app)
		self.assertTrue(app.map["Sudan"].governance != 0)
		self.assertTrue(app.map["Sudan"].aid == 1)
		self.assertTrue(app.map["Sudan"].alignment == "Ally")

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Sudan")
 		app.map["Sudan"].alignment = "Adversary"
		app.deck["113"].playEvent("US", app)
		self.assertTrue(app.map["Sudan"].governance != 0)
		self.assertTrue(app.map["Sudan"].aid == 1)
		self.assertTrue(app.map["Sudan"].alignment == "Neutral")
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.prestige = 6
		app.deck["113"].playEvent("US", app)
		self.assertTrue(app.map["Sudan"].governance != 0)
		self.assertTrue(app.map["Sudan"].besieged == 1)
		self.assertTrue(app.map["Sudan"].alignment == "Adversary")

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.prestige = 6
 		app.testCountry("Sudan")
 		app.map["Sudan"].alignment = "Ally"
		app.deck["113"].playEvent("US", app)
		self.assertTrue(app.map["Sudan"].governance != 0)
		self.assertTrue(app.map["Sudan"].besieged == 1)
		self.assertTrue(app.map["Sudan"].alignment == "Neutral")
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["113"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Sudan"].governance != 0)
		self.assertTrue(app.map["Sudan"].aid == 1)
		self.assertTrue(app.map["Sudan"].alignment == "Ally")

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.testCountry("Sudan")
 		app.map["Sudan"].alignment = "Adversary"
		app.deck["113"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Sudan"].governance != 0)
		self.assertTrue(app.map["Sudan"].aid == 1)
		self.assertTrue(app.map["Sudan"].alignment == "Neutral")
		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.prestige = 6
		app.deck["113"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Sudan"].governance != 0)
		self.assertTrue(app.map["Sudan"].besieged == 1)
		self.assertTrue(app.map["Sudan"].alignment == "Adversary")

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.prestige = 6
 		app.testCountry("Sudan")
 		app.map["Sudan"].alignment = "Ally"
		app.deck["113"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Sudan"].governance != 0)
		self.assertTrue(app.map["Sudan"].besieged == 1)
		self.assertTrue(app.map["Sudan"].alignment == "Neutral")
		
class cardHundredFourteen(unittest.TestCase):
	'''GTMO'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["114"].playable("US", app))
		self.assertTrue(app.deck["114"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["114"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["114"].playEvent("US", app)
		self.assertTrue("GTMO" in app.lapsing)
		self.assertTrue(app.prestige != 7)
 		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["114"].playEvent("Jihadist", app)
		self.assertTrue("GTMO" in app.lapsing)
		self.assertTrue(app.prestige != 7)
		
class cardHundredFifteen(unittest.TestCase):
	'''Hambali'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.testCountry("Indonesia/Malaysia")
		app.map["Indonesia/Malaysia"].sleeperCells = 1
		app.map["Indonesia/Malaysia"].alignment = "Ally"
		self.assertTrue(app.deck["115"].playable("US", app))
		self.assertTrue(app.deck["115"].playable("Jihadist", app))
		app.map["Indonesia/Malaysia"].sleeperCells = 0
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.map["Indonesia/Malaysia"].sleeperCells = 1
		app.map["Indonesia/Malaysia"].alignment = "Neutral"
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.testCountry("Pakistan")
		app.map["Pakistan"].sleeperCells = 1
		app.map["Pakistan"].alignment = "Ally"
		self.assertTrue(app.deck["115"].playable("US", app))
		self.assertTrue(app.deck["115"].playable("Jihadist", app))
		app.map["Pakistan"].sleeperCells = 0
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.map["Pakistan"].sleeperCells = 1
		app.map["Pakistan"].alignment = "Neutral"
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.testCountry("India")
		app.map["India"].sleeperCells = 1
		app.map["India"].posture = "Hard"
		self.assertTrue(app.deck["115"].playable("US", app))
		self.assertTrue(app.deck["115"].playable("Jihadist", app))
		app.map["India"].sleeperCells = 0
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.map["India"].sleeperCells = 1
		app.map["India"].posture = "Soft"
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.testCountry("Thailand")
		app.map["Thailand"].sleeperCells = 1
		app.map["Thailand"].posture = "Hard"
		self.assertTrue(app.deck["115"].playable("US", app))
		self.assertTrue(app.deck["115"].playable("Jihadist", app))
		app.map["Thailand"].sleeperCells = 0
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.map["Thailand"].sleeperCells = 1
		app.map["Thailand"].posture = "Soft"
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.testCountry("Philippines")
		app.map["Philippines"].sleeperCells = 1
		app.map["Philippines"].posture = "Hard"
		self.assertTrue(app.deck["115"].playable("US", app))
		self.assertTrue(app.deck["115"].playable("Jihadist", app))
		app.map["Philippines"].sleeperCells = 0
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))
		app.map["Philippines"].sleeperCells = 1
		app.map["Philippines"].posture = "Soft"
		self.assertFalse(app.deck["115"].playable("US", app))
		self.assertFalse(app.deck["115"].playable("Jihadist", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["115"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Philippines")
		app.map["Philippines"].sleeperCells = 1
		app.map["Philippines"].posture = "Hard"
		app.deck["115"].playEvent("US", app)
		self.assertTrue(app.map["Philippines"].sleeperCells == 0)
 		
 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["Indonesia/Malaysia"])
		app.testCountry("Indonesia/Malaysia")
		app.map["Indonesia/Malaysia"].sleeperCells = 1
		app.map["Indonesia/Malaysia"].alignment = "Ally"
		app.testCountry("Philippines")
		app.map["Philippines"].sleeperCells = 1
		app.map["Philippines"].posture = "Hard"
		print "Choose Indonesia/Malaysia"
		app.deck["115"].playEvent("US", app)
		self.assertTrue(app.map["Indonesia/Malaysia"].sleeperCells == 0)
 		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Indonesia/Malaysia")
		app.map["Indonesia/Malaysia"].sleeperCells = 1
		app.map["Indonesia/Malaysia"].alignment = "Ally"
		app.deck["115"].playEvent("Jihadist", app)
		self.assertTrue(app.map["Indonesia/Malaysia"].plots == 1)
		
class cardHundredSixteen(unittest.TestCase):
	'''KSM'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["116"].playable("Jihadist", app))
		self.assertFalse(app.deck["116"].playable("US", app))
		app.testCountry("Iraq")
		app.map["Iraq"].alignment = "Ally"
		app.map["Iraq"].plots = 1
		self.assertTrue(app.deck["116"].playable("US", app))

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["116"].playable("Jihadist", app))
		self.assertFalse(app.deck["116"].playable("US", app))
		app.testCountry("Canada")
		app.map["Canada"].plots = 1
		self.assertTrue(app.deck["116"].playable("US", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["116"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].alignment = "Ally"
		app.map["Iraq"].plots = 2
		app.testCountry("Pakistan")
		app.map["Pakistan"].alignment = "Neutral"
		app.map["Pakistan"].plots = 2
		app.testCountry("Canada")
		app.map["Canada"].plots = 1
		app.deck["116"].playEvent("US", app)
		self.assertTrue(app.map["Iraq"].plots == 0)
		self.assertTrue(app.map["Pakistan"].plots == 2)
		self.assertTrue(app.map["Canada"].plots == 0)
 		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		app.deck["116"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 1)
 		self.assertTrue(app.map["Iraq"].activeCells == 0)
 		self.assertTrue(app.map["Iraq"].plots == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].governance = 4
		app.map["Iraq"].sleeperCells = 1
		app.deck["116"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 1)
 		self.assertTrue(app.map["Iraq"].activeCells == 0)
 		self.assertTrue(app.map["Iraq"].plots == 0)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.testCountry("Iraq")
		app.map["Iraq"].sleeperCells = 1
		app.map["United States"].sleeperCells = 1
		app.deck["116"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Iraq"].sleeperCells == 1)
 		self.assertTrue(app.map["Iraq"].activeCells == 0)
 		self.assertTrue(app.map["Iraq"].plots == 0)
 		self.assertTrue(app.map["United States"].sleeperCells == 1)
 		self.assertTrue(app.map["United States"].activeCells == 0)
 		self.assertTrue(app.map["United States"].plots == 1)

class cardHundredSeventeen(unittest.TestCase):
	'''Oil Price Spike'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["117"].playable("Jihadist", app))
		self.assertTrue(app.deck["117"].playable("US", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["117"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["117"].playEvent("US", app)
 		self.assertTrue(app.countryResources("Saudi Arabia") == 4)

 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["y"])
		app.deck["117"].playEvent("Jihadist", app)
 		self.assertTrue(app.countryResources("Saudi Arabia") == 4)
		app.deck["117"].playEvent("US", app)
 		self.assertTrue(app.countryResources("Saudi Arabia") == 5)

class cardHundredEightteen(unittest.TestCase):
	'''Oil Price Spike'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["118"].playable("Jihadist", app))
		self.assertTrue(app.deck["118"].playable("US", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["118"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["118"].playEvent("US", app)
 		self.assertTrue(app.countryResources("Saudi Arabia") == 4)

 		app = Labyrinth(1, 1, testBlankScenarioSetup, ["y"])
		app.deck["118"].playEvent("Jihadist", app)
 		self.assertTrue(app.countryResources("Saudi Arabia") == 4)
		app.deck["118"].playEvent("US", app)
 		self.assertTrue(app.countryResources("Saudi Arabia") == 5)

class cardHundredNineteen(unittest.TestCase):
	'''Saleh'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["119"].playable("Jihadist", app))
		self.assertTrue(app.deck["119"].playable("US", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["119"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["119"].playEvent("US", app)
 		self.assertTrue(app.map["Yemen"].governance != 0)
 		self.assertTrue(app.map["Yemen"].alignment == "Ally")
 		self.assertTrue(app.map["Yemen"].aid == 1)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.map["Yemen"].governance = 4
		app.map["Yemen"].alignment = "Neutral"
		app.deck["119"].playEvent("US", app)
 		self.assertTrue(app.map["Yemen"].governance != 0)
 		self.assertTrue(app.map["Yemen"].alignment == "Neutral")
 		self.assertTrue(app.map["Yemen"].aid == 0)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["119"].playEvent("Jihadist", app)
 		self.assertTrue(app.map["Yemen"].governance != 0)
 		self.assertTrue(app.map["Yemen"].alignment == "Adversary")
 		self.assertTrue(app.map["Yemen"].besieged == 1)

class cardHundredTwenty(unittest.TestCase):
	'''US Election'''

	def testPlayable(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertTrue(app.deck["120"].playable("Jihadist", app))
		self.assertTrue(app.deck["120"].playable("US", app))

	def testPutsCell(self):
		app = Labyrinth(1, 1, testBlankScenarioSetup)
		self.assertFalse(app.deck["120"].putsCell(app))			

	def testEvent(self):
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.executeCardUSElection(5)
 		self.assertTrue(app.prestige == 8)
 		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
 		app.executeCardUSElection(4)
 		self.assertTrue(app.prestige == 6)
 		
 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["120"].playEvent("US", app)
 		self.assertTrue(app.prestige != 7)

 		app = Labyrinth(1, 1, testBlankScenarioSetup)
		app.deck["120"].playEvent("US", app)
 		self.assertTrue(app.prestige != 7)

if __name__ == "__main__":
	unittest.main()   