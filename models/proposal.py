""" Module Proposal """


class Proposal:
    """Object who stock the data about each action"""

    def __init__(self, budget=0, total_gain=0):

        self.budget = budget
        self.list_action = []
        self.total_gain = total_gain