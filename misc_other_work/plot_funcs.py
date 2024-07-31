import matplotlib.pyplot as plt
import numpy as np

x = range(30)
y = np.random.random(30)
v = [i for i in x]

#plt.plot(x[:5],y[:5],'b',linewidth=1)
def plot_widening_lines(x, y, widths, steps = 2):
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

    steps : int, Optional
        amount of consecutive data points to plot with the same width
        computed by averaging width over that length

    Returns
    -------
    None.
    """
    len_data = len(x)   
    slices = [slice(i, min(i + steps +1, len_data))
                  for i in range(0, len_data, steps)]    

    for slice_ in slices:
        avg_width = sum(widths[slice_])/steps
        plt.plot(x[slice_], y[slice_],'b',
                 linewidth=avg_width)
plot_widening_lines(x, y, v, 3)

#%%  Example of random (x,y)'s in the plane
x = 4*np.random.random(90)
y = np.random.random(90)
v = [i**2 for i in x]
plot_widening_lines(x, y, v, 40)



#%% old way
    # for i in range(len(x)-(steps-1)):
    #     sl = slice(i,i + steps)
    #     print(sl)
    #     plt.plot(x[sl], y[sl],'g',
    #              linewidth = 
    #               sum(widths[sl]) / steps
    #              )

