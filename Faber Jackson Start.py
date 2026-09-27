import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

samiDR3 = pd.read_csv('samiDR3StelKin.csv')

#Tell me how many Rows and Columns in SamiDR3
print("Number of rows then columns in samiDR3")
print(samiDR3.shape)
#prints the names of columns
print("Column names in samiDR3")
print(samiDR3.columns)

# Now we want to check how many unique catids there are
uniquecatids = samiDR3['catid'].nunique()
print("Number of unique catids in samiDR3")
print(uniquecatids)
#this has given us 3068 unique compared to 3426 in original data set therefore there is 358
#extra rows