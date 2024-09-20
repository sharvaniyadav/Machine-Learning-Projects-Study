# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 08:52:03 2024

@author: Sharvani Yadav
"""

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Create a line plot
plt.plot(x, y)

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')

# Show the plot
plt.show()