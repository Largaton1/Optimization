VSCODE HELP
===========

- [VSCODE HELP](#vscode-help)
  - [I. Introduction](#i-introduction)
  - [II. Configuration](#ii-configuration)
  - [III. About TPs](#iii-about-tps)

I. Introduction
---------------

**VSCode** is a *Microsoft* code editor maintained by an open-source community. You can custom VSCode with extensions.

II. Configuration
-----------------

VSCode and all its extensions can be customized.

Default settings can be changed globally for the user and locally for the *workspace* (root opened folder).

Settings and their values are in `JSON` file, and in workspace you can find them in [.vscode/settings.json](../.vscode/settings.json) file.

III. About TPs
--------------

1. Install Microsoft extension `Python` in **VSCode**

> You can find in folder `TP_BASE` an already existing [.vscode/settings.json](../.vscode/settings.json) file. It was obtained following the next steps:

2. Create at the root directory `TP_BASE` (or renamed) a file (and the parent directory) `.vscode/settings.json`
3. Put the default python version you will use `python3` from the environment `.venv_3`:
    ```json
    {
        "python.defaultInterpreterPath": ".venv_3/bin/python3",
    }
    ```
4. If you have configure the complete environment (with *linters*), write in `.vscode/settings.json`:
    ```json
    {
        // Others configs ...
        // ...
        "python.analysis.diagnosticSeverityOverrides": {
            "reportUndefinedVariable": "none"
        },
        "python.linting.flake8CategorySeverity.F": "Warning",
        "python.linting.flake8Args": [
            "--config=tox.ini"
        ],
        "python.linting.flake8Enabled": true,
        "python.linting.pylintEnabled": true,
        "python.linting.pylintArgs": [
            "--rcfile=tox.ini"
        ],
        "python.linting.pylintCategorySeverity.refactor": "Information",
        "python.linting.pylintUseMinimalCheckers": false,
    }
    ```

