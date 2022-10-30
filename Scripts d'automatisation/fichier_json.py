# Json
# Manipuler des données structurées
import json
# Personne
#   nom : str
#   age : int
#   amis : [str]

# Paul
# 25
# Sophie, Marie, Jean
# Pierre
# 18
# Eric, Marc
"""
personne = {"nom" : "Paul",
            "age" : 25,
            "amis" : ["Sophie", "Marie", "Jean"]}

# Sérialiser DATA => TXT ""(json)   dumps
# Désérialiser TXT ""(json) => DATA loads
personne_json = json.dumps(personne)
print(personne_json)

f = open("fichier_json.txt","w")
f.write(personne_json)
f.close()
"""

f = open("fichier_json.txt", "r")
donne_json = f.read()
f.close()

personne = json.loads(donne_json)

print("Nome : " + personne["nom"])
