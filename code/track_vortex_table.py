#! /usr/bin/env python3
from pylab import *
from netCDF4 import Dataset
import scipy.ndimage.filters as filters

def order_position(x2, x1, p2, p1):
    num, y1, y2 = len(x2), [], []
    for i in range(num):
        dmin = 1E10
        for j in range(num):
            d2 = (x2[i]-p2[j])**2 + (x1[i]-p1[j])**2
            if d2 < dmin:
                n2, n1 = x2[i], x1[i]
                dmin = d2
        y2.append(n2)
        y1.append(n1)
    return array(y2), array(y1)

# read data
case = 'sp161211'
data = Dataset('../data/%s-b1-main.nc' % case, 'r')
time = data['time'][:]
x1 = data['x1'][:]
x2 = data['x2'][:]
pv = data['pv'][:,:,:,0]
num = 6

# find all local maximum
with open('%s_positions.txt' % case, 'w') as file:
    file.write('# SP Vortex Positions:\n')
    file.write('#%8s%10s%10s' % ('TIME', 'X0', 'Y0'))
    file.write('%10s%10s' % ('X1', 'Y1'))
    file.write('%10s%10s' % ('X2', 'Y2'))
    file.write('%10s%10s' % ('X3', 'Y3'))
    file.write('%10s%10s' % ('X4', 'Y4'))
    file.write('%10s%10s\n' % ('X5', 'Y5'))
    for it in range(len(pv)):
        pv_max = filters.maximum_filter(pv[it,:,:], 10, mode = 'wrap')
        pv_min = filters.minimum_filter(pv[it,:,:], 10, mode = 'wrap')
        diff = ((pv_max - pv_min) > 1.E-10)
        pv_max[diff == 0] = 0
        i2, i1 = where(pv[it,:,:] == pv_max)
        print(it, i2)
        assert(len(i2) == num)
        if it > 0:
            i2, i1 = order_position(i2, i1, p2, p1)
        file.write('%9.4g' % time[it])
        for j in range(num):
            file.write('%10.3g%10.3g' % (x2[i2[j]], x1[i1[j]]))
        file.write('\n')
        p2, p1 = i2, i1
