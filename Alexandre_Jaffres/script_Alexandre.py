def get_nb_films(section=None):
    nbfilms = 0
    films = json.load(open('./catalog.json'))
    print "Sections du catalogue: ", films.keys()
    for section in films.keys():
        print "Section: ", section
        section_nb_films = len(films[section])
        print "Nb films dans la section: ", section_nb_films
        nbfilms += section_nb_films
    print "Nb total de films : ", nbfilms
    return nbfilms

def get_persons_list():
    import glob
    glob.glob
    return ["jessy", "andy"]
