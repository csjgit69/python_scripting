"""
week for lessions/examples
"""
import math
import statistics
import functools
from functools import lru_cache
import logging
import datetime
import random

def build_quadratic_function(a, b, c):
    """Returns the formula f(x) = ax^2 + bx +c"""
    return lambda x: a*x**2 + b*x +c

def ex_lambda():
    """explain lambdas to myself"""
    print()
    print("Lambdas explaned:")
    print("f = lambda x, y: 2(x) + y")
    print("f is a var the anonymous function will be assigned to")
    print("lambda is key word to make an anonymous function")
    print("after lambda comes 0 or more variables passed into the function")
    print("after variables (or a space if there are zero) comes a : ")
    print("then a single function, the return value is the return val of the lambda")
    print("examples:")
    print()


    scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card",
                     "Douglas Adams", "H. G. Wells"]
    print("------------------------------")
    print("A list of unsorted names, use a lambda to sort by last name, pre sort:")
    print(scifi_authors)
    scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
    print("post sort:")
    print(scifi_authors)

    print(" ")
    f = build_quadratic_function(2, 3, -5)
    print(f(0)) #should be -5
    print(f(1)) #should be 0
    print(f(2)) #should be 9
    print(build_quadratic_function(3,0,1)(2)) #3x^2+1 evaluates to 2
    return 0

def area(r):
    """calc area of a circle"""
    return math.pi * (r**2)

def ex_map():
    """learning map function better"""
    print()
    print("map examples and lesion")
    print("create a set of radii and put them in a for loop to calc area:")
    radii = [2, 5, 7.1, 0.3, 10]
    areas = []
    for r_dummy in radii:
        areas.append(area(r_dummy))
    print(radii)
    print(areas)
    print("can be done in one line with map: map(area, radii) but output is a map object:")
    print(map(area, radii))
    print("this is an iterable object, but can be turned to a list easily: list(map(area, radii)):")
    print(list(map(area, radii)))
    print()

    temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27)]
    c_to_f = lambda data: (data[0], (9/5)*data[1] +32)
    print("using lambda to feed a function into map, input data is cities & temps in C:")
    print(temps)
    print("ouput is the list passed through the map, working on each tuple in the list:")
    print(list(map(c_to_f, temps)))

def ex_filter():
    """filter lessions and examples"""
    print()
    print("the FILTER function filter's OUT the data you do not want")

    print("an example with some made up fuel data:")
    data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
    avg = statistics.mean(data)
    print("made up data: ", data)
    print("average of data: ",avg)
    print()
    print("filter returns fliter object, like map:")
    print("filter on data above average: ", filter(lambda x: x > avg, data))
    print("and can be made a list also: ",list(filter(lambda x: x > avg, data)))
    print("items below the average: ",list(filter(lambda x: x < avg, data)))

    print()
    print("easty way to remove missing data:")
    countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador"]
    print("before filter: ", countries)
    print("after filter: ", list(filter(None, countries)))

def ex_reduce():
    """
    reduce function examples and lessions
    reduce not native in Python 3
    -- import functools to use it
    works by taking items in a list and operating on them:
    list [a, b, c, d, e, f]
    round 1: a, b
    round 2: ab, c
    round 3: abc, d
    etc...
    """
    data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print("use reduce to multiple first 10 prime numbers: ", data)
    multi = lambda x, y: x*y
    print("output of reduce(multi, data): ", functools.reduce(multi, data))
    print()
    product = 1
    for x in data:
        product = product * x
    print("using a for loop same result:", product)

