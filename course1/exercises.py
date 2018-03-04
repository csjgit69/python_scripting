import math
import re
from operator import itemgetter, attrgetter

"""
100+ python exercises to brush up my skills
"""

def get_input (input_str):
    """
    returns a list of numbers sperated by comas from the console
    Suppose the following input is supplied to the program:
    34,67,55,33,12,98
    Then, the output should be:
    ['34', '67', '55', '33', '12', '98']
    """
    usr_str = input(input_str)
    # print (usr_str)
    usr_str = re.sub(r'[,]+', " ", usr_str)
    usr_str = usr_str.split(" ")
    # print (usr_str)
    return usr_str

def get_lines (input_str):
    """
    gets many lines form console. empty line ends input
    :param input_str: string prompt for user
    :return: list of lines from console
    """
    lines = []
    while True:
        line = input(input_str)
        if line:
            lines.append(line)
        else:
            break
    return lines

def exer_1 (base, limit):
    """
    Question:
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.
    :param base: lower end number
    :param limit: upper end number
    :return: nothing
    """
    answer_list = []
    cnt = 0
    for num in range(base,limit):
        if((num%7 == 0) and (num%5 !=0)):
            answer_list.append(str(num))
            cnt += 1
    print (",".join(answer_list))
    print ("count was: ",cnt)
    return

def exer_2 ():
    """
    Question:
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    40320
    :return:
    """
    number = int(input("input an integer: "))
    fac = number
    while number > 1:
        fac = fac * (number-1)
        number = number - 1
    print(fac)
    return

def exer_3 ():
    """
    Question:
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
    such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    :return:
    """
    number = int(input("input an integer: "))
    num_dict = dict()
    while number > 0:
        num_dict[number] = number * number
        number -= 1
    print(num_dict)
    return

def exer_4 ():
    """
    Question:
    Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
    Suppose the following input is supplied to the program:
    34,67,55,33,12,98
    Then, the output should be:
    ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')
    """
    usr_str = input("input comma separated integers:")
    usr_list = list(usr_str.split(","))
    usr_tuple = tuple(usr_str.split(","))
    print(usr_str.split(","))
    print(usr_list)
    print(usr_tuple)
    return

class Exer_5:
    """
    Question:
    Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
    Hints:
    Use __init__ method to construct some parameters
    :return:
    """
    def __init__(self):
        self.my_string = ""

    def getString(self):
        self.my_string = input("Input a string: ")

    def printString(self):
        print(self.my_string.upper())

def exer_6(d):
    """
    Question:
    Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.
    Example
    Let us assume the following comma separated input sequence is given to the program:
    100,150,180
    The output of the program should be:
    18,22,24
    :return:
    """
    c = 50
    h = 30
    print("Passed in list: ",d)
    print("Passed in type: ",type(d))
    # b = [4,5,5,5,5]
    q = []
    for num in d:
        q.append(int(math.sqrt((2 * c * float(num))/h)))
    print(q)
    return

def exer_7(indx):
    """
    Question:
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
    The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡­Y-1.
    Example
    Suppose the following inputs are given to the program:
    3,5
    Then, the output of the program should be:
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    :return:
    """
    # col = int(indx[0])
    # row = int(indx[1])
    # print (indx,col,row)
    # print (type(indx),type(col),type(row))
    # col_l = []
    # for i in range(0,col):
    #     row_l = []
    #     for j in range(0,row):
    #         row_l.append(i*j)
    #     col_l.append(row_l)
    # print(col_l)

    # another way to do it, from the exercise file:
    dimensions=[int(x) for x in indx]
    rowNum=dimensions[0]
    colNum=dimensions[1]
    # create and pre-populate the 2D array and zero fill
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col]= row*col
    print (multilist)
    return

def exer_8(words):
    """
    Question:
    Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
    Suppose the following input is supplied to the program:
    without,hello,bag,world
    Then, the output should be:
    bag,hello,without,world
    :param words:
    :return:
    """
    l = []
    for name in sorted(words):
        l.append(name)
    print(l)
    return

