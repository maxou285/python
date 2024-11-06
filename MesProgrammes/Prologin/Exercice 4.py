from collections import defaultdict
from typing import List


def le_juste_etal(n: int, valeur: int, boites: List[int]) -> None:
    """
    :param n: le nombre de boites
    :param valeur: la valeur du marché du jour
    :param boites: le contenu de chaque boite
    """
    # TODO Afficher, sur une ligne, un unique entier : le nombre de séries
    # justes modulo $1,000,000,007$.
    MOD = 1000000007  # Modulo set à 1 000 000 007
    start_of_sum = [0] * (n + 1)  # 0 at the start
    remainder_count = defaultdict(int)
    remainder_count[0] = 1
    count_just_series = 0


    for i in range(1, n + 1):                                   # Calcule start_of_sum et nb time remainder
        start_of_sum[i] = (start_of_sum[i - 1] + boites[i - 1]) % valeur
        remainder = start_of_sum[i]

        count_just_series += remainder_count[remainder]         # Add nb time le remainder
        remainder_count[remainder] += 1

    print(count_just_series % MOD)


if __name__ == "__main__":
    n = int(input())
    valeur = int(input())
    boites = list(map(int, input().split()))
    le_juste_etal(n, valeur, boites)

