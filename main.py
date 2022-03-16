""" Module main """

from re import M
from controllers.controller import ControllerRunProgram

import time

def main():

    """ The main finder called the Program class """
    start = time.time()
    main = ControllerRunProgram()
    main.set_action_object()

    main.generate_combinason()

    end = time.time()
    print("combi", end - start)
    print("max: ", main.proposal.total_gain)

if __name__ == '__main__':
    main()




print("The time used to execute this is given below")
