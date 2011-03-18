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
	self.map["Saudi Arabia"].troops = 2
	self.map["Pakistan"].governance = 2
	self.map["Pakistan"].alignment = "Neutral"
	self.map["Pakistan"].troops = 2
	self.map["Pakistan"].activeCells = 4
	self.map["Gulf States"].governance = 2
	self.map["Gulf States"].alignment = "Ally"
	self.map["Gulf States"].troops = 4
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
	self.map["Saudi Arabia"].troops = 2
	self.map["Pakistan"].governance = 2
	self.map["Pakistan"].alignment = "Neutral"
	self.map["Pakistan"].troops = 2
	self.map["Pakistan"].activeCells = 4
	self.map["Gulf States"].governance = 2
	self.map["Gulf States"].alignment = "Ally"
	self.map["Gulf States"].troops = 2
	self.map["Gulf States"].sleeperCells = 1
	self.map["Gulf States"].activeCells = 4
	self.map["Afghanistan"].governance = 1
	self.map["Afghanistan"].alignment = "Ally"
	self.map["Afghanistan"].activeCells = 4
	self.map["Afghanistan"].regimeChange = 1
	self.map["Afghanistan"].troops = 6
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
	self.map["Saudi Arabia"].troops = 2
	self.map["Pakistan"].governance = 2
	self.map["Pakistan"].alignment = "Neutral"
	self.map["Pakistan"].troops = 2
	self.map["Pakistan"].activeCells = 4
	self.map["Gulf States"].governance = 2
	self.map["Gulf States"].alignment = "Ally"
	self.map["Gulf States"].troops = 4
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
		self.assertEqual(app.map["Afghanistan"].troops, 0)
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
		self.assertEqual(app.map["Afghanistan"].troops, 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 9)

		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops, 0)
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
		self.assertEqual(app.map["Afghanistan"].troops, 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 5)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops, 0)
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
		self.assertEqual(app.map["Afghanistan"].troops, 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 5)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops, 0)
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
		self.assertEqual(app.map["Afghanistan"].troops, 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 9)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops, 0)
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
		self.assertEqual(app.map["Afghanistan"].troops, 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 2)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops, 0)
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
		self.assertEqual(app.map["Afghanistan"].troops, 6)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 12)
		self.assertEqual(app.troops, 3)
	
		app = Labyrinth(1, 1, testScenarioSetup)
		app.troops -= 8
		app.map["Pakistan"].troops += 8
		app.map["United States"].posture = "Hard"
		self.assertEqual(app.map["Afghanistan"].governance, 4)
		self.assertEqual(app.map["Afghanistan"].alignment, "Adversary")
		self.assertEqual(app.map["Afghanistan"].troops, 0)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 4)
		self.assertEqual(app.map["Afghanistan"].activeCells, 0)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 0)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 1)
		self.assertEqual(app.map["Pakistan"].troops, 10)
		govRoll = 5
		prestigeRolls = (6,6,5)
		app.handleRegimeChange("Afghanistan", "Pakistan", 7, govRoll, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 2)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops, 7)
		self.assertEqual(app.map["Afghanistan"].sleeperCells, 0)
		self.assertEqual(app.map["Afghanistan"].activeCells, 4)
		self.assertEqual(app.map["Afghanistan"].regimeChange, 1)
		self.assertEqual(app.prestige, 12)
		self.assertEqual(app.troops, 1)
		self.assertEqual(app.map["Pakistan"].troops, 3)

