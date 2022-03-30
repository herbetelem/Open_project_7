import pdb
import pandas as pd
import time


class ActionModel():

    def __init__(self, name, cost, price, benef):
        self.name = name
        self.cost = cost
        self.price = price
        self.benef = benef
        self.profit = cost + benef


class ControllerRunProgram:

    def __init__(self, budget=500):
        # self.file_excel = pd.read_excel('annexe/action.xlsx')
        # self.file_excel = pd.read_excel('annexe/dataset1_Python+P7.xlsx')
        self.file_excel = pd.read_excel('annexe/dataset2_Python+P7.xlsx')
        self.file_excel = self.file_excel.to_numpy()

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
        start = time.time()
        self.set_action_object()
        self.generate_combinason()
        end = time.time()
        self.proposal["total_gain"] = round(self.proposal["total_gain"], 2)
        print("combi", end - start)
        print("max: ", self.proposal["total_gain"])
        import pdb; pdb.set_trace()

    def set_action_object(self):
        self.list_action = [ActionModel(data[0], data[1], data[2], round(
            data[1] * data[2], 2)) for data in self.file_excel]
        self.list_action.sort(key=lambda x: x.benef, reverse=True)

    def generate_combinason(self):
        [self.create_combi(action) for action in self.list_action]

    def create_combi(self, action):
        if self.budget >= action.cost and action.cost > 0:
            self.proposal["total_gain"] += action.profit
            self.proposal["budget"] += action.cost
            self.proposal["benef"] += action.benef
            self.proposal["list_action"].append(action)
            self.budget -= action.cost


if __name__ == '__main__':
    ControllerRunProgram()
