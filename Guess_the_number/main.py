import random

jouer = "oui"

while jouer == "oui":
    debut = int(input("Entrez le début de l'intervalle : "))
    fin = int(input("Entrez la fin de l'intervalle : "))
    print("Je pense à un nombre entre", debut, "et", fin, ". A toi de deviner !")
    
    nombre_a_deviner = random.randint(debut, fin)
    essais = 0
    
    while True:
        essai = int(input("Entrez un nombre : "))
        essais += 1
    
        if essai < nombre_a_deviner:
            print("Trop petit !")
        elif essai > nombre_a_deviner:
            print("Trop grand !")
        else:
            print("Bravo, tu as trouvé le nombre en", essais, "essais !")
            jouer = input("Voulez vous rejouer ? oui/non :")
            break

print("Vous avez quitté le jeu") 
