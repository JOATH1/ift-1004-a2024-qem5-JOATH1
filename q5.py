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


denombrement = compter_occurences("S.O.S.")
assert denombrement ==  {'S': 2, '.': 3, 'O': 1}
print(denombrement)