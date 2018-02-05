import geopandas as gpd
import numpy
import pylab

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

print worldx.head()
print world.crs
print 'word plot'
#print world.plot()
print 'oh... coming..'
world.plot()
pylab.show()
print 'i am done'