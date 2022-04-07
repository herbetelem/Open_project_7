from threading import Thread
import pandas as pd
from itertools import chain, combinations, islice
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


class CombiModel():
    """Object who stock the data about each combinaison of action"""

    def __init__(self, combi_list):
        """ This object will stock all the data for an action
        Args:
            combi_list (list object): list of action object
        """

        self.list_action = combi_list
        self.cost = sum(action.cost for action in combi_list)
        self.profit = sum(action.profit for action in combi_list)


class ControllerRunProgram:
    """Object controller for the all program
    """

    def __init__(self, budget=500):
        self.file_excel = pd.read_excel('annexe/action.xlsx')
        self.file_excel = pd.read_excel('annexe/dataset2_Python+P7.xlsx')
        self.file_excel = self.file_excel.to_numpy()

        self.list_action = []
        self.budget = budget

        self.proposal = {
            "total_gain": 0,
            "budget": 0,
            "list_action": []
        }
        self.check = True
        self.launch_algo()

    def launch_algo(self):
        # start = time.time()
        self.set_action_object()
        self.generate_combinason()
        # end = time.time()
        # print("combi", end - start)
        print("max: ", self.proposal["total_gain"])

    def set_action_object(self):
        [self.list_action.append(ActionModel(data[0], data[1], data[2], round(
            data[1] * (data[2] + 1), 2))) for data in self.file_excel]

    def generate_combinason(self):
        [self.check_combi(item) for item in self.powerset()]

    def powerset(self):
        s = list(self.list_action)
        return [combi_list for combi_list in chain.from_iterable(
            combinations(s, r) for r in range(len(s)+1))]

    def check_combi(self, combi_list):
        tmp_budget = sum(action.cost for action in combi_list)
        if tmp_budget <= self.budget:
            tmp_profit = sum(action.profit for action in combi_list)
            if self.proposal["total_gain"] < tmp_profit:
                self.proposal = {
                    "total_gain": tmp_profit,
                    "budget": tmp_budget,
                    "list_action": combi_list
                }

    def thread_combi(self):
        self.list_full = self.powerset()
        length_to_split = [len(self.list_full)//2]*2
        lst = iter(self.list_full)
        self.double_list = [list(islice(lst, elem))
                            for elem in length_to_split]

        th1 = Thread(target=self.threading_to_do)
        th2 = Thread(target=self.threading_to_do)

        th1.start()
        th2.start()

        th1.join()
        th2.join()

    def threading_to_do(self):
        if self.check:
            self.check = False
            list_combi = self.double_list[0]
        else:
            list_combi = self.double_list[1]

        list_combi = [self.asynch_combi(item) for item in list_combi]


if __name__ == '__main__':
    ControllerRunProgram()
