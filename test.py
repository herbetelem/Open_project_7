# import time
# troll = 50000000000000000000000000


# def toto():
#     for i in range(troll):
#         yield i


# start = time.time()
# k = toto()
# print(time.time() - start)


# def toto2():
#     result = []
#     for i in range(troll):
#         result.append(i)
#     return result


# start = time.time()
# b = toto2()
# print(time.time() - start)

# def calc_min_max(self, budget, value, revers):
#     self.list_action.sort(key=lambda x: x.cost, reverse=revers)
#     for i in self.list_action:
#         if budget > i.cost:
#             value += 1
#             budget -= i.cost
#     return value

# def generate_min_max(self):
#     self.min_combi = self.calc_min_max(self.budget, self.min_combi, True)
#     self.max_combi = self.calc_min_max(self.budget, self.max_combi, False)

# def generate_combinason_B(self):
#     for i in range(self.min_combi, (self.max_combi+1)):
#         list_combi = self.powerset_B(i)
#         for combi_list in list(list_combi):
#             tmp_proposal = m_proposal(self.budget)
#             tmp_profit = 0
#             for action in list_combi:
#                 tmp_proposal.list_action.append(action)
#                 tmp_proposal.budget -= action.cost
#                 tmp_profit += action.profit

# def powerset_B(self, nb_combi):
#     print(nb_combi)
#     test = combinations_with_replacement(self.list_action, nb_combi)
#     import pdb
#     pdb.set_trace()

#     return test
