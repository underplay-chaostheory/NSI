import csv

"""
possibilité d'ajouter de modifier ou de supprimmer des éléments
completer les fichiers, si envie
"""

def menu():
    print("\nVous pouvez effectuer des modifications sur la listes des scientifiques ou des découvertes, ou bien les consulter.\n")
    action = input("Modification -1-\nConsultation -2-\n").lower()
    if action == "modification" or action == "1":
        modification()
    elif action == "consultation" or action == "2":
        # TERMINER ET FONCTIONNE CORRECTEMENT
        consultation()
    else:
        print("Veuillez écrire votre action ou son numéro")


def consultation():  
# questions que l'utilisateur peut poser
    requete = ""
    while requete == "":
        nom_fichier = input("\nSur quel fichier voulez-vous travailler \nScientifiques -1-\nDecouvertes -2-\nLes deux fichiers -3-\n").lower()
        if nom_fichier == "scientifiques" or nom_fichier == "1":
            requete = input("\nInformation sur un scientifique -1-\nNom de tous les scientifiques -2-\nTous les scientifiques qui ont eu un prix Nobel -3-\nTous ceux qui ont vécu au XXème siècle -4-\nToutes les découvertes d'un scientifique -5-\n")
        elif nom_fichier == "decouvertes" or nom_fichier == "2":
            requete = input("\nInformation sur une découverte -1-\nNom de toutes les découvertes -2-\nToutes les découvertes du XXème siècle -3-\nNombre moyen de domaines d'application d'une découverte -4-\nTous les scientifiques qui ont participé à une découverte -5-\n")
        elif nom_fichier[:8] == "les deux" or nom_fichier == "3":
            requete = input("\nAnnées de découverte de toutes les découvertes d'un scientifique -1-\nLes prix de tous les scientifiques ayant participé à une découverte -2-\n")
        else: 
            print("Demande invalide, vérifier que vous n'avez pas écris d'accent ou écrivez le numéro.\n")
# réponseS aux questions
    if nom_fichier == "scientifiques" or nom_fichier == "1":
        with open("scientifiques.csv", newline="", encoding="utf-8") as scientifiques:
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
                scientifique_ses_decouverte(nom)
    if nom_fichier == "decouvertes" or nom_fichier == "2":
        with open("decouvertes.csv", newline="", encoding="utf-8") as decouvertes:
            reader = csv.DictReader(decouvertes, delimiter=";")
            if requete == "1":
                decouverte = input("Dénomination de la découverte : ")
                info_decouverte(reader, decouverte)
            if requete == "2":
                nom_decouvertes(reader)
            if requete == "3":
                XX_siecle_decouvertes(reader)
            if requete == "4":
                nb_moy_domaines(reader)
            if requete == "5":
                decouverte = input("Dénomination de la découverte : ").lower()
                decouverte_ses_scientifiques(decouverte)
    if nom_fichier[:8] == "les deux" or nom_fichier == "3":
        if requete == "1":
            nom = input("Nom (format nom prénom) : ")
            annee_decouvertes_scientifique(nom)
        if requete == "2":
            decouverte = input("Dénomination de la découverte : ")
            prix_scientifiques_decouverte(decouverte)
            
###########################################################################################################################################################################################

#questions sur les scientifiques            
def info_scientifique(reader, nom):
    # donne les informations disponibles sur un scientique : Nom, Année de naissance, Année de mort, Prix reçu(s)
    for row in reader:
        if row["nom"] == nom:
            print(row["nom"] + "  est né en " + row["year_birth"] + " et est mort en " + row["year_death"] + ". Ces prix sont : " + row["prix"])
def nom_scientifiques(reader):
    # donne la liste de tous les scientifiques présents dans le fichier scientifiques.csv
    for row in reader:
        print(row["nom"])
def nobel(reader):
    # donne la liste de tous les scientifiques ayant reçu un prix nobel dans le fichier scientifiques.csv
    for row in reader:
        if row["prix"][:5] == "Nobel":
            print(row["nom"])
def XX_siecle_scientifique(reader):
    # donne la liste de tous les scientifiques ayant vécu au XXème siècle
    for row in reader:
        if 2000 > int(row["year_birth"]) > 1900 or 1900 < int(row["year_death"]) < 2000:
            print(row["nom"])
