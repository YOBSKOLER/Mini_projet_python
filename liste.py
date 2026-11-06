
liste = []

while True:
    print("\n--- Ma liste de courses---")
    print("1: Ajouter")
    print("2: Retirer")
    print("3: Afficher")
    print("4: Quitter")

    choix = input("Ton choix : ")

    if choix == "1":
        fruit = input("Quel fruit ajouter vous ? :")
        liste.append(fruit)
        print(f"{fruit} ajouter !")

    elif choix == "2":
         fruit = input("Quel fruit retirer vous ?") 
         if fruit in liste:
             liste.remove(fruit)
         else:
             print("l n'est pas dans la liste")
    elif choix == "3":
        print("Ta liste de course :" , liste)
    elif choix == "4":
        print("Au revoir !")
        break                    