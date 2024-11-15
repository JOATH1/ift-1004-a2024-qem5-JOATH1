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