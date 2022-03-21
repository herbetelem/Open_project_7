""" Module main """

from re import M
from controllers.controller import ControllerRunProgram

import time

def main():

    """ The main finder called the Program class """
    start = time.time()
    start2 = time.time()
    main = ControllerRunProgram()
    end2 = time.time()
    print("create controller", end2 - start2)

    start2 = time.time()
    main.set_action_object()
    end2 = time.time()
    print("set action", end2 - start2)

    start2 = time.time()
    main.generate_combinason()
    end2 = time.time()
    print("generate combi", end2 - start2)

    end = time.time()
    print("combi", end - start)
    print("max: ", main.proposal.total_gain)

if __name__ == '__main__':
    main()




print("The time used to execute this is given below")
