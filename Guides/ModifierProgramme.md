# Modifier mon programme
Quand on veut modifier son programme on doit effectuer les actions suivantes :
1. S'assurer que la branche `Master en local` est égale à la branche `Master sur GitLab`
2. Créer une nouvelle branche de développement
3. Effectuer les nouveaux développements
4. Vérifier que le programme fonctionne bien
5. Valider les changements (Stage + Commit) 
6. Pousser la branche de développement sur GitLab
7. Merger la branche de développement avec la branche Master et supprimer la branche de développement sur GitLab
8. Synchroniser la branche Master locale avec la branche Master GitLab

## S'assurer que la branche `Master en local` est égale à la branche `Master sur GitLab`
Si ce n'est pas le cas, il faut :
- Dans VSC, cliquer sur l'icône `GitLens` (cercle avec embranchement)
- Activer la branche `Master` (Checkout)
- Cliquer sur l'icône `flêche vers le bas` (Pull Repositories)
- Supprimer les branches qui ne sont pas utiles s'il y en a

## Créer une nouvelle branche de développement
On a déjà vu comment il faut fairen, mais je le rappelle ici : 
1. Dans VSC, cliquer sur l'icône `GitLens` (un rond dans lequel on voit une espèce d'embranchement)
2. Click droit sur la branche `Master` puis `Create branch (via Terminal)`
3. Donner un nom à la branche : `mon-debut-de-code`
4. La ligne de commande est générée, il faut appuyer sur la touche `Enter` pour valider
5. La branche nouvellement créée est apparue, il faut l'activer. Pour cela, click droit sur `mon-debut-de-code` puis clicker sur`Checkout`

## Effectuer les nouveaux développements
On va ajouter un 'Bonjour Valentin" au programme :
1. Dans VSC, cliquer sur l'icône `Explorer` (fichier l'un sur l'autre)
2. Ouvrir hello.py et ajouter l'instruction Print. Le résultat est comme suit normalement : 
```shell
#! /usr/bin/python3

print("Salut Maxime")
print("Bonjour Valentin")
```
## Vérifier que le programme fonctionne bien
1. Dans VSC, cliquer sur l'icône `Explorer`
2. Click droit sur le fichier 'hello.py' et cliquer sur `Run Python File in Terminal`

On doit voir les 2 messages s'afficher comme il faut. 

## Valider les changements (Stage + Commit) 
Fastoche :
1. 


