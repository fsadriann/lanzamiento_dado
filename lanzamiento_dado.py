# Programa para simuar el lanzamiento de un dado

import random

print("--------------------------------------")
print("------- LANZAMIENTO DE UN DADO -------")
print("--------------------------------------")

#input

#processing

d = random.randint(1,6)
#d = random.randint(1,6)


if (d == 1):
    rta = "uno"
elif (d == 2):
    rta = "dos"
elif (d == 3):
    rta = "tres"
elif (d == 4):
    rta = "cuatro"
elif (d == 5):
    rta = "cinco"
elif (d == 6):
    rta = "seis"
else:
    rta = "no es la cara de un dado"

print("la cara es " + str(rta))