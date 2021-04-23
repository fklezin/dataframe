#Project Description

A DataFrame is a table with named columns, each of these columns is called Series, 
A DataFrame only holds one Series for each string name, but generally can be any number of Series in a DataFrame, 
with the limitation, that each Series has to have the same number of elements.

Features and use case of a Data Frame implementation can be seen through main.py and test/ modules.

#Structure Overview:
- src/dataframe.py - DataFrame class implementation
- src/series.py - Series class implementation
- src/main.py - example
- test/ - test module
- tesh.sh - tests run command + code analysis (tested on Ubuntu18 + Python 3.8)

Author: fklezin

#Datasets used:
https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
