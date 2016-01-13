__author__ = 'riskaditya'

class Angklung(object):
    def __init__(self):
        self._mark = None
        self._string = ""
        self.compatiblePairs = set()
        self.overlapWiths = set()


    def convertToNote(self, key):
        pass

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self.mark = value
        ##TODO : set string

    def asString(self):
        return self._string





