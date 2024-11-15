# ift-1004-a2024-qem5-JOATH1
Ce repository contient les réponses au questionnaire Exercices du module 5.
## Question 1
Écrivez une fonction vérifiant que deux chaînes de caractère en entrée sont les mêmes, mais sans être sensible à la casse. Par exemple, mot et mOT doivent retourner Vrai tandis que mot et mat doivent retourner Faux. 
```
```
### Réponse
``` Python
def verifier_deux_chaines_de_caracteres(chaine_1, chaine_2):
    """
    Fonction qui vérifie si deux chaînes de caracterès sont semblables
    tout en ignorant la case (case -insensitive)
    Args:
        chaine_1 (str): Première chaîne de caractères
        chaine_2 (str): Deuxième chaîne de caractères
    Returns:
        bool: Un drapeau permettant de rapporter si les chaînes sont semblables ou non. 
    """
    
    if chaine_1.lower() == chaine_2.lower():
        return True
    else:
        return False
        
chaine_1 = input("Entrez une chaîne de caractère: ")
chaine_2 = input("Entrez une autre chaîne de caractère: ")
print(verifier_deux_chaines_de_caracteres(chaine_1, chaine_2))
```
### Solutionnaire
```
def comparaison(chaine1, chaine2):
    return chaine1.lower() == chaine2.lower()
Vous pouvez aussi remplacer les deux lower par deux upper.  
```
#### Commentaires
```
```
## Question 2
Donnez l'affichage résultant des lignes suivantes: 
```
liste = ["un", 2, 3.0, [4], "5", (6,)]
print(liste[1:4][-1][0])
```
### Réponse
```
Trace:
liste[1:4][-1][0]
[1:4]
[2, 3.0, [4]]
[-1]
[4]
[0]
4

```
### Solutionnaire
```
Tour d'abord, la tranche liste[1:4] correspond à la la sous-liste [2, 3.0, [4]].
Ensuite, [2, 3.0, [4]] [-1] réfère au dernier élément de la sous-liste, c'est-à-dire [4] (cet élément étant lui-même une liste de longueur 1.)
Enfin [4] [0] réfère au premier (et seul) élément de la liste [4], soit l'entier 4.
```
#### Commentaires
```
```
## Question 3
Écrivez une fonction insertion_alphabetique(liste_mots, mot) qui insère la chaîne de caractère mot dans la liste liste_mots en ordre alphabétique. Par exemple, si liste_mots = ["bras", "jambe"], alors suite à insertion_alphabetique(liste_mots, "cou"), on aura liste_mots = ["bras", "cou", "jambe"]. Notez que c'est la liste originale qui est modifiée et que la fonction ne doit rien retourner. 

Vous pouvez vérifier que votre implémentation fonctionne en roulant l'assertion suivante: 
```
liste_mots = []
insertion_alphabetique(liste_mots, "jambe")
insertion_alphabetique(liste_mots, "bras")
insertion_alphabetique(liste_mots, "cou")
insertion_alphabetique(liste_mots, "pied")
assert liste_mots == ["bras", "cou", "jambe", "pied"]
```
Assumez que la liste en argument est toujours triée au préalable, c'est-à-dire que votre fonction n'a pas à gérer une liste en argument du genre ["zoo", "animal"]. 

Rappelez-vous que les opérateurs <, <=, > et >= sur les chaînes de caractère les comparent par ordre alphabétique. 
### Réponse
```
def insertion_alphabetique(liste_mots, mot):
    """
    Insère un mot dans une liste en ordre alphabétique
    Args:
        liste_mots (list): Liste de mots
        mot (str): Mot à insérer dans la liste de mots
    """
    position_mot = 0
    for recherche_mot in liste_mots:
        if mot[0] > recherche_mot[0]:
            position_mot += 1
    liste_mots.insert(position_mot, mot)
```
### Solutionnaire
```
def insertion_alphabetique(liste_mots, mot):
    i = 0
    while i < len(liste_mots) and mot > liste_mots[i]:
        i += 1
    liste_mots.insert(i, mot)
```
#### Commentaires
```
```
## Question 4
Donnez l'affichage résultant de l'exécution du code suivant:
```
liste1 = [4, 5, 6]
liste2 = liste1
liste3 = liste1.copy()
liste1[2] = 7

print(liste1)
print(liste2)
print(liste3)
```
### Réponse
```
Trace:
print(liste1)
[4, 5, 7]
print(liste2)
[4, 5, 7]
print(liste3)
[4, 5, 6]

Réponse:
Le résultat qui s'affiche à la suite de l'exécution du code est comme suit:
[4, 5, 7]
[4, 5, 7]
[4, 5, 6]

```
### Solutionnaire
```
[4, 5, 7]
[4, 5, 7]
[4, 5, 6]
liste1 et liste2 sont des noms de variable différents mais 
ils réfèrent à la même liste en mémoire. 
liste3 est une autre liste car elle a été créée par la méthode list.copy().
```
#### Commentaires
```
```
## Question 5
Écrivez une fonction compter_occurences(texte) qui retourne un dictionnaire contenant, pour chaque caractère, le nombre d'occurences de ce caractère dans la chaîne texte. 

Par exemple, pour texte="S.O.S." on devrait obtenir {'S': 2, '.': 3, 'O': 1}. 
```
```
### Réponse
```
def compter_occurences(texte):
    """
    Retourne un dictionnaire contenant, pour chaque caractère, 
    le nombre d'occurences de ce caractère dans la chaîne texte. 
    Args: texte (str): Texte à partir duquel se fait le dénombrement
    Returns:
    dict_denombrement_caracteres
    """
    i = 0
    caracteres =  {}
    while i < len(texte):
        if texte[i] in caracteres:
            n_caracteres = caracteres[texte[i]]
            n_caracteres += 1
            caracteres[texte[i]] = n_caracteres
        else:
            caracteres[texte[i]] = 1
        i += 1
    return caracteres
```
### Solutionnaire
```
def compter_occurences(texte):
    occurences = {}
    for c in texte:
        if c in occurences:
            occurences[c] += 1
        else:
            occurences[c] = 1
    return occurences
```
#### Commentaires
```
```
## Question 6

```
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
```
### Réponse
```

```
### Solutionnaire
```
```
#### Commentaires
```
```
## Question 

```
```
### Réponse
```
```
### Solutionnaire
```
```
#### Commentaires
```
```
## Question 

```
```
### Réponse
```
```
### Solutionnaire
```
```
#### Commentaires
```
```