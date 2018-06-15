"""
Course3 week two practice
"""

import datetime
import random

def p_1():
    """
    Template - Create a list nested_list consisting of five empty lists
    # Output
    # ???
    """
    nested_list = [[], [], [], [], []]
    # Tests
    print(nested_list)

    return 0

def p_2():
    """
    Template - Create a list nested_list of length 5 whose items
    are themselves lists consisting of 3 zeros
    # Output
    # ???
    """
    nested_list = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    # Tests
    print(nested_list)
    return 0


def trans_pos_ex():
    """
    example of List comprehension code
    :return:
    """
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12]]
    print([[row[i] for row in matrix] for i in range(4)])
    # improved with length so we don't need to know the length to do the work
    print([[row[i] for row in matrix] for i in range(len(matrix))])
    # that above does all the work of this below:
    transposed = []
    for i in range(len(matrix)):
    # the following 3 lines implement the nested listcomp
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
            print(row, ":  ", transposed_row)
        transposed.append(transposed_row)
    print(transposed)
    return 0

def p_3():
    """
    Template- Create a list zero_list consisting of 3 zeroes using a list comprehension
    https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

    As a challenge, redo the previous problem using a nested list comprehension
    https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
    # Output
    # [0, 0, 0]
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    zero_list = [0 for dummy_idx in range(3)]
    nested_list = [[0 for dummy_idx in range(3)] for dummy_idx2 in range(5) ]
    # Tests
    print(zero_list)
    print(nested_list)

    return 0

def p_4():
    """
    Template - Select a specific item in a nested list
    # Output
    # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
    # 7
    """

    # Define a nested list of lists
    nested_list = [[col + 3 * row for col in range(3)] for row in range(5)]
    print(nested_list)
    for row in nested_list:
        for item in row:
            if item == 7:
                print(item)
    return 0

def p_5():
    """
    Consider the list nested_list as defined in the provided template.
    Attempting to modify one item in nested_list has the unexpected effect of modifying several items.
    Examine this example and enter an explanation for this behavior.
    Solution - Analyze a reference issue involving a nested list
    # Erroneous output
    # [[0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0]]
    # [[0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0]]

    # Desired output
    # [[0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0]]
    # [[0, 2, 0], [0, 2, 0], [0, 7, 0], [0, 2, 0], [0, 2, 0]]
                                 ^
    """

    # Create a nested list
    zero_list = [0, 2, 0]
    nested_list = []
    for dummy_idx in range(5):
        # nested_list.append(zero_list)
        nested_list.append(list(zero_list))
    print(nested_list)

    # Update an entry to be non-zero
    nested_list[2][1] = 7
    print(nested_list)

    # Line 114 is unintentionally updating all 5 entries in nested_list due to a referencing issue.

    # Line 110 is creating five references to the SAME onject (the list zero_list) in nested_list.
    # Thus, updating one reference to zero_list in nested_list in line 13 updates
    # the other four references to zero_list in nested_list simultaneously.
    return 0

def p_6():
    """
    Template - Create a list list_dicts of 5 empty dictionaries
    # Output
    # ???
    """
    list_dicts =[{},{},{},{},{},{}]
    # Tests
    print(list_dicts)
    return 0

def p_7():
    """
    Template - Write a function dict_copies(my_dict, num_copies) that
    returns a list consisting of num_copies copies of my_dict
    # Output
    # []
    # [{}]
    # [{}, {}]
    # [{'a': 1, 'b': 2}, {'b': 2, 'a': 1}]
    # [{'b': 2, 'a': 1}, {'b': 2, 'a': 3}]

    # Note that you have a reference issue if the last line of output is
    # [{'a': 3, 'b': 2}, {'b': 2, 'a': 3}]
    """

    # Add code here
    def dict_copies(my_dict, num_copies):
        """
        Given a dictionary my_dict and an integer num_copies,
        returns a list consisting of num_copies copies of my_dict.
        """
        list_copies =[]
        for copy in range(num_copies):
            list_copies.append(dict(my_dict))

        return list_copies

    # Tests
    print(dict_copies({}, 0))
    print(dict_copies({}, 1))
    print(dict_copies({}, 2))

    test_dict = dict_copies({'a': 1, 'b': 2}, 2)
    print(test_dict)

    # Check for reference problem
    test_dict[1]["a"] = 3
    print(test_dict)
    return 0

def p_8():
    """
    Solution - Write a function make_dict_lists(length) that returns a dictionary whose keys are in range(length) and whose
    corresponding values are lists of zeros with length matching the key
    # Output
    # {}
    # {0: []}
    # {3: [0, 0, 0], 0: [], 4: [0, 0, 0, 0], 1: [0], 2: [0, 0]}
    """

    # Add code here
    def make_dict_lists(length):
        """
        Given an integer length, return a dictionary whose keys
        lie in range(length) and whose corresponding values are
        lists of zeros with length matching the key
        """
        new_dict = {}
        for idx in range(length):
            new_dict[idx] = [0 for dummy_idx in range(idx)]
            # new_dict[idx] = [0] * idx
        return new_dict

    # Tests
    print(make_dict_lists(0))
    print(make_dict_lists(1))
    print(make_dict_lists(5))
    return 0

def p_9():
    """
    Define a dictionary grade_table whose keys corresponds to names in the first column of the table below
    and whose corresponding values are a list of the grades in the name's row.
    Template - Create a dictionary grade_table whose keys are provided
    student names and values are associated list of grades
    # Output
    # [100, 98, 100, 13]
    # [75, 59, 89, 77]
    # [86, 84, 91, 78]
    """

    # Add code here
    grade_table = {"Joe": [100,98,100,13],
                   "Scott": [75, 59, 89, 77],
                   "John": [86, 84, 91, 78]}

    # Tests
    print(grade_table["Joe"])
    print(grade_table["Scott"])
    print(grade_table["John"])
    return 0

def p_10():
    """
    Challenge: Define a function make_grade_table(name_list, grades_list)that takes a list of names name_list
    and a list of grade lists and returns a dictionary whose keys corresponds to names name_list
    and whose corresponding values are the items grades_list.
    As a challenge, use the Python function zip() to simplfy the logic of your loop that creates the output dictionary
    Template - Create a function make_grade_table(name_list, grades_list)
    whose keys are the names in names and whose values are the
    lists of grades in grades
    # Output
    # {}
    # {'Scott': [75, 59, 89, 77], 'John': [86, 84, 91, 78], 'Joe': [100, 98, 100, 13]}
    """
    # Add code here
    def make_grade_table(name_list, grades_list):
        """
        Given a list of name_list (as strings) and a list of grades
        for each name, return a dictionary whose keys are
        the names and whose associated values are the lists of grades
        """
        grade_dict = {}
        for key, val in zip(name_list,grades_list):
            grade_dict[key] = val
        return grade_dict

    # Tests
    print(make_grade_table([], []))

    name_list = ["Joe", "Scott", "John"]
    grades_list = [100, 98, 100, 13], [75, 59, 89, 77], [86, 84, 91, 78]
    print(make_grade_table(name_list, grades_list))
    return 0

def quiz():
    my_dict = {"dude": 100}
    my_key = "dude"
    print(my_key in my_dict)
    print(my_key in my_dict.keys())

    for key, val in my_dict.items():
        print(key, ": ", val)

    my_dict = {0: 0, 5: 10, 10: 20, 15: 30, 20: 40}
    # print(my_dict[25])
    print(my_dict.get(25))

    def matrix(side):
        NUM_ROWS = side
        NUM_COLS = side

        # construct a matrix
        my_matrix = []
        for row in range(NUM_ROWS):
            new_row = []
            for col in range(NUM_COLS):
                new_row.append(row * col)
            my_matrix.append(new_row)

        # print the matrix
        for row in my_matrix:
            print(row)
        print(my_matrix[1][4])
        return my_matrix

    def m_trace(t_matrix):
        trace = 0
        for idx in range(len(t_matrix)):
            trace = trace + t_matrix[idx][idx]
        return trace

    # test_matrix = matrix(25)
    # print(m_trace(test_matrix))
    def dd_matrix():
        NUM_ROWS = 5
        NUM_COLS = 9

        # construct a matrix
        my_matrix = {}
        for row in range(NUM_ROWS):
            row_dict = {}
            for col in range(NUM_COLS):
                row_dict[col] = row * col
            my_matrix[row] = row_dict

        print(my_matrix)

        # print the matrix
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                print(my_matrix[row][col], end=" ")
            print()
        return my_matrix
    m_1 = {2: {6: 12, 2: 4, 0: 0, 7: 14, 5: 10, 3: 6, 8: 16, 4: 8, 1: 2}, 4: {0: 0, 3: 12, 2: 8, 6: 24, 4: 16, 5: 20, 8: 32, 7: 28, 1: 4}, 1: {2: 2, 5: 5, 3: 3, 8: 8, 4: 4, 1: 1, 7: 7, 0: 0, 6: 6}, 3: {4: 12, 0: 0, 8: 24, 6: 18, 7: 21, 3: 9, 5: 15, 1: 3, 2: 6}, 0: {8: 0, 1: 0, 6: 0, 2: 0, 4: 0, 5: 0, 3: 0, 0: 0, 7: 0}}
    m_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 2, 4, 6, 8, 10, 12, 14, 16], [0, 3, 6, 9, 12, 15, 18, 21, 24], [0, 4, 8, 12, 16, 20, 24, 28, 32]]
    m_3 = {1: {1: 2, 7: 2, 3: 2, 8: 2, 0: 2, 5: 2, 2: 2, 6: 2, 4: 2}, 2: {5: 4, 1: 4, 8: 4, 0: 4, 3: 4, 2: 4, 4: 4, 7: 4, 6: 4}, 3: {4: 6, 2: 6, 1: 6, 5: 6, 0: 6, 7: 6, 8: 6, 3: 6, 6: 6}, 0: {0: 0, 5: 0, 6: 0, 8: 0, 1: 0, 3: 0, 2: 0, 4: 0, 7: 0}, 4: {3: 8, 8: 8, 7: 8, 5: 8, 4: 8, 1: 8, 2: 8, 6: 8, 0: 8}}
    m_4 = {1: {7: 7, 4: 4, 3: 3, 8: 8, 6: 6, 5: 5, 2: 2, 0: 0, 1: 1}, 0: {0: 0, 7: 0, 3: 0, 4: 0, 8: 0, 6: 0, 5: 0, 1: 0, 2: 0}, 2: {0: 0, 8: 16, 5: 10, 2: 4, 7: 14, 4: 8, 1: 2, 3: 6, 6: 12}, 3: {1: 3, 7: 21, 2: 6, 8: 24, 3: 9, 4: 12, 6: 18, 0: 0, 5: 18}, 4: {3: 12, 7: 28, 0: 0, 2: 8, 1: 4, 4: 16, 6: 24, 5: 20, 8: 32}}

    mm = dd_matrix()
    print(mm == m_1)
    print(mm == m_2)
    print(mm == m_3)
    print(mm == m_4)

    return 0

def main():
    """
    main program to keep test and functions clean
    :return:
    """
    quiz()
    
    # p_1()
    # p_2()
    # trans_pos_ex()
    # p_3()
    # p_4()
    # p_5()
    # p_6()
    # p_7()
    # p_8()
    # p_9()
    # p_10()

if __name__ == "__main__":
    main()


