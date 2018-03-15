"""
Course3 week two lessions and examples
"""

def list_ex1():
    """
    Mutating Lists.
    """

    print("Updating Items")
    print("==============")

    lst = list(range(5))
    print(lst)

    lst[1] = -7
    lst[3] = 17
    print(lst)

    print("")
    print("Adding Items")
    print("============")

    lst.append(42)
    print(lst)

    lst.insert(2, 75)
    print(lst)

    lst2 = [-56, 27, 8]
    lst.extend(lst2)
    print(lst)
    lst.append(lst2)
    print(lst)

    print("")
    print("Removing Items")
    print("==============")

    lst.pop()
    print(lst)
    lst.pop(3)
    print(lst)
    return 0

def tuple_ex1():
    """
    Tuple examples.
    """

    # Lists and tuples are both sequences
    print("Sequences")
    print("=========")
    lst = [1, 5, 7, 3]
    tup = (1, 5, 7, 3)

    print(lst, tup)
    print(lst[2])
    print(tup[2])
    print(tup[:2])
    print(tup[2:3])

    # Tuples are immutable
    lst[0] = 9
    print(lst)
    # tup[0] = 9
    # print(tup)

    print("")
    print("Tuple Methods")
    print("=============")

    print(tup.index(7))
    print(tup.count(2))

    print("")
    print("Iteration")
    print("=========")

    for item in tup:
        print(item)

    print("")
    print("Conversion")
    print("==========")

    lst2 = [8, 6, 4, 8, 2]
    print(lst2)
    tup2 = tuple(lst2)
    print(tup2)
    # tup2[3] = 7
    lst3 = list(tup2)
    print(lst3)
    lst3[2] = 7
    print(lst2, tup2, lst3)
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
    # list_ex1()
    tuple_ex1()
    # list_ex3()
    # list_ex4()
    # list_ex5()


if __name__ == "__main__":
    main()


