# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:24:07 2024

@author: Sharvani Yadav
"""

import pandas as pd

df = pd.read_csv("housing.csv")

print(df.columns)

x_columns = ['longitude', 
             'latitude', 
             'housing_median_age', 
             'total_rooms',
             'total_bedrooms', 
             'population', 
             'households', 
             'median_income',
             'median_house_value', 
             'ocean_proximity']

y_column = ['median_house_value']
    
x = df[x_columns] #independent variables, predictors
y = df[y_column] #outcome measure, dependent variables