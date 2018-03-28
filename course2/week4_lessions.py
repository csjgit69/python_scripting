"""
Course2 week four lessions and examples
"""
import os


def read_ex1():
    """
    Reading files.
    """
    print("Opening Files")
    print("=============")
    # Open takes a filename and a mode
    openfile = open("the_idiot.txt", "rt")
    # Modes for reading:
    #  r - read (default)
    #  t - text (default)
    #  b - binary
    print(type(openfile))
    print(openfile)
    # Must close file after opening it
    openfile.close()
    print("")
    print("Errors")
    print("======")
    # nofile = open("nosuchfile.txt")
    print("")
    print("Reading")
    print("=======")
    datafile = open("the_idiot.txt", "rt")
    data = datafile.read()
    print("type:", type(data))
    print("length:", len(data))
    print("")
    print(data)
    datafile.close()
    return 0

def read_ex2():
    """
    Iterating over files.
    """
    # Using readlines()
    #  readlines creates a list of strings
    #  that you can iterate over
    datafile1 = open("the_idiot.txt", "rt")
    for line in datafile1.readlines():
        print(line)
    datafile1.close()
    print("")
    print("================================")
    print("")
    # Direct iteration
    #  This is faster for large files,
    #  as no list is created
    datafile2 = open("the_idiot.txt", "rt")
    for line in datafile2:
        print(line)
    datafile2.close()
    return 0

def write_ex1():
    """
    Writing Files.
    """

    print("Opening Files")
    print("=============")

    openfile = open("output.txt", "wt")

    # Modes for writing:
    #  w - write (erases the file first)
    #  a - write (appends to the end of the file)
    #  t - text (default)
    #  b - binary
    #  + - open for read and write

    print(type(openfile))
    print(openfile)

    # Always close files
    openfile.close()

    print("")
    print("Writing")
    print("=======")

    def checkfile(filename):
        """
        Read and print the contents of the file named filename.
        """
        datafile = open(filename, "rt")
        data = datafile.read()
        datafile.close()
        print(data)

    # Write
    outputfile = open("output.txt", "wt")
    outputfile.writelines(["first line\n", "second line\n"])
    outputfile.write("third line\nfourth line\n")
    outputfile.close()

    print("Initial file contents:")
    checkfile("output.txt")


    # Overwrite
    outputfile2 = open("output.txt", "wt")
    outputfile2.write("overwriting contents\n")
    outputfile2.close()

    print("Overwritten file contents:")
    checkfile("output.txt")


    # Append
    outputfile2 = open("output.txt", "at")
    outputfile2.write("appending to contents\n")
    outputfile2.close()

    print("Appended file contents:")
    checkfile("output.txt")
    return 0

"""
Examples of paths used in Python
Expects current_file.txt in same directory as this code
Expects parent_file.txt in parent directory of this code
Expects child_file.txt in sub-directory child
"""

def echo_file(file_name):
    """
    Open a file, read its contents, and echo to console
    """
    my_file = open(file_name, 'r')
    my_file_text = my_file.read()
    print(my_file_text)
    my_file.close()                         # close the file, Joe!



def run_absolute_path_examples():
    """
    Some simple examples of absolute and relative paths
    """

    # Examples using absolute paths on Windows - Use raw strings to handle backslash
    current_abs_path = r"C:\Users\jwarren\Dropbox\Python Scripting\course 2\week4\paths\current_file.txt"
    child_abs_path = r"C:\Users\jwarren\Dropbox\Python Scripting\course 2\week4\paths\child\child_file.txt"
    parent_abs_path = r"C:\Users\jwarren\Dropbox\Python Scripting\course 2\week4\parent_file.txt"
    echo_file(current_abs_path)
    echo_file(child_abs_path)
    echo_file(parent_abs_path)
    print()

def run_relative_path_examples():
    """
    Some simple examples of relative paths
    """

    # Examples using relative paths - current_file.txt in same directory as this code
    echo_file("current_file.txt")
    echo_file("child/child_file.txt")           # Note that slash works on Windows
    echo_file("../parent_file.txt")
    print()


def run_os_path_examples():
    """
    Examples of computing/manipulating paths reliably using the os module
    """

    # Get absolute path using os.path - note path uses backslashes on Windows
    current_abs_path = os.path.abspath("current_file.txt")
    print(current_abs_path)

    # Get absolute path to child_file.text using os.path
    child_abs_path = os.path.abspath("child/child_file.txt")
    print(child_abs_path)

    # Get current working directory
    working_dir = os.getcwd()
    print(working_dir)

    # Construct paths using os.path.join
    child_rel_path = os.path.join(working_dir, "child", "child_file.txt")
    print(child_rel_path)

    parent_rel_path = os.path.join(working_dir, os.pardir, "parent_file.txt")
    print(parent_rel_path)


def main():
    """
    main program to keep test and functions clean
    :return:
    """
    # read_ex1()
    # read_ex2()
    # write_ex1()
    run_absolute_path_examples()
    run_relative_path_examples()
    run_os_path_examples()


if __name__ == "__main__":
    main()


