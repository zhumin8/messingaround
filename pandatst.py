
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


# do this before importing pylab or pyplot
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# import csv file
df=pd.read_csv('tc1sales.csv')
df['SALE.DATE']=pd.to_datetime(df['SALE.DATE'])

# do first plot and output, then clear
plot1=df.plot.scatter(x='GROSS.SQUARE.FEET', y='pricepsf');
fig1=plot1.get_figure()
fig1.savefig('test1.png')
plt.clf()


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

# do second plot and output
plot= nbhd_counts.plot(kind='barh')
fig = plot.get_figure()
fig.savefig('test.png')
plt.clf()

# aggregate values
dfsh.groupby('neighbor').aggregate(sum)
print dfsh.groupby('neighbor').median().add_prefix('median_')

# try seaborn plots
import seaborn as sns
sns.set(color_codes=True)
plot2 = sns.distplot(df['pricepsf']);
fig2 = plot2.get_figure()
fig2.savefig('sns_tst.png')
plt.clf()

plot = sns.jointplot(x="GROSS.SQUARE.FEET", y="pricepsf", data=df, kind="kde");
#fig = plot.get_figure()
plot.savefig('sns_tst2.png')
plt.clf()


plot = sns.pairplot(df[['pricepsf','story','grosqft.x','yrbuilt']]);
plot.savefig('sns_tst3.png')
plt.clf()