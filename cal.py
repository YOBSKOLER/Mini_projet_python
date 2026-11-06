
a = input('entrer un nombre a : ' )
b = input('entrer un nombre b : ' )

try:
  add = int(a) + int(b)
  print(add)
except ValueError:
 print("ce que vous avez entrer n'est pas un nombre")