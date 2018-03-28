"""
Week 4 practice project template for Python Data Representation
Update syntax for print in CodeSkulptor Docs
from "print ..." syntax in Python 2 to "print(...)" syntax for Python 3
"""

import examples3_file_diff as file_diff

# HTML tags that bounds example code
PREFIX = "<pre class='cm'>"
POSTFIX = "</pre>"
PRINT = "print"

def update_line(line):
    """
    Takes a string line representing a single line of code
    and returns a string with print updated
    """
    # Strip left white space using built-in string method lstrip()
    # print("\n******")
    t_line = line.lstrip()
    # If line is print statement,  use the format() method to add insert parentheses
    if t_line[:len(PRINT)] == PRINT:
        # print(line[:PRINT])
        s_idx = line.find(PRINT) + len(PRINT) # location to insert '(' char
        e_idx = s_idx + 1 # +1 to eat space between PRINT and next char
        line = "{0}{1}{2}{3}".format(line[0:s_idx],"(",line[e_idx:],")")

    # class solution:
    # if stripline[:len(PRINT)] == PRINT:
    #     spaces = ' ' * line.find(PRINT)
    #     content = stripline[len(PRINT) + 1:]
    #     return '{}print({})'.format(spaces, content)

    return line

def update_pre_block(pre_block):
    """
    Take a string that correspond to a <pre> block in html and parses it into lines.
    Returns string corresponding to updated <pre> block with each line
    updated via process_line()
    """
    # print("pre_block:\n", pre_block)
    updated_block = ""
    first = True
    for line in pre_block.splitlines():
        # print("line:",line)
        if first:
            updated_block = updated_block + "\n" + update_line(line)
            first = False
        else:
            updated_block = update_line(line)
        line_cnt += 1

    # class solution:
    # lines = pre_block.split("\n")
    # updated_block = update_line(lines[0])
    # for line in lines[1:]:
    #     updated_block += "\n"
    #     updated_block += update_line(line)
    # return updated_block

    return updated_block

def update_file(input_file_name, output_file_name):
    """
    Open and read the file specified by the string input_file_name
    Proces the <pre> blocks in the loaded text to update print syntax)
    Write the update text to the file specified by the string output_file_name
    """
    # open file and read text in file as a string
    in_file = open(input_file_name, "rt")
    in_text = in_file.read()
    # c_idx = 0
    e_idx = 0
    # out_text = in_text
    while in_text.find(PREFIX,e_idx) != -1:
        s_idx = in_text.index(PREFIX,e_idx)
        e_idx = in_text.index(POSTFIX,s_idx+6)
        block = in_text[s_idx:e_idx+len(POSTFIX)]
        pre_block = in_text[s_idx+len(PREFIX):e_idx]
        # print(block)
        # print(pre_block)
        pre_block = update_pre_block(pre_block)
        e_idx = e_idx + len(POSTFIX)
        in_text = in_text[:s_idx] + PREFIX + pre_block + POSTFIX + in_text[e_idx:]

    out_file = open(output_file_name, "wt")
    out_file.write(in_text)

    in_file.close()
    out_file.close()

    # # open file and read text in file as a string
    # with open(input_file_name) as doc_file:
    #     doc_text = doc_file.read()
    #
    # # split text in <pre> blocks and update using update_pre_block()
    # parts = doc_text.split(PREFIX)
    # updated_text = parts[0]
    # for part in parts[1:]:
    #     updated_text += PREFIX
    #     [pre_block, filler] = part.split(POSTFIX, 1)
    #     updated_text += update_pre_block(pre_block)
    #     updated_text += POSTFIX
    #     updated_text += filler
    #
    # # Write the answer in the specified output file
    # with  open(output_file_name, "w") as processed_file:
    #     processed_file.write(updated_text)

    pass

def test_update_line():
    """
    Some simple tests
    Expect output

    foobar()
    print(1 + 1)
       print(2, 3, 4)
    """
    print(update_line(""))
    print(update_line("foobar()"))
    print(update_line("print 1 + 1"))
    print(update_line("    print 2, 3, 4"))

    return 0

def test_update_pre_block():
    """
    Some simple tests
    Expected output:

    foobar()
    if foo():
       bar()
    print()
    print(1+1)
    print(2, 3, 4)
       print(a + b)
       print(23 * 34)
           print(1234)
    """
    print(update_pre_block(""))
    print(update_pre_block("foobar()"))
    print(update_pre_block("if foo():\n    bar()"))
    print(update_pre_block("print\nprint 1+1\nprint 2, 3, 4"))
    print(update_pre_block("    print a + b\n    print 23 * 34\n        print 1234"))

    return 0

def test_update_file():
    """
    Expected output
    table_updated.html and table_updated_solution.html are the same
    docs_updated.html and docs_updated_solution.html are the same
    """
    # A couple of test files
    update_file("table.html", "table_updated.html")
    update_file("docs.html", "docs_updated.html")
    #
    file_diff.compare_files("table_updated.html", "table_updated_solution.html")
    file_diff.compare_files("docs_updated.html", "docs_updated_solution.html")


def main():
    """
    main program to call test units
    :return:
    """
    print("")
    print("week4 project1\n")
    print("testing update_line():")
    test_update_line()

    print("")
    print("*********")
    print("testing update_pre_block():")
    test_update_pre_block()

    print("")
    print("*********")
    print("testing update_file():")
    test_update_file()

if __name__ == "__main__":
    main()


