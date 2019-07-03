# Les tests
Les tests sont importants en programmation. Ils permettent d'orienter l'exécution des instructions dans un sens ou dans l'autre. 

## Comment faire des tests
Pour cela on utilise des opérateurs de comparaison. Ils servent à déterminer si l'expression est vrai ou fausse. Dans l'exemple précédent, l'opérateur est `>`.

## Le type de variable booleen
En anglais *boolean*, il s'agit juste d'une variable qui ne peut prendre que 2 valeurs : VRAI ou FAUX.

## L'instruction en Python
On utilise les instruction `if`, `elif` et `else` sui ont la signification suivante :

Instruction | Signification
--- | ---
if | si
elif | sinon si
else | sinon

Elle s'utilise comme suit : 
```python
if <condition 1> :
    <instructions>                                                  # exécuté si condition 1 est vraie
elif <condition 2> :
    <instructions>                                                  # exécuté si condition 2 est vraie
else
    <instructions>                                                  # exécuté dans tous les autres cas
```

A noter que l'on peut avoir autant de `elif` que l'on souhaite. Par exemple : 
```python
if <condition 1> :
    <instruction 1>                                                 # exécuté si condition 1 est vraie
    <instruction 2>                                                 # exécuté si condition 1 est vraie
elif <condition 2> :
    <instructions si condition 2 est vrai>                          # exécuté si condition 2 est vraie
elif <condition 3> :
    <instructions si condition 2 est vrai>                          # exécuté si condition 3 est vraie
elif <condition 4> :
    <instructions si condition 2 est vrai>                          # exécuté si condition 4 est vraie
elif <condition 5> :
    <instructions si condition 2 est vrai>                          # exécuté si condition 5 est vraie
else
    <instructions si les conditions 1,2,3,4 et 5 sont fausses>      # exécuté dans tous les autres cas
```

A noter que c'est une bonne pratique de traiter **TOUS** les cas. C'est l'objectif de l'instruction `else` que l'on met en dernier du coup. 

## L'indentation en Python est primordial
Avez-vous remarqué le décalage dans les lignes précédente ?
Ce décalage informe Python que le bloc d'instructions n'est réalisé que si la *condition* est vraie.

## Opérateurs de comparaison
Pour pouvoir comparer, il faut des comparateurs. On les appelle des *opérateurs de comparaison*.

Voici la liste des opérateurs utilisables :

Opérateur | Signification
--- | ---
&nbsp;== | égal
&nbsp;= | non égal
&nbsp;> | supérieur
&nbsp;>= | supérieur ou égal
&nbsp;< | inférieur
&nbsp;< | inférieur ou égal

Du coup, le résultat est forcément **vrai** ou **faux**. Il n'y a pas de **presque vrai** :-)

Par exemple, ça peut donner :

```python
A=23                                    # initialisation de la variable que je veux tester

if (A > 0):                             # si A > 0 alors
    print("Le nombre est positif")          # imprime "Le nombre est positif" si A > 0
else                                    # sinon
    print("Le nombre est négatif")          # imprime "Le nombre est négatif"
```

## Comment combiner des comparaisons
Les combinaisons de comparaison permettent de tester :
- plusieurs états pour **une** variable 
- l'état de **plusieurs** variables

Pour cela on utilise des opérateurs de jonction dont voici la liste :
Opérateur | Signification
--- | ---
and | et
or | ou

### Exemple de comparaison de plusieurs états pour **une** variable
```python
A=23                                                            # initialisation de la variable que je veux tester

if (A >= 10) and (A <= 100):                                    # si (A<=10) ET (A<=100) alors
    print("Le nombre est supérieur à 10 et inférieur à 100")        # imprime "Le nombre est supérieur à 10 et inférieur à 100"
else                                                            # sinon
    print("Le nombre n'est pas compris entre 10 et 100")            # imprime "Le nombre n'est pas compris entre 10 et 100"
```

### Exemple de comparaison impliquant plusieurs variables
```python
age=23                                                          # initialisation de la variable age
prenom="Maxime"                                                 # initialisation de la variable prenom 

if (prenom == "Maxime") and (age > 10):                         # ici on teste les valeurs pour 2 variables différentes : prenom et age
    print("Tu t'appelles Maxime et tu as plus de 10 ans")
elif (prenom != "Maxime") 
    print("Tu ne t'appelles pas Maxime")      
elif (age <= 10) 
    print("Tu as moins de 10 ans")      
else 
    print("Ce message ne sert à rien puisque l'on a testé tous les cas au-dessus donc on pourrait s'en passer")   
```

## Programme pour tester tout cela
Le programme que je vous propose de réaliser est le suivant :
1. Demander à l'utilisateur comment il va
2. S'il répond "bien" ou "Bien" (avec la majuscule) alors lui dire "C'est super !" sinon lui dire "Trop dommage. J'espère que tu vas aller mieux"
3. Puis lui demander son âge 
4. S'il a moins de 11 ans, lui dire "Tu es un enfant". S'il a entre 11 et 18 ans, lui dire que c'est un adolescent. Sinon lui dire que c'est un adulte 