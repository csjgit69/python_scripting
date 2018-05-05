"""
Course3 week one pratice
"""

import datetime
import random

def p_1():
    """
    Template - Initialize a dictionary my_dict to be empty
    # Output
    #<class 'dict'>
    #{}
    """
    my_dict = {}
    # Tests
    print(type(my_dict))
    print(my_dict)

    return 0

def p_2():
    """
    Template - Create a dictionary my_dict that contains
    two specified value/pairs
    # Output - note that order of key/values pairs in output is unimportant
    #<class 'dict'>
    #1
    #2
    #???
    """

    my_dict = {"Joe":1, "Scott":2}

    # Tests
    print(type(my_dict))
    print(my_dict["Joe"])
    print(my_dict["Scott"])
    print(my_dict)

    return 0

def p_3():
    """
    Template - Add the specified key/value pair to an
    existing dictionary my_dict
    # Output - note that order of key/values pairs in output is unimportant
    #<class 'dict'>
    #1
    #2
    #3
    #{'Scott': 2, 'John': 3, 'Joe': 1}
    """

    # Initialize dictionary
    my_dict = {"Joe" : 1, "Scott" : 2}
    my_dict["John"] = 3
    # Tests
    print(type(my_dict))
    print(my_dict["Joe"])
    print(my_dict["Scott"])
    print(my_dict["John"])
    print(my_dict)

    return 0

def p_4():
    """
    Template - Write an expression that determines whether
    a key is in a dictionary
    Output
    True
    True
    False
    """

    # Initialize dictionary
    my_dict = {"Joe" : 1, "Scott" : 2, "John" : 3}

    # Print True/False depending on whether the key "Joe" is in my_dict
    print("Joe" in my_dict)
    # Print True/False depending on whether the key "John" is in my_dict
    print("John" in my_dict)
    # Print True/False depending on whether the key "Stephen" is in my_dict
    print("Stephen" in my_dict)

    return 0

def is_empty(my_dict):
    """
    Given a dictionary my_dict, return True if the
    dictionary is empty and False otherwise
    """
    return len(my_dict) == 0
    # return bool(my_dict)

def p_5():
    """
    Solution - Write a function is_empty(my_dict) that
    returns True if a dictionary is empty and False otherwise
    Output
    True
    False
    False
    """
    # Testing code
    print(is_empty({}))
    print(is_empty({0 : 1}))
    print(is_empty({"Joe" : 1, "Scott" : 2}))

    return 0

def value_sum(my_dict):
    """
    Given a dictionary my_dict whose values are numbers, return
    the sums of the values in my_dict
    """
    sum = 0
    for key in my_dict.keys():
        sum += my_dict[key]
    return sum

def p_6():
    """
    Template - Write a function value_sum(my_dict) that
    returns the sum of the values in a dictionary
    Output
    0
    1
    7
    """
    # Testing code
    print(value_sum({}))
    print(value_sum({0 : 1}))
    print(value_sum({"Joe" : 1, "Scott" : 2, "John" : 4}))
    return 0

def make_dict(key_value_list):
    """
    Given a list of tuples of the form (key, value),
    return a dictionary with the corresponding keys and values
    """
    my_dict = {}
    for key, val in key_value_list:
        # key = tup[0]
        # val = tup[1]
        # print (tup, key, val)
        my_dict[key] = val
    return my_dict

def p_7():
    """
    Template - Write a function make_dict(key_value_list) that
    takes a list of tuples (key, value) and returns a
    dictionary with these keys and values
    Output
    {}
    {0: 1}
    {'John': 4, 'Joe': 1, 'Scott': 2}
    """

    # Testing code
    print(make_dict([]))
    print(make_dict([(0, 1)]))
    print(make_dict([("Joe", 1), ("Scott", 2), ("John", 4)]))
    return 0

def encrypt(phrase, cipher_dict):
    """
    Take a string phrase (lower case plus blank)
    and encypt it using the dictionary cipher_dict
    """
    crypt = ""
    for chr in phrase:
        crypt += cipher_dict[chr]
    return crypt

def p_8():
    """
    Template for part 1
    Using substitution ciphers to encrypt and decrypt plain text
    Output for part 1
    vif
    hunnybtygnd
    """
    # Part 1 - Use a dictionary that represents a substition cipher to
    # encrypt a phrase

    # Example of a cipher dictionary 26 lower case letters plus the blank
    CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

    # Tests
    print("Output for part 1")
    print(encrypt("pig", CIPHER_DICT))
    print(encrypt("hello world", CIPHER_DICT))
    print()

    return 0

