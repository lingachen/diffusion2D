import numpy as np
import matplotlib.pyplot as plt

def create_plot(fig, data, timestamp, subplot_pos, vmin, vmax):
    """This is the function to create one plot for a particular time stamp.
    """
    ax = fig.add_subplot(subplot_pos)
    im = ax.imshow(data, cmap=plt.get_cmap('hot'), vmin=vmin, vmax=vmax)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(timestamp))
    return im

def output_plots(fig, im):
    """This is the function to output all the four plots as one figure.
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()