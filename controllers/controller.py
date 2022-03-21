import pdb
from re import A
import pandas as pd
from itertools import chain, combinations, combinations_with_replacement
from threading import Thread
import time


from models.action import ActionObj as m_action
from models.proposal import Proposal as m_proposal

from controllers.proposal import Proposal as c_proposal


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

    def set_action_object(self):
        for data in self.file_excel:
            self.list_action.append(
                m_action(data[0], data[1], data[2], round(data[1] * (data[2] + 1), 2)))

    def generate_combinason(self):
        list_combi = self.powerset()
        for combi_list in list_combi:
            self.asynch_combi(combi_list)

    def powerset(self):
        s = list(self.list_action)
        tmp_list = chain.from_iterable(combinations(s, r)
                                       for r in range(len(s)+1))
        return [combi_list for combi_list in tmp_list]

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
