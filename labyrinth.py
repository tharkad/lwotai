import cmd
import random

class Country:
	name = ""
	type = ""
	posture = ""
	alignment = ""
	governance = 0
	schengen = False
	recruit = 0
	troops = 0
	activeCells = 0
	sleeperCells = 0
	oil = False
	resources = 0
	links = []
	schengenLink = False
	aid = 0
	besiged = 0
	regimeChange = 0
	cadre = 0
	plots = 0
	
	def __init__(self, theName, theType, thePosture, theAlignment, theGovernance, theSchengen, theRecruit, no1,no2,no3, theOil, theResources):
		self.name = theName
		self.type = theType
		self.posture = thePosture
		self.alignment = theAlignment
		self.governance = theGovernance
		self.schengen = theSchengen
		self.recruit = theRecruit
		self.troops = 0
		self.activeCells = 0
		self.sleeperCells = 0
		self.oil = theOil
		self.resources = theResources
		self.aid = 0
		self.besieged = 0
		self.regimeChange = 0
		self.cadre = 0
		self.plots = 0
		self.links = []
		
	def govStr(self):
		if self.governance == 1:
			return "Good"
		elif self.governance == 2:
			return "Fair"
		elif self.governance == 3:
			return "Poor"
		elif self.governance == 4:
			return "Islamic Rule"

	def typePretty(self, theType):
		if theType == "Non-Muslim":
			return "NM"
		elif theType == "Suni":
			return "SU"
		elif theType == "Shia-Mix":
			return "SM"
		else:
			return "IR"
		
	def countryStr(self):
		if self.type == "Shia-Mix" or self.type == "Suni":
			return "%s, %s %s\n   Troops:%d Active:%d Sleeper:%d Cadre:%d Aid:%d Besieged:%d Reg Ch:%d Plots:%d" % (self.name, self.govStr(),self.alignment,self.troops,self.activeCells,self.sleeperCells, self.cadre, self.aid, self.besieged, self.regimeChange, self.plots)
		elif self.type == "Non-Muslim" and self.type != "United States":
			return "%s - Posture:%s\n   Active:%d Sleeper:%d Cadre:%d Plots:%d" % (self.name,self.posture, self.activeCells,self.sleeperCells, self.cadre, self.plots)
			
	def printCountry(self):
		print self.countryStr()
		
class Card:
	number = 0
	name = ""
	type = ""
	ops = 0
	
	def __init__(self, theNumber, theName, theType, theOps):
		self.number = theNumber
		self.name = theName
		self.type = theType
		self.ops = theOps
		
	def playable(self, side):
		return False
		
	def playEvent(self, side):
		print "DEBUG: Event play not implemented"
		
	def useForOpsStr(self):
		return "* Card %s used for %d Ops." % (self.number, self.name)

