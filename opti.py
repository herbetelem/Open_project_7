import pdb
import pandas as pd
import time


class ActionModel():

    def __init__(self, name, cost, percent_value, moy_percent):
        self.name = name
        self.cost = cost

        if moy_percent > 1:
            percent_value = round(percent_value * 0.01, 4)

        self.percent_value = percent_value
        self.money_benef = cost * percent_value
        self.profit = cost + self.money_benef


class ControllerRunProgram:

    def __init__(self, budget=500):
        # self.file_excel = pd.read_excel('annexe/action.xlsx')
        # self.file_excel = pd.read_excel('annexe/dataset1_Python+P7.xlsx')
        self.file_excel = pd.read_excel('annexe/dataset2_Python+P7.xlsx')

        self.file_excel = self.file_excel.to_numpy()
        self.calc_moy()

        self.list_action = []
        self.budget = budget

        self.proposal = {
            "total_gain": 0,
            "budget": 0,
            "money_benef": 0,
            "list_action": []
        }
        self.launch_algo()

    def launch_algo(self):
        # start = time.time()
        self.set_action_object()
        self.generate_combinason()
        # end = time.time()
        self.proposal["total_gain"] = round(self.proposal["total_gain"], 2)
        # print("combi", end - start)
        print("max: ", self.proposal["money_benef"])
        print("buget: ", self.proposal["budget"])

    def calc_moy(self):
        self.moy_percent = sum([data[2] for data in self.file_excel]) / len(self.file_excel)

    def set_action_object(self):
        self.list_action = [ActionModel(data[0], data[1], data[2], self.moy_percent) for data in self.file_excel]
        self.list_action.sort(key=lambda x: x.money_benef, reverse=True)

    def generate_combinason(self):
        [self.create_combi(action) for action in self.list_action]

    def create_combi(self, action):
        if self.budget >= action.cost and action.cost > 0 and action.cost < action.profit:
            if action.percent_value >= (int(max([data[2] for data in self.file_excel])) * 0.01):
                self.proposal["total_gain"] += action.profit
                self.proposal["budget"] += action.cost
                self.proposal["money_benef"] += action.money_benef
                self.proposal["list_action"].append(action)
                self.budget -= action.cost
                print(action.name)


if __name__ == '__main__':
    ControllerRunProgram()
