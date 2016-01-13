__author__ = 'riskaditya'

class Performance(object):
    def __init__(self):
        self._song = list()
        self._player = list()
        self._angklungs = list()

    def addSong(self, song):
        self._song.append(song)

    def deleteSongByTitle(self, title):
        self._song = filter(lambda s : s.title().lower()!= title.lower(), self._song)

    def addPlayer(self, player):
        self._player.append(player)

    def deletePlayerByName(self, name):
        self._player = filter(lambda p : p.name().lower()!=name.lower(), self._player)

    def distributeAngklung(self):
        pass

