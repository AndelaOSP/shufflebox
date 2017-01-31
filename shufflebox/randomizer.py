#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from random import shuffle, choice
from itertools import izip_longest


class Randomizer(object):
    """This class creates groups using a random shuffle and
    picks an item from a list of entities at random."""

    def __init__(self, items):
        """Initialize Randomizer.

        :selection: Number of desired users per group.
        :items: List of items to be manipulated.
        """
        self.items = items

    def get_single(self):
        """Get a single random entity from a list of items

        :returns: A single item chosen at random.
        """
        return choice(self.items)

    def create_groups(self, group_size):
        """Generate groups with random users.

        :size: Number of desired items per group.
        :returns: List of selected item tuples with selection length.
        """
        self.group_size = group_size
        shuffle(self.items)

        return list(izip_longest(*(iter(self.items),) * self.group_size))
