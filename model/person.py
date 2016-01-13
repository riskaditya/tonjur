__author__ = 'riskaditya'

class Person(object):
    def __init__(self, name = ""):
        self._name = name
		# self.id =

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	def setRole(self, role):
		self.role = role

