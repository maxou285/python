# Mon premier programme
GitLab est un gestionnaire de sources codes sur Internet. Il permet de stocker tous mes codes sources et d'y avoiraccès depuis n'importe où. Il permet aussi de le partager. 

Je vais stocker tous mes codes sources Python dans le répertoire Python sur GitLab, puis je créérai un répertoire par projet. 

L'objet de ce chapitre est de montrer :
- Comment créer un projet sur GitLab pour son projet
- Comment cloner ce projet sur son poste de travail avec 'git clone'
- Comment créer une branche locale Git qu va contenir mon code source
- Comment ajouter une répertoire qui va contenir le code source de mon proemier programme en local (sur mon poste de travail)
- Comment créer un fichier Python qui va contenir le code source de mon programme en local 
- Comment tester mon programme en local 
- Comment pousser ma branche dans lmon repository sur GitLab
- Comment merger ma branche sur GitLab avec la branche Master

## Créer mon répertoire sur GitLab pour mon projet
1. Se connecter sur <https://gitlab.com> 
2. Créer un projet Python en cliquant sur 'New Project'
3. Lui donner le nom 'Pyhton' et le laisser 'Private'

Ca y est, on a créer notre projet. Mais il n'existe que sur GitLab, or je veux développer sur mon poste de travail. Je vais donc le 'cloner' sur mon poste de travail

## Cloner le projet sur mon poste de travail
1. Sur GitLab, cliquer sur `Clone` (en haut à droite) et copier le texte pour cloner en SSH : git@gitlab.com:maxime285/python.git
1. Ouvrir une boite de commander sous Windows ou un Terminal sous MacOS/Linux
2. Se positionner dans le répertoire où on veut cloner le répertoire de travail 
3. Exécuter la commande suivante :
```shell
git clone git@gitlab.com:maxime285/python.git
```

Ca y est, vous avez `cloné` le contenu qui était sur Internet sur votre poste de travail. Pour le moment, il n`y a rien dedans. Nous allons maintenant créer une branche de travail. En effet, il ne faut pas toucher à la branche "Master" directement. Celle-ci doit uniquement contenir des codes qui fonctionnent parfaitement. 

## Créer une branche de travail
1. Dans VSC, cliquer sur l'icône `GitLens` (un rond dans lequel on voit une espèce d'embranchement)
2. Click droit sur la branche `Master` puis `Create branch (via Terminal)`
3. Donner un nom à la branche : `mon-debut-de-code`
4. La ligne de commande est générée, il faut appuyer sur la touche `Enter` pour valider
5. La branche nouvellement créée est apparue, il faut l'activer. Pour cela, click droit sur `mo,n-debut-de-code` puis clicker sur`Checkout`

Tous les changements auront maintenant lieu dans cette branche sans altérer la branche principale (Master).

Nous allons maintenant, créer le répertoire pour notre premier programme, le tester et le stocker dans notre repository GitLab sur Internet. 

## Créer mon projet
Mon premier programme Python est très simple. Il s'agit juste d'afficher un message 'Salut Maxime" à l'écran. 

1. Dans VSC, ouvrir le projet : `File -> Open` et naviguer jusqu'au répertoire `Python`

A ce stade, le répertoire Python apparait dans la partie Gauche de VSC. Je vais créer un répertoire `Hello` pour mon programme puis créer le fichier source hello.py qui contient le code source :

2. Si ce n'est pas le cas, cliquer sur l'icône `Explorer` en haut à gauche (2 fichiers l'un sur l'autre)
3. Click droit sur `Python` puis `New Folder` et donner le nom `Hello`
4. Click droit sur `Hello` puis `New File` et donner le nom `hello.py`

Maintenant, je double clique sur hello.py pour entrer le code suivant sui va afficher le message :
```shell
#! /usr/bin/python3

print("Salut Maxime")
```
La première ligne informe qu'il faut utiliser la version 3 de Python. La deuxième ligne contient l'instruction d'affichage du message "Salut Maxime".

5. Sauvegarder le programme avec `CTRL+S`

## Tester si le programme fonctionne bien
1. Click droit sur le hello.py 
2. Cliquer sur `Run Python File in Terminal'

Observer que ça affiche bien le message 'Salut Maxime'

## Pousser la branche sur GitLab
Ca se passe en 2 étapes :
1. Stage + Commit de nos changements
2. Poussage de la branche avec nos commits sur le site internet gitlab.com

### Stage + Commit
Définitions :
- Stage = acter des changements effectués dans notre programme. Un changement peut être un ajout/suppression de code, ou même l'ajout/retrait de fichier ou de dossiers dans notre projet
- Commit = confirmer des changements et les rendre prêts à être pousser sur gitlab.com. Quand on Commit, on doit fournir un message d'explication : ex: ajout du programme hello.py 

1. Cliquer sur l'icône `Source Control` (en forme de Y). Normalement, il y a un nombre qui informe sur le nombre de changements à stager et à commmitter.
2. On voit tous les fichiers qui ont subi des modifications. Cliquer sur '+'  et donner un message d'explication' dans le champs 'Message 