def ex_list_comp():
    """
    lesion on list comprehensions
    list: [1, 2, 3, 'a', 'b', 'c']
    list comprehension:
        [expr for val in collection]
        [expr for val in collection if <test>]
        [expr for val in collection if <test1> and <test2>]
        [expr for val1 in colection1 and val2 in collection2]
    """
    print()
    print("LIST COMPREHENSION")
    print()
    sqrs = []
    for i in range (1, 11):
        sqrs.append(i**2)
    print("list of 1st 10 square numbers using a for loop to create it: ")
    print(sqrs)
    sqrs2 = [i**2 for i in range(1, 11)]
    print("list again using List Comp [i**2 for i in range(1, 11)]: ")
    print(sqrs2)
    print()

    remainders5 = [x**2%5 for x in range (1, 101)]
    print("list of first 100 squares mod 5 by [x**2%5 for x in range 1, 101]: ")
    print(remainders5)
    print()

    name_list = ["Stu", "Bill", "Sussy", "John", "Adam", "Buck", "Tom", "Tim", "Tonny"]
    t_names = [name for name in name_list if name.startswith("T")]
    print("orginal name list: ")
    print(name_list)
    print("Make a sub list with [name for name in names if names.startswith('T')]: ")
    print(t_names)
    print()

    name_age = [("Stu", 48), ("Bill", 52), ("Sussy", 47), ("John", 34), ("Adam", 28), ("Buck", 71), ("Tom", 51), ("Tim", 53), ("Tonny", 80)]
    under_50 = [name for (name,age) in name_age if age < 50]
    print("List of names and ages: ")
    print(name_age)
    print("to get names of people under 50 [name for (name,age) in name_age if age < 50]:")
    print(under_50)
    print()

    vec = [2, -3, 1]
    print("multiple a val across a list(vector): ")
    print(vec)
    vec4 = [4*val for val in vec]
    print("4*vec == [4*val for val in vec]: ")
    print(vec4)
    print()

    aset = [1, 3, 5, 7]
    bset = [2, 4, 6, 8]
    cartesian_product = [(a, b) for a in aset for b in bset]
    print("join two sets (cartesian product): ", aset, bset)
    print("with [(a, b) for a in aset for b in bset]: ")
    print(cartesian_product)

def ex_sets():
    """
    some examples of things you can do with sets in Python3
    """
    odds = set([1,3,5,7,9])
    evens = set([2,4,6,8,10])
    primes = set([2,3,5,7])
    composites = set([4,6,8,10])
    print()
    print("odds:       ", odds)
    print("evens:      ", evens)
    print("primes:     ", primes)
    print("composites: ", composites)
    print("odds.union(evens): ", odds.union(evens))
    print("odds.intersection(primes): ", odds.intersection(primes))
    print("primes.intersection(evens): ", primes.intersection(evens))
    print("primes.union(composites): ", primes.union(composites))
    print("2 in primes: ", 2 in primes)
    print("6 in odds: ", 6 in odds)
    print("9 not in evens: ", 9 not in evens)
    print("dir(primes):\n",dir(primes))

def ex_logging():
    """
    examples of Python logging module
    :return:
    """
    # create and configure logger
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "test_log.log",
                        level = logging.DEBUG,
                        format = LOG_FORMAT,
                        filemode='w')                       # overwrite log file
    logger = logging.getLogger()

    #create a log
    logger.debug("test debug message.")
    logger.info("test info message.")
    logger.warning("test warning message.")
    logger.critical("test critical message.")

    print(logger.level)

@lru_cache(maxsize=1000)
def fibonacci(n):
    '''
    @lru_cache (from functools) builds a cache of [maxsize] of the last recent used inputs to this function
    and returns the results for that input if it is in the cache without processing the function
    trades memory for compute.
    In this case it is very worth it.
    '''
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

def ex_recursion():
    """
    Recursion, Fibonacci Sequence and Memoirztion
    :return:
    """

    print("1-101 fib numbers with recursion alone (super slow): ")
    for num in range (101):
        print(num, ":", fibonacci(num))


def main():

    # ex_lambda()
    # ex_map()
    # ex_filter()
    # ex_reduce()
    # ex_list_comp()
    # ex_sets()
    # ex_logging()
    ex_recursion()

if __name__ == "__main__":
    main()


