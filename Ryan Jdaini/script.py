#!/usr/bin/python

import json


def film_suivant(personid):
    films_vus = get_films_vus(personid)
    # utiliser une difference de "set" pour trouver le prochain film a voir
    return "FILM_A_VOIR"

def get_films_vus(personid):
    jsonFile = json.loads(open('../catalog.json').read())
    return []


def get_persons_list():
    # utilisez le module glob avec le pattern *.txt
    return ["Ryan"]



def get_nb_films():
    jsonFile = json.loads(open('../catalog.json').read())
    length = 0
    for category in jsonFile:
        length = length + len(jsonFile[category])
    return length


def main():
    print "Nb total de films dans le catalogue : ", get_nb_films()
    for p in get_persons_list():
        print "La personne %s a vu %s films"%(p, 0)
        print "  => elle devra regarder le film suivant : %s"%(film_suivant(p))


if __name__ == '__main__':
    main()
