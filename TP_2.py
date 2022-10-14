
import random
nombre_essaie = 0
print("Choisissait bos nombre minimal et un nombre maximal pour jouer")
nombremm = int(input("Entrer un nombre minimal:"))
nombremx = int(input("Entrer un nombre miximal:"))
nombre_aleatoire = random.randint(nombremm, nombremx)
print("J'ai choisit un chiffre entre", nombremm, "et", nombremx, "je pense a quoi")
while True:
    nbr_essaie = int(input("Entrez un nombre:"))
    if nbr_essaie < nombre_aleatoire :
        nombre_essaie = nombre_essaie + 1
        print("Non, le nombre est plus grande que:", nbr_essaie)

    elif nbr_essaie > nombre_essaie:
        nombre_essaie = nombre_essaie + 1
        print("Non, le nombre est plus petit que:", nbr_essaie)

    if nbr_essaie == nombre_aleatoire:

        print("Bravo le nombre etait:", nbr_essaie, "Nombre de d'essaie:", nombre_essaie)
        rejouer = input("Veux tu rejouer? oui/non:")

        if rejouer == "oui" :
            pass
            nombre_essaie = 0
            print("Choisissait bos nombre minimal et un nombre maximal pour jouer")
            nombremm = int(input("Entrer un nombre minimal:"))
            nombremx = int(input("Entrer un nombre miximal:"))
            nombre_aleatoire = random.randint(nombremm, nombremx)
            print("J'ai choisit un chiffre entre", nombremm, "et", nombremx, "je pense a quoi")

        elif rejouer == "non" :
            break