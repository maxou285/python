# Modifier mon programme

#### IMPORTANT : les détails des opérations à effectuer sont décrits dans les paragraphes numérotés. 

Quand on veut modifier son programme on doit effectuer les actions suivantes :
- S'assurer que la branche `Master en local` est égale à la branche `Master sur GitLab`
- Créer une nouvelle branche de développement
- Effectuer les nouveaux développements
- Vérifier que le programme fonctionne bien
- Valider les changements (Stage + Commit) 
- Pousser la branche de développement sur GitLab
- Merger la branche de développement avec la branche Master et supprimer la branche de développement sur GitLab
- Synchroniser la branche Master locale avec la branche Master GitLab et supprimer la branche de développement en local

## 1. S'assurer que la branche Master en local est égale à la branche Master sur GitLab
Si ce n'est pas le cas, il faut :
1. Dans VSC, cliquer sur l'icône `GitLens` (cercle avec embranchement)
2. Activer la branche `Master` (Checkout)
3. Cliquer sur l'icône `flêche vers le bas` (Pull Repositories)
4. Supprimer les branches qui ne sont pas utiles s'il y en a

## 2. Créer une nouvelle branche de développement
On a déjà vu comment il faut faire, mais je le rappelle ici : 
1. Dans VSC, cliquer sur l'icône `GitLens` (un rond dans lequel on voit une espèce d'embranchement)
2. Click droit sur la branche `Master` puis `Create branch (via Terminal)`
3. Donner un nom à la branche : `ajout-print-valentin`
4. La ligne de commande est générée, il faut appuyer sur la touche `Enter` pour valider
5. La branche nouvellement créée est apparue, il faut l'activer. Pour cela, click droit sur `ajout-print-valentin` puis clicker sur`Checkout`

## 3. Effectuer les nouveaux développements
On va ajouter un 'Bonjour Valentin" au programme :
1. Dans VSC, cliquer sur l'icône `Explorer` (fichiers l'un sur l'autre)
2. Ouvrir hello.py et ajouter l'instruction Print. Le résultat est comme suit normalement : 
```shell
#! /usr/bin/python3

print("Salut Maxime")
print("Bonjour Valentin")
```
## 4. Vérifier que le programme fonctionne bien
1. Dans VSC, cliquer sur l'icône `Explorer`
2. Click droit sur le fichier 'hello.py' et cliquer sur `Run Python File in Terminal`

On doit voir les 2 messages s'afficher comme il faut. 

## 5. Valider les changements (Stage + Commit) 
Fastoche :
1. Cliquer sur l'icône `Source Control` (en forme de Y). Normalement, il y a un nombre qui informe sur le nombre de changements à stager et à commmitter.
2. On voit tous les fichiers qui ont subi des modifications. Cliquer sur '+'  
3. Puis donner un message d'explication' dans le champs 'Message et cliquer la 'coche de validation' pour Committer

## 6. Pousser la branche de développement sur GitLab
1. Cliquer sur `GitLens` à gauche (icône ronde avec un embranchement dedans)
2. Clicker sur la flêche qui va vers le haut qui correspond à `Push Repositories'

## 7. Merger la branche de développement avec la branche Master et supprimer la branche de développement sur GitLab
1. Se connecter sur gitlab.com
2. Sélectionner la branche `ajout-print-valentin`
3. Cliquer sur `Merge`
4. Mettre un message qui décrit les changements
5. Cliquer sur `Assign to` et se sélectionner soi-même si personne d'autre n'a à valider les changements
6. Sélectionner 'Delete source branch'
7. Valider
8. On demande encore de cliquer sur `Merge` pour confirmer le Merge

## 8. Synchroniser la branche Master locale avec la branche Master GitLab
1. Dans VSC, cliquer sur l'icône `GitLens`(icône ronde avec embranchement)
2. Activer la branche Master en faisant (click droit sur `Master` puis `Checkout`). 
3. Clicker sur l'icône de `flêche vers le bas` qui correspond à `Pull Repositories`
4. Click droit sur la branche `ajout-print-valentin` puis `Delete branch (via Terminal)` et appuyer sur `Enter` dans la fenêtre Terminal

# BRAVO
On vient de modifier notre programme et de mettre GitLab et le poste de travail au même niveau de version. 


