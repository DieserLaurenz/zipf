# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:59:26 2023

@author: laure
"""
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.max_columns', 20)
    df = pd.read_csv("mcdonalds_menu.csv")
    
    # count the number of items in each category
    category_counts = df['Category'].value_counts()
    
    # create a bar plot of the category counts
    plt.figure(figsize=(20, 10))
    plt.bar(category_counts.index, category_counts.values)
    
    # set the labels and title of the plot
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Number of Items in each Category')
    
    # show the plot
    plt.show()