import random

'''
See PDF of problem definition first.

For convenience, decks are represented by ranges so that the absolute
difference can be taken by subtracting each shuffled element from
its index

Ex: D = [ 0, 1, 2 ], D' = [ 2, 1, 0 ], <D, D'> = |2-0| + |1-1| + |0-2| = 4
'''

# D is a shuffled deck. The original deck is known, so only pass shuffled deck
def distance(D_hat):
    return reduce(
        lambda acc, (c, i): acc + abs(c - i),
        enumerate(D_hat),
        0
    )

# This is an alternative metric for measuring distance to original neighbors
# Also called the "scattered to the wind" metric
def n_distance(D_hat):
    def d_from_neighbors(c):
        if c != len(D_hat) - 1 and c != 0:
            return abs(c - D_hat.index(c + 1)) + abs(c - D_hat.index(c - 1))
        elif c == 0:
            return abs(c - D_hat.index(1))
        else:
            return abs(c - D_hat.index(c - 1))

    return reduce(
        lambda acc, (c, i): acc + d_from_neighbors(c),
        enumerate(D_hat),
        0
    )

class Shuffler:
    def __init__(self, n = 60, metric = distance):
        self.n = n
        self.metric = distance

    def deck(self):
        return list(range(self.n))

    def test_shuffle(self, psi = lambda D: D):
        return self.metric(psi(self.deck()))

    def avg_shuffle(self, psi, times = 5000):
        samples = map(
            lambda _: self.test_shuffle(psi),
            range(times)
        )

        return sum(samples) / len(samples)

def shift(arr, k):
    return arr[k:] + arr[:k]

def random_shuffle(arr):
    random.shuffle(arr)

    return arr

def invert(arr):
    return arr[::-1]

def double_invert(arr):
    first = invert(arr)

    pivot = len(first)//2
    yin = first[:pivot]
    yang = first[pivot:]

    return invert(yin) + invert(yang)

def recursive_invert(arr):
    first = invert(arr)

    if len(arr) <= 2:
        return first
    else:
        pivot = len(first)//2
        yin = first[:pivot]
        yang = first[pivot:]

        return recursive_invert(yin) + recursive_invert(yang)

def pile_shuffle(arr):
    piles = [[],[],[],[],[],[],[],[]]
    k = 0

    while k < len(arr):
        piles[k % 8].append(arr[k])
        k += 1

    return sum(piles, [])

# Sattolo's algorithm (from https://danluu.com/sattolo/) (about the same as random)
def sattolo(a):
    n = len(a)
    for i in range(n - 1):  # i from 0 to n-2, inclusive.
        j = random.randrange(i, n)  # j from i to n-1, inclusive.
        a[i], a[j] = a[j], a[i]  # swap a[i] and a[j].

    return a

def print_results(shuffler):
    shift_distances = map(lambda k: shuffler.test_shuffle(lambda arr: shift(arr, k)), range(61))
    print "Distance when shifting the deck 60 times:"
    print shift_distances
    print "Average of shifts:"
    print sum(shift_distances) / len(shift_distances)
    print "Max of shifts:"
    print max(shift_distances)
    print "Average of random shuffles with 5000 samples:"
    print shuffler.avg_shuffle(random_shuffle)
    print "Inverting the deck:"
    print shuffler.test_shuffle(invert)
    print "Inverting the deck, then inverting two halves:"
    print shuffler.test_shuffle(double_invert)
    print "Inverting the deck, then recursively inverting halves:"
    print shuffler.test_shuffle(recursive_invert)
    print "Pile shuffling with eight groups:"
    print shuffler.test_shuffle(pile_shuffle)
    print "Sattolo shuffle:"
    print shuffler.test_shuffle(sattolo)

if __name__ == '__main__':
    n_cards = 60

    print "Now using distance from original index metric"
    print_results(Shuffler(n_cards, distance))
    print

    print "Now using distance from neighbors metric"
    print_results(Shuffler(n_cards, n_distance))
