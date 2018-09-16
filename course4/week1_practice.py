"""
Simple example code for pygal, use to test installation
From http://www.pygal.org/en/latest/index.html
"""
from typing import Any, Union

import pygal
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray
import webbrowser

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

def c_test_alg(test_val):
    odd_list = [0,1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41]
    start = -1 * (test_val**2)
    print("Start: ", start, " 0^0", 0**0)
    last_val = start
    ans  = []
    ans.append(last_val)
    for cnt in range(1, test_val*3):
        last_val = (last_val + (cnt*2))-1 #odd_list[cnt]
        print("cnt: ", cnt, "val: ", last_val)
        ans.append(last_val)
    print(ans)

def c_lession():
    x = 2
    y = x * 3
    z = y/2
    x = (2+z)%2
    print("x: ",x," y: ",y," z: ",z )
    x = 5 * 2
    y = (x + 1) % 3
    print(y - x)

def c_lession_g (x, y):
    x = x + y
    z = 2 * x - y
    print(z)

def f(x, y):
    if (x + 2 < y):
        x = x + 3
        return y * x
    else:
        return x + y + 2

def f_while(x, y):
    while(x < y):
        print("val:", y - x)
        x = x + 1
        y = y - 1

def f_loops1 (n):
    ans = 0
    for i in range(n): # (int i = 1; i < n; i++):
        if (i < int(n/2)):
            ans = ans - i
        else:
            ans = ans + i
    return ans

def g_loops (x, n):
    for i in range(n): #(int i = 0; i < n; i++):
        if (i % 2 == 0):
            x *= i + 1
            continue
        x = x - 1
        if (x == 0):
            break
    return x

def c_quiz ():
    a = 3
    b = 6
    while (a <= b):
        if (a % 2 == 1):
            print("a is ", a)
        else:
            print("b is ", b)
            i = 0
            while (i < (b - a)):
                # for (int i = 0; i < b - a ; i++)
                print("a * i + b = ", a * i + b)
                i += 1
        a += 1
        b -= 1
    return


def c_anotherFunction(a, b):
    answer = 42
    x = 0
    print("In anotherFunction(",a,",",b,")")
    while (b > a):
        print("a is ",a,", b is ",b)
        answer = answer + (b - a)
        b -= x
        a += x / 2
        x += 1
    return answer

def c_someFunction(x, y):
  a = x + y
  if (x < y):
    i = 0
    while (i < x):
    #for (int i = 0; i < x; i++) {
        print("In the loop with i = ",i,", a = ",a)
        a = a + x
        i += 1
  else:
    y = anotherFunction(y,a+4)
  return a * y


def main():
    # Houston location
    USA_SVG_SIZE = [555, 352]

    # ex_pygal()
    # draw_USA_map("USA_Counties_555x352.png")
    # draw_USA_map("USA_Counties_1000x634.png")
    # webbrowser.open_new("http://yahoo.com")
    # c_test_alg(5)
    # c_lession()

    # c_lession_g(3, -10)
    # x = -1
    # y = 3
    # x = x + y
    # print(x - y)
    # print((-1 * -2) == (14 % 4))
    # x = 6
    # print((-3 < 5) and not (x % 3 == 0))
    # print("function: ", f(5,7))
    # print("c_while: ", f_while(-1, 4))
    # print("c_loops1: ", f_loops1(7))
    # print("g_loops1: ", g_loops(1,3))
    # c_quiz()

    print()
    print("***********")
    print()

    x = 2
    a = c_someFunction(x,3)
    print("a = ",a)
    print("x = ",x)

if __name__ == '__main__':
    main()