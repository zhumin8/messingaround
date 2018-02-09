
# This is a test file to try on on data wrangling techniques with pandas

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# df=pd.read_csv('tc1salesxys.csv')
#
# df.plot.hexbin(x='xcoord', y='ycoord', gridsize=25)
#
#
# df.plot.scatter(x='xcoord', y='ycoord', s=df['SALE.PRICE']/50000);
# df['YEAR.BUILT'].diff().hist()


import pandas as pd
import matplotlib.pyplot as plt

# import csv file
df=pd.read_csv('tc1sales.csv')

# cat var count of each category
zones_counts = df['zone1'].value_counts()
print zones_counts

# cut cols from original df
dfsh=df[['neighbor','pricepsf','grosqft.x']]

# another way to show category counts
nbhd_counts=dfsh.groupby('neighbor').size()
print nbhd_counts

# change index: label nbhd names
nbhd_counts.index = ['asto','coro','elmh','JH','LIC']
print nbhd_counts
# nbhd_counts.plot(kind='bar')

# aggregate values
dfsh.groupby('neighbor').aggregate(sum)
print dfsh.groupby('neighbor').median().add_prefix('median_')

