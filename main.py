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
    print(main.list_proposal[0].total_gain)
    end = time.time()

    print(end - start)

if __name__ == '__main__':
    main()




print("The time used to execute this is given below")
