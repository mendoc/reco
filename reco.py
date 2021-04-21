from utils import nb_els_prec

nb   = 16
nbu  = 14
rang = 96

nbp = 0
rang -= 1
it = 0
element = ""
for i in range(nbu, 0, -1):
    for k in range(nb):
        suiv = nb_els_prec(i, k)
        if suiv > rang:
            break
        nbp = suiv
        it = k
    pos = nb - it - i
    while len(element) < pos:
        element += "0"
    element += "1"
    print("nb: " + str(nb) + " | nbu: " + str(i) + " | rang: " + str(rang) + " | nbp: " + str(nbp) + " | it: " + str(it) + " | pos: " + str(pos))
    rang -= nbp

while len(element) < nb:
        element += "0"

print("Element: " + element)
