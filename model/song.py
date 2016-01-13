__author__ = 'riskaditya'

class Song(object):
    def __init__(self, title, composer, arranger = ""):
        self._title = title
        self._composer = composer
        self._arranger = arranger
        self._partitur = None
        self.players = list()
        self.angklungs = list()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def composer(self):
        return self._composer

    @composer.setter
    def composer(self, name):
        self._composer = name

    @property
    def arranger(self):
        return self._arranger

    @arranger.setter
    def arranger(self, name):
        self._arranger = name

    def getPlayers(self):
        if (not self.players):
            raise ("Player doesn't exists.")
        return self.player

    def getPlayerByName(self, name):
        return filter(lambda p: p.name.lower()==name.lower(), self.players)

    def getPlayersByAngklung(self, angklung):
        return filter(lambda p : True if angklung in p.angklungs() else False, self.players)

    def getPlayersByRole(self, role):
        return filter(lambda p: p.role == role, self.players)

    def convertToAngklung(self):
        pass

    def listOfAngklungs(self):
        return self.angklungs

    def listOfPlayers(self):
        return self.players

    @property
    def partitur(self):
        if (not self._partitur):
            raise ('No partitur.')
        return  self._partitur
