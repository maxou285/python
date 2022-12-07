import time
#strings = time.strftime("%Y,%m,%d,%H,%M,%S")       # Avoir l'année le mois le jour l'heure les minutes et les secondes
strings = time.strftime("%H,%M")                    # Avoir l'heure et les minutes
t = strings.split(',')
numbers = [ int(x) for x in t ]
n2 = str(numbers)
numbers_splited = n2.split(", ")
print(numbers)
print(numbers_splited)
print("Affichage de l'heure : " + numbers_splited[0][1:] + ":" + str(numbers_splited[1][:-1]))