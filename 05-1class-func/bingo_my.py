import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)  # <1>
        random.shuffle(self._items)  # <2>

    def pick(self):
        #first
        """some comment
        and do something"""
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # <4>

    def __call__(self):  # <5>
        return self.pick()

# END BINGO
bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())

callable(bingo)
random.shuffle.__doc__
print(bingo.pick.__doc__)
