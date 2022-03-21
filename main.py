import pandas as pd
from itertools import chain, combinations
import time


class ActionModel():
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


class ControllerRunProgram:
    """Object controller for the all program
    """

    def __init__(self, budget=500):
        self.file_excel = pd.read_excel('annexe/action.xlsx')
        self.file_excel = self.file_excel.to_numpy()

        self.list_action = []
        self.budget = budget

        self.proposal = {
            "total_gain": 0,
            "budget": 0,
            "list_action": []
        }
        self.launch_algo()

    def launch_algo(self):
        start = time.time()
        self.set_action_object()
        start2 = time.time()
        self.generate_combinason()
        end2 = time.time()
        print("generate combi", end2 - start2)
        end = time.time()
        print("combi", end - start)
        print("max: ", self.proposal["total_gain"])

    def set_action_object(self):
        list_action = [self.list_action.append(ActionModel(data[0], data[1], data[2], round(
            data[1] * (data[2] + 1), 2))) for data in self.file_excel]

    def generate_combinason(self):
        list_combi = [self.asynch_combi(item) for item in self.powerset()]
        # self.list_combi = self.powerset()
        # self.test()

    def powerset(self):
        s = list(self.list_action)
        return [combi_list for combi_list in chain.from_iterable(combinations(s, r) for r in range(len(s)+1))]

    def asynch_combi(self, combi_list):
        tmp_budget = sum(action.cost for action in combi_list)
        if tmp_budget <= self.budget:
            tmp_profit = sum(action.profit for action in combi_list)
            if tmp_profit > self.budget:
                if self.proposal["total_gain"] < tmp_profit:
                    self.proposal = {
                        "total_gain": tmp_profit,
                        "budget": tmp_budget,
                        "list_action": combi_list
                    }

    def test(self):
        import pdb
        pdb.set_trace()
        self.list_combi.sort(key=lambda x: sum(
            x.list_action.cost), reverse=True)
        import pdb
        pdb.set_trace()


if __name__ == '__main__':
    ControllerRunProgram()











######  Shema de liste de mes objet  #######
# list = [
#     {
#         "name": "combi_1",
#         "list_action": [
#             {
#                 "nom": "action_1",
#                 "cost": 34,
#                 "total_gain": 40
#             },
#             {
#                 "nom": "action_2",
#                 "cost": 34,
#                 "total_gain": 40
#             },
#         ]
#     },
#     {
#         "name": "combi_2",
#         "list_action": [
#             {
#                 "nom": "action_2",
#                 "cost": 34,
#                 "total_gain": 40
#             },
#             {
#                 "nom": "action_3",
#                 "cost": 34,
#                 "total_gain": 40
#             },
#         ]
#     },
#     {
#         "name": "combi_3",
#         "list_action": [
#             {
#                 "nom": "action_1",
#                 "cost": 34,
#                 "total_gain": 40
#             },
#             {
#                 "nom": "action_3",
#                 "cost": 34,
#                 "total_gain": 40
#             },
#         ]
#     },
# ]


##### Shema itertools #####
# (1, 2, 3)
# ()

# (1)
# (2)
# (3)

# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)

# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 2, 1)
# (3, 1, 2)