def exer_9():
    """
    Question:
    Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
    Suppose the following input is supplied to the program:
    Hello world
    Practice makes perfect
    Then, the output should be:
    HELLO WORLD
    PRACTICE MAKES PERFECT
    :return:
    """
    l = []
    while True:
        line = input("Input a string, or return to end: ")
        if line:
          l.append(line.upper())
        else:
            break;
    print(l)
    for line in l:
        print (line)
    return

def exer_10():
    """
    Question:
    Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
    Suppose the following input is supplied to the program:
    hello world and practice makes perfect and hello world again
    Then, the output should be:
    again and hello makes perfect practice world
    :return:
    """
    words = input("input words separated by spaces: ").split(" ")
    ul = []
    for word in sorted(words):
        if word not in ul:
            ul.append(word)

    print(words)
    print(" ".join(ul))
    # from exercise file, set() is a list(collection) with no duplicate items in it
    s = sorted(set([word for word in words]))
    print(" ".join(s))
    return

def exer_11(in_str):
    """
    Question:
    Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
    and then check whether they are divisible by 5 or not. 
    The numbers that are divisible by 5 are to be printed in a comma separated sequence.
    Example:
    0100,0011,1010,1001
    Then the output should be:
    1010
    :return:
    """
    # bins = [int(x,base=2) for x in in_str]
    # print(bins)
    # print(type(bins))
    l = []
    for x in in_str:
        if int(x,base=2)%5==0:
            l.append(x)
    print(",".join(l))
    return

def exer_12(in_str):
    """
    Question:
    Write a program, which will find all such numbers between 1000 and 3000 (both included)
    such that each digit of the number is an even number.
    The numbers obtained should be printed in a comma-separated sequence on a single line.
    :return:
    """
    base, limit = [int(x) for x in in_str]
    #limit += 1
    print(base, limit)
    l = []
    for num in range(base,limit+1):
        # print("\nNum = ",num)
        even = True
        for c in str(num):
            if (int(c) == 0) or (int(c)%2!=0):
                even = False
            # print("c = ",c,"even = ",even)
        if even:
            l.append(str(num))
    # print(l)
    print(",".join(l))
    # l = []
    # for num in range(base,limit+1):
    #     len = len(str(num))
    return

def exer_13(in_str):
    """
    Question:
    Write a program that accepts a sentence and calculate the number of letters and digits.
    Suppose the following input is supplied to the program:
    hello world! 123
    Then, the output should be:
    LETTERS 10
    DIGITS 3
    :param in_str:
    :return:
    """
    dig_cnt = 0
    alph_cnt = 0
    for x in in_str:
        for c in x:
            if c.isdigit():
                dig_cnt += 1
            if c.isalpha():
                alph_cnt += 1
    print("LETTERS: ",alph_cnt)
    print("DIGITS: ",dig_cnt)
    return

def exer_14(in_str):
    """
    Question:
    Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
    Suppose the following input is supplied to the program:
    Hello world!
    Then, the output should be:
    UPPER CASE 1
    LOWER CASE 9
    :param in_str:
    :return:
    """
    # example of another way to keep counters, in a simple data struct
    cnts = {"u_cnt": 0, "l_cnt": 0}
    for w in in_str:
        for c in w:
            if c.islower():
                cnts["l_cnt"] += 1
            if c.isupper():
                cnts["u_cnt"] += 1
    print("UPPER CASE: ",cnts["u_cnt"])
    print("LOWER CASE: ",cnts["l_cnt"])
    return

def exer_15(in_str):
    """
    Question:
    Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
    Suppose the following input is supplied to the program:
    9
    Then, the output should be:
    11106
    :return:
    """
    d = in_str[0]
    s = int(d) + int(d+d) + int(d+d+d) + int(d+d+d+d)
    print(s)
    return

def exer_16(in_list):
    """
    Question:
    Use a list comprehension to square each odd number in a list.
    The list is input by a sequence of comma-separated numbers.
    Suppose the following input is supplied to the program:
    1,2,3,4,5,6,7,8,9
    Then, the output should be:
    1,3,5,7,9
    :return:
    """
    # there has to be a cleaner way to do this vs all the casting in and out of str/int like i did below
    odd_list = [str(int(x)**2) for x in in_list if int(x)%2!=0]
    print("Just the odd values in the list: ")
    print(",".join(odd_list))
    return

