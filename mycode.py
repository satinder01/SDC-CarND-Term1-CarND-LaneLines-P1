import numpy as np
#import matplotlib.pyplot as plt

# sample data
x = np.arange(10)
y = 5*x + 10 
print(x)
print(y)
# fit with np.polyfit
m, b = np.polyfit(x, y, 1)

#plt.plot(x, y, '.')
#plt.plot(x, m*x + b, '-')