def scientifique_ses_decouverte(nom):
    # donne la liste des découvertes auxquelles un scientifiques a participé
    with open("decouvreurs.csv", newline="", encoding="utf-8") as decouvreurs:
        reader = csv.DictReader(decouvreurs, delimiter=";")
        for row in reader:
            if row["decouvreurs"] == nom:
                print(row["nom_decouverte"])
                
###########################################################################################################################################################################################

# questions sur les découvertes
def info_decouverte(reader,decouverte):
    # donne les informations disponibles sur une découverte : Dénomination, année de découverte, domaines d'application
    for row in reader:
        if row["denomination"] == decouverte:
            print(row["denomination"] + " a été decouvert en " + row["year"] + " et appartient aux domaines suivants : " + row["domaines"])
def nom_decouvertes(reader):
    # donne la liste de toutes les découvertes présentes dans le fichier decouverte.csv
    for row in reader:
        print(row["denomination"])
def XX_siecle_decouvertes(reader):
    # donne toutes les découvertes dont l'année de découverte se trouve au XXème siècle des découvertes du fichier decouvertes.csv
    for row in reader:
        if 2000 > int(row["year"]) > 1900:
            print(row["denomination"])
def nb_moy_domaines(reader):
    # donne le nombre moyen de domaines d'application des découvertes du fichier decouvertes.csv
    somme = 0
    nb_decouverte = 0
    for row in reader:
        domaines = row["domaines"].split(", ")
        somme += len(domaines)
        nb_decouverte += 1
    print(somme/nb_decouverte)
def decouverte_ses_scientifiques(decouverte):
    # donne tous les scientifiques ayant participé à la découverte d'une découverte
     with open("decouvreurs.csv", newline="", encoding="utf-8") as decouvreurs:
        reader = csv.DictReader(decouvreurs, delimiter=";")
        for row in reader:
            if row["nom_decouverte"] == decouverte:
                print(row["decouvreurs"])
                
############################################################################################################################################################################################

# questions sur les deux fichiers
def annee_decouvertes_scientifique(nom):
    # donne l'année de découverte de toutes les découvertes d'un scientifique
    decouvertes_du_scientifique = []
    with open("decouvreurs.csv", newline="", encoding="utf-8") as decouvreurs:
        reader = csv.DictReader(decouvreurs, delimiter=";")
        for row in reader:
            if row["decouvreurs"] == nom:
                decouvertes_du_scientifique.append(row["nom_decouverte"])
    with open("decouvertes.csv", newline="", encoding="utf-8") as decouvertes:
        reader = csv.DictReader(decouvertes, delimiter=";")
        for row in reader:
            if decouvertes_du_scientifique.count(row["denomination"]) == 1:
                print(row["year"])
def prix_scientifiques_decouverte(decouverte):
    # donne tous les prix reçu par tous les scientifiques ayant participés à une découverte
    decouvreurs_de_la_decouverte = []
    with open("decouvreurs.csv", newline="", encoding="utf-8") as decouvreurs:
        reader = csv.DictReader(decouvreurs, delimiter=";")
        for row in reader:
            if row["nom_decouverte"] == decouverte:
                decouvreurs_de_la_decouverte.append(row["decouvreurs"])
    with open("scientifiques.csv", newline="", encoding="utf-8") as scientifiques:
        reader = csv.DictReader(scientifiques, delimiter=";")
        for row in reader:
            if decouvreurs_de_la_decouverte.count(row["nom"]) == 1:
                print(row["nom"] + " a reçu les prix suivants : " + row["prix"])
                
############################################################################################################################################################################################
############################################################################################################################################################################################

# modification des fichiers
def modification():
    print("")


############################################################################################################################################################################################
############################################################################################################################################################################################

#boucle pour que le programme se relance dès qu'il est terminé
print("Ce programme vous permet de manipuler deux fichiers contenant des informations sur des scientifiques, tel que leur nom, leur année de naissance, leur année de décès et leur prix scientifiques. Le deuxième contient des lois et leurs informations comme leur nom, leur année de découverte et leurs domaines.\n")
i = 0
while i < 1:
    menu()
