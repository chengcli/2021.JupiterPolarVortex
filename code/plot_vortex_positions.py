#! /usr/bin/env python3
from pylab import *

case = 'sp161211-b2'
data = genfromtxt('%s_positions.txt' % case)
plot(data[:,0], data[:,1::2])
savefig('%s_positions.png' % case)
