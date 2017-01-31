#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from random import shuffle, choice
from itertools import izip_longest

class Randomizer(object):

    """Randomizer creates groups of lists."""

    def __init__(self, users_list, selection=1):
        """Initialize Randomizer.

        :selection: Number of desired users per group.
        :users_list: List of all users ids.
        """
        self.users_list = users_list
        self.selection = selection

    def random_user(self):
        """Get single random user

        :returns: A single random user (id).
        """
        return choice(self.users_list)

    def generate_groups(self, selection):
        """Generate groups with random users.

        :selection: Number of desired users per group.
        :returns: List of selected user tuples with selection length.
        """
        self.selection = selection
        shuffle(self.users_list)
        return list(izip_longest(*(iter(self.users_list),) * self.selection))
