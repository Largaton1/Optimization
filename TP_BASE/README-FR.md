TUTORIEL - LINUX
================

> All the TPs are designed on a Linux OS.
> Please, use a Linux OS in order to be helped easily

Sommaire
--------

- [TUTORIEL - LINUX](#tutoriel---linux)
  - [Sommaire](#sommaire)
  - [Initialisation environnement de travail](#initialisation-environnement-de-travail)
    - [Minimal requis](#minimal-requis)
    - [Configuration de l'environnement de travail](#configuration-de-lenvironnement-de-travail)
      - [Environnement](#environnement)
      - [Versions de packages](#versions-de-packages)
      - [Configuration automatique](#configuration-automatique)
    - [Résumé de la structure du projet pour les TPs](#r%C3%A9sum%C3%A9-de-la-structure-du-projet-pour-les-tps)
  - [Déroulement classique d'un TP](#d%C3%A9roulement-classique-dun-tp)
  - [Méthode de travail suggérée](#m%C3%A9thode-de-travail-sugg%C3%A9r%C3%A9e)


Initialisation environnement de travail
-------------------------------------

### Minimal requis

- `Python 3.8` (via le [site web de Python](https://www.python.org/downloads/))
  ```python
  python>=3.8<3.9
  ```

Il nous faudra également le gestionnaire de package python `pip`. Dans un terminal :
- pour savoir s'il est installé :
    ```bash
    which pip  # renvoie le chemin de l'installation
    pip --version  # si pip installé, renvoie le détail de la version
    ```
- pour l'installer :
    ```bash
    sudo apt install python3-pip
    ```

### Configuration de l'environnement de travail

#### Environnement

Pour tous les TPs, nous utiliserons un même environnement de travail. Le package python `venv` nous permet de construire un environnement où l'on controle toutes les versions de chaque package (*c.f.* [PEP405](https://www.python.org/dev/peps/pep-0405/) pour plus de détails).

#### Versions de packages

La convention de structure d'un projet nous invite aujourd'hui à indiquer la version minimale et maximale de chaque package dans des fichiers `requirements*.txt`

Vous trouverez dans le dossier [requirements](./requirements/) les fichiers suivants :
- [requirements.txt](./requirements/requirements.txt) : la version des packages necesaires pour faire tous les TPs
- [requirements-linters.txt](./requirements/requirements-linters.txt) : la version de quelques guides de codage (*linters*), en accord avec des conventions de codes admises jusqu'ici.

#### Configuration automatique

Nous vous suggérons une structure de fichiers pour les TPS :

1. Le dossier racine `TP_BASE` peut être renommé
   1. il contiendra notre environnement de travail
   2. il contiendra un dossier par TP
2. Utilisez le script d'initialisation d'environnement
   ```bash
   # Dans TP_BASE
   ./configs/config_venv3.sh  # minimum
   # OU
   ./configs/config_venv3_all.sh  # minimum + linters
   ```
3. Activation de l'environnement
    ```bash
    source ./.venv_3/bin/activate
    (.venv_3)  # le terminal utilise maintenant l'environnement
    ```
      - vous pouvez configurer vos éditeurs de codes en leur indiquant le chemin de python lié à cet environnement (*c.f.* pour VSCode [docs/README_VSCODE.md](./docs/README_VSCODE.md))

### Résumé de la structure du projet pour les TPs

```bash
TP_BASE
|
|__ .venv_3  # environnement python3
|   |__ ...
|
|__ configs  # Dossier de configs environnement
|   |__ ...
|
|__ docs  # Some documentation
|   |__ ...
|
|__ requirements  # Versions des packages
|   |__ ...
|
|__ TP0
|   |__ base_model.py  # Python skeleton for TPs
|
|__ README.md  # This README
|
|__ tox.ini  # linters configurations

```

Déroulement classique d'un TP
-----------------------------

1. Créer un dossier `TPi` pour le *i-ème* TP et se placer à l'intérieur
2. Utiliser le programme squelette dans [TP0/base_model.py](./TP0/base_model.py) pour démarrer votre TP
3. Codez
4. Testez
   1. dans un terminal
      ```bash
      # ./TPi
      (.venv_3) python3 prog.py
      ```
   2. autrement avec votre éditeur de code GUI préféré


Méthode de travail suggérée
---------------------------

Nous vous suggérons d'utiliser l'éditeur de texte VSCode pour être en accord avec les conventions utilisées dans les corrections de TPs. Une aide peut être trouvée dans le fichier [docs/README_VSCODE.md](./docs/README_VSCODE.md).
