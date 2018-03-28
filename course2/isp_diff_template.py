"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    # print("")
    # print("**** In singleline_diff ****")
    s_len = len(line1) if len(line1) < len(line2) else len(line2)
    # print("line 1:", line1)
    # print("line 2:", line2)
    # print("s_len :", s_len)
    for pos in range(s_len):
        if line1[pos] != line2[pos]:
            return pos
    if len(line1) != len(line2):
        return s_len

    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    # print ("s_d_f: {}, {}, {}".format(line1, line2, idx))
    len1 = len(line1)
    len2 = len(line2)
    # print ("l1_l2_i {} {} {}".format(len1, len2, idx))
    if (idx < 0) or (idx > len2) or (idx > len1):
        return ""
    if ("\n" in line1) or ("\r" in line1) or \
        ("\n" in line2) or ("\r" in line2):
        return ""
    o_str = "{}{}".format("="*idx,"^")
    # if line1 >= line2:
    return line1 + "\n" + o_str + "\n" + line2 + "\n"
    # else:
    #     return line1 + "\n" + o_str + "\n" + line2 + "\n"
    # return ""


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    s_len = len(lines1) if len(lines1)<len(lines2) else len(lines2)

    if len(lines1) == 0 and len(lines2) == 0:
        return (IDENTICAL, IDENTICAL)
    elif s_len == 0:
        return (0 , 0)
    # print("s_len: ", s_len)
    for line_num in range(s_len):
        # print("line_num: ", line_num)
        # print("1> {}: {}".format(line_num,lines1[line_num]))
        # print("2> {}: {}".format(line_num,lines2[line_num]))
        idx = singleline_diff(lines1[line_num], lines2[line_num])
        # print("idx ",idx)
        if idx != IDENTICAL:
            return (line_num, idx)

    if len(lines1) > len(lines2):
        return (len(lines2), 0)
    if len(lines1) < len(lines2):
        return (len(lines1), 0)

    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    in_file = open(filename, "rt")
    in_text = []
    # print("----------------------------")
    # print("----------------------------")
    for line in in_file.readlines():
        # print("raw line:",line)
        line = line.strip()
        # line.strip("\r")
        in_text.append(line)
    in_file.close()
    return in_text


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    dif_line, dif_pos = multiline_diff(lines1, lines2)
    # print("diff result: {}, {}".format(dif_line,dif_pos))
    if (dif_line, dif_pos) == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    # print(singleline_diff_format(lines1[dif_line], lines2[dif_line], dif_pos))
    rstr = "Line {}:\n".format(dif_line)
    line1 = ""
    line2 = ""
    if len(lines1) > 0:
        line1 = lines1[dif_line]
    if len(lines2) > 0:
        line2 = lines2[dif_line]
    # print(line1, line2)
    rstr = rstr + singleline_diff_format(line1, line2, dif_pos)
    return rstr

def main():
    """
    main, call functions from here
    """
    # str1 = "line1"
    # str2 = "line2"
    # str3 = "line3"

    # print (singleline_diff(str1, str2))
    # print ()
    # print (singleline_diff_format(str1, str2, singleline_diff(str1, str2)))
    # print ("1: \n", singleline_diff_format('abcdefg', 'abc', 5))
    # print ()
    print ("2: \n", singleline_diff_format('abcdefg', '', 0))

    # slst1 = [str1,str2]
    # slst2 = [str1,str2,str3]
    # print ()
    # print (multiline_diff(slst1,slst2))

    # print (file_diff_format("test.txt","test1.txt"))

    # file1 = "isp_diff_files/file1.txt"
    # file2 = "isp_diff_files/file2.txt"
    # file3 = "isp_diff_files/file3.txt"
    # file4 = "isp_diff_files/file4.txt"
    # file5 = "isp_diff_files/file5.txt"
    # file6 = "isp_diff_files/file6.txt"
    # file7 = "isp_diff_files/file7.txt"
    # file8 = "isp_diff_files/file8.txt"
    # file9 = "isp_diff_files/file9.txt"
    # file10 = "isp_diff_files/file10.txt"
    #
    # print (file_diff_format(file8, file9))

if __name__ == "__main__":
    main()
