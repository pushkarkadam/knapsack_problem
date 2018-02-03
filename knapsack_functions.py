#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:36:08 2018

@author: pushkarkadam
"""
import numpy as np

# Brute force algorithm
def knapsack(product, items, knapsack_capacity, weight, value):
    best_value = 0
    best_candidate = []
    item_list = []
    power_set = np.arange(items)
    for candidate in power_set:
        if weight[candidate] <= knapsack_capacity:
            if value[candidate] > best_value:
                best_value = value[candidate]
                best_candidate.append(candidate)
    for stuffs in best_candidate:
        items_in_sack = product[stuffs,0]
        item_list.append(items_in_sack)
    return print("The best option is {}".format(item_list))