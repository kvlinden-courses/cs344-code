"""
Graphs two simple functions using matplotlib:
   f(x) = maximum/2 - abs(maximum/2 - x)
   f(x) = abs(x * sin(x)) 

@author: kvlinden
@version 6feb2013
"""

from matplotlib.pyplot import plot, show
from numpy.core.numeric import arange
from numpy.ma.core import sin

maximum = 30
x = arange(0.0, maximum, 0.01)
plot(x, maximum / 2 - abs(maximum / 2 - x))
plot(x, abs(x * sin(x)))
show()
