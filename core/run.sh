#!  /bin/bash

make

python3 grab.py

./generate.sh top_module

make clean
