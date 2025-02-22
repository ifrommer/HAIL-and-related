### more ideas
don't forget about seaborn - I have older code using it, was very good for scatter plots I did
snippet from gallery: 
ns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(1, 8), linewidth=0,
                data=diamonds, ax=ax)

and what this shows is that using color and pt size can be helpful for displays.  how would these be used in my case?

this shows ease of use of seaborn to do lineplots - put in dataframe first
https://seaborn.pydata.org/examples/wide_data_lineplot.html

can you figure out when the cycling group is travelling at different speeds - i.e. high for a while, then gets into a 
low speed period.  and visualize this.  related - speed averages over regions - like lats, lons, boxes of lat/lons,
and not just speed, other quantities like altitude



### Looks promising
https://sustainability-gis.readthedocs.io/en/latest/lessons/L5/mobility-analytics.html
uses geopandas and movingpandas (https://movingpandas.org/ MovingPandas provides trajectory data structures and functions for handling movement data based on Pandas, GeoPandas, and HoloViz.)
**I think movingpandas could be huge**.  It has several things I was already thinking about using, like computing acceleration from the data, and it can also do direction, and way more.
back to that tutorial, see https://sustainability-gis.readthedocs.io/en/latest/lessons/L5/mobility-analytics.html#exploratory-analysis-with-space-time-cube-stc this part has nice plot to visualize how it wasn't moving for a while

take a closer look at:  https://anitagraser.com/2020/01/12/movement-data-in-gis-27-extracting-trip-origin-clusters-from-movingpandas-trajectories/

try also python noaa

### searching for python and ais might help

### 3D plot
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

#Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()

### This could be good for multiple signals over time
https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventplot_demo.html#sphx-glr-gallery-lines-bars-and-markers-eventplot-demo-py

### Maybe - varying dashing of lines
https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html#sphx-glr-gallery-lines-bars-and-markers-line-demo-dash-control-py

### main thing I see here is coloring and sizing of symbols in scatter plot
https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_masked.html#sphx-glr-gallery-lines-bars-and-markers-scatter-masked-py
plt.scatter(x, y, s=area1, marker='^', c=c)  # s is marker size, c is color (e.g. 'r' or rgb values)

# animation of graph might be cool
https://matplotlib.org/stable/gallery/animation/animate_decay.html#sphx-glr-gallery-animation-animate-decay-py

# arrows
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver





