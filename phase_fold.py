#Planet Hunting with Python.
#Project by QMUL using Keplar spacecraft data.
#This program 'phase folds' detrended light data to produce
#a light curve representing the change of LUX as a planet transits a star.
# coding: utf-8
#Example uses: data source KIC006922244

import numpy as np
import matplotlib.pyplot as plt #this allows us to use plt

#Unpack data and create lists
dummy, x, y = np.loadtxt('KIC006922244.tbl', unpack=True, skiprows=3)

#Get user input.
#The user will have to read the graph of data and select points
#launch graph and zoom in on a section with 10 to 15 periods
#Start is the bottom of a dip, end the bottom of say 10th period along
#period is distance between these points, divided by period.
START = float(raw_input('What is the start?'))
end = float(raw_input('What is the end?'))
orbits = float(raw_input('How many periods'))
period = (end-START) / orbits
START = START - (period/2)
end = end + (period/2)

start_location = 0
end_location = 0

#New list based on chosen section of data
a, b = [], []

#This pulls out the relevant section we are looking at
#And identifies where to start and end the section.
#it's crude.
while x[start_location]<START:
   start_location +=1

while x[end_location]<end:
   end_location +=1

#This phase folds by using modulus division
#note adjustment to ensure first period is not modulated
for each in x[start_location-1:end_location-1]:
   if each < START+period:
       a.append(each-START)
       b.append(y[start_location])
       start_location +=1
   else:
       a.append((each-START)%period)
       b.append(y[start_location])
       start_location +=1


plt.plot(a,b, 'r.')
plt.show() #this draws the figures
