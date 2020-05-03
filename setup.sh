#!/bin/bash

# install virtualenv
pip3 install virtualenv

# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install requirements
pip3 install -r requirements.txt
