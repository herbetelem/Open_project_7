import pdb
import pandas as pd
import time


class ActionModel():

    def __init__(self, name, cost, price, moy_percent):
        self.name = name
        self.cost = cost

        if moy_percent > 1:
            price = round(price * 0.01, 4)

        self.price = price
        self.benef = cost * price
        self.profit = cost + self.benef


    # demo
    # ('SHARE-TEST', 200, 10, 23):
        # self.name = "SHARE-TEST"
        # self.cost = 200
        # price 0.1
        # self.price = 0.1
        # self.benef = 20
        # self.profit = 220

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
            "benef": 0,
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
        print("max: ", self.proposal["benef"])
        print("buget: ", self.proposal["budget"])

    def calc_moy(self):
        self.moy_percent = sum([data[2] for data in self.file_excel]) / len(self.file_excel)

    def set_action_object(self):
        self.list_action = [ActionModel(data[0], data[1], data[2], self.moy_percent) for data in self.file_excel]
        self.list_action.sort(key=lambda x: x.benef, reverse=True)

    def generate_combinason(self):
        [self.create_combi(action) for action in self.list_action]

    def create_combi(self, action):
        if self.budget >= action.cost and action.cost > 0 and action.benef > 0:
            if action.price >= (int(max([data[2] for data in self.file_excel])) * 0.01):
                self.proposal["total_gain"] += action.profit
                self.proposal["budget"] += action.cost
                self.proposal["benef"] += action.benef
                self.proposal["list_action"].append(action)
                self.budget -= action.cost
                print(action.name)
                print(action.cost)


if __name__ == '__main__':
    ControllerRunProgram()
