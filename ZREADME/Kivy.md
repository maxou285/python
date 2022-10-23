# Python
Module Kivy
1) Introduction

Le module kivy est genial car il permet d'avoir un seul code pour différents environnements par exemple le code ne change pas si on developpe une application pour ordinateur ou pour android/ios

https://www.udemy.com/course/developpeur-python-formation-complete/learn/lecture/21064596#questions

Pour en savoir plus

2) Compiler vers Android

https://www.udemy.com/course/developpeur-python-formation-complete/learn/lecture/21065218#questions

On a besoin d'une Machine Virtuelle Linux Ubuntu 


1)Virtual Box : https://www.virtualbox.org Machine virtuelle : https://bit.ly/2OMMtvu
(compte : pythondev / mot de passe: a)
1)Copier un projet
1 Créer un « Shared Folder » (cocher les 2 options « make permanent » et « auto-mount »)
2 Ouvrir un terminal et taper la commande « mount » pour voir le point de montage
3 cd /home/pythondev/Projects
4 cp -R /media/sf_XXXX . (remplacer par le nom de votre montage)
5 cd XXXX (aller dans le répertoire du projet)
6 Supprimer le dossiers inutiles
1 rm -rf venv
2 rm -rf __pycache_ deux tirets de chaque cotés
2Compiler un projet
FORMATION PYTHON
  1 2.
3 4 5.
buildozer init (commande à taper dans le répertoire du projet) gedit buildozer.spec
1 Titre
2 Package name
3 Ajouter « ttf » dans la liste des extensions (ou autres types de fichiers resources
necessaires: wav, gif...)
4 requirements = python3==3.7.5,hostpython3==3.7.5,kivy
ATTENTION: fichiers kv -> en minuscules (mv LeLab.kv lelab.kv)
ATTENTION: les gif animés posent problème -> les commenter dans le code buildozer --verbose android debug (attention il y a 2 tirets collés devant « verbose »)
Déployer sur votre téléphone Android
1 Vérifiez que le mode USB DEBUG est bien activé sur votre téléphone (options développeur)
2 Connectez votre téléphone à votre ordinateur avec un cable USB de qualité
3 Connectez le téléphone à la VM
4 buildozer --verbose android deploy
5 buildozer --verbose android run
Commande « tout en un » : buildozer --verbose android debug deploy run
