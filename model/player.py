class Player(Person):
	def __init__(self, name = ""):
		self._name = name
		# self.id =
		self._angklungs = list()
		self.role = "Angklung Player"

	@property
	def angklungs(self):
		return self.angklungs

	@angklungs.setter
	def angklungs(self, angklungs):
		self._angklungs = angklungs

	def addAngklung(self, angklung):
		self._angklungs.append(angklung)

	def removeAngklung(self, angklung):
		self._angklungs.remove(angklung)



