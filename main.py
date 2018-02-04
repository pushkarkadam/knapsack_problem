#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:53:27 2018

@author: pushkarkadam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from knapsack_functions import *



# Importing the dataset
dataset = pd.read_csv('knapsack.csv')

product = dataset.iloc[:,0:1].values
value = dataset.iloc[:,1:2].values
weight = dataset.iloc[:,2:3].values
knapsack_capacity = 10

items = len(product)

main_timed(knapsack(product, items, knapsack_capacity, weight, value))


#Greedy Knapsack response
data_matrix = dataset.as_matrix()
sort_by_value = data_matrix[data_matrix[:,1].argsort()]

main_timed(greedy_knapsack(sort_by_value))