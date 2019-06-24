# Les tests
Les tests sont importants en programmation. Ils permettent d'orienter l'exécution des instructions dans un sens ou dans l'autre. 

## Comment faire des tests
Pour cela on utilise des opérateurs de comparaison. Ils servent à déterminer si l'expression est vrai ou fausse. Dans l'exemple précédent, l'opérateur est `>`.

## Le type de variable booleen
En anglais *boolean*, il s'agit juste d'une variable qui ne peut prendre que 2 valeurs : VRAI ou FAUX.

## L'instruction en Pyhton
On utilise les instruction `if`, `elif` et `else` sui ont la signification suivante :

Instruction | Signification
--- | ---
if | si
elif | sinon si
else | sinon

Elle s'utilise comme suit : 
```python
if <condition 1> :
    <instructions si condition 1 est vrai>
elif <condition 2> :
    <instructions si condition 2 est vrai>
else
    <instructions si condition 1 ET condition 2 sont fausses>
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
== | égal
!= | non égal
> | supérieur
>= | supérieur ou égal
< | inférieur
< | inférieur ou égal

Du coup, le résultat est forcément **vrai** ou **faux**. Il n'y a pas de **presque vrai** :-)

Par exemple, ça peut donner :

```python
A=23                                    # initialisation de la variable que je veux tester

if (A > 0):
    print("Le nombre est positif")      # imprime "Le nombre est positif" si A > 0
else
    print("Le nombre est négatif")      # sinon imprime "Le nombre est négatif"
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

if (A >= 10) and (A <= 100):
    print("Le nombre est supérieur à 10 et inférieur à 100")
else
    print("Le nombre n'est pas compris entre 10 et 100")      
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
1. Demander son prénom à l'utilisateur en lui posant une question et stocker la réponse dans une variable
2. Demander ensuite l'âge de l'utilisateur et stocker la réponse dans une variable
3. Si l'âge de l'utilisateur est inférieur à 10 ans alors lui dire qu'il a le droit au menu "Enfant"
4. Si l'âge de l'utilisateur est entre 10 et 18 ans alors lui dire qu'il a le droit au menu "Enfant XL"
5. Sinon lui dire qu'il a le droit au menu "Adulte" uniquement

Ca serait bien que la phrase l'informant soit du type : "Salut Maxime, tu as le droit au menu Enfant XL". Evidemment, c'est donné à titre d'exemple. "Maxime" doit correspondre au contenu d'une variable qui aura été remplie lors de la question 1. 
