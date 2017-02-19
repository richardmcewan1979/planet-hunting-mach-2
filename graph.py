#KIC006922244 detrended star luminosity data
#LUX over TIME
import numpy as np
import matplotlib.pyplot as plt #this allows us to use plt

dummy, x, y = np.loadtxt('KIC006922244.tbl', unpack=True, skiprows=3)

plt.plot(x,y, 'r.')
plt.show() #this draws the figures
