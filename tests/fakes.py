from lwotai import DieRoller, Randomizer


class FakeDieRoller(DieRoller):
    """Allows die rolls to be faked during unit tests"""

    def __init__(self, *results):
        DieRoller.__init__(self)
        self.__results = list(results)

    def roll(self, times):
        return self.__results


class FakeRandomizer(Randomizer):
    """Allows randomness to be removed during unit tests"""

    choices = []

    def set_choices(self, choices):
        """Sets the choices to be returned by the 'pick' method"""
        self.choices = choices

    def pick(self, quantity, candidates):
        """Returns the choices set up by the 'set_choices' method"""
        return self.choices

    def pick_one(self, candidates):
        """Returns the first choice set up by the 'set_choices' method"""
        return self.choices[0]
