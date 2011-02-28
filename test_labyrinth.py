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

if __name__ == "__main__":
	unittest.main()   