"""
Projet TP3 | Jeu de monstre. "RPG"
Nom: Noah Chamoiseau
Groupe: 4567
"""


import random


player_health = 20
game = True
rounds = 0
nb_monstres_morts = 0

print("Si tu veux les règles, écrit 'règles' ")
print(f"Tu as {player_health}PV (pointes de vie)")

def game():
    monster_damage = random.randint(1, 8)

    monster_name = random.choice(["gobelin", "loup", "dragon"])

    win_lose = random.choice(["Win", "Lose"])

    global player_health, game, rounds, nb_monstres_morts

    #la question
    print(f"Il y a un {monster_name}")
    fight = input("Est-ce que tu veux te battre? (o/n) ")

    if fight == "y":

        if win_lose == "Win":
            print("Tu gagnes! + 3PV")
            player_health += 3
            print(f"Tu as {player_health}PV")
            rounds += 1
            nb_monstres_morts += 1

        if win_lose == "Lose":
            print(f"Tu perds. -{monster_damage}PV")
            player_health -= monster_damage
            print(f"Tu as {player_health}PV")
            rounds += 1

    if fight == "n":
        print("Tu perds 2 PV automatiquement.")
        player_health -= 2
        print(f"Tu as {player_health}PV")
        rounds += 1

    if fight == "règles":
        print(" Tu as deux choix: éviter (n) et battre (y). \n Si tu choisis d'éviter, tu perds 2 PV automatiquement. \n Si tu choisi de battre, il y a une chance que tu gange (+ 3PV) ou tu perds (-1 à 8PV aléoatoirement)")

    if player_health <= 0:
        print(f"\n Oh non! Tu as perdu tous tes PVs :( \n en {rounds} parties tu avait tué {nb_monstres_morts} monstres.")
        rounds = 12

while rounds <= 11:
    game()

    #si le joueur gagne le jeu en tout
    if rounds == 10 and player_health > 0:
        print(f"Bravo! Tu as gagné!\nEn dix parties, tu as tué {nb_monstres_morts} monstres.")
        rounds = 12
