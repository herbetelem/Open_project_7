""" Module Proposal """


class Proposal:
    """Object who stock the data about each action"""

    def __init__(self, budget):

        self.budget = budget
        self.list_action = []
        self.total_gain = 0