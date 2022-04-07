# Project Openclassroom : Résolver des problèmes en utilisant des algorythmesen Python
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](http://forthebadge.com).

Ce projet a pour objectif de créer un algorythme qui vas chercher a trouver parmis une liste d'action, la meilleurs combinaison possible dans le but de generer le plus de profit possible dans une limite d'un budget pres definit

### Prerequisites

il faud installer les requierements avec la commande ``pip3 install -r requirements.txt``, et vos fichier a inspecter doivent être en excel et avoir la ligne 1 en header, puis des la ligne 2 lister les actions

## Launching

Si vous souhaitez lancer le code brutforce, utilisez la commande ``python3 bruteforce.py`` en vous assurant a la ligne 44 que vous allez inspecter le bon fichier excel d'actions a prospecter


Si vous souhaitez lancer le code optimized, utilisez la commande ``python3 optimized.py`` en vous assurant a la ligne 25 que vous allez inspecter le bon fichier excel d'actions a prospecter


## Functional

Une fois que vous avez lancer l'algorythme, vous aurez un résultat en a peu pres 2s pour le bruteforce, et -1s pour le optimized (le temps varie en fonction du nombre d'actions), et ensuite il y aura un print qui vous donnera le gain obtenu, la liste d'action choisie, et le budget dépensé

Si vous souhaitez voir le temps il faud décommenter les lignes 60, 63, 64 pour le fichier bruteforce, et les lignes 42, 45, 48 pour le fichier optimized, cela vous ajoutera l'information du temps d'execution de l'algorythme dans votre console


## Made with

* [Visual Studio Code](https://code.visualstudio.com/) - Code editor


## Author

* **Hadrien Herbet** _alias_ [@herbetelem](https://github.com/herbetelem)
