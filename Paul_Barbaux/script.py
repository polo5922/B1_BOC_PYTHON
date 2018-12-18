
import json
import glob

def get_nb_films():
    jsonFile = json.loads(open('../catalog.json').read())
    length = 0
    for category in jsonFile:
        length = length + len(jsonFile[category])
    return length

def get_name_filmotheque():
    nameList = []
    for nameString in glob.glob("../filmotheque/*.vu"):
        newString = nameString.replace("../filmotheque/","")
        newString = newString.replace(".vu","")
        nameList.append(newString)
    return nameList

def main():
    print "Nb total de films dans le catalogue :", get_nb_films()
    print "name : ", ",".join(get_name_filmotheque())

if __name__ == '__main__':
    main()
