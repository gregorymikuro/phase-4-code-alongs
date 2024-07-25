import numpy as np
import pandas as pd

# Random seed reproducibility
np.random.seed(8)

# Number of samples for the dataset
samples = 1000

"""
    DATA DESCRIPTION
    ----------------
    Features; x = size, bedrooms, age, bathrooms
    Target; y = price  
"""

size = np.random.normal(1500, 500, samples) # size in square feet
bedrooms = np.random.randit(1, 6, samples) # number of bedrooms
age = np.random.randit(1, 50, samples) # the age of the house
bathrooms = np.random.randit(1, 4, samples) # the number of bathrooms

# Generate the target variable
price = (size * 0.2 + bedrooms * 10 + age * -1.5 + bathrooms * 15) + np.random.normal(0, 50, samples)


