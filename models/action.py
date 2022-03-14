""" Module Action """


class ActionObj:
    """Object who stock the data about each action"""

    def __init__(self, name, cost, price, profit):
        """ This object will stock all the data for an action

        Args:
            name (str): the name of the action
            cost (int): the cost of the action
            price (int): the value in the market of this action
            profit (int): the profit after 2 year
        """

        self.name = name
        self.cost = cost
        self.price = price
        self.profit = profit
