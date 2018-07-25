"""
Simple example code for pygal, use to test installation
From http://www.pygal.org/en/latest/index.html
"""
from typing import Any, Union

import pygal
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray


def ex_pygal():
    """
    simple pygal examples
    :return:
    """
    # Saves to SVG file - http://www.pygal.org/en/stable/documentation/output.html#file
    pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4).render_to_file("pygal_test.svg")

    # Render in browser - needs packages lxml installed - http://www.pygal.org/en/stable/documentation/output.html#browser
    pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4).render_in_browser()


"""
Week 1 practice project template for Python Data Visualization
Load a county-level PNG map of the USA and draw it using matplotlib
"""


def rb(args):
    pass


def draw_USA_map(map_name):
    """
    Given the name of a PNG map of the USA (specified as a string),
    draw this map using matplotlib
    """
    # Load map image, note that using 'rb'option in open() is critical since png files are binary
    with open(map_name, "rb") as map_file:
        # pict will be a numpy array
        pict = plt.imread(map_file)
        # print("type of pict is:", type(pict))

    #  Get dimensions of USA map image, .shape is a numpy method on the array
    ypixels, xpixels, bands = pict.shape
    print("Y pixels:", ypixels, xpixels, bands)

    # Optional code to resize plot as fixed size figure -
    DPI = 80.0                  # adjust this constant to resize your plot
    xinch = xpixels / DPI
    yinch = ypixels / DPI
    plt.figure(figsize=(xinch,yinch))

    # Plot USA map
    img_map = plt.imshow(pict)

    # Plot green scatter point in center of map
    plt.scatter(x = xpixels / 2, y = ypixels / 2, s = 20, c = "Green")

    # Plot red scatter point on Houston, Tx - include code that rescale coordinates for larger PNG files
    plt.show()

    pass

def main():
    # Houston location
    USA_SVG_SIZE = [555, 352]

    # ex_pygal()
    draw_USA_map("USA_Counties_555x352.png")
    # draw_USA_map("USA_Counties_1000x634.png")

if __name__ == '__main__':
    main()