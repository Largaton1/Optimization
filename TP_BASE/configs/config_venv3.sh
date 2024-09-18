#!/usr/bin/env bash

# USAGE:
#   ./configs/config_venv3.sh

python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m virtualenv .venv_3
source ./.venv_3/bin/activate
pip install "pip>=21.3.1,<21.4"
pip install -r requirements/requirements.txt
