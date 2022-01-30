import csv

"""
possibilité d'ajouter de modifier
completer les fichiers, si envie
"""

def menu():
    print("\nVous pouvez effectuer des modifications sur la listes des scientifiques ou des découvertes, ou bien les consulter.\n")
    action = input("Modification -1-\nConsultation -2-\nReset les fichiers -3-\n")
    if action == "1":
        modification()
    elif action == "2":
        consultation()
    elif action == "3":
        reset()
    else:
        print("Veuillez écrire votre par son numéro")

def consultation():  
# questions que l'utilisateur peut poser
    requete = ""
    while requete == "":
        nom_fichier = input("\nSur quel fichier voulez-vous travailler \nScientifiques -1-\nDecouvertes -2-\nLes deux fichiers -3-\n")
        if nom_fichier == "1":
            requete = input("\nInformation sur un scientifique -1-\nNom de tous les scientifiques -2-\nTous les scientifiques qui ont eu un prix Nobel -3-\nTous ceux qui ont vécu au XXème siècle -4-\nToutes les découvertes d'un scientifique -5-\n")
        elif nom_fichier == "2":
            requete = input("\nInformation sur une découverte -1-\nNom de toutes les découvertes -2-\nToutes les découvertes du XXème siècle -3-\nNombre moyen de domaines d'application d'une découverte -4-\nTous les scientifiques qui ont participé à une découverte -5-\n")
        elif nom_fichier == "3":
            requete = input("\nAnnées de découverte de toutes les découvertes d'un scientifique -1-\nLes prix de tous les scientifiques ayant participé à une découverte -2-\n")
        else: 
            print("Demande invalide, appelez l'action par son numéro.\n")
# réponses aux questions
    if nom_fichier == "1":
        with open("scientifiques.csv", newline="", encoding="utf-8") as scientifiques:
            reader = csv.DictReader(scientifiques, delimiter=";")
            if requete == "1":
                prenom = input("Prénom : ")
                nom = input("Nom : ")
                nom = prenom + " " + nom
                info_scientifique(reader, nom)
            elif requete == "2":
                nom_scientifiques(reader)
            elif requete == "3":
                nobel(reader)
            elif requete == "4":
                xx_siecle_scientifique(reader)
            elif requete == "5":
                prenom = input("Prénom : ")
                nom = input("Nom : ")
                nom = prenom + " " + nom
                scientifique_ses_decouverte(nom)
    if nom_fichier == "2":
        with open("decouvertes.csv", newline="", encoding="utf-8") as decouvertes:
            reader = csv.DictReader(decouvertes, delimiter=";")
            if requete == "1":
                decouverte = input("Dénomination de la découverte : ")
                info_decouverte(reader, decouverte)
            if requete == "2":
                nom_decouvertes(reader)
            if requete == "3":
                xx_siecle_decouvertes(reader)
            if requete == "4":
                nb_moy_domaines(reader)
            if requete == "5":
                decouverte = input("Dénomination de la découverte : ").lower()
                decouverte_ses_scientifiques(decouverte)
    if nom_fichier == "3":
        if requete == "1":
            prenom = input("Prénom : ")
            nom = input("Nom : ")
            nom = prenom + " " + nom
            annee_decouvertes_scientifique(nom)
        if requete == "2":
            decouverte = input("Dénomination de la découverte : ")
            prix_scientifiques_decouverte(decouverte)
            
###########################################################################################################################################################################################

#questions sur les scientifiques            
def info_scientifique(reader, nom):
    # donne les informations disponibles sur un scientifique : Prénom Nom, Année de naissance, Année de mort, Prix reçu(s)
    for row in reader:
        if row["nom"] == nom:
            print(row["nom"] + "  est né en " + row["year_birth"] + " et est mort en " + row["year_death"] + ". Ces prix sont : " + row["prix"])
def nom_scientifiques(reader):
    # donne la liste de tous les scientifiques
    for row in reader:
        print(row["nom"])
def nobel(reader):
    # donne la liste de tous les scientifiques ayant reçu un prix
    for row in reader:
        if row["prix"][:5] == "Nobel":
            print(row["nom"])
def xx_siecle_scientifique(reader):
    # donne la liste de tous les scientifiques ayant vécu au XXème siècle
    for row in reader:
        if (2000 > int(row["year_birth"]) > 1900) or (1900 < int(row["year_death"]) < 2000):
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
    # donne la liste de toutes les découvertes
    for row in reader:
        print(row["denomination"])
def xx_siecle_decouvertes(reader):
    # donne toutes les découvertes dont l'année de découverte se trouve au XXème siècle
    for row in reader:
        if 2000 > int(row["year"]) > 1900:
            print(row["denomination"])
def nb_moy_domaines(reader):
    # donne le nombre moyen de domaines d'application des découvertes
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
    decouvertes_du_scientifique = sauvegarder_association("decouvreurs", "nom_decouverte",nom)
    with open("decouvertes.csv", newline="", encoding="utf-8") as decouvertes:
        reader = csv.DictReader(decouvertes, delimiter=";")
        for row in reader:
            if decouvertes_du_scientifique.count(row["denomination"]) == 1:
                print(row["year"])