class Labyrinth(cmd.Cmd):

	map = {}
	scenario = 0
	ideology = 0
	prestige = 0
	troops = 0
	cells = 0
	funding = 0
	startYear = 0
	turn = 0
	uCard = 0
	jCard = 0
	phase = ""
	history = []
	deck = {}

	def __init__(self, theScenario, theIdeology, setupFuntion = None):
		cmd.Cmd.__init__(self)
		self.scenario = theScenario
		self.ideology = theIdeology
		self.prestige = 0
		self.troops = 0
		self.cells = 0
		self.funding = 0
		self.startYear = 0
		self.turn = 1
		self.uCard = 1
		self.jCard = 1
		self.phase = ""
		self.map = {}
		self.mapSetup()
		if setupFuntion:
			setupFuntion(self)
		else:
			#self.scenarioSetup()
			self.testScenarioSetup()
		self.history = []
		self.prompt = "Command: "
		self.outputToHistory("Game Start")
		print "%d (Turn %s)" % (self.startYear + (self.turn - 1), self.turn)
		self.outputToHistory(self.phase)
		self.deck = {}
		self.deckSetup()

	def mapSetup(self):
		self.map["Canada"] = Country("Canada", "Non-Muslim", "", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["United States"] = Country("United States", "Non-Muslim", "Hard", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["United Kingdom"] = Country("United Kingdom", "Non-Muslim", "", "", 1, False, 3, 0, 0, 0, False, 0)
		self.map["Serbia"] = Country("Serbia", "Non-Muslim", "", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["Israel"] = Country("Israel", "Non-Muslim", "Hard", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["India"] = Country("India", "Non-Muslim", "", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["Scandinavia"] = Country("Scandinavia", "Non-Muslim", "", "", 1, True, 0, 0, 0, 0, False, 0)
		self.map["Eastern Europe"] = Country("Eastern Europe", "Non-Muslim", "", "", 1, True, 0, 0, 0, 0, False, 0)
		self.map["Benelux"] = Country("Benelux", "Non-Muslim", "", "", 1, True, 0, 0, 0, 0, False, 0)
		self.map["Germany"] = Country("Germany", "Non-Muslim", "", "", 1, True, 0, 0, 0, 0, False, 0)
		self.map["France"] = Country("France", "Non-Muslim", "", "", 1, True, 2, 0, 0, 0, False, 0)
		self.map["Italy"] = Country("Italy", "Non-Muslim", "", "", 1, True, 0, 0, 0, 0, False, 0)
		self.map["Spain"] = Country("Spain", "Non-Muslim", "", "", 1, True, 2, 0, 0, 0, False, 0)
		self.map["Russia"] = Country("Russia", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["Caucasus"] = Country("Caucasus", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["China"] = Country("China", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["Kenya/Tanzania"] = Country("Kenya/Tanzania", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["Thailand"] = Country("Thailand", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["Philippines"] = Country("Philippines", "Non-Muslim", "", "", 2, True, 3, 0, 0, 0, False, 0)
		self.map["Morocco"] = Country("Morocco", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 2)
		self.map["Algeria/Tunisia"] = Country("Algeria/Tunisia", "Suni", "", "", 0, False, 0, 0, 0, 0, True, 2)
		self.map["Libya"] = Country("Libya", "Suni", "", "", 0, False, 0, 0, 0, 0, True, 1)
		self.map["Egypt"] = Country("Egypt", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 3)
		self.map["Sudan"] = Country("Sudan", "Suni", "", "", 0, False, 0, 0, 0, 0, True, 1)
		self.map["Somalia"] = Country("Somalia", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 1)
		self.map["Jordan"] = Country("Jordan", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 1)
		self.map["Syria"] = Country("Syria", "Suni", "", 0, 0, False, 0, 0, 0, 0, False, 2)
		self.map["Central Asia"] = Country("Central Asia", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 2)
		self.map["Indonesia/Malaysia"] = Country("Indonesia/Malaysia", "Suni", "", "", 0, False, 0, 0, 0, 0, True, 3)
		self.map["Turkey"] = Country("Turkey", "Shia-Mix", "", "", 0, False, 0, 0, 0, 0, False, 2)
		self.map["Lebanon"] = Country("Lebanon", "Shia-Mix", "", "", 0, False, 0, 0, 0, 0, False, 1)
		self.map["Yemen"] = Country("Yemen", "Shia-Mix", "", "", 0, False, 0, 0, 0, 0, False, 1)
		self.map["Iraq"] = Country("Iraq", "Shia-Mix", "", "", 0, False, 0, 0, 0, 0, True, 3)
		self.map["Saudi Arabia"] = Country("Saudi Arabia", "Shia-Mix", "", "", 0, False, 0, 2, 0, 0, True, 3)
		self.map["Gulf States"] = Country("Gulf States", "Shia-Mix", "", "", 0, False, 0, 2, 0, 0, True, 3)
		self.map["Pakistan"] = Country("Pakistan", "Shia-Mix", "", "", 0, False, 0, 0, 0, 0, False, 2)
		self.map["Afghanistan"] = Country("Afghanistan", "Shia-Mix", "", "", 0, False, 0, 0, 0, 0, False, 1)
		self.map["Iran"] = Country("Iran", "Iran", "", "", 0, False, 0, 0, 0, 0, False, 0)
	
	# 	self.map["Canada"] = Country("Canada", "Non-Muslim", "", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["Canada"].links.append(self.map["United States"])
		self.map["Canada"].links.append(self.map["United Kingdom"])
		self.map["Canada"].schengenLink = True
	# 	self.map["United States"] = Country("United States", "Non-Muslim", "Hard", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["United States"].links.append(self.map["Canada"])
		self.map["United States"].links.append(self.map["United Kingdom"])
		self.map["United States"].links.append(self.map["Philippines"])
		self.map["United States"].schengenLink = True
	# 	self.map["United Kingdom"] = Country("United Kingdom", "Non-Muslim", "", "", 1, False, 3, 0, 0, 0, False, 0)
		self.map["United Kingdom"].links.append(self.map["Canada"])
		self.map["United Kingdom"].links.append(self.map["United States"])
		self.map["United Kingdom"].schengenLink = True
	# 	self.map["Serbia"] = Country("Serbia", "Non-Muslim", "", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["Serbia"].links.append(self.map["Russia"])
		self.map["Serbia"].links.append(self.map["Turkey"])
		self.map["Serbia"].schengenLink = True
	# 	self.map["Israel"] = Country("Israel", "Non-Muslim", "Hard", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["Israel"].links.append(self.map["Lebanon"])
		self.map["Israel"].links.append(self.map["Jordan"])
		self.map["Israel"].links.append(self.map["Egypt"])
	# 	self.map["India"] = Country("India", "Non-Muslim", "", "", 1, False, 0, 0, 0, 0, False, 0)
		self.map["India"].links.append(self.map["Pakistan"])
		self.map["India"].links.append(self.map["Indonesia/Malaysia"])
	# 	self.map["Russia"] = Country("Russia", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["Russia"].links.append(self.map["Serbia"])
		self.map["Russia"].links.append(self.map["Turkey"])
		self.map["Russia"].links.append(self.map["Caucasus"])
		self.map["Russia"].links.append(self.map["Central Asia"])
		self.map["Russia"].schengenLink = True
	# 	self.map["Caucasus"] = Country("Caucasus", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["Caucasus"].links.append(self.map["Russia"])
		self.map["Caucasus"].links.append(self.map["Turkey"])
		self.map["Caucasus"].links.append(self.map["Iran"])
		self.map["Caucasus"].links.append(self.map["Central Asia"])
	# 	self.map["China"] = Country("China", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["China"].links.append(self.map["Central Asia"])
		self.map["China"].links.append(self.map["Thailand"])
	# 	self.map["Kenya/Tanzania"] = Country("Kenya/Tanzania", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["Kenya/Tanzania"].links.append(self.map["Sudan"])
		self.map["Kenya/Tanzania"].links.append(self.map["Somalia"])
	# 	self.map["Thailand"] = Country("Thailand", "Non-Muslim", "", "", 2, True, 0, 0, 0, 0, False, 0)
		self.map["Thailand"].links.append(self.map["China"])
		self.map["Thailand"].links.append(self.map["Philippines"])
		self.map["Thailand"].links.append(self.map["Indonesia/Malaysia"])
	# 	self.map["Philippines"] = Country("Philippines", "Non-Muslim", "", "", 2, True, 3, 0, 0, 0, False, 0)
		self.map["Philippines"].links.append(self.map["United States"])
		self.map["Philippines"].links.append(self.map["Thailand"])
		self.map["Philippines"].links.append(self.map["Indonesia/Malaysia"])
	# 	self.map["Morocco"] = Country("Morocco", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 2)
		self.map["Morocco"].links.append(self.map["Algeria/Tunisia"])
		self.map["Morocco"].schengenLink = True
	# 	self.map["Algeria/Tunisia"] = Country("Algeria/Tunisia", "Suni", "", "", 0, False, 0, 0, 0, 0, True, 2)
		self.map["Algeria/Tunisia"].links.append(self.map["Morocco"])
		self.map["Algeria/Tunisia"].links.append(self.map["Libya"])
		self.map["Algeria/Tunisia"].schengenLink = True
	# 	self.map["Libya"] = Country("Libya", "Suni", "", "Adversary", 3, False, 0, 0, 0, 0, True, 1)
		self.map["Libya"].links.append(self.map["Algeria/Tunisia"])
		self.map["Libya"].links.append(self.map["Egypt"])
		self.map["Libya"].links.append(self.map["Sudan"])
		self.map["Libya"].schengenLink = True
	# 	self.map["Egypt"] = Country("Egypt", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 3)
		self.map["Egypt"].links.append(self.map["Libya"])
		self.map["Egypt"].links.append(self.map["Israel"])
		self.map["Egypt"].links.append(self.map["Sudan"])
	# 	self.map["Sudan"] = Country("Sudan", "Suni", "", "", 0, False, 0, 0, 0, 0, True, 1)
		self.map["Sudan"].links.append(self.map["Libya"])
		self.map["Sudan"].links.append(self.map["Egypt"])
		self.map["Sudan"].links.append(self.map["Kenya/Tanzania"])
		self.map["Sudan"].links.append(self.map["Somalia"])
	# 	self.map["Somalia"] = Country("Somalia", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 1)
		self.map["Somalia"].links.append(self.map["Sudan"])
		self.map["Somalia"].links.append(self.map["Kenya/Tanzania"])
		self.map["Somalia"].links.append(self.map["Yemen"])
	# 	self.map["Jordan"] = Country("Jordan", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 1)
		self.map["Jordan"].links.append(self.map["Israel"])
		self.map["Jordan"].links.append(self.map["Syria"])
		self.map["Jordan"].links.append(self.map["Iraq"])
		self.map["Jordan"].links.append(self.map["Saudi Arabia"])
	# 	self.map["Syria"] = Country("Syria", "Suni", "Adversary", "Fair", 2, False, 0, 0, 0, 0, False, 2)
		self.map["Syria"].links.append(self.map["Turkey"])
		self.map["Syria"].links.append(self.map["Lebanon"])
		self.map["Syria"].links.append(self.map["Jordan"])
		self.map["Syria"].links.append(self.map["Iraq"])
	# 	self.map["Central Asia"] = Country("Central Asia", "Suni", "", "", 0, False, 0, 0, 0, 0, False, 2)
		self.map["Central Asia"].links.append(self.map["Russia"])
		self.map["Central Asia"].links.append(self.map["Caucasus"])
		self.map["Central Asia"].links.append(self.map["Iran"])
		self.map["Central Asia"].links.append(self.map["Afghanistan"])
		self.map["Central Asia"].links.append(self.map["China"])
	# 	self.map["Indonesia/Malaysia"] = Country("Indonesia/Malaysia", "Suni", "", "", 0, False, 0, 0, 0, 0, True, 3)
		self.map["Indonesia/Malaysia"].links.append(self.map["Thailand"])
		self.map["Indonesia/Malaysia"].links.append(self.map["India"])
		self.map["Indonesia/Malaysia"].links.append(self.map["Philippines"])
		self.map["Indonesia/Malaysia"].links.append(self.map["Pakistan"])
	# 	self.map["Turkey"] = Country("Turkey", "Shia-Mix", "", "", 0, False, 0, 0, 0, 0, False, 2)
		self.map["Turkey"].links.append(self.map["Serbia"])
		self.map["Turkey"].links.append(self.map["Russia"])
		self.map["Turkey"].links.append(self.map["Caucasus"])
		self.map["Turkey"].links.append(self.map["Iran"])
		self.map["Turkey"].links.append(self.map["Syria"])
		self.map["Turkey"].links.append(self.map["Iraq"])
		self.map["Turkey"].schengenLink = True
	# 	self.map["Lebanon"] = Country("Lebanon", "Shia-Mix", "", "", 0, False, 0, 0, 0, 0, False, 1)
		self.map["Lebanon"].links.append(self.map["Syria"])
		self.map["Lebanon"].links.append(self.map["Israel"])
		self.map["Lebanon"].schengenLink = True
	# 	self.map["Yemen"] = Country("Yemen", "Shia-Mix", "", "", 0, False, 0, 0, 0, 0, False, 1)
		self.map["Yemen"].links.append(self.map["Saudi Arabia"])
		self.map["Yemen"].links.append(self.map["Somalia"])
	# 	self.map["Iraq"] = Country("Iraq", "Shia-Mix", "", "Adversary", 3, False, 0, 0, 0, 0, True, 3)
		self.map["Iraq"].links.append(self.map["Syria"])
		self.map["Iraq"].links.append(self.map["Turkey"])
		self.map["Iraq"].links.append(self.map["Iran"])
		self.map["Iraq"].links.append(self.map["Gulf States"])
		self.map["Iraq"].links.append(self.map["Saudi Arabia"])
		self.map["Iraq"].links.append(self.map["Jordan"])
	# 	self.map["Saudi Arabia"] = Country("Saudi Arabia", "Shia-Mix", "", "Ally", 3, False, 0, 2, 0, 0, True, 3)
		self.map["Saudi Arabia"].links.append(self.map["Jordan"])
		self.map["Saudi Arabia"].links.append(self.map["Iraq"])
		self.map["Saudi Arabia"].links.append(self.map["Gulf States"])
		self.map["Saudi Arabia"].links.append(self.map["Yemen"])
	# 	self.map["Gulf States"] = Country("Gulf States", "Shia-Mix", "", "Ally", 2, False, 0, 2, 0, 0, True, 3)
		self.map["Gulf States"].links.append(self.map["Iran"])
		self.map["Gulf States"].links.append(self.map["Pakistan"])
		self.map["Gulf States"].links.append(self.map["Saudi Arabia"])
		self.map["Gulf States"].links.append(self.map["Iraq"])
	# 	self.map["Pakistan"] = Country("Pakistan", "Shia-Mix", "", "Neutral", 2, False, 0, 0, 0, 0, False, 2)
		self.map["Pakistan"].links.append(self.map["Iran"])
		self.map["Pakistan"].links.append(self.map["Afghanistan"])
		self.map["Pakistan"].links.append(self.map["India"])
		self.map["Pakistan"].links.append(self.map["Gulf States"])
		self.map["Pakistan"].links.append(self.map["Indonesia/Malaysia"])
	# 	self.map["Afghanistan"] = Country("Afghanistan", "Shia-Mix", "", "Adversary", 4, False, 0, 0, 0, 4, False, 1)
		self.map["Afghanistan"].links.append(self.map["Central Asia"])
		self.map["Afghanistan"].links.append(self.map["Pakistan"])
		self.map["Afghanistan"].links.append(self.map["Iran"])
	# 	self.map["Iran"] = Country("Iran", "Iran", "", "", 0, False, 0, 0, 0, 0, False, 0)
		self.map["Iran"].links.append(self.map["Central Asia"])
		self.map["Iran"].links.append(self.map["Afghanistan"])
		self.map["Iran"].links.append(self.map["Pakistan"])
		self.map["Iran"].links.append(self.map["Gulf States"])
		self.map["Iran"].links.append(self.map["Iraq"])
		self.map["Iran"].links.append(self.map["Turkey"])
		self.map["Iran"].links.append(self.map["Caucasus"])
		
	def scenarioSetup(self):
		if self.scenario == 1 or self.scenario == 2: # Let's Roll
			self.startYear = 2001
			self.turn = 1
			self.prestige = 7
			self.troops = 11
			self.funding = 9
			self.cells = 11
			self.phase = "Jihadist Action Phase"
			self.map["Libya"].governance = 3
			self.map["Libya"].alignment = "Adversary"
			self.map["Syria"].governance = 2
			self.map["Syria"].alignment = "Adversary"
			self.map["Iraq"].governance = 3
			self.map["Iraq"].alignment = "Adversary"
			self.map["Saudi Arabia"].governance = 3
			self.map["Saudi Arabia"].alignment = "Ally"
			self.map["Saudi Arabia"].troops = 2
			self.map["Gulf States"].governance = 2
			self.map["Gulf States"].alignment = "Ally"
			self.map["Gulf States"].troops = 2
			self.map["Pakistan"].governance = 2
			self.map["Pakistan"].alignment = "Neutral"
			self.map["Afghanistan"].governance = 4
			self.map["Afghanistan"].alignment = "Adversary"
			self.map["Afghanistan"].sleeperCells = 4
			self.map["Somalia"].besieged = 1
			if self.scenario == 1:
				self.map["United States"].posture = "Hard"
			else:
				self.map["United States"].posture = "Soft"			
	
	def testScenarioSetup(self):
		if self.scenario == 1 or self.scenario == 2: # Let's Roll
			self.startYear = 2001
			self.turn = 1
			self.prestige = 7
			self.troops = 11
			self.funding = 9
			self.cells = 11
			self.phase = "Jihadist Action Phase"
			self.map["France"].posture = "Hard"
			self.map["France"].cadre = 1
			self.map["Spain"].posture = "Soft"
			self.map["Spain"].sleeperCells = 1
			self.map["Germany"].posture = "Hard"
			self.map["Germany"].activeCells = 1
			self.map["Germany"].sleeperCells = 1
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
			self.map["Pakistan"].governance = 3
			self.map["Pakistan"].alignment = "Ally"
			self.map["Pakistan"].troops = 2
			self.map["Pakistan"].activeCells = 4
			self.map["Gulf States"].governance = 2
			self.map["Gulf States"].alignment = "Ally"
			self.map["Gulf States"].troops = 2
			self.map["Gulf States"].sleeperCells = 3
			self.map["Gulf States"].activeCells = 4
			self.map["Pakistan"].governance = 2
			self.map["Pakistan"].alignment = "Neutral"
			self.map["Afghanistan"].governance = 4
			self.map["Afghanistan"].alignment = "Adversary"
			self.map["Afghanistan"].sleeperCells = 4
			self.map["Somalia"].besieged = 1
			if self.scenario == 1:
				self.map["United States"].posture = "Hard"
			else:
				self.map["United States"].posture = "Soft"		
				
	def deckSetup(self):
		self.deck["1"] = Card(1,"US","Backlash",1)
		self.deck["2"] = Card(2,"US","Biometrics",1)
		self.deck["3"] = Card(3,"US","CTR",1)
		self.deck["4"] = Card(4,"US","Moro Talks",1)
		self.deck["5"] = Card(5,"US","NEST",1)
		self.deck["6"] = Card(6,"US","Sacntions",1)
		self.deck["7"] = Card(7,"US","Sanctions",1)
		self.deck["8"] = Card(8,"US","Special Forces",1)
		self.deck["9"] = Card(9,"US","Special Forces",1)
		self.deck["10"] = Card(10,"US","Special Forces",1)
		self.deck["11"] = Card(11,"US","Abbas",2)
		self.deck["12"] = Card(12,"US","Al-Azhar",2)
		self.deck["13"] = Card(13,"US","Anbar Awakening",2)
		self.deck["14"] = Card(14,"US","Covert Action",2)
		self.deck["15"] = Card(15,"US","Ethiopia Strikes",2)
		self.deck["16"] = Card(16,"US","Euro-Islam",2)
		self.deck["17"] = Card(17,"US","FSB",2)
		self.deck["18"] = Card(18,"US","Intel Community",2)
		self.deck["19"] = Card(19,"US","Kemalist Republic",2)
		self.deck["20"] = Card(20,"US","King Abdullah",2)
		self.deck["21"] = Card(21,"US","Let's Roll",2)
		self.deck["22"] = Card(22,"US","Mossad and Shin Bet",2)
		self.deck["23"] = Card(23,"US","Predator",2)
		self.deck["24"] = Card(24,"US","Predator",2)
		self.deck["25"] = Card(25,"US","Predator",2)
		self.deck["26"] = Card(26,"US","Quartet",2)
		self.deck["27"] = Card(27,"US","Sadam Captured",2)
		self.deck["28"] = Card(28,"US","Sharia",2)
		self.deck["29"] = Card(29,"US","Tony Blair",2)
		self.deck["30"] = Card(30,"US","UN Nation Building",2)
		self.deck["31"] = Card(31,"US","Wiretapping",2)
		self.deck["32"] = Card(32,"US","Back Channel",3)
		self.deck["33"] = Card(33,"US","Benazir Bhutto",3)
		self.deck["34"] = Card(34,"US","Enhanced Measures",3)
		self.deck["35"] = Card(35,"US","Hijab",3)
		self.deck["36"] = Card(36,"US","Indo-Pakistani Talks",3)
		self.deck["37"] = Card(37,"US","Iraqi WMD",3)
		self.deck["38"] = Card(38,"US","Libyan Deal",3)
		self.deck["39"] = Card(39,"US","Libyan WMD",3)
		self.deck["40"] = Card(40,"US","Mass Turnout",3)
		self.deck["41"] = Card(41,"US","NATO",3)
		self.deck["42"] = Card(42,"US","Pakistani Offensive",3)
		self.deck["43"] = Card(43,"US","Patriot Act",3)
		self.deck["44"] = Card(44,"US","Renditions",3)
		self.deck["45"] = Card(45,"US","Safer Now",3)
		self.deck["46"] = Card(46,"US","Sistani",3)
		self.deck["47"] = Card(47,"US","The door of Itjihad was closed",3)
		self.deck["48"] = Card(48,"Jihadist","Adam Gadahn",1)
		self.deck["49"] = Card(49,"Jihadist","Al-Ittihad al-Islami",1)
		self.deck["50"] = Card(50,"Jihadist","Ansar al-Islam",1)
		self.deck["51"] = Card(51,"Jihadist","FREs",1)
		self.deck["52"] = Card(52,"Jihadist","IEDs",1)
		self.deck["53"] = Card(53,"Jihadist","Madrassas",1)
		self.deck["54"] = Card(54,"Jihadist","Moqtada al-Sadr",1)
		self.deck["55"] = Card(55,"Jihadist","Uyghur Jihad",1)
		self.deck["56"] = Card(56,"Jihadist","Vieira de Mello Slain",1)
		self.deck["57"] = Card(57,"Jihadist","Abu Sayyaf",2)
		self.deck["58"] = Card(58,"Jihadist","Al-Anbar",2)
		self.deck["59"] = Card(59,"Jihadist","Amerithrax",2)
		self.deck["60"] = Card(60,"Jihadist","Bhutto Shot",2)
		self.deck["61"] = Card(61,"Jihadist","Detainee Release",2)
		self.deck["62"] = Card(62,"Jihadist","Ex-KGB",2)
		self.deck["63"] = Card(63,"Jihadist","Gaza War",2)
		self.deck["64"] = Card(64,"Jihadist","Hariri Killed",2)
		self.deck["65"] = Card(65,"Jihadist","HEU",2)
		self.deck["66"] = Card(66,"Jihadist","Homegrown",2)
		self.deck["67"] = Card(67,"Jihadist","Islamic Jihad Union",2)
		self.deck["68"] = Card(68,"Jihadist","Jemaah Islamiya",2)
		self.deck["69"] = Card(69,"Jihadist","Kazakh Strain",2)
		self.deck["70"] = Card(70,"Jihadist","Lashkar-e-Tayyiba",2)
		self.deck["71"] = Card(71,"Jihadist","Loose Nuke",2)
		self.deck["72"] = Card(72,"Jihadist","Opium",2)
		self.deck["73"] = Card(73,"Jihadist","Pirates",2)
		self.deck["74"] = Card(74,"Jihadist","Schengen Visas",2)
		self.deck["75"] = Card(75,"Jihadist","Schroeder & Chirac",2)
		self.deck["76"] = Card(76,"Jihadist","Abu Ghurayb",3)
		self.deck["77"] = Card(77,"Jihadist","Al Jazeera",3)
		self.deck["78"] = Card(78,"Jihadist","Axis of Evil",3)
		self.deck["79"] = Card(79,"Jihadist","Clean Operatives",3)
		self.deck["80"] = Card(80,"Jihadist","FATA",3)
		self.deck["81"] = Card(81,"Jihadist","Foreign Fighters",3)
		self.deck["82"] = Card(82,"Jihadist","Jihadist Videos",3)
		self.deck["83"] = Card(83,"Jihadist","Kashmir",3)
		self.deck["84"] = Card(84,"Jihadist","Leak",3)
		self.deck["85"] = Card(85,"Jihadist","Leak",3)
		self.deck["86"] = Card(86,"Jihadist","Lebanon War",3)
		self.deck["87"] = Card(87,"Jihadist","Martyrdom Operation",3)
		self.deck["88"] = Card(88,"Jihadist","Martyrdom Operation",3)
		self.deck["89"] = Card(89,"Jihadist","Martyrdom Operation",3)
		self.deck["90"] = Card(90,"Jihadist","Quagmire",3)
		self.deck["91"] = Card(91,"Jihadist","Regional al-Qaeda",3)
		self.deck["92"] = Card(92,"Jihadist","Saddam",3)
		self.deck["93"] = Card(93,"Jihadist","Taliban",3)
		self.deck["94"] = Card(94,"Jihadist","The door of Itjihad was closed",3)
		self.deck["95"] = Card(95,"Jihadist","Wahhabism",3)
		self.deck["96"] = Card(96,"Unassociated","Danish Cartoons",1)
		self.deck["97"] = Card(97,"Unassociated","Fatwa",1)
		self.deck["98"] = Card(98,"Unassociated","Gaza Withdrawal",1)
		self.deck["99"] = Card(99,"Unassociated","HAMAS Elected",1)
		self.deck["100"] = Card(100,"Unassociated","Hizb Ut-Tahrir",1)
		self.deck["101"] = Card(101,"Unassociated","Kosovo",1)
		self.deck["102"] = Card(102,"Unassociated","Former Soviet Union",2)
		self.deck["103"] = Card(103,"Unassociated","Hizballah",2)
		self.deck["104"] = Card(104,"Unassociated","Iran",2)
		self.deck["105"] = Card(105,"Unassociated","Iran",2)
		self.deck["106"] = Card(106,"Unassociated","Jaysh al-Mahdi",2)
		self.deck["107"] = Card(107,"Unassociated","Kurdistan",2)
		self.deck["108"] = Card(108,"Unassociated","Musharraf",2)
		self.deck["109"] = Card(109,"Unassociated","Tora Bora",2)
		self.deck["110"] = Card(110,"Unassociated","Zarqawi",2)
		self.deck["111"] = Card(111,"Unassociated","Zawahiri",2)
		self.deck["112"] = Card(112,"Unassociated","Bin Ladin",3)
		self.deck["113"] = Card(113,"Unassociated","Darfur",3)
		self.deck["114"] = Card(114,"Unassociated","GTMO",3)
		self.deck["115"] = Card(115,"Unassociated","Hambali",3)
		self.deck["116"] = Card(116,"Unassociated","KSM",3)
		self.deck["117"] = Card(117,"Unassociated","Oil Price Spike",3)
		self.deck["118"] = Card(118,"Unassociated","Oil Price Spike",3)
		self.deck["119"] = Card(119,"Unassociated","Saleh",3)
		self.deck["120"] = Card(120,"Unassociated","US Election",3)
	
	def getCountryFromUser(self, prompt, special, helpFunction, helpParameter = None):
		goodCountry = None
		while not goodCountry:
			input = raw_input(prompt)
			if input == "":
				return ""
			elif input == "?":
				helpFunction(helpParameter)
				continue
			elif input == special:
				return special
			possible = []
			for country in self.map:
				if input.lower() == country.lower():
					possible = []
					possible.append(country)
					break
				elif input.lower() in country.lower():
					possible.append(country)
			if len(possible) == 0:
				print "Unrecognized country."
				print ""
			elif len(possible) > 1:
				print "Be more specific", possible
				print ""
			else:
				goodCountry = possible[0]
		return goodCountry
	
	def getNumFromUser(self, prompt, max):
		goodNum = None
		while not goodNum:
			try:
				input = raw_input(prompt)
				input = int(input)
				if input <= max:
					return input
				else:
					print "Not enough troops."
					print ""
			except:
				print "Entry error"
				print ""
		
	def getRollFromUser(self, prompt):
		goodNum = None
		while not goodNum:
			try:
				input = raw_input(prompt)
				if input == "r":
					return random.randint(1,6)
				input = int(input)
				if 1 <= input and input <= 6:
					return input
				else:
					raise
			except:
				print "Entry error"
				print ""
				
	def gwotPenalty(self):
		worldPos = 0
		for country in self.map:
			if self.map[country].type == "Non-Muslim" and self.map[country].name != "United States":
				if self.map[country].posture == "Hard":
					worldPos += 1
				elif self.map[country].posture == "Soft":
					worldPos -= 1
		if worldPos > 0:
			worldPosStr = "Hard"
		elif worldPos < 0:
			worldPosStr = "Soft"
		else:
			worldPosStr = "Even"
		if worldPos > 3:
			worldPos = 3
		elif worldPos < -3:
			worldPos = -3
		if self.map["United States"].posture != worldPosStr:
			return -(abs(worldPos))
		else:
			return 0
				
	def modifiedWoIRoll(self, baseRoll, country):
		modRoll = baseRoll
		#print "DEBUG: base roll:%d" % modRoll
		
		if self.prestige <= 3:
			modRoll -= 1
		elif self.prestige >= 7 and self.prestige <=9:
			modRoll += 1
		elif self.prestige >= 10:
			modRoll += 2
		#print "DEBUG: w/prestige mod:%d" % modRoll
		
		if self.map[country].alignment == "Ally" and self.map[country].governance == 2:
			modRoll -= 1
		#print "DEBUG: w/to good mod:%d" % modRoll
		
		modRoll += self.gwotPenalty()
		#print "DEBUG: w/GWOT penalty:%d" % modRoll
		
		if self.map[country].aid > 0:
			modRoll += 1
		#print "DEBUG: w/aid:%d" % modRoll
		
		for adj in self.map[country].links:
			if adj.alignment == "Ally" and adj.governance == 1:
				modRoll += 1
				break
		#print "DEBUG: w/adj good:%d" % modRoll
		return modRoll
		
	def handleMuslimWoI(self, roll, country):
		if roll <= 3:
			self.outputToHistory("* WoI in %s failed." % country)
		elif roll == 4:
			self.map[country].aid = 1
			self.outputToHistory("* WoI in %s adds Aid." % country)
		else:
			if self.map[country].alignment == "Neutral":
				self.map[country].alignment = "Ally"
				self.outputToHistory("* WoI in %s succeeded - Alignment now Ally." % country)
			elif self.map[country].alignment == "Ally":
				self.map[country].governance -= 1
				if self.map[country].governance <= 1:
					self.map[country].governance = 1
				self.outputToHistory("* WoI in %s succeeded - Governance now %s." % (country, self.map[country].govStr()))
				
	def handleAlert(self, country):
		if self.map[country].plots > 0:
			self.map[country].plots -= 1
			self.outputToHistory("* Alert in %s - %d plot(s) remain." % (country, self.map[country].plots))
			
	def handleReassessment(self):
		if self.map["United States"].posture == "Hard":
			self.map["United States"].posture = "Soft"
		else:
			self.map["United States"].posture = "Hard"
		self.outputToHistory("* Reassessment = US Posture now %s" % self.map["United States"].posture)
		
	def handleRegimeChange(self, where, moveFrom, howMany, govRoll, prestigeRolls):
		if self.map["United States"].posture == "Soft":
			return
		if moveFrom == 'track':
			self.troops -= howMany
		else:	
			self.map[moveFrom].troops -= howMany
		self.map[where].troops += howMany
		sleepers = self.map[where].sleeperCells
		self.map[where].sleeperCells = 0
		self.map[where].activeCells += sleepers
		self.map[where].alignment = "Ally"
		if govRoll <= 4:
			self.map[where].governance = 3
		else:
			self.map[where].governance = 2
		self.map[where].regimeChange = 1
		presMultiplier = 1
		if prestigeRolls[0] <= 4:
			presMultiplier = -1
		self.prestige += (min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
		self.outputToHistory("* Regime Change in %s" % where, False)
		self.outputToHistory(self.map[where].countryStr(), False)
		if moveFrom == "track":
			self.outputToHistory("%d Troops on Troop Track" % self.troops, False)
		else:
			self.outputToHistory("%d Troops in %s" % (self.map[moveFrom].troops, moveFrom), False)
		self.outputToHistory("US Prestige %d" % self.prestige)
				
	def handleWithdraw(self, moveFrom, moveTo, howMany, prestigeRolls):
		if self.map["United States"].posture == "Hard":
			return
		self.map[moveFrom].troops -= howMany
		if moveTo == "track":
			self.troops += howMany
		else:
			self.map[moveTo].troops += howMany
		self.map[moveFrom].aid = 0
		self.map[moveFrom].besieged = 1
		presMultiplier = 1
		if prestigeRolls[0] <= 4:
			presMultiplier = -1
		self.prestige += (min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
		self.outputToHistory("* Withdraw troops from %s" % moveFrom, False)
		self.outputToHistory(self.map[moveFrom].countryStr(), False)
		if moveTo == "track":
			self.outputToHistory("%d Troops on Troop Track" % self.troops, False)
		else:
			self.outputToHistory("%d Troops in %s" % (self.map[moveTo].troops, moveTo), False)
			self.outputToHistory(self.map[moveTo].countryStr(), False)
		self.outputToHistory("US Prestige %d" % self.prestige)
		
	def executeJihad(self, country, rollList):
		successes = 0
		failures = 0
		for roll in rollList:
			if roll <= self.map[country].governance:
				successes += 1
			else:
				failures += 1
		isMajorJihad = country in self.majorJihadPossible(len(rollList))
		if isMajorJihad: # all cells go active
			self.outputToHistory("* Major Jihad attempt in %s" % country) 
			sleepers = self.map[country].sleeperCells
			self.map[country].sleeperCells = 0
			self.map[country].activeCells += sleepers
			if failures == 3 and self.map[country].governance == 3:
				self.outputToHistory("Major Jihad Failure") 
				self.map[country].besieged = 1
				self.outputToHistory("Besieged Regime") 
				if self.map[country].alignment == "Adversary":
					self.map[country].alignment = "Neutral"
				elif self.map[country].alignment == "Neutral":
					self.map[country].alignment = "Ally"
				self.outputToHistory("Alignment %s" % self.map[country].alignment)
		else: # a cell is active for each roll
			self.outputToHistory("* Minor Jihad attempt in %s" % country) 
			for i in range(len(rollList) - self.map[country].activeCells):
				self.map[country].sleeperCells -= 1
				self.map[country].activeCells += 1
		while successes > 0 and self.map[country].governance < 3:
			self.map[country].governance += 1
			successes -= 1
		if isMajorJihad and ((successes >= 2) or ((self.map[country].besieged > 0) and (successes >= 1))) : # Major Jihad
			self.outputToHistory("Islamic Revolution in %s" % country) 
			self.map[country].governance = 4
			self.map[country].alignment = "Adversary"
			self.map[country].regimeChange = 0
			self.map[country].besieged = 0
			self.map[country].aid = 0
			self.funding = min(9, self.funding + self.map[country].resources)
			if self.map[country].troops > 0:
				self.prestige = 1
		for i in range(failures):
			if self.map[country].activeCells > 0:
				self.map[country].activeCells -= 1
			else:
				self.map[country].sleeperCells -= 1		
		self.outputToHistory(self.map[country].countryStr()) 
		
	def handleJihad(self, country, ops):
		cells = self.map[country].sleeperCells + self.map[country].activeCells
		rollList = []
		for i in range(min(cells, ops)):
			rollList.append(random.randint(1,6))
		self.executeJihad(country, rollList)
		
	def majorJihadPossible(self, ops):
		'''Return list of countries where regime change is possible.'''
		possible = []
		plusCellsNeeded = 5
		if self.ideology >= 3:
			plusCellsNeeded = 3
		for country in self.map:
			if self.map[country].type == "Suni" or self.map[country].type == "Shia-Mix":
				if self.map[country].governance != 4:
					if ((self.map[country].sleeperCells + self.map[country].activeCells) - self.map[country].troops) >= plusCellsNeeded:
						need = 2
						need += 3 - self.map[country].governance
						if self.map[country].besieged:
							need -= 1
						if ops >= need:
							possible.append(country)
		return possible
				
	def majorJihadChoice(self, ops):
		'''Return AI choice country.'''
		possible = self.majorJihadPossible(ops)
		if possible == []:
			return False
		else:
			if "Pakistan" in possible:
				return "Pakistan"
			else:
				maxResource = 0
				for country in possible:
					if self.map[country].resources > maxResource:
						maxResource = self.map[country].resources
				newPossible = []
				for country in possible:
					if self.map[country].resources == maxResource:
						newPossible.append(country)
				return random.choice(newPossible)

	def minorJihadPossibleInGoodFair(self):
		return False
		
	def cellsAvailable(self):
		return False
		
	def eventPutsCell(self, cardNum):
		return False
		
	def playableNonUSEvent(self, cardNum):
		# return self.deck[str(cardNum)].type != "US" and  self.deck[str(cardNum)].playable("Jihadist")
		return False

	def playableUSEvent(self, cardNum):
		# self.deck[str(cardNum)].type == "US" and  self.deck[str(cardNum)].playable("US")
		return False
		
	def aiFlowChartTop(self, cardNum):
		print "DEBUG: START"
		print "DEBUG: Playble Non-US event? [1]"
		if self.playableNonUSEvent(cardNum):
			print "DEBUG: YES"
			print "Event Recruits or places cell? [2]"
			if self.eventPutsCell(cardNum):
				print "DEBUG: YES"
				print "Track has cell? [3]"
				if self.cells > 0:
					print "DEBUG: YES"
					self.aiFlowChardPlayEvent(cardNum)
				else:
					print "DEBUG: NO"
					print "DEBUG: [][]self.radicalization() [4]"
			else:
				print "DEBUG: NO"
				self.aiFlowChardPlayEvent(cardNum)
		else:
			print "DEBUG: NO"
			print "DEBUG: Playble US event? [7]"
			if self.playableUSEvent(cardNum):
				print "DEBUG: YES"
				print "DEBUG: Plot Here [5]"
				print "DEBUG: END"
			else:
				print "DEBUG: NO"
				self.aiFlowChartMajorJihad(cardNum)

	def aiFlowChardPlayEvent(self, cardNum):
		print "Play Event [6]"
		self.deck[str(cardNum)].playEvent("Jihadist")
		print "Unassociated Event? [8]"
		if self.deck[str(cardNum)].type == "Unassociated":
			print "DEBUG: YES"
			self.aiFlowChartMajorJihad(cardNum)
		else:
			print "DEBUG: NO"
			print "end [9]"

	def aiFlowChartMajorJihad(self, cardNum):
		print "DEBUG: Major Jihad success possible? [10]"
		country = self.majorJihadChoice(self.deck[str(cardNum)])
		if country:
			print "DEBUG: YES"
			print "DEBUG: Major Jihad [11]"
			self.handleJihad(country)
		else:
			print "DEBUG: NO"
			print "DEBUG: Jihad possible in Good/Fair? [12]"
			country = self.minorJihadPossibleInGoodFair():
			if country:
				print "DEBUG: YES"
				self.handleJihad(country)
			else:
				print "DEBUG: NO"
				print "DEBUG: Cells Available? [14]"
				if self.cellsAvailable():
					print "DEBUG: YES"
					print "DEBUG: [][]self.recruit() [15]"
				else:
					print "DEBUG: NO"
					print "DEBUG: [][]self.travel() [16]"
					
	def listCountriesWithTroops(self, needed = None):
		print ""
		print "Contries with Troops"
		print "--------------------"
		if needed == None:
			needed = 0
		if self.troops > needed:
			print "Troop Track: %d" % self.troops
		for country in self.map:
			if self.map[country].troops > needed:
				print "%s: %d" % (country, self.map[country].troops)
		print ""

	def listMuslimAllies(self, na = None):
		print ""
		print "Muslim Allies"
		print "-------------"
		for country in self.map:
			if self.map[country].alignment == "Ally":
				print "%s: %d troops" % (country, self.map[country].troops)
		print ""

	def listDisruptableCountries(self, na = None):
		print ""
		print "Disruptable Countries"
		print "--------------------"
		for country in self.map:
			if self.map[country].sleeperCells + self.map[country].activeCells > 0 or self.map[country].cadre > 0:
				if self.map[country].troops > 0 or self.map[country].type == "Non-Muslim" or self.map[country].alignment == "Ally":
					postureStr = ""
					troopsStr = ""
					if self.map[country].type == "Non-Muslim":
						postureStr = ", Posture %s" % self.map[country].posture
					else:
						troopsStr = ", Troops: %d" % self.map[country].troops
					print "%s - %d Active Cells, %d Sleeper Cells, %d Cadre%s%s" % (country, self.map[country].activeCells, self.map[country].sleeperCells, self.map[country].cadre, troopsStr, postureStr)
		print ""
		
	def listWoICountries(self, na = None):
		print ""
		print "War of Ideas Eligible Countries"
		print "-------------------------------"
		for country in self.map:
			if self.map[country].alignment == "Neutral" or self.map[country].alignment == "Ally":
				print "%s, %s %s - %d Active Cells, %d Sleeper Cells, %d Cadre, %d troops" % (country, self.map[country].govStr(), self.map[country].alignment, self.map[country].activeCells, self.map[country].sleeperCells, self.map[country].cadre, self.map[country].troops)
		for country in self.map:
			if self.map[country].type == "Non-Muslim" and country != "United States" and self.map[country].posture == "Hard":
				print "%s, Posture %s" % (country, self.map[country].posture)
		for country in self.map:
			if self.map[country].type == "Non-Muslim" and country != "United States" and self.map[country].posture == "Soft":
				print "%s, Posture %s" % (country, self.map[country].posture)
		for country in self.map:
			if self.map[country].type == "Non-Muslim" and country != "United States" and self.map[country].posture == "":
				print "%s, Untested" % country
		
	def listPlotCountries(self, na = None):
		print ""
		print "Contries with Active Plots"
		print "--------------------------"
		for country in self.map:
			if self.map[country].plots > 0:
				self.map[country].printCountry()
		print ""
		
	def listIslamicCountries(self, na = None):
		print ""
		print "Islamic Rule Countries"
		print "----------------------"
		for country in self.map:
			if self.map[country].governance == 4:
				self.map[country].printCountry()
		print ""
		
	def listRegimeChangeCountries(self, na = None):
		print ""
		print "Regime Change Countries"
		print "----------------------"
		for country in self.map:
			if self.map[country].regimeChange > 0:
				self.map[country].printCountry()
		print ""
		
	def outputToHistory(self, output, lineFeed = True):
		print output
		if lineFeed:
			print ""
		self.history.append(output)
		
	def do_status(self, rest):
		goodRes = 0
		islamRes = 0
		goodC = 0
		islamC = 0
		worldPos = 0
		for country in self.map:
			if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni": 
				if self.map[country].governance == 1:
					goodC += 1
					print country
					goodRes += self.map[country].resources
				elif self.map[country].governance == 2:
					goodC += 1
				elif self.map[country].governance == 3:
					islamC += 1
				elif self.map[country].governance == 4:
					islamC += 1
					islamRes += self.map[country].resources
			elif self.map[country].type != "Iran" and self.map[country].name != "United States":
				if self.map[country].posture == "Hard":
					worldPos += 1
				elif self.map[country].posture == "Soft":
					worldPos -= 1
		print ""
		print "GOOD GOVERNANCE"
		num = 0
		for country in self.map:
			if self.map[country].type != "Non-Muslim" and self.map[country].governance == 1:
				num += 1
				self.map[country].printCountry()
		if not num:
			print "none"
		print ""
		print "FAIR GOVERNANCE"
		num = 0
		for country in self.map:
			if self.map[country].type != "Non-Muslim" and self.map[country].governance == 2:
				num += 1
				self.map[country].printCountry()
		if not num:
			print "none"
		print ""
		print "POOR GOVERNANCE"
		num = 0
		for country in self.map:
			if self.map[country].type != "Non-Muslim" and self.map[country].governance == 3:
				num += 1
				self.map[country].printCountry()
		if not num:
			print "none"
		print ""
		print "ISLAMIC RULE"
		num = 0
		for country in self.map:
			if self.map[country].type != "Non-Muslim" and self.map[country].governance == 4:
				num += 1
				self.map[country].printCountry()
		if not num:
			print "none"
		print ""
		print "HARD POSTURE"
		num = 0
		for country in self.map:
			if self.map[country].posture == "Hard":
				num += 1
				self.map[country].printCountry()
		if not num:
			print "none"
		print ""
		print "SOFT POSTURE"
		num = 0
		for country in self.map:
			if self.map[country].posture == "Soft":
				num += 1
				self.map[country].printCountry()
		if not num:
			print "none"
		print ""
		print "PLOTS"
		plotCountries = 0
		for country in self.map:
			if self.map[country].plots > 0:
				plotCountries += 1
				print "%s: %d plot(s)" % (country, self.map[country].plots)
		if plotCountries == 0:
			print "No Plots"
		print ""
		print "VICTORY"
		print "Good Resources   : %d" % goodRes
		print "Islamic Resources: %d" % islamRes
		print "---"
		print "Good/Fair Countries   : %d" % goodC
		print "Poor/Islamic Countries: %d" % islamC
		print ""
		print "GWOT"
		print "US Posture: %s" % self.map["United States"].posture
		if worldPos > 0:
			worldPosStr = "Hard"
		elif worldPos < 0:
			worldPosStr = "Soft"
		else:
			worldPosStr = "Even"
		print "World Posture: %s %d" % (worldPosStr, worldPos)
		print "US Prestige: %d" % self.prestige
		print ""
		print "TROOPS"
		if self.troops >= 10:
			print "Low Intensity: %d troops available" % self.troops
		elif self.troops >= 5:
			print "War: %d troops available" % self.troops
		else:
			print "Overstretch: %d troops available" % self.troops
		print ""
		print "JIHADIST FUNDING"
		print "Funding: %d" % self.funding
		print "Cells Available: %d" % self.cells
		print ""
		print "DATE"
		print "%d (Turn %s)" % (self.startYear + (self.turn - 1), self.turn)
		print ""
		
	def help_status(self):
		print "Display game status."
		print ""
		
	def do_sta(self, rest):
		self.do_status(rest)
		
	def help_sta(self):
		self.help_status()
		
	def do_history(self,rest):
		for str in self.history:
			print str
		print ""

	def help_history(self):
		print "Display Game History."
		print ""
		
	def do_his(self, rest):
		self.do_history(rest)
		
	def help_his(self):
		self.help_history()

	def do_deploy(self, rest):
		moveFrom = None
		available = 0
		while not moveFrom:
			input = self.getCountryFromUser("From what country (track for Troop Track) (? for list)?: ",  "track", self.listCountriesWithTroops)	
			if input == "":
				print ""
				return
			elif input == "track":
				if self.troops <= 0:
					print "There are no troops on the Troop Track."
					print ""
					return
				else:
					print "Deploy from Troop Track - %d available" % self.troops
					print ""
					available = self.troops
					moveFrom = input
			else:
				if self.map[input].troops <= 0:
					print "There are no troops in %s." % input
					print ""
					return
				else:
					print "Deploy from %s = %d availalbe" % (input, self.map[input].troops)
					print ""
					available = self.map[input].troops
					moveFrom = input
		moveTo = None
		while not moveTo:
			input = self.getCountryFromUser("To what country (track for Troop Track)  (? for list)?: ",  "track", self.listMuslimAllies)	
			if input == "":
				print ""
				return
			elif input == "track":
				print "Deploy troops from %s to Troop Track" % moveFrom
				print ""
				moveTo = input
			else:
				print "Deploy troops from %s to %s" % (moveFrom, input)
				print ""
				moveTo = input
		howMany = 0
		while not howMany:
			input = self.getNumFromUser("Deploy how many troops (%d available)? " % available, available)
			if input == "":
				print ""
				return
			else:
				howMany = input
		if moveFrom == "track":
			self.troops -= howMany
			troopsLeft = self.troops
		else:
			if self.map[moveFrom].regimeChange:
				if (self.map[moveFrom].troops - howMany) < (5 + self.map[moveFrom].sleeperCells + self.map[moveFrom].activeCells):
					print "You cannot move that many troops from a Regime Change country."
					print ""
					return
			self.map[moveFrom].troops -= howMany
			troopsLeft = self.map[moveFrom].troops
		if moveTo == "track":
			self.troops += howMany
			troopsNow = self.troops
		else:
			self.map[moveTo].troops += howMany
			troopsNow = self.map[moveTo].troops
		self.outputToHistory("* %d troops deployed from %s (%d) to %s (%d)" % (howMany, moveFrom, troopsLeft, moveTo, troopsNow))
		
	def help_deploy(self):
		print "Move Trops"
		print ""
		
	def do_dep(self, rest):
		self.do_deploy(rest)
		
	def help_dep(self):
		self.help_toops()
		
	def do_disrupt(self, rest):
		where = None
		sleepers = 0
		actives = 0
		while not where:
			input = self.getCountryFromUser("Disrupt what country?  (? for list): ",  "XXX", self.listDisruptableCountries)	
			if input == "":
				print ""
				return
			else:
				if self.map[input].sleeperCells + self.map[input].activeCells <= 0 and self.map[input].cadre <= 0:
					print "There are no cells or cadre in %s." % input
					print ""
					return
				elif self.map[input].troops > 0 or self.map[input].type == "Non-Muslim" or self.map[input].alignment == "Ally":
					print "Disrupt in %s - %d Active Cells, %d Sleeper Cells" % (input, self.map[input].activeCells, self.map[input].sleeperCells)
					print ""
					where = input
					sleepers = self.map[input].sleeperCells
					actives = self.map[input].activeCells
				else:
					print "You can't disrupt there."
					print ""
		numToDisrupt = 1
		if self.map[where].troops > 0 or self.map[where].posture == "Hard":
			numToDisrupt = 2
		if self.map[where].sleeperCells + self.map[where].activeCells <= 0 and self.map[input].cadre > 0:
			self.outputToHistory("* Cadre removed in %s" % where)
			self.map[input].cadre = 0
		elif self.map[where].sleeperCells + self.map[where].activeCells <= numToDisrupt:
			self.outputToHistory("* %d cell(s) disrupted in %s." % (self.map[where].sleeperCells + self.map[where].activeCells, where))
			if self.map[where].sleeperCells > 0:
				self.map[where].activeCells += self.map[where].sleeperCells
				numToDisrupt -= self.map[where].sleeperCells
				self.map[where].sleeperCells = 0
			if numToDisrupt > 0:
				self.map[where].activeCells -= numToDisrupt
				if self.map[where].activeCells < 0:
					self.map[where].activeCells = 0
			if self.map[where].sleeperCells + self.map[where].activeCells <= 0:
				self.outputToHistory("Cadre added in %s." % where)
				self.map[where].cadre = 1
			self.outputToHistory("%s - %d Active Cells, %d Sleeper Cells, %d Cadre" % (where, self.map[where].activeCells, self.map[where].sleeperCells, self.map[where].cadre))
		else:
			if self.map[where].activeCells == 0:
				self.map[where].activeCells += numToDisrupt
				self.map[where].sleeperCells -= numToDisrupt
				self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
			elif self.map[where].sleeperCells == 0:
				self.map[where].activeCells -= numToDisrupt
				self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
				if self.map[where].sleeperCells + self.map[where].activeCells <= 0:
					print "Cadre added."
					self.map[where].cadre = 1
			else:
				if numToDisrupt == 1:
					disStr = None
					while not disStr:
						input = raw_input("You can disrupt one cell. Enter a or s: ")
						input = input.lower()
						if input == "a" or input == "s":
							disStr = input
					if disStr == "a":
						self.map[where].activeCells -= numToDisrupt
						self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
					else:
						self.map[where].sleeperCells -= numToDisrupt
						self.map[where].activeCells += numToDisrupt
						self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
				else:
					disStr = None
					while not disStr:
						if self.map[where].sleeperCells >= 2 and self.map[where].activeCells >= 2:
							input = raw_input("You can disrupt two cells. Enter aa, as, or ss: ")
							input = input.lower()
							if input == "aa" or input == "as" or input == "sa" or input == "ss":
								disStr = input
						elif self.map[where].sleeperCells >= 2:
							input = raw_input("You can disrupt two cells. Enter as, or ss: ")
							input = input.lower()
							if input == "as" or input == "sa" or input == "ss":
								disStr = input
						elif self.map[where].activeCells >= 2:
							input = raw_input("You can disrupt two cells. Enter aa, or as: ")
							input = input.lower()
							if input == "as" or input == "sa" or input == "aa":
								disStr = input
					if input == "aa":
						self.map[where].activeCells -= 2
						self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
					elif input == "as" or input == "sa":
						self.map[where].sleeperCells -= 1
						self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
					else:
						self.map[where].sleeperCells -= 2
						self.map[where].activeCells += 2
						self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
			self.outputToHistory("%s - %d Active Cells, %d Sleeper Cells, %d Cadre" % (where, self.map[where].activeCells, self.map[where].sleeperCells, self.map[where].cadre))

	def help_disrupt(self):
		print "Disrupt Cells or Cadre."
		print ""

	def do_dis(self, rest):
		self.do_disrupt(rest)
				
	def help_dis(self):
		self.help_disrupt()
		
	def do_woi(self, rest):
		where = None
		while not where:
			input = self.getCountryFromUser("War of Ideas in what country?  (? for list): ", "XXX", self.listWoICountries)
			if input == "":
				print ""
				return
			else:
				if self.map[input].type == "Non-Muslim" and input != "United States":
					where = input
				elif self.map[input].alignment == "Ally" or self.map[input].alignment == "Neutral":
					where = input
				else:
					print "Country not elligable for War of Ideas."
					print ""
			if self.map[where].type == "Non-Muslim" and input != "United States": # Non-Muslim
				postureRoll = self.getRollFromUser("Enter Posture Roll or r to have program roll: ")
				if postureRoll <= 4:
					self.map[where].posture = "Hard"
					self.outputToHistory("* War of Ideas in %s - Posture Hard" % where)
					if self.map["United States"].posture == "Hard":
						self.prestige += 1
						if self.prestige > 9:
							self.prestige = 9
						else:
							self.outputToHistory("US Prestige now %d" % self.prestige)
				else:
					self.map[where].posture = "Soft"
					self.outputToHistory("* War of Ideas in %s - Posture Soft" % where)
					if self.map["United States"].posture == "Soft":
						self.prestige += 1
						if self.prestige > 9:
							self.prestige = 9
						else:
							self.outputToHistory("US Prestige now %d" % self.prestige)
			else: # Muslim
				woiRoll = self.getRollFromUser("Enter WoI roll or r to have program roll: ")
				modRoll = self.modifiedWoIRoll(woiRoll, where)
				self.handleMuslimWoI(modRoll, where)
				
	def help_woi(self):
		print "Conduct War of Ideas operation."
		
	def do_alert(self, rest):
		where = None
		while not where:
			input = self.getCountryFromUser("Alert in what country?  (? for list): ", "XXX", self.listPlotCountries)
			if input == "":
				print ""
				return
			else:
				if self.map[input].plots < 1:
					print "Country has not plots."
					print ""
				else:
					where = input
		self.handleAlert(where)
					
	def help_alert(self):
		print "Alert an active Plot."

	def do_alr(self, rest):
		self.do_alert(rest)
				
	def help_alr(self):
		self.help_alert()
		
	def do_reassessment(self, rest):
		self.handleReassessment()
					
	def help_reassessment(self):
		print "Reassessment of US Posture."

	def do_rea(self, rest):
		self.do_reassessment(rest)
				
	def help_rea(self):
		self.help_reassessment()

	def do_regime(self, rest):
		if 	self.map["United States"].posture == "Soft":
			print "No Regime Change with US Posture Soft"
			print ""
			return
		where = None
		while not where:
			input = self.getCountryFromUser("Regime Change in what country?  (? for list): ", "XXX", self.listIslamicCountries)
			if input == "":
				print ""
				return
			else:
				if self.map[input].governance == 4:
					where = input
				else:
					print "Country not Islamic Rule."
					print ""
		moveFrom = None
		available = 0
		while not moveFrom:
			input = self.getCountryFromUser("Deploy 6+ troops from what country (track for Troop Track) (? for list)?: ",  "track", self.listCountriesWithTroops, 6)	
			if input == "":
				print ""
				return
			elif input == "track":
				if self.troops <= 6:
					print "There are not enough troops on the Troop Track."
					print ""
					return
				else:
					print "Deploy from Troop Track - %d available" % self.troops
					print ""
					available = self.troops
					moveFrom = input
			else:
				if self.map[input].troops <= 6:
					print "There are not enough troops in %s." % input
					print ""
					return
				else:
					print "Deploy from %s = %d availalbe" % (input, self.map[input].troops)
					print ""
					available = self.map[input].troops
					moveFrom = input
		howMany = 0
		while not howMany:
			input = self.getNumFromUser("Deploy how many troops (%d available)? " % available, available)
			if input == "":
				print ""
				return
			elif input < 6:
				print "At least 6 troops needed for Regime Change"
			else:
				howMany = input
		govRoll = self.getRollFromUser("Enter Governance roll or r to have program roll: ")
		preFirstRoll = self.getRollFromUser("Enter first die (Raise/Drop) for Prestige roll or r to have program roll: ")
		preSecondRoll = self.getRollFromUser("Enter second die for Prestige roll or r to have program roll: ")
		preThirdRoll = self.getRollFromUser("Enter thrid die for Prestige roll or r to have program roll: ")
		self.handleRegimeChange(where, moveFrom, howMany, govRoll, (preFirstRoll, preSecondRoll, preThirdRoll))
		
	def help_regime(self):
		print "Regime Change in Islamist Rule Country."
				
	def do_reg(self, rest):
		self.do_regime(rest)
				
	def help_reg(self):
		self.help_regime()
		
	def do_withdraw(self, rest):
		if 	self.map["United States"].posture == "Hard":
			print "No Withdrawl with US Posture Hard"
			print ""
			return
		moveFrom = None
		available = 0
		while not moveFrom:
			input = self.getCountryFromUser("Withdrawl in what country?  (? for list): ", "XXX", self.listRegimeChangeCountries)
			if input == "":
				print ""
				return
			else:
				if self.map[input].regimeChange > 0:
					moveFrom = input
					available = self.map[input].troops
				else:
					print "Country not Regime Change."
					print ""
		moveTo = None
		while not moveTo:
			input = self.getCountryFromUser("To what country (track for Troop Track)  (? for list)?: ",  "track", self.listMuslimAllies)	
			if input == "":
				print ""
				return
			elif input == "track":
				print "Withdraw troops from %s to Troop Track" % moveFrom
				print ""
				moveTo = input
			else:
				print "Withdraw troops from %s to %s" % (moveFrom, input)
				print ""
				moveTo = input
		howMany = 0
		while not howMany:
			input = self.getNumFromUser("Withdraw how many troops (%d available)? " % available, available)
			if input == "":
				print ""
				return
			else:
				howMany = input
		preFirstRoll = self.getRollFromUser("Enter first die (Raise/Drop) for Prestige roll or r to have program roll: ")
		preSecondRoll = self.getRollFromUser("Enter second die for Prestige roll or r to have program roll: ")
		preThirdRoll = self.getRollFromUser("Enter thrid die for Prestige roll or r to have program roll: ")
		self.handleWithdraw(moveFrom, moveTo, howMany, (preFirstRoll, preSecondRoll, preThirdRoll))

	def help_withdraw(self):
		print "Withdraw Troops from Regime Change Country."
				
	def do_wit(self, rest):
		self.do_withdraw(rest)
				
	def help_wit(self):
		self.help_withdraw()
		
	def do_j(self, rest):
		if self.phase != "Jihadist Action Phase":
			print "It is not the Jihadist Action Phase"
			return
		cardNum = None
		try:
			input = int(rest)
			if input < 1 or input > 120:
				print "Enter j then the card number e.g. j 24"
				print ""
				return
			else:
				cardNum = input
		except:
			print "Enter j then the card number e.g. j 24"
			print ""
			return
		self.aiFlowChartTop(cardNum)
		
	def help_j(self):
		print "Enter the number of the Jihadist card when it is their card play."
			
def main():
	print "Labyrinth: The War on Terror AI Player"
	print ""
	scenario = 0
	ideology = 0
	while scenario == 0:
		try:
			print "Choose Scenario"
			print "(1) Let's Roll"
			print "(2) You Can Call Me Al"
			print "(3) Anaconda"
			print "(4) Mission Accomplished"
			input = raw_input("Enter choice:")
			input = int(input)
			if input >= 1 and input <= 4:
				scenario = input
				print ""
			else:
				raise
		except:
			print "Entry error"
			print ""

	while ideology == 0:
		try:
			print "Choose Jihadist Ideology"
			print "(1) Normal"
			print "(2) Attractive"
			print "(3) Potent"
			print "(4) Infectious"
			print "(5) Virulent"
			input = raw_input("Enter choice:")
			input = int(input)
			if input >= 1 and input <= 5:
				ideology = input
				print ""
			else:
				raise
		except:
			print "Entry error"
			print ""

	app = Labyrinth(scenario, ideology)
	app.cmdloop()

if __name__ == "__main__":
	main()