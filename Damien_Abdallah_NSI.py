import csv

"""
possibilité de relancer le programme
possibilité d'ajouter de modifier ou de supprimmer des éléments
question qui fait le liens entre plusisurs fichier :
    années de découverte de toutes les découvertes d'un scientifiques
    les prix de tous les découvreurs d'une lois
completer les fichier
"""
def menu():
# lance le programme  + possibilité de recommencer
    print("Ce programme vous permet de manipuler deux fichiers contenant des informations sur des scientifiques, tel que leur nom, leur année de naissance et de mort et leur prix. Le deuxième contient des lois et leurs informations comme leur nom, leur année de découverte et leurs domaines.\n")
    # on pourrais rajouter le pays d'origine
    print("Vous pouvez effectuer des actions sur la listes des scientifiques ou des découvertes, ou bien les consulter.\n")
    action = input("Scientifiques -1-\nDecouvertes -2-\nConsultation -3-\n").lower()
    if action == "scientifiques" or action == "1":
        modification_scientifiques()
    elif action == "decouvertes" or action == "2":
        modification_découvertes()
    elif action == "consultation" or action == "3":
        consultation()


def consultation():  
# questions que l'utilisateur peut poser
    requete = ""
    while requete == "":
        nom_fichier = input("\nSur quel fichier voulez-vous travailler \nScientifiques -1-\nDecouvertes -2-\n").lower()
        if nom_fichier == "scientifiques" or nom_fichier == "1":
            requete = input("\nInformation sur un scientifique -1-\nNom de tous les scientifiques -2-\nTous les scientifiques qui ont eu un prix Nobel -3-\nTous ceux qui ont vécu au XXème siècle -4-\nToutes les découvertes d'un scientifique -5-\n")
        elif nom_fichier == "decouvertes" or nom_fichier == "2":
            requete = input("\nInformation sur une découverte -1-\nNom de toutes les découvertes - 2-\nToutes les découvertes du XXème siècle - 3-\nNombre moyen de domaines d'application d'une découverte -4-\nTous les scientifiques qui ont participé à une découverte -5-\n")
        else: 
            print("Demande invalide, vérifier que vous n'avez pas écris d'accent ou écrivez le numéro.")
    if nom_fichier == "scientifiques" or nom_fichier == "1":
        with open(r"U:\damien.decarre\scientifiques.csv", newline="", encoding="utf-8") as scientifiques:
            reader = csv.DictReader(scientifiques, delimiter=";")
            if requete == "1":
                nom = input("Nom (format nom prénom) : ")
                info_scientifique(reader, nom)
            elif requete == "2":
                nom_scientifiques(reader)
            elif requete == "3":
                nobel(reader)
            elif requete == "4":
                XX_siecle_scientifique(reader)
            elif requete == "5":
                nom = input("Nom (format nom prénom) : ")
                scientifique_decouverte(nom)
    if nom_fichier == "decouvertes" or nom_fichier == "2":
        with open(r"U:\damien.decarre\decouvertes.csv", newline="", encoding="utf-8") as decouvertes:
            reader = csv.DictReader(decouvertes, delimiter=";")
            if requete == "1":
                nom = input("Nom : ")
                info_decouverte(reader, nom) #bug
            if requete == "2":
                nom_decouvertes(reader)
            
def info_scientifique(reader, nom):
    for row in reader:
        if row["nom"] == nom:
            print(row["nom"] + "  est né en " + row["year_birth"] + " et est mort en " + row["year_death"] + ". Ces prix sont : " + row["prix"])
def nom_scientifiques(reader):
    for row in reader:
        print(row["nom"])
def nobel(reader):
    for row in reader:
        if row["prix"][:5] == "Nobel":
            print(row["nom"])
def XX_siecle_scientifique(reader):
    for row in reader:
        if int(row["year_birth"]) > 1900 or int(row["year_death"]) < 2000:
            print(row["nom"])
def scientifique_decouverte(nom):
    with open(r"U:\damien.decarre\decouvreurs.csv", newline="", encoding="utf-8") as decouvreurs:
        reader = csv.DictReader(decouvreurs, delimiter=";")
        for row in reader:
            if row["decouvreurs"] == nom:
                print(row["nom_decouverte"])

def info_decouverte(reader,nom):#bug
    for row in reader:
        if row["denomination"] == nom:
            print(row["denomination"] + " a été decouvert en " + row["year"] + " et appartient aux domaines suivants : " + row["domaines"])
def nom_decouvertes(reader):
    for row in reader:
        print(row["denomination"])