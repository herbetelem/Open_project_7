import pandas as pd
from itertools import chain, combinations
import time


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


def powerset(list_action):
    s = list(list_action)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


start = time.time()
file_excel = pd.read_excel('../annexe/action.xlsx')
file_excel = file_excel.to_numpy()
budget = 500
# set up all my action

list_action = []
for data in file_excel:
    profit = round(data[1] * (data[2] + 1), 2)
    list_action.append(ActionObj(data[0], data[1], data[2], profit))


start_2 = time.time()
# proposal = Proposal()
proposal = {
    "total_gain": 0,
    "budget": 0,
    "list_action": []
}

list_combi = [combi_list for combi_list in powerset(list_action)]

for combi_list in list_combi:
    tmp_budget = sum(action.cost for action in combi_list)
    if tmp_budget <= budget:
        tmp_profit = round(sum(action.profit for action in combi_list), 2)
        if tmp_profit > budget:
            if proposal["total_gain"] < tmp_profit:
                proposal = {
                    "total_gain": tmp_profit,
                    "budget": tmp_budget,
                    "list_action": combi_list
                }


end_2 = time.time()
print("generer les combi", end_2 - start_2)
end = time.time()
print("combi", end - start)


# (1, 2, 3)
# [(),
# (1),
# (2),
# (3),
# (1, 2),
# (1, 3),
# (2, 1),
# (2, 3),
# (3, 1),
# (3, 2),
# (1, 2, 3),]
