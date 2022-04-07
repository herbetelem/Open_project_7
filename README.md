# Project Openclassroom : Résolver des problèmes en utilisant des algorythmesen Python
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](http://forthebadge.com).

This project aims to create an algorithm that will seek to find among a list of actions, the best possible combination in the but to generate the most profit possible within a limit of a budget defined.


### library and tools

- https://github.com/PyCQA/mccabe Mccabe
- https://pandas.pydata.org/ Pandas
- https://numpy.org/ Numpy
- https://docs.python.org/fr/3/library/itertools.html Itertools


### Prerequisites

you have to install the requirements with the command ``pip3 install -r requirements.txt``, and your files to inspect must be in excel and have line 1 in the header, then line 2 list the actions


## Launching

If you want to run the bruteforce code, use the ``python3 bruteforce.py`` command, making sure at line 44 that you are going to inspect the correct excel file of actions to prospect

If you want to run the optimized code, use the ``python3 optimized.py`` command, making sure on line 25 that you are going to inspect the correct excel file of actions to prospect


## Functional

Once you have launched the algorithm, you will have a result in about 2s for the bruteforce, and -1s for the optimized (the time varies according to the number of actions), and then there will be a print which will give you the gain obtained, the action list chosen, and the budget spent

If you want to see the time you have to uncomment lines 60, 63, 64 for the bruteforce file, and lines 42, 45, 48 for the optimized file, this will add the information of the execution time of the algorithm in your console

If you want to re-generate the complexity graphs, use the command ``python3 -m mccabe --dot bruteforce.py | dot -Tpng -o appendix/bruteforce.png`` for the bruteforce file, and the command ``python3 -m mccabe --dot optimized.py | dot -Tpng -o annex/optimized.png`` for the optimized file


## Made with

* [Visual Studio Code](https://code.visualstudio.com/) - Code editor


## Author

* **Hadrien Herbet** _alias_ [@herbetelem](https://github.com/herbetelem)