def exer_17(in_lines):
    """
    Write a program that computes the net amount of a bank account based a transaction log from console input.
    The transaction log format is shown as following:
    D 100
    W 200
    ¡­
    D means deposit while W means withdrawal.
    Suppose the following input is supplied to the program:
    D 300
    D 300
    W 200
    D 100
    Then, the output should be:
    500
    """
    print(in_lines)
    total = 0
    for line in in_lines:
        print(line," is type: ", type(line))
        line = line.split(" ")
        print(line," is type: ", type(line))
        if line[0].upper() == "D":
            total += int(line[1])
        if line[0].upper() == "W":
            total -= int(line[1])
    print("Bank account total is: ", total)
    return

def exer_18():
    """
    Question:
    A website requires the users to input username and password to register.
    Write a program to check the validity of password input by users.
    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
    Example
    If the following passwords are given as input to the program:
    ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:
    ABd1234@1
    :return:
    """
    in_pw = get_input("""Enter a password
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    ---> """)
    pw = in_pw[0]
    # print(pw, "is type: ", type(pw), " and len: ", len(pw))
    len_ok = False
    lower_ok = False
    upper_ok = False
    number_ok = False
    special_ok = False
    if len(pw) >= 6 and len(pw) <= 12:
        len_ok = True
    for c in pw:
        # print(c, "c is lower:", c.islower())
        if c.islower():
            lower_ok = True
        if c.isupper():
            upper_ok = True
        if c.isdigit():
            number_ok = True
        if c in "$#@":
            special_ok = True
    if len_ok and lower_ok and upper_ok and number_ok and special_ok:
        print("Your password passed!")
    else:
        print("Your password failed!")
        print("len_ok = ", len_ok)
        print("lower_ok = ", lower_ok)
        print("upper_ok = ", upper_ok)
        print("number_ok = ", number_ok)
        print("special_ok = ", special_ok)
    return

def exer_19():
    """
    You are required to write a program to sort the (name, age, height) tuples by ascending order
    where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score.
    The priority is that name > age > score.
    If the following tuples are given as input to the program:
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
    Then, the output of the program should be:
    [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
    We use itemgetter to enable multiple sort keys.
    :return:
    """
    # !!!!
    # I didn't know this one at all, sorted is something i need to study up on
    tuples = [("Tom","19","80"),("John","20","90"),("Jony","17","91"),("Jony","17","93"),("Json","21","85")]
    print(sorted(tuples, key=itemgetter(0,1,2)))
    print(itemgetter.__doc__)
    return

class exer_20(lim):
    """
    Question:
    Define a class with a generator which can iterate the numbers, which are divisible by 7,
    between a given range 0 and n.

    Hints:
    Consider use yield
    """
    def __init__(self):
        self.my_string = "Exercise 20"

    def getString(self):
        self.my_string = input("Input a string: ")

    def printString(self):
        print(self.my_string.upper())


def main():
    # exer_1(2000, 3200)
    # exer_2()
    # exer_3()
    # exer_4()

    # exer_5 = Exer_5()
    # exer_5.getString()
    # exer_5.printString()
    # exer_6(get_input("Input comma separated numbers: "))
    # exer_7(get_input("Input 2 comma separated integers: "))
    # exer_8(get_input("Input comma separated words: "))
    # exer_9()
    # exer_10()
    # exer_11(get_input("Input list of binary numbers, comma separated: "))
    # exer_12(get_input("Input two Integers, comma separated.\nAll numbers between them with all positive digits will be listed, inclusive: "))
    # exer_13(get_input("Enter a string of letters and digits: "))
    # exer_14(get_input("Enter a sentence with upper and lower case: "))
    # exer_15(get_input("Enter an integer: "))
    # exer_16(get_input("Enter a list of integers: "))
    # exer_17(get_lines("Input bank transaction: "))
    # exer_18()
    exer_19()


if __name__ == '__main__':
  main()
