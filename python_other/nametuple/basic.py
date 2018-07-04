import collections
from collections import deque
from collections import defaultdict
import itertools


Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    """
    纸牌
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')

print(beer_card)

def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        #yield s / n
        
            

moving_average_test = [40, 30, 50, 46, 39, 44]
#moving_average(moving_average_test)

def constant_factory(value):
    return lambda: value

def constant_factory_test():
    d = defaultdict(constant_factory('<missing>'))
    d.update(name='John', action='ran')
    print('%(name)s %(action)s to %(object)s' % d)

constant_factory_test()


import bisect
import sys
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |' 
        print(ROW_FMT.format(needle, position, offset))

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]
class StrKeyDict0(dict): 
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)] 
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
             return  "1" 
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
    testDic = StrKeyDict0()
    testDic = {"1",1}
    print(testDic(1))