#
# Created on Tue Aug 31 2021
#
# Hacker: Brazil91
# Copyright (c) 2021 Brazil91
#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#
import pandas as pd
import numpy as np
import os
import csv

file_dir, _ = os.path.split(os.path.realpath(__file__))
items = os.listdir(".") # in this current directory

def find_and_replace(csv_path, search_expr: list, replace_expr: list):
    s_one, s_two, s_three = search_expr
    r_one, r_two, r_three = replace_expr
    with open(csv_path) as file:
        data = file.read().replace(s_one, r_one).replace(s_two, r_two).replace(s_three, r_three)
    with open(csv_path, 'w') as file:
        file.write(data)
        
if __name__ == '__main__':
    for file_names in items:
        if file_names.endswith(".csv"):
            csv_path = os.path.join(file_dir, file_names)
            
            search_characters = ['Bezechnung', '', '']
            replace_with = ['Bezeichnung', '', ''] 
            
            find_and_replace(csv_path, search_characters, replace_with)