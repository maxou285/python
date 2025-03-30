# Concours Prologin 2025
# Probleme : Passage tout juste
# Auteur : Maxou285

from typing import List

def force_maximale(longueur: int, tunnel: List[int]) -> None:
    
    #:param longueur: la longueur (en mètres) du passage souterrain
    #:param tunnel: le tableau représentant les zones sûres et les zones de danger du passage souterrain. Un chiffre par mètre : Un `0` correspond à une position dans une zone sûre, et un `1` correspond à une position dans une zone de danger

    
    # TODO Afficher la valeur de force maximale que Joseph Nageant peut obtenir
    
    # en passant le tunnel.
    # Pour commencer on va initialiser quelques variables : 
    esquive_max, repos_min, dparcourue, danger=0, 10**18, 0, tunnel[0]==1
    #esquive_max : plus longue séquence d'esquives dans une zone de danger => intialiser à 0
    #repos_min   : plus petit nombre de mètres de repos dans une zone sûre=> valeur impossible qui sera forcément modifiée
    #dparcourue  : compteur de la distance parcourue (à acutaliser à chaque metre) => initialiser à 0
    #danger   : indique si joseph est ou pas en danger, pour l'instant au début 
   

    for i in range(0,longueur):                       # on va parcourir le tunnel mètre par mètre et agir en fonction de si la zone actuelle est dangereuse ou non
        zone_sure = True if tunnel[i]==0 else 0     # zone_sure => True si on est en zone sure, False si en zone de danger
        
        if zone_sure:                                       # si joseph est dans une zone sure à tunnel[i]
            if danger:                                   
                esquive_max = max(esquive_max, dparcourue)
                dparcourue = 1                              # réinitialisantion pour la nouvelle zone sure
                danger = False                           # actualise in_danger 
            else:
                dparcourue += 1                             # sinon on avance => actualise la taille de la zone
                #print("Distance parcourue : ", dparcourue)
        elif not zone_sure:                          
            if not danger:                       # si on rentre dans une zone de danger
                repos_min = min(repos_min, dparcourue) # on met à jour le repos minimal
                dparcourue = 1                        # réinitialisantion pour la nouvelle zone sure
                danger = True                    # on actualise in_danger puisque la zone actuelle est dangereuse
            else:
                dparcourue += 1                     # sinon on avance (et donc on actualise la taille de la zone)    
                #print("Distance parcourue : ", dparcourue) 
    # on gère la dernière zone séparement et on calcule la force maximale
    if danger:                       
        esquive_max = max(esquive_max, dparcourue)
    else:
        repos_min = min(repos_min, dparcourue)
    print(repos_min - esquive_max)          # reponse_min-esquive_max nous donne la force maximale trouvée
    # a noter qu'on peut facilement optimiser un peu de temps à chaque fois qu'on utilise max et min mais bon le temps n'est pas compté donc :$ 

if __name__ == "__main__":
    longueur = int(input())
    tunnel = list(map(int, input().split()))
    force_maximale(longueur, tunnel)