class withdrawHandler(unittest.TestCase):
	'''Test Withdraw'''
	
	def testWithdraw(self):
		app = Labyrinth(1, 1, test2ScenarioSetup)
		app.map["United States"].posture = "Soft"	
		self.assertEqual(app.map["Afghanistan"].governance, 1)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops, 6)
		self.assertEqual(app.map["Afghanistan"].aid, 1)
		self.assertEqual(app.map["Afghanistan"].besieged, 0)
		self.assertEqual(app.map["Saudi Arabia"].troops, 2)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 3)
		prestigeRolls = (5,2,5)
		app.handleWithdraw("Afghanistan", "Saudi Arabia", 4, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 1)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops, 2)
		self.assertEqual(app.map["Afghanistan"].aid, 0)
		self.assertEqual(app.map["Afghanistan"].besieged, 1)
		self.assertEqual(app.map["Saudi Arabia"].troops, 6)
		self.assertEqual(app.prestige, 9)
		self.assertEqual(app.troops, 3)

		app = Labyrinth(1, 1, test2ScenarioSetup)
		app.map["United States"].posture = "Soft"	
		self.assertEqual(app.map["Afghanistan"].governance, 1)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops, 6)
		self.assertEqual(app.map["Afghanistan"].aid, 1)
		self.assertEqual(app.map["Afghanistan"].besieged, 0)
		self.assertEqual(app.map["Saudi Arabia"].troops, 2)
		self.assertEqual(app.prestige, 7)
		self.assertEqual(app.troops, 3)
		prestigeRolls = (2,3,5)
		app.handleWithdraw("Afghanistan", "track", 5, prestigeRolls)
		self.assertEqual(app.map["Afghanistan"].governance, 1)
		self.assertEqual(app.map["Afghanistan"].alignment, "Ally")
		self.assertEqual(app.map["Afghanistan"].troops, 1)
		self.assertEqual(app.map["Afghanistan"].aid, 0)
		self.assertEqual(app.map["Afghanistan"].besieged, 1)
		self.assertEqual(app.map["Saudi Arabia"].troops, 2)
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
		app.map["Gulf States"].besieged = 0
		app.map["Afghanistan"].governance = 3
		app.map["Afghanistan"].sleeperCells = 3
		app.map["Afghanistan"].activeCells = 3
		app.map["Afghanistan"].troops = 1
		app.map["Afghanistan"].besieged = 0

		self.assertEqual(app.majorJihadChoice(3), "Gulf States")	# 3 Ops
		self.assertEqual(app.majorJihadChoice(2), "Gulf States")	# 2 Ops
		self.assertEqual(app.majorJihadChoice(1), False)	# 1 Ops
		
		app.map["Saudi Arabia"].governance = 3
		app.map["Saudi Arabia"].sleeperCells = 5
		app.map["Saudi Arabia"].activeCells = 4
		app.map["Saudi Arabia"].troops = 4
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
		app.map["Pakistan"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 0
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Gulf States"].troops = 4
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
		app.map["Iraq"].troops = 2
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
		app.map["Gulf States"].troops = 5
		self.assertEqual(app.recruitChoice(), "Iraq")
		app.map["Gulf States"].troops = 6
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
		app.map["Afghanistan"].troops = 1
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
		app.map["Afghanistan"].troops = 1
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
		app.map["Egypt"].troops = 2
		sources = app.travelSources(dest, 1)
		self.assertEqual(sources,["Iraq"])
		app.map["Egypt"].activeCells = 3
		sources = app.travelSources(dest, 1)
		self.assertEqual(sources,["Egypt"])
		
		app.map["Yemen"].governance = 4
		app.map["Yemen"].activeCells = 3
		app.map["Yemen"].troops = 2
		sources = app.travelSources(dest, 3)
		self.assertEqual(sources,["Egypt"])
		sources = app.travelSources(dest, 2)
		self.assertEqual(sources,["Yemen"])
		
	#multi	

		app = Labyrinth(1, 1, testBlankScenarioSetup)
		
		app.map["Gulf States"].governance = 3
		app.map["Gulf States"].besieged = 1
		
		app.map["Afghanistan"].governance = 3
		app.map["Afghanistan"].troops = 1
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
		app.map["Egypt"].troops = 2
		app.map["Egypt"].activeCells = 3
		
		app.map["Yemen"].governance = 4
		app.map["Yemen"].activeCells = 4
		app.map["Yemen"].troops = 2
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
		app.map["Iraq"].troops = 2
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
		app.map["Iraq"].troops = 1
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
		app.map["Iraq"].troops = 1
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
		app.map["Iraq"].troops = 1
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
		app.map["Iraq"].troops = 1
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
		app.map["Iraq"].troops = 1
		app.map["Philippines"].sleeperCells = 1
		app.map["Philippines"].troops = 1
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
				
				
if __name__ == "__main__":
	unittest.main()   