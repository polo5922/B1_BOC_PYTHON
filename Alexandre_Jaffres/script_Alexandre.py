#!/usr/bin/python3

import json
import os
import sys
import glob


def film_suivant(personid):
    films_vus = get_films_vus(personid)
    # utiliser une difference de "set" pour trouver le prochain film a voir

    return "FILM_A_VOIR"

def get_films_vus(personid):
    # utilisez la methode readlines
    personfile = "filmotheque/%s.vu"%(personid)
    return open(personfile).readlines()


def get_persons_list():
    # utilisez le module glob avec le pattern *.txt
    persons = [ os.path.basename(f).split('.')[0] for f in glob.glob('filmotheque/*.vu') ]
    # la ligne precedente revient au meme que :
    # persons = []
    # for f in glob.glob('filmotheque/*.vu'):
    #     name = os.path.basename(f).split('.')[0]
    #     persons.append(name)
    return persons


def get_nb_films(section=None):
    nbfilms = 0
    films = json.load(open('./catalog.json'))
    #print "Sections du catalogue: ", films.keys()
    for section in films.keys():
        #print "Section: ", section
        section_nb_films = len(films[section])
        #print "Nb films dans la section: ", section_nb_films
        nbfilms += section_nb_films
    #print "Nb total de films : ", nbfilms
    return nbfilms


def main():
    print("Nb total de films dans le catalogue : ", get_nb_films())
    for p in get_persons_list():
        print("La personne %s a vu %s films"%(p, len(get_films_vus(p))))
        print("  => elle devra regarder le film suivant : %s"%(film_suivant(p)))


if __name__ == '__main__':
    main()
