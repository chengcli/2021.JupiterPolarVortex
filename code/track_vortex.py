#! /usr/bin/env python3
from pylab import *
from netCDF4 import Dataset
import scipy.ndimage.filters as filters

# read data
case = 'sp161211-b2'
data = Dataset('../data/%s-main.nc' % case, 'r')
x1 = data['x1'][:]
x2 = data['x2'][:]
pv = data['pv'][:,:,:,0]

# find all local maximum
it = 159
pv_max = filters.maximum_filter(pv[it,:,:], 10, mode = 'wrap')
pv_min = filters.minimum_filter(pv[it,:,:], 10, mode = 'wrap')
diff = ((pv_max - pv_min) > 1.E-8)
pv_max[diff == 0] = 0
i2, i1 = where(pv[it,:,:] == pv_max)

figure(1, figsize = (10,10))
ax = axes()
#ax.contourf(x1, x2, pv[0,:,:])
ax.imshow(pv[it,:,:])
#ax.plot(x1[i1], x2[i2], 'o')
ax.plot(i1, i2, 'ok')

show()

#savefig('sp161211_local_max.png')
