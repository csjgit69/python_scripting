"""
Course4 week one lesions and examples
"""
import random


def ex_sorting1():
    """
    Example code to sort sequences.
    """
    # Easily create a list of numbers
    data = list(range(10))
    print("range data:", data)
    # Randomly shuffle those numbers
    random.shuffle(data)
    print("shuffled data:", data)
    # Sort the list of numbers
    data.sort()
    print("sorted data:", data)
    # Shuffle it again
    random.shuffle(data)
    print("shuffled data:", data)
    # Use sorted to sort the list
    newdata = sorted(data)
    print("data after sorted:", data)
    print("returned from sorted:", newdata)
    # Convert to a tuple
    datatup = tuple(data)
    print("data tuple:", datatup)
    # Sort the tuple of numbers
    # datatup.sort() # can't sort a tuple, tuple ar none-mutable
    print("tuple after sort: (didn't call it as it will throw an error)", datatup)
    # Use sorted to sort the tuple
    newdatatup = sorted(datatup)
    print("returned from sorted (tuple now a list, sorted returns lists):", newdatatup)
    # Create a dictionary of squares (dictionary comprehension)
    datamap = {key: key ** 2 for key in datatup}
    print("data dictionary:", datamap)

    # Use sorted to sort the dictionary
    sortmap = sorted(datamap)
    print("returned from sorted (sorted returns just the keys):", sortmap)
    return 0


def square(val):
    return val ** 2

def ex_lambdas1():
    """
    Examples of creating and using anonymous functions.
    """
    # Easily create a list of numbers
    data = list(range(10))
    print("range data:", data)

    # Square all numbers in the list
    squares = list(map(square, data))
    print("squares (created by map func):", squares)

    # Double all numbers in the list
    doubles = list(map(lambda num: num * 2, data))
    print("doubles done with a lambda into map:", doubles)

    # Create a list of random numbers (list comprehension)
    randnums = [random.randrange(2, num + 3) for num in range(10)]
    print("random numbers:", randnums)

    # Create a list of tuples
    tups = list(map(lambda num1, num2: (num1, num2), data, randnums))
    print("tuples:", tups)

    # Create a list of the min values in the tuples
    mins = list(map(lambda pair: min(pair[0], pair[1]), tups))
    print("minimums:", mins)

    # Create a list only of tuples where the second item is less than the first
    newtups = list(filter(lambda pair: pair[1] < pair[0], tups))
    print("filtered:", newtups)
    return 0

def ex_sorting2():
    """
    More advanced sorting examples.
    """
    # Easily create a shuffled list of numbers
    data = list(range(10))
    random.shuffle(data)
    print("shuffled data:", data)
    # Sort the list of numbers
    data.sort()
    print("ascending sort:", data)
    data.sort(reverse=True)
    print("descending sort:", data)
    # Create a list of tuples
    datatups = [(item, random.randrange(3, 15)) for item in data]
    print("data tuples:", datatups)
    # Sort the list
    datatups.sort()
    print("sorted data tuples:", datatups)

    datatups.sort(key=lambda pair: pair[1])
    print("sorted by second item:", datatups)

    datatups.sort(key=lambda pair: pair[0] * pair[1], reverse=True)
    print("sorted by product:", datatups)

    # Shuffle it again
    random.shuffle(datatups)
    print("shuffled tuples:", datatups)

    # Use sorted to sort the list
    newdata = sorted(datatups, key=lambda pair: pair[1], reverse=True)
    print("tuples after sorted:", datatups)
    print("returned from sorted:", newdata)
    return 0

def ex_refactor1():
    """
    Converting the average daily temperatures for several planets
    from Kelvin to Farenheit --- Version 3
    """

    # Initialize temperatures for various planets
    # http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
    mercury = 440
    venus = 737
    mars = 210

    # Compute temperature in Farenheit
    def compute_celsius(temp):
        """
        Given a floaring point temperature temp in Kelvin,
        return the corresponding temperature in Celsius
        """
        return temp - 275.15

    def compute_farenheit(temp):
        """
        Given a floating point temperature temp in Kelvin,
        return the corresponding temperature in Farenheit
        """
        temp_celsius = compute_celsius(temp)
        return temp_celsius * 9 / 5 + 32

    mercury_result = compute_farenheit(mercury)
    venus_result = compute_farenheit(venus)
    mars_result = compute_farenheit(mars)

    # Print out results
    def print_temp(planet, temp):
        """
        Print out the average daily temps
        """
        print("The daily average temperature on", planet, "is", temp, "Farenheit")

    print_temp("Mercury", mercury_result)
    print_temp("Venus", venus_result)
    print_temp("Mars", mars_result)

    # Output
    ##The daily average temperature on Mercury is 328.73 Farenheit
    ##The daily average temperature on Venus is 863.33 Farenheit
    ##The daily average temperature on Mars is -85.27 Farenheit
    return 0

def main():
    """
    main program to keep test and functions clean
    :return:
    """

    # ex_sorting1()
    # ex_lambdas1()
    # ex_sorting2()
    ex_refactor1()


if __name__ == "__main__":
    main()