def prix_scientifiques_decouverte(decouverte):
    # donne tous les prix reçu par tous les scientifiques ayant participés à une découverte
    decouvreurs_de_la_decouverte = sauvegarder_association("nom_decouverte", "decouvreurs",decouverte)
    with open("scientifiques.csv", newline="", encoding="utf-8") as scientifiques:
        reader = csv.DictReader(scientifiques, delimiter=";")
        for row in reader:
            if decouvreurs_de_la_decouverte.count(row["nom"]) == 1:
                print(row["nom"] + " a reçu les prix suivants : " + row["prix"])          

############################################################################################################################################################################################
############################################################################################################################################################################################

# modification des fichier en cours
def modification():
    print("")

def reset():
    scientifiques =[['nom', 'year_birth', 'year_death', 'prix'],['Ernest Rutherford', '1871', '1937', 'Nobel de Chimie, Médaille Copley'],['Joseph John Thomson', '1856', '1940', 'Nobel de Physique'],
    ['James Chadwick', '1891', '1932', 'Nobel de Physique'],['Niels Bohr', '1885', '1962', 'Nobel de Physique, Médaille Copley'],['Albert Einstein', '1879', '1955', 'Nobel de Physique'],
    ['Marie Curie', '1867', '1934', 'Nobels de Physique et de Chimie'],['John Dalton', '1766', '1844', 'Aucun'],['Henri Becquerel', '1852', '1908', 'Nobel de Physique']]

    decouvertes =[['denomination', 'year', 'domaines'],['Les rayonnements radioactifs', '1899', 'Physique nucléiare, Modèle standard'],['La désintégration radioactive', '1902', 'Physique nucléaire, Modèle standard'],
    ["L'effet photoélectrique", '1921', 'Physique, Physique nucléaire'],['Le radium', '1898', 'Chimie, Physique nucléaire, Physique'],['Le modèle atomique', '1960', 'Physique nucléaire, Modèle standard'],
    ['Le neutron', '1932', 'Physique nucléaire, Modèle standard'],["L'électron", '1897', 'Physique nucléaire, chimie, Modèle standard'],
    ['Le principe de complémentarité', '1927', 'Physique quantique, Modèle standard'], ["L'énergie de masse", '1905', 'Physique nucléaire, Mécanique céleste, Modèle standard']]

    decouvreurs =[['nom_decouverte', 'decouvreurs'],['Les rayonnements radioactifs', 'Ernest Rutherford'],['La désintégration radioactive', 'Ernest Rutherford'],['Le modèle atomique', 'Ernest Rutherford'],
    ['Le modèle atomique', 'John Dalton'],['Le modèle atomique', 'Joseph John Thomson'],["L'électron", 'Joseph John Thomson'],['Le modèle atomique', 'James Chadwick'],
    ['Le neutron', 'James Chadwick'],['Le modèle atomique', 'Niels Bohr'],['Le principe de complémentarité', 'Niels Bohr'],["L'énergie de masse", 'Albert Einstein'],["L'effet photoélectrique", 'Albert Einstein'],
    ['Le radium', 'Marie Curie'],['Les rayonnements radioactifs', 'Marie Curie'],['La désintégration radioactive', 'Marie Curie'],['La désintégration radioactive', 'Henri Becquerel']]

    reecriture(scientifiques,"scientifiques.csv")
    reecriture(decouvertes,"decouvertes.csv")
    reecriture(decouvreurs,"decouvreurs.csv")

############################################################################################################################################################################################

def sauvegarder_association(clé, valeur, condition):
    stockage = []
    with open("decouvreurs.csv", newline="", encoding="utf-8") as decouvreurs:
        reader = csv.DictReader(decouvreurs, delimiter=";")
        for row in reader:
            if row[clé] == condition:
                stockage.append(row[valeur])
    return stockage

def ajout(nouvelle_ligne,fichier):
    # ajoute nouvelle_ligne au fichier
    with open(fichier,'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(nouvelle_ligne)
def sauvegarder(fichier):
    # prend le nom d'un fichier comme paramètre
    # retourne une liste contenant pour sous-liste chaque lignes du fichier 
    stockage = []
    with open(fichier, newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:  			
            stockage.append(row)
    return stockage
def reecriture(sauvegarde,fichier):
    # écrase les données d'un fichier par les sous-listes d'une sauvegarde, chacunes correspondant à une ligne du nouveau fichier
    with open(fichier,'w', newline='', encoding="utf-8") as file:
    # réécrit le fichier
        writer = csv.writer(file, delimiter=";")
        for row in sauvegarde:
            writer.writerow(row)

############################################################################################################################################################################################
############################################################################################################################################################################################

#boucle pour que le programme se relance dès qu'il est terminé
print("Ce programme vous permet de manipuler deux fichiers contenant des informations sur des scientifiques, tel que leur nom, leur année de naissance, leur année de décès et leur prix scientifiques. Le deuxième contient des lois et leurs informations comme leur nom, leur année de découverte et leurs domaines.\n")
i = 0
while i < 1:
    menu()
