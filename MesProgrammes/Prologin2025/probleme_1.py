# Concours Prologin 2025
# Probleme : Le juste Message
# Auteur : Maxou285

from typing import List

def dechiffrer_message(n: int, message: List[str]) -> None:
    
    #:param n: la taille du message reçu
    #:param message: le message à restaurer
    
    # TODO Afficher, sur une ligne, le message restauré, c'est-à-dire le
    # message sans les chiffres qui ont été ajoutés lors du transfert.
    message_déchiffré = ""
    élément_précédent = message[0]
    nbr_chiffre = 0
    for élément in message:
        if élément.isdigit() == False:
            message_déchiffré+=élément
        else:
            nbr_chiffre += 1
            if nbr_chiffre==1:
                message_déchiffré+=élément
            elif élément_précédent<=élément:
                message_déchiffré+=élément
            élément_précédent = élément

    print(message_déchiffré)

if __name__ == "__main__":
    n = int(input())
    message = list(input())
    dechiffrer_message(n, message)
