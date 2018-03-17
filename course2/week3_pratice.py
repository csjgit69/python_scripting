"""
Course2 week one pratice
"""

import datetime

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
    Template - Create a list formed by excluding the first and last items of example_list
    Output
    [3, 5, 7, 11]
    """
    example_list = [2, 3, 5, 7, 11, 13]
    middle_list =example_list[1:-1]
    print(middle_list)

    return 0

def p_4():
    """
    Template - Create a list formed by 8 copies of True and 8 copies of False
    Output
    [True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False]
    """
    truefalse_list =[True]*8+[False]*8
    print(truefalse_list)

    return 0

def p_5():
    """
    Template - Create a list of words form a string consisting of words separated by spaces
    Output
    ['Bring', 'me', 'a', 'shrubbery']
    """
    quote = "Bring me a shrubbery"
    words = quote.split(" ")
    print (words)
    return 0

def word_count(text, word):
    """
    counts number of time word is in text
    """
    words = text.split(" ").count(word)
    return words


def p_6():
    """
    Given a string text consist of words separate by spaces and a string word
    (with no spaces), return the number of times that word appears in the text
    Output
    2
    1
    1
    """
    # Tests
    print(word_count("this pigdog is a fine pigdog", "pigdog"))
    print(word_count("this pigdog is not a dog", "dog"))
    print(word_count("this pigdog is not a pig", "pigdog"))
    print(word_count("this this this pigdog is not a pig", "this"))

    return 0

def p_7():
    """
    Template - Analyze an example of a list reference situation
    Output
    [2, 3, 5, 7, 11, 13]
    [2, 3, 5, 7, 11, 13]
    [0, 3, 5, 7, 11, 13]
    [0, 3, 5, 7, 11, 13]
    """

    # Initial list
    list1 = [2, 3, 5, 7, 11, 13]

    # Another reference to list1
    list2 = list1

    # Print out both lists
    print(list1)
    print(list2)

    # Update the first item in second list to zero
    list2[0] = 0

    # Print out both lists
    print(list1)
    print(list2)

    # Explain what happens to list1 in a comment
    print("list1 and list2 are the same object in memory, so change to list2 affects list1")
    return 0

def p_8():
    """
    Template - Analyze another example of a list reference situation
    Output
    [2, 3, 5, 7, 11, 13]
    [2, 3, 5, 7, 11, 13]
    [2, 3, 5, 7, 11, 13]
    [0, 3, 5, 7, 11, 13]
    """

    # Initial list
    list1 = [2, 3, 5, 7, 11, 13]

    # Make a copy of list1
    list2 = list(list1)

    # Print out both lists
    print(list1)
    print(list2)

    # Update the first item in second list to zero
    list2[0] = 0

    # Print out both lists
    print(list1)
    print(list2)

    # Explain what happens to list1 in a comment
    print("command list(list1) returns a new list")

    return 0

def list_max(numbers):
    """
    return the largest value in the list
    """
    # numbers.sort()
    # m_num = numbers[-1]
    # m_num = max(numbers)
    m_num = numbers[0]
    for n in numbers:
        if n>m_num:
            m_num = n
    return m_num

def p_9():
    """
    Template - Take a list of integers and concatenate their digits
    Output:
    4
    404
    123456789
    327961000
    """

    # Tests
    print(concatenate_ints([4]))
    print(concatenate_ints([4, 0, 4]))
    print(concatenate_ints([123, 456, 789]))
    print(concatenate_ints([32, 796, 1000]))
    return 0

def concatenate_ints(int_list):
    """
    Given a list of integers int_list, return the integer formed by
    concatenating their decimal digits together
    """
    cat = ""
    for n in int_list:
        cat = cat + str(n)
    return int(cat)

def quiz():
    print("***** 1:")
    print(list(range(0,5,1)))
    print(range(6))
    print(list(range(6)))
    print(list(range(0,6)))

    print("***** 2:")
    ml = [1,2,3,4,5,6,7,8]
    print(ml[0:len(ml)//2] , ml[len(ml)//2:len(ml)])
    print(ml[:len(ml)//2], ml[len(ml)//2:])

    print("***** 3:")
    n, m  = 3, 5
    init_list = list(range(1, n))
    final_list = init_list * m
    print(final_list)

    print("***** 4:")
    n = 5
    test_string = "xxx" + " " * n + "xxx"
    split_list = test_string.split(" ")
    print(split_list)

    print("***** 5:")
    l1 = list(range(1,10))
    l2 = [] + l1
    l2[0] = 99
    print (l1, l2)
    l1 = list(range(1,10))
    l2 = l1[:]
    l2[0] = 99
    print (l1, l2)

    print("***** 7:")
    print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
    print(strange_sum(list(range(123)) + list(range(77))))
    return 0

def strange_sum(numbers):
    """
    returns sum of numbers not divisible by 3
    """
    total = 0
    for n in numbers:
        if n%3 != 0:
            total += n

    return total

def main():
    """
    main program to keep test and functions clean
    :return:
    """
    # p_1()
    p_2()
    # p_3()
    # p_4()
    # p_5()
    # p_6()
    # p_7()
    # p_8()
    # p_9()
    # p_10()
    # quiz()


if __name__ == "__main__":
    main()


