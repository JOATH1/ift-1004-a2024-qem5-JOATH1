def insertion_alphabetique(liste_mots, mot):
    """
    tout en ignorant la case (case -insensitive)
    Args:
        liste_mots (list): Liste de mots
        mot (str): Mot à insérer dans la liste de mots
    """
    position_mot = 0
    for recherche_mot in liste_mots:
        if mot[0] > recherche_mot[0]:
            position_mot += 1
    liste_mots.insert(position_mot, mot)

liste_mots = []
insertion_alphabetique(liste_mots, "jambe")
insertion_alphabetique(liste_mots, "bras")
insertion_alphabetique(liste_mots, "cou")
insertion_alphabetique(liste_mots, "pied")
assert liste_mots == ["bras", "cou", "jambe", "pied"]