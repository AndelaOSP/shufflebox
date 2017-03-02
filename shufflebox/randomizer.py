#!/usr/bin/env python
from random import shuffle, choice
from itertools import zip_longest

class Randomizer(object):
    """Provides functions to:
        1. Create groups of specified length from a shuffled set of items.
        2. Randomly pick a random item from a set of items."""

    def __init__(self, items):
        """Initialize Randomizer.

        :items: List of items to be manipulated.
        """
        self.items = items

    def get_random(self):
        """Get a single random item from a list of items

        :returns: A single random item.
        """
        return choice(self.items)

    def create_groups(self, n):
        """Generate tuples containing random items of n size.

        :n: Number of desired items in each tuple.
        :returns: List of groups as tuples.
        """
        self.n = n
        shuffle(self.items)
        groups = list(zip_longest(*(iter(self.items),) * self.n))

        return [list(x) for x in groups]
