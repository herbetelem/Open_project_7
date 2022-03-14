import pdb
import pandas as pd
from itertools import chain, combinations, combinations_with_replacement


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

        self.list_proposal = []

        self.min_combi = 0
        self.max_combi = 0

    def set_action_object(self):
        for data in self.file_excel:
            profit = round(data[1] * (data[2] + 1), 2)
            self.list_action.append(m_action(data[0], data[1], data[2], profit))

    def create_the_proposals(self):
        proposal = m_proposal(self.budget)
        for index in range(len(self.list_action)):
            tmp_list_action = []
            while proposal.budget > 0:
                for i in self.list_action:
                    if i.cost <= proposal.budget:
                        tmp_list_action.append(i)
                        proposal.budget -= i.cost

    def generate_combinason(self):
        list_combi = self.powerset()
        import pdb; pdb.set_trace()
        for combi_list in list_combi:
            tmp_proposal = m_proposal(self.budget)
            tmp_profit = 0
            for action in combi_list:
                if tmp_proposal.budget > 0:
                    tmp_proposal.list_action.append(action)
                    tmp_proposal.budget -= action.cost
                    tmp_profit += action.profit
            tmp_proposal.total_gain = tmp_profit
            self.list_proposal.append(tmp_proposal)
        self.list_proposal.sort(key=lambda x: x.total_gain, reverse=True)

    def powerset(self):
        s = list(self.list_action)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