### Pousser la branche sur gitlab.com

1. Cliquer sur `GitLens` à gauche (icône ronde avec un embranchement dedans)
2. Clicker sur la fl^che qui va vers le haut qui correspond à `Push Repositories'

Un message nous informe que la branche n'existe pas sur GitLab. Cliquer sur OK. Que s'est-il passé :
- VSC a exécuté la commande 'git push' pour nous
- Le programme git que l'on a installé sur notre poste a contacté notre repository sur le site internet 'GitLab'
- Le programme git a poussé notre branche 'mon-debut-de-code' dnas niotre repository

Maintenant, il faut aller sur GitLab et merger la branche avec la branche principale "Master".

## Merger la branche de travail avec la branche principale
La branche principale "Master" est la branche qui contient du code qui fonctionne. L'idée est de ne la modifier que lorsqu'on est sûr que le code sur lequel on a travaillé fonctionne correctement. 

L'action Merge consiste à incorporer les changements que l'on a dans notre branche de travail (mon-debut-de-code) dans la branche principale (Master). Ca se passe sur le site GitLab.

1. Se connecter sur gitlab.com
2. Constater qu'il y a maintenant 2 branches sur gitlab.com en cliquant sur la flêche à côté de 'Master'
3. Dans la branche Master, il n'y a rien (pas de répertoire Hello par exemple). Il s'agit de la version 0 (V0)
4. Sélectionner la branche `mon-debut-de-code`. On voit alors qu'il y a un répertoire qui se nomme 'Hello'. Si on clique sur 'Hello' on voit qu'il y a notre programme 'hello.py'. Ils ne sont pas encore dans la branche principale (Master). On va merger cette branche pour pousser tout cela dans la branche Master
5. Cliquer sur `Merge`
6. Mettre un message qui décrit les changements
7. Cliquer sur `Assign to` et se sélectionner soi-même si personne d'autre n'a à valider les changements
8. Sélectionner 'Delete source branch'
9. Valider
10. On demande encore de cliquer sur `Merge` pour confirmer le Merge

C'est fait. GitLab a intégré les changements dans la branche principale. 

On peut le vérifier ainsi :
- Constater qu'il n'y a plus que la branche Master dans GitLab en cliquant sur la petite flêche juste à c$oté de Master
- Voir que les changements ont bien été pris en compte : il y a un répertoire Hello et le fichier hello.py dedans. Master est en version 1 (V1)

Il s'agit maintenant de faire en sorte que le poste de travail soit au même niveau que gitlab.com. Pour le moment, ils ne sont pas dans le même état comme le présente le tableau ci-dessous
&nbsp | Poste de travail | GitLab | Action requise
--- |--- | ---  | --- 
Niveau de la branche Master | V0 | V1 | Passer la branche Master en local de V0 à V1 en tirant (pull) depuis GitLab
Branches | Master et mon-debut-de-code | Master | Supprimer la branche mon-debut-de-code

### Passer la branche Master en local de V0 à V1 en tirant (pull) depuis GitLab
1. Aller dans VSC 
2. Cliquer sur l'icône Passer la branche Master en local de V0 à V1 en tirant (pull) depuis `GitLens`(icône ronde avec embranchement)
3. Activer la branche Master en faisant : click droit sur `Master` puis `Checkout`. On est en V0 en local, donc il n'y a ni le répertoire 'Hello' ni le fichier 'hello.py'. Se rassurer, ils ne sont pas perdus. C'est juste qu'ils ne sont pas dans la branche locale Master. Si on activait la branche 'mon-debut-de-code' on les retrouverait. Mais on veut passer la branche Master de V0 à V1 donc on reste sur celle-ci
4. Clicker sur l'icône de `flêche vers le bas` qui correspond à `Pull Repositories`

Git en local (sur le poste de travail), applique tous les changements de branche Master de GitLab sur la branche Master en local. Il est possible de vérifier que les changements sont bien apparus en voyant que maintenant il y a bien le répertoire 'Hello' et 'hello.py'. 

### Supprimer la branche mon-debut-de-code
On a plus besoin de la branche mon-debut-de-code alors on va la supprimer :

1. Click droit sur `mon-debut-de-code'
2. Cliquer sur `Delete branch (via Terminal)`
3. Appuyer sur `Enter` dans la fenêtre Terminal. Ca supprime la branche

Résultat des courses on se retrouve comme suit : 
&nbsp | Poste de travail | GitLab 
--- |--- | --- 
Niveau de la branche Master | V1 | V1 
Branches | Master | Master 

On est bien au même niveau. 

## BRAVO
Dans ce chapitre, on a : 
- Créé un nouveau projet vide 'Hello' sur GitLab
- Cloné ce projet vide sur notre poste de travail
- Créé une branche de développement de notre prohgramme
- Créé un répertoire pour notre programme et on développer un programme Python très simple
- Testé que notre programme fonctionne bien
- Poussé notre branche de développement sur GitLab
- Mergé notre branche de développement avec la branche Master et supprimé la branche de développement sur GitLab 
- Fait en sorte que le poste de travail soit au même niveau que GitLab
