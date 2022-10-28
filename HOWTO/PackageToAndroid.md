Bienvenue dans ce tuto pour compiler et déployer une app kivy sur android

# Sommaire 
- 1)  Installation
- 2) Copier un projet
- 3) Compiler un projet
- 4) Déployer sur un téléphone android
- 5) Bugs recurrents

# 1) Installation
Pour réaliser ce projet vous aurez besoin d'une machine virtuelle linux ubuntu 
Il faut donc installer Virtual Box : https://www.virtualbox.org
=> Un environnement déja pret peut etre téléchargé via ce lien  https://bit.ly/2OMMtvu (VM Ubuntu 18 déja configuré/compte = pythondev / mot de passe: a)

# 2) Copier un projet 

1. Créer un « Shared Folder » (cocher les 2 options « make permanent » et « auto-mount »)
2. Ouvrir un terminal et taper la commande « mount » pour voir le point de montage
3. cd /home/pythondev/Projects
4. cp -R /media/sf_XXXX . (remplacer par le nom de votre montage)
5. cd XXXX (aller dans le répertoire du projet)
6. Supprimer le dossiers inutiles
    1. rm -rf venv
    2. rm -rf __pycache__

# 3) Compiler un projet

1. buildozer init (commande à taper dans le répertoire du projet) 
2. gedit buildozer.spec
    1. Titre
    2. Package name
    3. Ajouter « ttf » dans la liste des extensions (ou autres types de fichiers resources
    necessaires: wav, gif...)
    4. requirements = python3==3.7.5,hostpython3==3.7.5,kivy
4. ATTENTION: fichiers kv -> en minuscules (mv LeLab.kv lelab.kv)
5. ATTENTION: les gif animés posent problème -> les commenter dans le code buildozer --verbose android debug (attention il y a 2 tirets collés devant « verbose »)

Notez qu'il faut dans requirements spécifier tous les modules utilisés et il est préférable de spécifier la version de python à utiliser

# 4) Déployer sur votre téléphone Android
1. Vérifiez que le mode USB DEBUG est bien activé sur votre téléphone (options développeur)
2. Connectez votre téléphone à votre ordinateur avec un cable USB de qualité
3. Connectez le téléphone à la VM
4. buildozer --verbose android deploy
5. buildozer --verbose android run
Commande « tout en un » : buildozer --verbose android debug deploy run

ATTENTION: Il peut arriver que l'ordinateur ou la VM ne reconnaise pas le telephone dans ce cas il va nous falloir trouver un autre moyen de récupérer le fichier .apk
Sur la VM
1. Copier coller le fichier .apk dans le repertoire partagé entre l'ordinateur et la VM de cette manière on récupère le fichier .apk sur notre ordinateur
2. S'envoyer le fichier .apk par gmail sous forme de lien google drive pour éviter les refus d'ouverture à l'arrivée
3. Depuis un téléphone télécharger le fichier .apk et l'ouvrir en ayant éctivé l'option ouvrir les apps téléchargées depuis internet


# 5) Bugs récurrents
ATTENTION la VM téléchargeable est presque déja entièrement configurée cependant j'ai rencontré certain bugs lorsque j'ai moi mème essayé de compiler un projet
1) Lors de la commande buildozer --verbose android debug vous pourriez avoir un bug au début de la compilation 
    ...
    ValueError: read of closed file
Pour régler ce problème vous devez désinstaller et réinstaller buildozer à l'aide des commandes suivantes:
-Clear old buildozer files
```$rm -rf .buildozer```
-Uninstall latest version
```$pip uninstall buildozer cython```
-Install old stable version
```$pip install buildozer, cython```
-Initialize buildozer and sdk
```$buildozer init && buildozer android adb -- version```

2) Lors de la commande buildozer --verbose android debug vous pourriez avoir un autre bug vers la fin de la compilation 
```[WARNING]: ERROR: /home/pythondev/Projects/openweather/sf_OpenWeather/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists/mymeteoapp/gradlew failed! ... Puis il y aura un grand message rouge```

Ce problème est en fait du à un problème d'update de la VM car gradle, un module nécessaire lors de la compilation a besoin de java 11 pour fonctionner or la Machine virtuelle est en java 1.8 
Taper donc 
```sudo apt-get install openjdk-11-jdk```
Pour installer java 11 et la compilation devrait se dérouler sans problèmes
