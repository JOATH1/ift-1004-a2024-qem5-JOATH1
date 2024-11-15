"""

f_1 = open('fichier1.txt', 'r')

produit = 1
somme = 0
line = f_1.readline()
while line != "":
    if line != "----------\n":
        produit = produit * int(line)
    else:
        somme += produit
        produit = 0
    line = f_1.readline()

f_1.close()

print(somme)

"""

#34622

#Le code suivant peut vous mener à cette réponse. Assurez-vous que votre fichier s'appelle fichier1.txt et soit placé dans le même dossier que le fichier contenant votre code.

file = open("fichier1.txt", 'r')
lines = file.readlines()
file.close()
somme = 0
for i in range(len(lines) // 3):
    somme += int(lines[3 * i]) * int(lines[3 * i + 1])
print(somme)

