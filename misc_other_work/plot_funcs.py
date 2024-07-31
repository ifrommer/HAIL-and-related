import matplotlib.pyplot as plt
import numpy as np

x = range(9)
y = np.random.random(9)
v = [i**2 for i in x]

#plt.plot(x[:5],y[:5],'b',linewidth=1)
def plot_widening_lines(x, y, widths):
    """
    Parameters
    ----------
    x, y : array-like or scalar
            The horizontal / vertical coordinates of the data points. 
            x values are optional and default to range(len(y)).
            Commonly, these parameters are 1D arrays. (via plt.plot)

    widths : array-like or scalar
        widths of segments, same size as x and y
        e.g. width can represent altitude for an (x,y) trajectory
        or fuel consumption, etc.

    Returns
    -------
    None.

    """
    for i in range(len(x)-1):
        plt.plot(x[i:i+2],
                 y[i:i+2],'g',
                 linewidth = 
                  (widths[i]+widths[i+1])/2
                 )

plot_widening_lines(x, y, v)
#%%  Example of random (x,y)'s in the plane
x = 4*np.random.random(9)
y = np.random.random(9)
v = [i**2 for i in x]
plot_widening_lines(x, y, v)

