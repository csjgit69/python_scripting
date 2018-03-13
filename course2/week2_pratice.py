"""
Course2 week one pratice
"""

import datetime

def p_1():
    """
    Template- Create a list of the first six primes and print the 2nd, 4th, and 6th
    :return:
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    print(primes[1], " ", primes[3], " ", primes[5])
    return 0

def p_2():
    """
    Template - Create a list formed by the first and last items of example_list
    Output
    [2, 13]
    """
    example_list = [2, 3, 5, 7, 11, 13]
    # firstlast_list = list((example_list[0],example_list[-1]))
    firstlast_list = [example_list[0],example_list[-1]]
    print(firstlast_list)
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

def p_5(call,repeats):
    """
    Echo the string call to the console repeats number of time
    Each echo should be on a separate line
    :param call:
    :param repeats:
    :return:
    """
    # for dummy_cnt in range(0,repeats):
    #     print(call)
    answer = call + ("\n" + call) * (repeats -1)
    print(answer)
    answer = "? " * (repeats)
    print(answer)
    return 0

def is_substring(example_string, test_string):
    """
    Function that returns True if test_string
    is a substring of example_string and False otherwise
    # enter one line of code for substring test here
    """
    # return example_string.find(test_string) != -1
    return test_string in example_string
def p_6():
    """
    calls test function
    Output

    True
    True
    False
    False
    True
    :return:
    """
    example_string = "It's just a flesh wound."

    print(is_substring(example_string, "just"))
    print(is_substring(example_string, "flesh wound"))
    print(is_substring(example_string, "piddog"))
    print(is_substring(example_string, "it's"))
    print(is_substring(example_string, "It's"))
    return 0

def make_nametag(first_name, topic):
    """
    Given two strings first_name and topic,
    return a string of the form ""Hi! My name
    is XXX. This lecture covers YYY." where
    XXX and YYY are first_name and topic.
    """
    # return  "Hi! My name is {}. This lecture covers {}.".format(first_name,topic)
    return "Hi! My name is {0}. This lecture covers {1}.".format(first_name, topic)


def p_7():
    """
    # Output
    # Hi! My name is Scott. This lecture covers Python.
    # Hi! My name is Joe. This lecture covers games.
    # Hi! My name is John. This lecture covers programming tips.
    """
    print(make_nametag("Scott", "Python"))
    print(make_nametag("Joe", "games"))
    print(make_nametag("John", "programming tips"))
    return 0


def make_int(int_string):
    """
    Given the string int_string, return the associated integer if all
    digits are decimal digits.  Other return -1.
    """
    # is_int = True
    # for chrs in int_string:
    #     if not chrs.isdigit():
    #         return -1
    # if int(int_string)>0:
    #     return int(int_string)
    if int_string.isdigit():
        return int(int_string)
    return -1
def p_8():
    """
    Tests
    123
    123
    -1
    -1
    """
    print(make_int("123"))
    print(make_int("00123"))
    print(make_int("1.23"))
    print(make_int("-123"))
    return 0


def name_swap(name_string):
    """
    Given the string name string of the form "first last", return
    the string "Last First" where both names are now capitalized
    """
    # words = name_string.split(" ")
    # words[0] = words[0][0].upper()+words[0][1:]
    # words[1] = words[1][0].upper()+words[1][1:]
    # return words[1]+" "+words[0]
    (first, last) = name_string.split(" ")
    return last.capitalize() + " " + first.capitalize()

def p_9():
    """
    Tests Output
    Warren Joe
    Rixner Scott
    Greiner John
    """
    print(name_swap("joe warren"))
    print(name_swap("scott rixner"))
    print(name_swap("john greiner"))
    return 0
def count_vowels(val):
    sum = val.count("a")
    sum += val.count("e")
    sum += val.count("i")
    sum += val.count("o")
    sum += val.count("u")
    return sum
def demystify(l1_string):
    l1_string = l1_string.replace("l","a")
    l1_string = l1_string.replace("1","b")
    return l1_string
    

def quiz():
    print("1:")
    print("Grail"[-4])
    print("")
    print("2:")
    val = "Castle Anthrax"
    print(val[7:15])
    print(val[7:])
    print(val[8:])
    print(val[8:15])
    print("")
    print("4:")
    print("")
    print("6:")
    print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
    print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
    print("")
    print("7:")
    print(demystify("lll111l1l1l1111lll"))
    print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))

    return 0


def main():
    """
    main program to keep test and functions clean
    :return:
    """
    # p_1()
    # p_2()
    # p_3()
    p_4()
    # p_5("Hello", 5)
    # p_5("Goodbye", 3)
    # p_6()
    # p_7()
    # p_8()
    # p_9()
    # p_10()
    # quiz()


if __name__ == "__main__":
    main()


