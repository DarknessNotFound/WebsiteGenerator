#! /bin/bash

rm testing.html
touch tmp.txt
python3 htmlGeneration.py < input.txt > tmp.txt
rm tmp.txt