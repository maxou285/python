# TELECHARGER UNE IMAGE AVEC REQUESTS
#
# https://codeavecjonathan.com/res/papillon.jpg


import requests

reponse = requests.get("https://codeavecjonathan.com/res/papillon.jpg")
if reponse.status_code == 200:
    f = open("papillon.jpg","wb")
    f.write(reponse.content)
    f.close()
    print("Ecriture terminée")
else:
    print("ERREUR code : " + str(reponse.status_code))

    