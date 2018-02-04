#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:36:08 2018

@author: pushkarkadam
"""
import numpy as np
from time import time

# Function to calculate time of excuting algorithm
def main_timed(program):
    start = time()
    program
    print("Time taken for execution: {}".format(time() - start))

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
    
    list_length = np.arange(0,len(item_list))
    
    print("Solution to Knapsack Problem (Brute Force Algorithm)")
    if len(item_list) < 2:
        print("The best option is {}".format(item_list[0]))
    else:
        print("The best options are:")
        for x in list_length:
            print("{},".format(item_list[x]))
    
    return item_list

# Greedy Knapsack problem: Heuristics approach
def greedy_knapsack(sort_by_value):
    bag_weight = 0
    bag_items = []
    item_list = []
    weight = sort_by_value[:,2]
    product = sort_by_value[:,0]
    max_weight = max(weight)
    all_the_items = np.arange(0,len(sort_by_value[:,0]))
    
    for item in all_the_items:
        if max_weight <= bag_weight + weight[item]:
            bag_weight = bag_weight + weight[item]
            bag_items.append(item)
            
    for items in bag_items:
        items_in_sack = product[items]
        item_list.append(items_in_sack)
        
    list_length = np.arange(0,len(item_list))
    
    print("Solution to Greedy Knapsack Problem (Heuristic approach)")
    if len(item_list) < 2:
        print("The best option is {}".format(item_list[0]))
    else:
        print("The best options are: ")
        for x in list_length:
            print("{},".format(item_list[x]))
    return item_list