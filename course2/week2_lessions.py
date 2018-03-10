"""
Course2 week two lessions and examples
"""

def list_ex():
    """
    List
    creation.
    """
    print("List Literals")
    print("=============")
    # List literals
    empty = []
    print(empty)
    numbers = [1, 5, 8, 3, 2]
    print(numbers)
    letters = ["a", "z", "c", "q", "c", "a"]
    print(letters)
    languages = ["python", "java", "javascript", "lisp", "c++", "haskell"]
    print(languages)
    # Don't mix types in a list!
    mixed = ["a", 1, True]
    print(mixed)
    print("")
    print("Creating Lists")
    print("==============")
    mylist = list()
    print(mylist)
    seq = range(5)
    print(seq)
    seqlst = list(seq)
    print(seqlst)
    seq2 = range(7, 13)
    print(seq2, list(seq2))
    seq3 = range(4, 27, 5)
    print(seq3, list(seq3))
    seq4 = range(9, 2, -1)
    print(seq4, list(seq4))

    return 0

def list_ex2():
    """
    List indexing and slicing.
    """
    print("List Indexing")
    print("=============")
    groceries = ["butter", "milk", "bacon", "spaghetti", "asparagus"]
    print(groceries)
    # first item
    print(groceries[0])
    # third item
    print(groceries[2])
    # length of list
    numitems = len(groceries)
    print(numitems)
    # last item
    print(groceries[-1])
    print(groceries[numitems - 1])
    # third from last item
    print(groceries[-3])
    # Out of bounds
    # print(groceries[numitems])
    # print(groceries[-17])
    # Indices
    # list = [7, 8, 3, 2, 9, 4]
    # item        7  8  3  2  9  4
    # pos index   0  1  2  3  4  5
    # neg index  -6 -5 -4 -3 -2 -1
    print("")
    print("List Slicing")
    print("============")
    numbers = list(range(72, 5, -12))
    print(numbers)
    # Sublists
    print(numbers[2:3])
    print(numbers[1:4])
    # Open ended slices
    print(numbers[1:])
    print(numbers[:3])
    # Using negative indices
    print(numbers[-2:])
    print(numbers[1:-4])
    # Empty slices
    print(numbers[3:2])
    print(numbers[10:12])
    return 0

def list_ex3():
    """
    Splitting and Joining Strings
    """
    print("Splitting")
    print("=========")
    # From "A Girl I knew" by J. D. Salinger
    sentence = "She wasn't doing a thing that I could see, except standing there leaning on the balcony railing, holding the universe together."
    print(sentence)
    # String split
    words = sentence.split()
    print(words)
    # Explicit separator
    words2 = sentence.split(" ")
    print(words2)
    phrases = sentence.split(",")
    print(phrases)
    parts = sentence.split("the")
    print(parts)
    print("")
    print("Joining")
    print("=======")
    items = ["flowers", "puddle", "mouse pad", "outlet", "bread", "house"]
    print(items)
    # Join together
    print("".join(items))
    print(" ".join(items))
    print(",".join(items))
    print(", ".join(items))
    return 0

def list_ex4():
    """
    Searching lists.
    """
    toys = ["blocks", "slinky", "fidget spinner", "cards", "doll house", "legos", "blocks", "teddy bear"]
    # Finding items in a list
    print(toys.index("legos"))
    print(toys.index("blocks"))
    # print(toys.rindex("video game")) # doesn't work on lists like it does on strings
    # print(toys.index("video game"))
    print("")
    # Checking if items are in a list
    print("legos" in toys)
    print("blocks" in toys)
    print("video game" in toys)
    print("teddy bear" not in toys)
    print("dice" not in toys)
    print("")
    # Counting items in list
    print(toys.count("slinky"))
    print(toys.count("blocks"))
    return 0

def print_items(alist):
    """
    Iterate over alist and print all items.
    """
    for item in alist:
        print(item)

def print_items_bad(alist):
    """
    Iterate over alist and print all items.
    List indexing in this way is error prone and unnecessary.
    """
    length = len(alist)
    for index in range(length):
        print(alist[index])

def count_items(alist):
    """
    Count number of items in alist.
    """
    count = 0
    for item in alist:
        count = count + 1
    return count

def count_odd_items(numlist):
    """
    Count number of odd numbers in numlist.
    """
    count = 0
    for num in numlist:
        if num % 2 == 1:
            count += 1
    return count

def list_ex5():
    """
    Iterating over lists.
    """
    numbers = list(range(5, 82, 3))
    strings = ["python", "is", "fun", "!"]
    print("Iterate over lists and print items")
    print("")
    print_items(numbers)
    print_items(strings)
    print_items_bad(numbers)
    print("")
    print("Iterate over lists and process them")
    print("")
    print(count_items(numbers))
    print(count_items(strings))
    print(count_odd_items(numbers))
    return 0

def main():
    """
    main program to keep test and functions clean
    :return:
    """
    # list_ex()
    # list_ex2()
    # list_ex3()
    # list_ex4()
    list_ex5()


if __name__ == "__main__":
    main()


