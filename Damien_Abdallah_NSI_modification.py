import csv

def modification():
    # Si modif du nom, le modifier dans les autres fichiers 
    print("\nVoulez-vous :\n")
    action = input("Ajouter un scientifique -1-\nSupprimer un scientifique -2-\nModifier les informations d'un scientifique -3-\nAjouter une découverte -4-\nSupprimer une découverte -5-\nModifier les informations sur une découverte -6-\nAjouter une associatioin découverte:scientifique -7-\nSupprimer une associatioin découverte:scientifique -8-\n")
    if action =="1":
	nom = input("Scientifique au format : Prénom Nom, Année de naissance, Année de mort, Prix scientifique-s-(En comment par les Nobels) :\n")
        scientifique_ajout(nom)
    elif action =="2":
	nom = input("Nom du scientifique au format Prénom Nom :\n")
        scientifique_suppression(nom)
    elif action =="3":
	print("pas encore disponible")
        # scientifique_modif() #########
    elif action =="4":
	denomination = input("Découverte au format : Dénomination de la découverte, Année de découverte, Domaines impactés :\n")
        decouverte_ajout(denomination)
    elif action =="5":
	denomination = input("Dénomination de la découverte :\n")
        decouverte_suppression(denomination)
    elif action =="6":
	print("pas encore disponible")
        # decouverte_modification() ##########
    elif action =="7":
	relation = input("Relation au format : Dénomination de la découverte, Nom Prénom (du scientifique) :\n")
        decouvreur_ajout(relation)
    elif action =="8":
	relation = input("Relation au format : Dénomination de la découverte, Nom Prénom (du scientifique) :\n")
        decouvreur_suppression(relation)

###################################################################################################################################################################################################################################

def scientifique_ajout(nom):
# ajout d'un scientifique et des informations le concernant
    ajout(nom.split(", "),"scientifiques.csv")
def scientifique_suppression(nom):
#suppression d'un scientifique du fichier scientifiques
    scientifiques = sauvegarder("scientifiques.csv")
    with open(r"U:\damien.decarre\scientifiques.csv",'w', newline='', encoding="utf-8") as file:
    # réécrit le fichier scientifiques sans la valeur à supprimer
        writer = csv.writer(file, delimiter=";")
        for row in scientifiques:
            if row != []:
                if row[0] != nom:
                    writer.writerow(row)
    decouvreurs = sauvegarder("decouvreurs.csv")
    with open(r"U:\damien.decarre\decouvreurs.csv",'w', newline='', encoding="utf-8") as file:
    # réécrit le fichier decouvreurs sans les valeur qui contient le scientifique ayant été retiré
        writer = csv.writer(file, delimiter=";")
        for row in decouvreurs:
            if row != []:
                if row[1] != nom:
                    writer.writerow(row)	

###################################################################################################################################################################################################################################
					
def decouverte_ajout(denomination):
# ajout d'une decouverte et des informations le concernant
    ajout(denomination.split(", "),"decouvertes.csv")
def decouverte_suppression(denomination):
#suppression d'une découverte du fichier decouvertes
    decouvertes = sauvegarder("decouvertes.csv")
    with open(r"U:\damien.decarre\decouvertes.csv",'w', newline='', encoding="utf-8") as file:
    # réécrit le fichier decouvertes sans la valeur à supprimer
        writer = csv.writer(file, delimiter=";")
        for row in decouvertes:
            if row != []:
                if row[0] != denomination:
                    writer.writerow(row)
    decouvreurs = sauvegarder("decouvreurs.csv")
    with open(r"U:\damien.decarre\decouvreurs.csv",'w', newline='', encoding="utf-8") as file:
    # réécrit le fichier decouvreurs sans les valeur qui contient le scientifique ayant été retiré
        writer = csv.writer(file, delimiter=";")
        for row in decouvreurs:
            if row != []:
                if row[0] != denomination:
                    writer.writerow(row)

###################################################################################################################################################################################################################################

def decouvreur_ajout(relation):
# ajout d'une relation si le scientifque et la découverte existent déjà
    nouvelle_ligne = relation.split(", ")
    existe_scientifique = False
    existe_decouverte = False
    with open(r"U:\damien.decarre\scientifiques.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row != []:
                if row[0] == nouvelle_ligne[1]:
                    existe_scientifique = True
    with open(r"U:\damien.decarre\decouvertes.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row != []:
                if row[0] == nouvelle_ligne[0]:
                    existe_decouverte = True
    if existe_deouverte and existe_decouverte:
        ajout(nouvelle_ligne,"decouvreurs.csv")
def decouvreur_suppression(relation):
    relation = relation.split(", ")
    decouvreurs = sauvegarder("decouvreurs.csv")
    with open(r"U:\damien.decarre\decouvreurs.csv",'w', newline='', encoding="utf-8") as file:
    # réécrit le fichier decouvreurs sans la valeur à retirer
        writer = csv.writer(file, delimiter=";")
        for row in decouvreurs:
            if row != []:
                if row[0] != relation[0] and row[1] != relation[1]:
                    writer.writerow(row)

###################################################################################################################################################################################################################################

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
