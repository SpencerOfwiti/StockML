#!/bin/bash

# Windows systems
if [["$OSTYPE" == "mysys"]]; then
  # install virtualenv
  pip install --user virtualenv

  # create virtual environment
  py -m venv venv

  # activate virtual environment
  .\venv\Scripts\activate

# Unix systems
else
  # install virtualenv
  pip install --user virtualenv

  # create virtual environment
  python3 -m venv venv

  # activate virtual environment
  source venv/bin/activate

fi

# install requirements
pip install -r requirements.txt
