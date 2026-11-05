"""
Projet TP3 | Jeu de monstre. "RPG"
Nom: Noah Chamoiseau
Groupe: 4567
"""


import random


noms_monstres = ["gobelin", "loup", "dragon"]


def afficher_etat(pv, tour, nb_monstres):
    print(f"Vous avez {pv} points de vie.\nNous sommes au tour {tour} et vous avez vaincque {nb_monstres} monstres.")


def combattre(pv):
    """Génère la force du monstre et retire des PV."""
    global monstre, monstres_tue
    win = random.randint(False, True)
    if monstre == "gobelin":
        force_monstre = random.randint(2, 4)
    elif monstre == "loup":
        force_monstre = random.randint(4, 6)
    elif monstre == "dragon":
        force_monstre = random.randint(6, 8)
    if win:
        print("Vous avez gagné! +1 PV")
        monstres_tue += 1
        pv += 1
    else:
        print(f"Vous avez perdu... -{force_monstre} PV")
        pv -= force_monstre
    return pv


def eviter(pv):
    """Applique la pénalité fixe."""
    pv -= 2
    return pv


def afficher_regles():
    """Affiche les règles du jeu."""
    print("Vous commencez la partie avec 20 points de vie (PV)."
          "La partie se termine immédiatement en défaite si vos PV atteignent 0 ou moins.\n"
          "À chaque tour, un nouveau monstre apparaît et vous devez choisir une des actions suivantes :\n"
          "Combattre le monstre : \nle combat peut se solder par votre victoire ou votre défaite. "
          "En cas de victoire, vous gagnez un certain nombre de PV (1 PV).\n"
          "En cas de défaite, vous perdez un certain nombre de PV, lié à la force du monstre généré aléatoirement.\n"
          "Les goblins sont les moins forts, les loups semi-forts, et les dragons les plus forts\n"
          "Éviter le monstre : \nle combat n'a pas lieu, mais vous perdez tout de même une "
          "pénalité fixe de points de vie (2 PV), pour représenter le risque pris en fuyant.\n"
          "Afficher les règles du jeu :\nvous pouvez aussi demander à revoir les règles en tout temps avant de faire son choix.\n"
          "Cette action n'a aucun effet sur vos PV et ne fait pas avancer le tour."
          "Défaite : vos PV atteignent 0 ou moins.\n"
          "Victoire : vous survivez 10 tours, ou vaincquez un certain nombre de monstres. (8)")


pv_hero = 20
tours = 0
monstres_tue = 0

while pv_hero > 0 and tours < 10 or monstres_tue == 8:
    monstre = random.choice(noms_monstres)
    print(f"\nIl y a un {monstre}.\nVoulez-vous : ")
    choix = input("(C)ombattre, (é)viter ou (r)ègles ? ").lower()
    if choix == "c":
        pv_hero = combattre(pv_hero)
        tours += 1
    elif choix == "e":
        pv_hero = eviter(pv_hero)
        tours += 1
    elif choix == "r":
        afficher_regles()
    if tours < 9:
        afficher_etat(pv_hero, tours, monstres_tue)

    potion = random.randint(1, 15)
    if potion == 1:
        force_potion = random.randint(2, 6)
        print(f"\nVous avez trouvé une potion! Elle vous ajoute {force_potion} PV!\n")
        pv_hero += force_potion

# Affiche une victoire ou défaite
if pv_hero > 0 or monstres_tue >= 8:
    print(f"Bravo! Vous avez gagné!\nVous avez survécu {tours} tours et avez tué {monstres_tue} monstres.")
elif pv_hero <= 0:
    print(f"Vous avez perdu... Dommage...\nVous avez survécu {tours} tours et avez tué {monstres_tue} monstres.")
