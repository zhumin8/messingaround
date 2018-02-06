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


# The usual preamble
import pandas as pd


df=pd.read_csv('tc1salesxys.csv')

zones_counts = df['zone1'].value_counts()