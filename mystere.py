import random


nombre_mystere = random.randint(1,100)

max_essais =6
print(f"\n Devinez le nombre mystere entre 1 et 100 . vous avez {max_essais} essais.")

for essai in range(1,max_essais+1):
 print(f"\n----Essai {essai}/{max_essais}----")

 nombre = input("entrer le nombre que vous coiyais etre sure !! :") 
 if not nombre.isdigit():
    print("Entrer un vrai nombre")
    continue

 nombre = int(nombre)

 if nombre_mystere == nombre:
        print(f"Bravo! Vous avez reussir c'est bien le nombre mystere en {essai} essais. ")
        break
 elif nombre < nombre_mystere:
        print("c'est plus grand !")    
 else:
     print("c'est plus petit !")       
else:
   print(f"\n Perdu vous avaz epuiser votre limite d'essaie de {max_essais} essais. Le nombre etait {nombre_mystere}")