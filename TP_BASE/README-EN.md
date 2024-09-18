TUTORIAL - LINUX
================

> All the TPs are designed on a Linux OS.
> Please, use a Linux OS in order to be helped easily

Summary
-------

- [TUTORIAL - LINUX](#tutorial---linux)
  - [Summary](#summary)
  - [Workspace initialisation](#workspace-initialisation)
    - [Minimal requirements](#minimal-requirements)
    - [Workspace configuration](#workspace-configuration)
      - [Environment](#environment)
      - [Package versions](#package-versions)
      - [Auto-configuration](#auto-configuration)
    - [Workspace structure for TPs](#workspace-structure-for-tps)
  - [Course of a typical TP](#course-of-a-typical-tp)
  - [Working method suggest](#working-method-suggest)


Workspace initialisation
------------------------

### Minimal requirements

- `Python 3.8` (install from the [Python website](https://www.python.org/downloads/))
  ```python
  python>=3.8<3.9
  ```

The package
We will also need the python package manager `pip`. In a terminal :
- to see if it is installed :
    ```bash
    which pip  # return the installation path
    pip --version  # if pip is installed, return its version
    ```
- to install it :
    ```bash
    sudo apt install python3-pip
    ```

### Workspace configuration

#### Environment

For all the TPs, we will use the same working environment. The python package `venv` allows us to build an environment where we control the versions of all the packages (see [PEP405](https://www.python.org/dev/peps/pep-0405/) for more details).

#### Package versions

Nowaday, the convention for structuring a project is to indicate the minimum and maximum version of each package in `requirements*.txt` files.

You will find in the [requirements](./requirements/) folder the following files:
- [requirements.txt](./requirements/requirements.txt): the versions of all the necessary packages for all the TPs.
- [requirements-linters.txt](./requirements/requirements-linters.txt): the version of somes coding guides (called *linters*), following the current code conventions.

#### Auto-configuration

We suggest to use the following structures for all the TPs:

1. The root folder `TP_BASE` can be renammed:
   1. it contains our workspace
   2. it contains one folder by TP
2. Use the environment initialisation script:
   ```bash
   # Dans TP_BASE
   ./configs/config_venv3.sh  # minimal
   # OR
   ./configs/config_venv3_all.sh  # minimal + linters
   ```
3. Activate the environment:
    ```bash
    source ./.venv_3/bin/activate
    (.venv_3)  # your terminal now use the environment
    ```
     - you can configurate your code editors by indicating the path of python linked to this environment (*c.f.* for VSCode [docs/README_VSCODE.md](./docs/README_VSCODE.md))

### Workspace structure for TPs

```bash
TP_BASE
|
|__ .venv_3  # environment python3
|   |__ ...
|
|__ configs  # Folder containing the environment configuration
|   |__ ...
|
|__ docs  # Some documentation
|   |__ ...
|
|__ requirements  # Packages' versions
|   |__ ...
|
|__ TP0
|   |__ base_model.py  # Python skeleton for TPs
|
|__ README.md  # This README
|
|__ tox.ini  # linters configurations

```

Course of a typical TP
----------------------

1. Build a folder `TPi` fir the *i-th* TP and place it inside the `TP_BASE` folder
2. Use un program skeleton in [TP0/base_model.py](./TP0/base_model.py) to start your TP
3. Code
4. Test
   1. In a terminal:
      ```bash
      # ./TPi
      (.venv_3) python3 prog.py
      ```
   2. With your favorite code editor GUI

Working method suggest
----------------------

Use VSCode in order to use TPs conventional way of coding, help can be found in [docs/README_VSCODE.md](./docs/README_VSCODE.md) file.
