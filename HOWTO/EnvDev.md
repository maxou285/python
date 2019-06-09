# Environnement de développement
C'est l'environnement qui permet de développer efficacement et qui inclut : 
- le langage de développement : Python
- l'IDE (integrated development environment) est l'outil dans lequel on développe, on débugge, et on synchronise avec le gestionnaire de codes sources (git) : Visual Studio Code (VSC)
- le gestionnaire de code source : Git

Il faut installer ces 3 outils sur votre poste de travail en fonction de son OS. Pour git, nous avons créé un compte sur gitlab et créé une clef pour s'authentifier et se connecter simplement.

## Git
Lien utile pour créer sa clef sur git : <https://gitlab.com/help/ssh/README#generating-a-new-ssh-key-pair>

Ne pas oublier aussi de créer ses variables globales avec les commandes suivantes :
```shell
git config --global user.name "My Name"
git config --global user.email my@email.com
```

## VSC (Visual Studio Code)
Il est conseillé d'installer les extensions suivantes :
- GitLens
- markdownlint
- Git History
- Python