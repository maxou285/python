Bienvenue dans ce tuto pour passer d'une application kivy à un executable et meme une application qui apparait dans le dock sur mac


# Sommaire
- 1) Installation de Pyinstaller
- 2) Créer le fichier .spec
- 3) Configurer le fichier .spec
- 4) Compiler les fichiers
- 5) Liens utiles
- 6) Problemes avec le son les fonts et les images
- 7) Exemple de fichier .spec 



# 1) Installation de Pyinstaller

Pyinstaller est le module qui va permettre la compilation d'un fichier python(.py)
On l'installe avec pip
    pip install Pyinstaller



# 2) Créer le fichier .spec

Avant de compiler notre application nous allons devoir configurer les paramètres de la compilation
- L'icone de l'application
- Importer les fichiers externes(png, kv, wav...)
...
Un fichier .spec est donc un fichier de specifications 
Pour créer un fichier .spec nous devons executer la commande suivante dans le terminal dans le repertoire de notre application

pyi-makespec -—noconsole --onefile --icon=icon.ico main.py

Ici on demande à pyinstaller de créer un fichier spec à partir du fichier principal
de notre application(ici main.py) puis on passe deux paramètres

ATTENTION: en copiant les commandes les -- ne vont pas etre bien reproduis donc il faut les retaper sinon on aura une erreur commande/paramètre non reconnu

- --noconsole => Pour éviter qu'une console de terminal ne s'affiche au lancement de l'application 
- --onefile => pour indiquer à pyinstaller qu'il doit tout compiler en un seul fichier executable
- --icon=icon.ico => Pour indiquer le fichier .ico qui servira d'icon à l'application



# 3) Configurer le fichier .spec

Après avoir créer le fichier de specifications de notre application il va falloit l'éditer
ATTENTION: Dans un fichier .spec les syntaxes sont particulières

# Importer les fichiers externes(png, wav, kv...)
Pour importer des fichiers externes on doit les ajouter dans la liste des datas dans le fichier .spec

On ajoute les élements dans un tuple avec en premier paramètre le type de fichier ou le fichier lui meme
et en second paramètre le chemin('.'si on réalise les commandes dans le repertoire de l'application)
    
    datas=[('*.kv', '.'),('ding.wav', '.'), ('ChunkFivePrint.otf', '.'), ('icon.png','.')],

Ici on import donc tous les fichiers .kv ainsi qu'un fichier ding.wav , un fichier de font ChunkFivePrint.otf et un fichier .png

# Les hidden_imports
Les hidden_imports ce sont tous les imports indirects pyinstaller ne peut âs les lire directement et dnoc ne les import pas automatiquement
    hiddenimports=["kivymd.icon_definitions"],
Ici on ajoute l'import icon_definitions situé dans la librairie kivymd

# Specifications Speciales avec KivyMd
Si vous utilisez KivyMd vous devrez spécifié 
    hookspath=[kivymd_hooks_path],
    et avoir import kivymd_hooks_path auparavant
    from kivymd import hooks_path as kivymd_hooks_path



# Ajouter l'icone de l'application

Dans la catégorie app BUNDLE du fichier .spec vous devez simplement spécifier un fichier .ico importé auparavant dans les datas
    icon='icon.ico',
    et 
    icon=['icon.ico'],
    dans la catégorie exe du fichier .spec
L'autre solution est de spécifier l'icone au moment de la création du .spec en rajoutant un paramètre
    pyi-makespec -—noconsole --onefile --icon=icon.ico main.py



# 4) Compiler les fichiers

Une fois que toutes les spécifications sont enregistrées il ne reste plus qu'a lancer la compilation avec pyinstaller
Pour cela rien de plus simple ! 
On rentre juste la commande 
    pyinstaller main.spec dans le terminal dans le repertoire de l'application



# 5) Liens Utiles

Add datas dans le .spec: https://stackoverflow.com/questions/68905407/black-screen-for-kivy-based-windows-exe-generated-using-pyinstaller
Problemes de son: https://stackoverflow.com/questions/64213325/python-error-audiofileopen-failed-wht-play-audio-file-on-pong-game
KivyMD hook: https://stackoverflow.com/questions/43741763/import-error-using-kivymd-and-pyinstaller
Trouver une icone pour son app: https://icon-icons.com/download/192276/PNG/512/
Modifier l'icone: https://stackoverflow.com/questions/40666323/how-to-change-the-icon-on-the-window-when-i-run-my-program-in-kivy




# 6) Problemes son, fonts et images

Si votre application n'arrive pas à demarrer lancez la avec le fichier console pour voir l'erreur
Si l'erreur indique fichier_font.otf not found par exemple vérifiez bien que vous importez le fichier dans le fichier .spec
Si l'importation réussi mais que le fichier n'est pas trouver c'est certainement car vous utilisez un relative path pour charger votre fichier
Dans ce cas il faut utilisez un absolute path dans le fichier .py 
Dans le fichier .py:
    - Obtenir le repertoire courant:
        dir_path = os.path.dirname(os.path.realpath(__file__)) 
    - Indiquer dans une variable le chemin absolu pour trouver votre fichier wav, otf, png etc
        dingfile = os.path.join(dir_path, "ding.wav")
        iconfile = os.path.join(dir_path, "icon.png")
        fontfile = os.path.join(dir_path, "ChunkFivePrint.otf")
    - A l'utilisation d'un fichier son par exemple on donne dingfile qui a été défini plus tot
        os.system('afplay "{}"'.format(dingfile))

ATTENTION: Pour les fonts avec kivy
Plutot que d'utilisez les markup de kivy il faut utiliser la propriété font_name: "font_file"
On aura défini plus tot dans le fichier .py à quoi correspon fichier_de_font:
    from kivy.core.text import LabelBase
    fontfile = os.path.join(dir_path, "ChunkFivePrint.otf")
    LabelBase.register(name="myfont", fn_regular=fontfile)



# 7) Exemple de fichier .spec

    # -*- mode: python ; coding: utf-8 -*-

    from kivymd import hooks_path as kivymd_hooks_path
    block_cipher = None


    a = Analysis(
        ['client.py'],
        pathex=[],
        binaries=[],
        datas=[('*.kv', '.'),('ding.wav', '.'), ('ChunkFivePrint.otf', '.'), ('icon.png','.')],
        hiddenimports=["kivymd.icon_definitions"],
        hookspath=[kivymd_hooks_path],
        hooksconfig={},
        runtime_hooks=[],
        excludes=[],
        win_no_prefer_redirects=False,
        win_private_assemblies=False,
        cipher=block_cipher,
        noarchive=False,
    )
    pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name='client',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=['icon.ico'],
    )
    app = BUNDLE(
        exe,
        name='client.app',
        icon='icon.ico',
        bundle_identifier=None,
    )
