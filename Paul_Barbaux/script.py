
import json

def get_nb_films():
    jsonFile = json.loads(open('../catalog.json').read())
    length = 0
    for category in jsonFile:
        length = length + len(jsonFile[category])
    return length

def main():
    print "Nb total de films dans le catalogue :", get_nb_films()


if __name__ == '__main__':
    main()
