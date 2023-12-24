import random
import time


def nbr_generator(ronde,nbmax):
    for i in range(1,ronde):
        print("Niveau " + str(i) + " : Partie 1")
        for n in range(0,nbmax):
            print(random.randint(1,9))
            time.sleep(1)
        print("Niveau " + str(i) + " : Partie 2")
        for n in range(0,nbmax):
            print(random.randint(1,9))
            time.sleep(1)
        nbmax += 1


nbr_generator(6, 3)
