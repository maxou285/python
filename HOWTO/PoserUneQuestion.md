# Poser une question
Avec le premier programme, nous avons appris à utiliser Git comme gestion de codes sources. Le programme lui-même était le plus simpliste possible : une référence au niveau de Python à utiliser et affichage d'un message (instruction 'print'). A partir de maintenant, il s'agit d'aller plus en profondeur dans l'apprentissage du langage Python. 

Dans ce deuxième programme, nous allons apprendre une nouvelle instruction pour poser une question à l'utilisateur. La réponse de l'utilisateur sera enregistrée dans une 'variable'. Nous utiliserons cette variable pour afficher un message. 

Comme d'habitude, on mettra en pratique tout cela mais avant, il y a une notion importante à maitriser : les variables.

## 1. Les variables

### 1.1 Qu'est-ce qu'une variable ?
On peut voir une variable comme étant un morceau de papier sur lequel on va écrire/effacer/modifier des infomations. 

### 1.2 Type (ou classe) d'une variable
Python est un langage qui détermine le type (ou classe) d'une variable par lui-même. Cependant, il est parfois bien pratique de connaître le type de la variable car c'est ce qui détermine les actions (ou méthodes) que l'on peut lui appliquer. 

Quelques exemples : 
- int = numérique entier --> on peut faire des opérations mathématiques telles que des additions. Ainsi, si A=2 et B=3, alors A+B=5
- string =chaine de caractères --> on peut faire des opérations de concaténations. Ainsi, si A="Coucou " et B="les amis", A+B="Coucou les amis". La subtiilité réside dans le fait que les caractères numériques (0 à 9) peuvent être des considérés comme des cacactères et non des nombres entiers. Ainsi, si A="2" (notez les guillemets pour signifier que ce n'est pas un chiffre mais un caractère) et si B="3", alors A+B="23" c'est-à-dire le caractère "2" concaténé au caractère "3"

Comme on le voit le résultat n'est pas le même et pourtant l'opération (+) semble identique. 

Nota : quelle est la différence entre 'type' et 'class' ? A ce stade, on ne va pas traité des classes d'objet. On verra ça un peu plus tard, mais je l'aborde ici par rapport au chapître suivant. Rassurez-vous, rien de bien complexe. 

### 1.3 Création d'une variable

La création d'une variable est très simple en Python. Quand on en a besoin, on déclare un nom et on lui affecte une valeur. 

Exemple : 
```python
prenom="Salut Maxime"       # création d'une variable dont le nom est 'prenom' et la valeur est "Salut Maxime". Astuce pas d'accent dans les noms de variables

nombre_entier=34            # création d'une variable dont le nom est 'nombre_entier' et sa valeur est 34
```

Note : On peut mettre des commentaires dans son code si on précède du symbole `#`.

### 1.4 Connaître le type d'une variable
La programmation est un art dans lequel on passe notre temps à créér/coder une idée, mais on passe un temps fou à débugger c'est-à-dire à enlever les bugs de fonctionnement de notre programme. 

Comme on ne déclare pas le type des variables en Python, on peut parfois croire faire une opération qui en fait donne comme un résultat mauvais tout ça parce qu'on se trompe de type de variable. Aussi, il existe une méthode pour connaître le type d'une variable :
```python
type(nom_de_variable)
```

Exemple : 
```python
#! /usr/bin/python3

A="Salut Maxime"
print(A)
print(type(A))
```

Le résultat est: 
```
Salut Maxime
(class,str)
```
Comme vous le voyez, le type (=classe) est `str` ce qui correspond au type 'string' (chaine de caractères).

Alors que se passe t'il si on affecte une valeur numérique à la variable A. Et bien, c'est simple, Python va changer le type de la variable. Illustration :
```python
#! /usr/bin/python3

A="Salut Maxime"
print(A)
print(type(A))

A=2
print(A)
print(type(A))
```

Le résultat est: 
```
Salut Maxime
(class,str)
2
(class, int)
```
Comme on peut le voir, quand A="Salut Maxime" alors son type est 'str' mais ensuite on change sa valeur par la valeur numérique 2 (sans guillemets donc numérique). Quand on affiche son type, celui-ci est devenu 'int' (entier numérique). Python s'est adapté. C'est cool mais cela impose de la rigueur. Autant vous dire qu'on ne peut pas faire ça dans les langages déclaratifs comme Java.

### 1.5 Tester le type d'une variable
En fait, quand Python créé une variable, en réalité il créé une instance qui correspond au type de la variable. L'instance est la création du 'papier' sur lequel on va écrire les informations que va contenir notre variable. Pour l'ordinateur, cela revient à réserver l'espace mémoire dont il a besoin pour la variable. 

Il peut être utile de connaître le type de la variable. Pour cela, on utilise l'instruction `isinstance(nom_variable,type)`.

Exemple : 
```python
msg = 'Hello'

print(isinstance(msg,int))          # msg est-il un nombre entier ?
print(isinstance(msg,str))          # msg est-il de type chaine de caractères ?
```

Résultat :
```
False
True
```
"False" correspond au fait que "msg" n'est pas un nombre entier. "True" au contraire confirme qu'il s'agit bien d'une chaine de caractères.

### 1.5 Changer le type d'une variable = casting
Parfois, on voudra convertir une variable d'un type dans un autre. Par exemple, on a une variable de type 'str' A qui est une chaine de caractère ayant la valeur "23". On peut la convertir on un nombre entier 23 (sans les guillemets pour faire des opérations numériques dessus). Dans ce cas, on va faire une opération dite de 'casting' très simple. 

Exemple : 
```python
A="23"
print(A)
print(type(A))

print("----------------")

A=int(A)            # ici est le 'cast' ou le changement de type si vous préférez
print(type(A))
print(A)
```

Donne comme résultat :
```
23
(class, str)
----------------
23
(class, int)
```
Comme on le voit, on imprime 2 fois la même chose mais le premier 23 est une chaine de caractère 'str' alors que le deuxième 23 est un nombre entier 'int'. 

## 2. Le programme qui pose une question
Maintenant qu'on en sait plus sur les variables, on va créer le programme qui pose une question à l'utilisateur. Cela va se dérouler ainsi :
- Demander à l'utilisateur comment il s'appelle
- Afficher le message "Salut "+ 'nom de l'utilisateur'

### 2.1 Préparation
Ne pas oublier de créer une nouvelle branche de travail git. Ensuite, on va mettre notre nouveau programme dans un nouveau répertoire (folder) dans le répertoire 'Python'. Vous devez déjà savoir comment faire. Sinon, reportez-vous au chapître [Mon premier programme](https://gitlab.com/maxime285/python/blob/master/HOWTO/PremierProgramme.md)

Nommer votre répertoire : `PoseQuestion`

Puis créer votre fichier : `posequestion.py`

### 2.2 Instructions 'input' et 'raw_input'
L'instruction 'input' est l'instruction qui permet de poser une question à l'utilisateur et de stocker la réponse dans une variable. Le type de la variable dépend de la réponse de l'utilisateur. S'il saisit un nombre alors ça sera de type 'int'. Si c'est une réponse entre guillemets alors ça sera de type 'str'.
Du coup, cette instruction n'est pas pratique car il faut tester son type. 

C'est pour ça qu'il est préférable d'utiliser l'instruction 'raw_input'. Elle fait le même boulot mais stocke le résultat dans une variable de type `str` dans tous les cas. Ensuite, il est possible de convertir le résultat dans le type que l'on souhaite avec le mécanisme de 'cast' vu plus haut.

Sa syntaxe est la suivante :
```python
nom_variable=raw_input('message :')
```

### 2.3 Le code du programme
A toi de jouer Maxime en utilisant les connaissances expliquées au-dessus. Je documenterai la solution plus tard :-)

Rappel. Ton programme doit :
- poser la question : "Comment t'appelles-tu ?"
- afficher le message : "Tu te nommes " + prénom