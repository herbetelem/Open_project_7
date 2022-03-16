""" Module main """

from re import M
from controllers.controller import ControllerRunProgram

import time

def main():

    start = time.time()
    """ The main finder called the Program class """
    main = ControllerRunProgram()
    main.set_action_object()
    main.generate_combinason()
    main.list_proposal.sort(key=lambda x: x.total_gain, reverse=True)
    print(main.list_proposal[0].total_gain)
    print(main.list_proposal[len(main.list_proposal)-1].total_gain)
    end = time.time()

    print(end - start)
    # for item in main.list_proposal:
    #     print(f"cout: {item.budget}, rental: {item.total_gain}")

if __name__ == '__main__':
    main()




print("The time used to execute this is given below")
