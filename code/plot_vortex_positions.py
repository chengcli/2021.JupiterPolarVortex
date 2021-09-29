#! /usr/bin/env python3
from pylab import *

data = genfromtxt('sp161211_positions.txt')
plot(data[:,0], data[:,1::2])
show()
