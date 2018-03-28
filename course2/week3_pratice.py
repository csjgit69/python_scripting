"""
Course2 week one pratice
"""

import datetime
import random

def p_1():
    """
    Template - Update an item in a list
    Output
    [2, 3, 5, 7, 11, 13]
    [2, 3, 0, 7, 11, 13]
    """

    example_list = [2, 3, 5, 7, 11, 13]
    print(example_list)

    example_list[2] = 0
    print(example_list)
    return 0

def p_2():
    """
    Template - Update a slice of a list
    Output
    [2, 3, 5, 7, 11, 13]
    [2, 0, 0, 0, 7, 11, 13]
    """

    example_list = [2, 3, 5, 7, 11, 13]
    print(example_list)
    example_list[1:3] = [0,0,0]
    print(example_list)
    return 0

def p_3():
    """
    Template - Append an item to a list
    Output
    [2, 3, 5, 7, 11, 13]
    [2, 3, 5, 7, 11, 13, 0]
    """

    example_list = [2, 3, 5, 7, 11, 13]
    print(example_list)
    example_list.append(0)
    print(example_list)
    return 0

def p_4():
    """
    Template - Extend a list with another list
    Output
    [2, 3, 5, 7, 11, 13]
    [2, 3, 5, 7, 11, 13, 0, 0, 0]
    """

    example_list = [2, 3, 5, 7, 11, 13]
    print(example_list)
    example_list.extend([0,0,0])
    print(example_list)
    return 0

def p_5():
    """
    Template - Concatenate one list onto another
    Output
    [2, 3, 5, 7, 11, 13]
    [2, 3, 5, 7, 11, 13]
    [2, 3, 5, 7, 11, 13, 0, 0, 0]
    """
    example_list = [2, 3, 5, 7, 11, 13]
    print(example_list)
    new_list = list(example_list) + [0,0,0]
    print(example_list)
    print(new_list)
    return 0

def mut_list(in_list, item):
    """
    add item to in_list
    """
    in_list.append(item)
    return 0

def p_6():
    """
    Template - Append several item to a list
    # Output
    #[2, 3, 5, 7, 11, 13]
    #[2, 3, 5, 7, 11, 13, 0, 0, 0]
    """
    example_list = [2, 3, 5, 7, 11, 13]
    print(example_list)
    for n in range(3):
        mut_list(example_list, 0)
    print(example_list)

    for number in [0, 0, 0]:
        example_list.append(number)
    print(example_list)
    return 0

def p_7():
    """
    Template - Convert a list to a tuple
    Output
    [2, 3, 5, 7, 11, 13]
    (2, 3, 5, 7, 11, 13)
    """
    example_list = [2, 3, 5, 7, 11, 13]
    print(example_list)
    example_tuple = tuple(example_list)
    print(example_tuple)
    return 0

def p_8():
    """
    Template - Shuffle the items in a list
    # Output - note that order of second list may vary due to randomness
    #[2, 3, 5, 7, 11, 13]
    #[11, 2, 7, 5, 13, 3]
    """
    example_list = [2, 3, 5, 7, 11, 13]
    print(example_list)
    random.shuffle(example_list)
    print(example_list)
    return 0

def flatten(nested_list):
    """
    Given a list whose items are list,
    return the list formed by joining all of these lists
    """
    out_list = []
    print("-->",nested_list)
    # for n in nested_list:
    #     for m in n:
    #         out_list.append(m)
    for n in nested_list:
        out_list.extend(n)
    return out_list

def p_9():
    """
    Template - Flatten a nested list
    Output
    []
    []
    [1, 2, 3]
    ['cat', 'dog', 'pig', 'cow']
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    # Test code
    print("1:",flatten([]))
    print("")
    print("2:",flatten([[]]))
    print("")
    print("3:",flatten([[1, 2, 3]]))
    print("")
    print("4:",flatten([["cat", "dog"], ["pig", "cow"]]))
    print("")
    print("5:",flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))
    print("")
    return 0

def remove_duplicates(items):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order
    """
    # myList = list(items)
    # cleanlist = []
    # [cleanlist.append(x) for x in myList if x not in cleanlist]

    cleanlist = []
    for item in items:
        if item not in cleanlist:
            cleanlist.append(item)
    return cleanlist

    return cleanlist

def p_10():
    """
    Template - Remove duplicates from a list while preserving the order of items
    Output
    []
    [1, 2, 3, 4]
    [1, 2, 3, 4, 5, 6]
    ['cat', 'dog', 'pig', 'cow', 'pug']
    """
    myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
    cleanlist = []
    [cleanlist.append(x) for x in myList if x not in cleanlist]
    # Test code
    print(remove_duplicates([]))
    print(remove_duplicates([1, 2, 3, 4]))
    print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
    print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))
    return 0

def quiz():
    print("***** 1:")
    my_list = [1,3,5,7,9]
    print(my_list[3:])
    print(my_list[2:])
    print(my_list[2:5])
    print(my_list[3:5])

    print("***** 2:")
    my_tup = (1,)
    print(len(my_tup), type(my_tup))
    # my_tup = (1)
    # print(len(my_tup))
    my_tup = tuple([1])
    print(len(my_tup), type(my_tup))

    print("***** 3:")
    # instructors = ("Scott", "Joe", "John", "Stephen")
    # instructors[2 : 4] = []
    # print(instructors)
    print("***** 4:")

    print("***** 5:")
    my_list = [1, 3, 5, 7, 9]
    my_list.reverse()
    print(my_list.reverse())

    print("***** 6:")
    fib = [0,1]
    for n in range(20):
        m = fib[-1]+fib[-2]
        fib.append(m)
    print("fib: ",fib[-1])

    print("***** 7:")
    print(len(compute_primes(200)))
    print(len(compute_primes(2000)))

    return 0

"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """

    answer = list(range(2, bound))
    for divisor in range(2, bound):
        kill = divisor
        for cnt in range(divisor, bound):
            kill += divisor
            if kill in answer:
                answer.remove(kill)
    return answer

def main():
    """
    main program to keep test and functions clean
    :return:
    """
    # p_1()
    # p_2()
    # p_3()
    # p_4()
    # p_5()
    # p_6()
    # p_7()
    # p_8()
    # p_9()
    # p_10()
    quiz()


if __name__ == "__main__":
    main()


