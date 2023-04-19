import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
spadl_config = {
    "length": 3.66,
    "width": 22.56,
    "origin_x": 0,
    "origin_y": 0,
}
#plt.rcParams['figure.figsize'] = [2, 6]
def _plot_rectangle(x1, y1, x2, y2, ax, color):
    ax.plot([x1, x1], [y1, y2], color=color)
    ax.plot([x2, x2], [y1, y2], color=color)
    ax.plot([x1, x2], [y1, y1], color=color)
    ax.plot([x1, x2], [y2, y2], color=color)
    ax.set_facecolor("#1fd655")
def pitch(
    ax=None,
    linecolor="green",
    fieldcolor=None,
    alpha=1,
    figsize=None,
    pitch_config=spadl_config,
    show=True,
):
    cfg = pitch_config
    # Create figure
    if ax is None:
        fig = plt.figure()
        ax = fig.gca()
    # Pitch Outline 
    x1, y1, x2, y2 = (
        cfg["origin_x"],
        cfg["origin_y"],
        cfg["origin_x"] + cfg["length"],
        cfg["origin_y"] + cfg["width"],
    )
    _plot_rectangle(x1, y1, x2, y2, ax=ax, color=linecolor)
    #lower crease rectangle
    x1 = 0.51
    x2 = 3.15
    y1 = 1.22
    y2 = 2.44
    _plot_rectangle(x1, y1, x2, y2, ax=ax, color='white')
    # upper crease rectangle
    x1 = 0.51
    x2 = 3.15
    y1 = 20.12
    y2 = 21.34
    _plot_rectangle(x1, y1, x2, y2, ax=ax, color='white')
    plt.axvline(x = 0.51, color = 'white')
    plt.axvline(x = 3.15, color = 'white')
    plt.axhline(y = 20.12, color = 'white', linestyle = '-')
    plt.axhline(y = 2.44, color = 'white', linestyle = '-')
    if show:
        plt.show()
    return ax
pitch(show=False)
url = 'Deepak Chahar.csv'
balls_xy = pd.read_csv(url)
plt.rcParams['figure.figsize'] = [2.5, 6]

ax = sns.scatterplot(balls_xy.iloc[:,0]+1.83,balls_xy.iloc[:,1], hue = balls_xy.iloc[:,2],palette='hot')

norm = plt.Normalize(balls_xy.iloc[:,2].min(), balls_xy.iloc[:,2].max())
sm = plt.cm.ScalarMappable(cmap="hot", norm=norm)
sm.set_array([])

# Remove the legend and add a colorbar
ax.get_legend().remove()
ax.figure.colorbar(sm)