def make_decipher_dict(cipher_dict):
    """
    Take a cipher dictionary and return the cipher
    dictionary that undoes the cipher
    """
    decrypt = {}
    for key, val in cipher_dict.items():
        decrypt[val] = key
    return decrypt

def p_9():
    """
    Part 2 - Compute an inverse substitution cipher that decrypts
    an encrypted phrase
    Output for part 2 - note order of items in dictionary is not important
    {'p': 'f', 'n': 'l', 'm': 'a', 'i': 'i', 'd': 'd', 'x': 'k', 'b': ' ', 'l': 'v', 'f': 'g', 'o': 's', 'u': 'e', 'a': 'n', 'c': 'y', 'r': 'q', 'e': 'z', 'k': 'c', 'w': 'm', 'g': 'r', 'y': 'o', ' ': 't', 'h': 'h', 'v': 'p', 'j': 'x', 'q': 'u', 't': 'w', 's': 'b', 'z': 'j'}
    pig
    hello world
    """
    CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}
    DECIPHER_DICT = make_decipher_dict(CIPHER_DICT)

    # Tests - note that applying encrypting with the cipher and decipher dicts
    # should return the original results
    print("Output for part 2")
    print(DECIPHER_DICT)
    print(encrypt(encrypt("pig", CIPHER_DICT), DECIPHER_DICT))			      # Uncomment when testing
    print(encrypt(encrypt("hello world", CIPHER_DICT), DECIPHER_DICT))	# Uncomment when testing
    print()

    return 0

def make_cipher_dict(alphabet):
    """
    Given a string of unique characters, compute a random
    cipher dictionary for these characters
    """
    letters= list(alphabet)
    shuffled_letters = list(alphabet)
    random.shuffle(shuffled_letters)

    cipher_dict = {}
    for idx in range(len(alphabet)):
        letter = letters[idx]
        shuffled_letter = shuffled_letters[idx]
        cipher_dict[letter] = shuffled_letter
    return cipher_dict

    # chr_list = list(alphabet)
    # random.shuffle(chr_list)
    # cipher = {}
    # cnt = 0
    # for chr in alphabet:
    #     cipher[chr] = chr_list[cnt]
    #     cnt += 1
    # return cipher

def p_10():
    """
    Part 3 - Create a random cipher dictionary
    Output for part 3 -  note that answers are randomized
    {}
    {'a': 'a', 't': 'c', 'c': 't'}
    {'a': 'h', 'l': 'u', 'u': 'q', 'b': 'v', 'y': 'a', 'm': 'r', 'p': 'j', 'k': 'e', 'n': 'p', 't': 'x', 'd': 'o', 'c': 'c', 'w': ' ', 'f': 'd', 'r': 'z', 'v': 'l', 's': 'y', 'e': 'b', 'o': 'i', 'x': 'm', 'h': 's', 'i': 'w', 'q': 'g', 'g': 'n', 'j': 'f', 'z': 'k', ' ': 't'}
    """


    # Tests
    print("Output for part 3")
    print(make_cipher_dict(""))
    print(make_cipher_dict("cat"))
    print(make_cipher_dict("abcdefghijklmnopqrstuvwxyz "))
    return 0

def count_letters(word_list):
    """ See question description """

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    letter_count = {}
    answer = ""
    max = 0

    for letter in ALPHABET:
        letter_count[letter] = 0
    for word in word_list:
        for letter in word:
            letter_count[letter] = letter_count[letter] + 1
    keys = letter_count.keys()
    keys = sorted(keys)
    for key in keys:
        # print(key, "::", letter_count[key])
        if letter_count[key] > max:
            answer = key
            max = letter_count[key]

    return answer

def quiz():
    my_list = [1,1]
    my_dict2 = {1:1}
    my_dict = {}
    my_dict[(1,0)] = 10
    # my_dict[my_dict2] = 10
    # my_dict[my_list] = 10
    my_dict[1.0] = 10

    my_dict[1.0] = "10"
    my_dict[1.0] = my_dict2
    my_dict[1.0] = (1,1)
    my_dict[1.0] = False

    # print (my_dict[a])
    print("most letter: ", count_letters(["hello", "world"]))

    monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

    monty_words = monty_quote.split(" ")
    print("most letter: ", count_letters(monty_words))
    return 0

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
    p_10()
    quiz()


if __name__ == "__main__":
    main()


