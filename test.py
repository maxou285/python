from typing import List

def plus_petit_ecart(liste: List[int]) -> int:
    liste.sort()
    min_ecart = float('inf')
    for i in range(1, len(liste)):
        ecart = abs(liste[i] - liste[i - 1])
        min_ecart = min(min_ecart, ecart)
    
    return min_ecart

# Exemple d'utilisation
liste = [6, 3, 8, 15, 1]
print("Le plus petit écart est :", plus_petit_ecart(liste))
