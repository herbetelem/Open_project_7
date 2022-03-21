import pandas as pd
from itertools import chain, combinations


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

class Proposal:
    """Object who stock the data about each action"""

    def __init__(self, budget=0, total_gain=0):

        self.budget = budget
        self.list_action = []
        self.total_gain = total_gain

def powerset(list_action):
    s = list(list_action)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

file_excel = pd.read_excel('../annexe/action.xlsx')
file_excel = file_excel.to_numpy()
budget = 500

# set up all my action

list_action = []
for data in file_excel:
    profit = round(data[1] * (data[2] + 1), 2)
    list_action.append(ActionObj(data[0], data[1], data[2], profit))

list_proposal = []
list_combi = powerset(list_action)
for combi_list in list_combi:
    tmp_proposal = Proposal(budget)
    tmp_profit = 0
    for action in combi_list:
        if tmp_proposal.budget > 0:
            tmp_proposal.list_action.append(action)
            tmp_proposal.budget -= action.cost
            tmp_profit += action.profit
    tmp_proposal.total_gain = tmp_profit
    list_proposal.append(tmp_proposal)
list_proposal.sort(key=lambda x: x.total_gain, reverse=True)
result = list_proposal[0]