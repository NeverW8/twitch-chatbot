#!/bin/bash

echo 'Run during setup, ctrl +c to interupt'
sleep 5
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
