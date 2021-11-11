#!/bin/sh
python3 -m venv local_lib 
source local_lib/bin/activate
pip install --upgrade --quiet --force-reinstall --disable-pip-version-check  --target=local_lib  git+https://github.com/jaraco/path.git --log install.log
echo "\x1b[32mPip version:\x1b[0m"; pip --version
python3 my_program.py
deactivate 