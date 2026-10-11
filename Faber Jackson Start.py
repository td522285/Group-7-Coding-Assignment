import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


gamad = pd.read_csv('InputCatGAMADR3.csv')
catclust = pd.read_csv('samiDR3InputCatClusters.csv')
stel = pd.read_csv('samiDR3StelKin.csv')
morph = pd.read_csv('samiDR3VisualMorphology.csv')

#Tell me how many Rows and Columns in stel
print("Number of rows then columns in stel")
print(stel.shape)
#prints the names of columns
print("Column names in stel")
print(stel.columns)

# Now we want to check how many unique catids there are
uniquecatids = stel['catid'].nunique()
print("Number of unique catids in stel")
print(uniquecatids)
#this has given us 3068 unique compared to 3426 in original data set therefore there is 358
#extra rows