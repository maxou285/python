# Challenge de code Cuisson des oeufs
import time
import os

dingfile = os.path.join("resources", "ding.wav")

def timer(time):
    timeminutes = time//60
    timeseconde = time - timeminutes*60
    return timeminutes, timeseconde

def cuisson(time_secondes):
        while time_secondes != 0:
            timetuple = timer(time_secondes)
            print(f"\nDurée restante: {timetuple[0]:02d} : {timetuple[1]:02d} .", end="")
            for i in range(0,10):
                print("." ,end="", flush=True)
                time.sleep(0.1)
                time_secondes -= 1
        print("\n\nCuisson terminée ! ")
        os.system("afplay " + dingfile)

def mainapp():
    print("Cuisson des Oeufs\n------------------------------")
    print("a) Oeufs à la coque: 3 minutes")
    print("b) Oeufs mollets: 6 minutes")
    print("c) Oeufs durs: 9 minutes")
    reponse = input("Votre choix: ")
    message = print("\n    -- Cuisson en cours --")
    if reponse == "a":
        cuisson(180)
    elif reponse == "b":
        cuisson(360)
    elif reponse == "c":
        cuisson(540)
    else:
        print("Vous devez rentrer une lettre (a, b ou c)")
        mainapp()

mainapp()



