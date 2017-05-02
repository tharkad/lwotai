from lwotai import DieRoller


class FakeDieRoller(DieRoller):
    """Allows die rolls to be faked during unit tests"""

    def __init__(self, *results):
        DieRoller.__init__(self)
        self.__results = list(results)

    def roll(self, times):
        return self.__results