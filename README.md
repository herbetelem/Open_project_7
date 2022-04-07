# Project Openclassroom : Résolver des problèmes en utilisant des algorythmesen Python
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](http://forthebadge.com).

Ce projet a pour objectif de créer un algorythme qui vas chercher a trouver parmis une liste d'action, la meilleurs combinaison possible dans le but de generer le plus de profit possible dans une limite d'un budget pres definit

### Prerequisites

il faud installer les requierements avec la commande ``pip3 install requirements.txt``

## Launching

Once this requirement have been done, you will only have to open the index.html file into your browser


## Functional

The menu at the top is there to allow you to reach the different parts of the site, the search bar on the other hand is only there to look pretty
In the section:
- First section: here, you will have a movie showing, you will have a link to watch it online, see its trailer, and have some information such as the description of the movie, its title, a poster, ...
- Top 10 section: in this section you will have the top 10 films that come from the api database made available for this project.
- Category section: in this section you will have the 10 films from the category defined in advance, if you wish to change category, you will have to modify lines 152, 153, 155, 156, 158, 159 with a link such as this ``http://localhost:8000/api/v1/titles/?genre={GENRE}{&min_year=xxxx}``.
In this link, the ``{GENRE}`` have to be replace by the genre you want to have, and the ``{&min_year=xxxx}`` have to be place if you want to get the movies who have been realised after a precise year, the xxxx respresanted the year.
- Film info section: once you click on a film, you will have a card that will give you information about the chosen film (director, cast, genre, ...)


## Made with

* [Visual Studio Code](https://code.visualstudio.com/) - Code editor


## Author

* **Hadrien Herbet** _alias_ [@herbetelem](https://github.com/herbetelem)
