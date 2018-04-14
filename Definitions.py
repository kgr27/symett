class Structure:
	
	class CommandCenter:
		def __init__(self, mineral, gas, time):
			self.mineral = 400
			self.gas = 0
			self.time = 71			
	class SupplyDepot:
		def __init__(self, mineral, gas, time):
			self.mineral = 100
			self.gas = 0
			self.time = 21
	class Refinery:
		def __init__(self, mineral, gas, time):
			self.mineral = 75
			self.gas = 0
			self.time = 21
	class Barracks:
		def __init__(self, mineral, gas, time):
			self.mineral = 150
			self.gas = 0
			self.time = 46
	class GhostacAcademy:
		def __init__(self, mineral, gas, time):
			self.mineral = 150
			self.gas = 50
			self.time = 29
	class Factory:
		def __init__(self, mineral, gas, time):
			self.mineral = 150
			self.gas = 100
			self.time = 43
	class Starport:	
		def __init__(self, mineral, gas, time):
			self.mineral = 150
			self.gas = 100
			self.time = 36
	class EngineeringBay:
		def __init__(self, mineral, gas, time):
			self.mineral = 125
			self.gas = 0
			self.time = 25
	class Armory:
		def __init__(self, mineral, gas, time):
			self.mineral = 150
			self.gas = 100
			self.time = 46
	class FusionCore:
		def __init__(self, mineral, gas, time):
			self.mineral = 150 
			self.gas = 150
			self.time = 46
	class Reactor:
		def __init__(self, mineral, gas, time):
			self.mineral = 50
			self.gas = 50
			self.time = 36
	class TechLab:
		def __init__(self, mineral, gas, time):
			self.mineral = 50
		self.gas = 25
		self.time = 18
	class OrbitalCommand:
		def __init__(self, mineral, gas, time):
			self.mineral = 150
			self.gas = 0
			self.time = 25
			self.energy = 0
	class PlanetaryFortress:
		def __init__(self, mineral, gas, time):
			self.mineral = 150
			self.gas = 150
			self.time = 26
	class MissileTurret:
		def __init__(self, mineral, gas, time):
			self.mineral = 100
			self.gas = 0
			self.time = 18
	class SensorTower:
		def __init__(self, mineral, gas, time):
			self.mineral = 125
			self.gas = 100
			self.time = 18
	class Bunker:
		def __init__(self, mineral, gas, time):
			self.mineral = 100
			self.gas = 0
			self.time =29

class Unit:
	class Scv:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 50
			self.gas = 0
			self.time = 12
			self.supply = 1	
	class Mule:
		def __init__(self, mineral, gas, time, supply, energy):
			self.mineral = 0
			self.gas = 0
			self.time = 0
			self.supply = 0
			self.energy = 25 
	class Marine:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 50
			self.gas = 0
			self.time = 18
			self.supply = 1
	class Reaper:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 50
			self.gas = 50
			self.time = 32
			self.supply = 1
	class Marauder:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 100
			self.gas = 25
			self.time = 21
			self.supply = 2
	class Ghost:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 150
			self.gas = 125
			self.time = 29
			self.supply = 2
	class Hellion:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 100
			self.gas = 0
			self.time = 21
			self.supply = 2
	class WidowMine:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 75
			self.gas = 25
			self.time = 21
			self.supply = 2
	class Cyclone:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 150
			self.gas = 100
			self.time = 32
			self.supply = 3
	class SeigeTank:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 150
			self.gas = 125
			self.time = 32
			self.supply = 3
	class Thor:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 300
			self.gas = 200
			self.time = 43
			self.supply = 6
	class Viking:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 150
			self.gas = 75
			self.time = 30
			self.supply = 2
	class Medivac:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 100
			self.gas = 100
			self.time = 30
			self.supply = 2
	class Liberator:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 150
			self.gas = 150
			self.time = 43
			self.supply = 3
	class Raven:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 100
			self.gas = 200
			self.time = 43
			self.supply = 2
	class Banshee:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 150
			self.gas = 100
			self.time = 43
			self.supply = 3
	class Battlecruiser:
		def __init__(self, mineral, gas, time, supply):
			self.mineral = 400
			self.gas = 300
			self.time = 64
			self.supply = 6