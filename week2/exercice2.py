def left_right_chars(*files, numchars=1):
    char_list = []
    for file in files:
        with open(file) as f:
            for lines in f:
                beginning = [lines.rstrip()[:numchars]]
                end = [lines.rstrip()[-numchars:]]
    char_list.append(beginning)
    char_list.append(end)
    return char_list


left_right_chars('example.txt', 'example2.txt', numchars=3)

"""
Solution 
"""


def left_right_chars_old(*args, numchars=1):
    output = []
    for one_file in args:
        for one_line in one_file:
            output.append([one_line[:numchars],
                           one_line.rstrip()[-numchars:]])
    return output


"""
Solution with list comprehension - nested loops
explanation:

TIPS: write nested list comprehensions on multiple lines, 
-> The idea is that the "for" loops execute from top to bottom, and the output line (on top) 
will produce output once for each inner (lower) "for" loop.

We no longer need to define an "output" list, because we're creating a list via our list comprehension. 
We're first iterating over "args" (as before) and then iterating over "one_line in one_file", also as before. 
And we're even saying that the output expression, in the first line, will be a list containing two elements -- 
the first "numchars" characters from "one_line", and the final "numchars" characters from "one_line".
"""


def left_right_chars(*args, numchars=1):
    return [[one_line[:numchars], one_line.rstrip()[-numchars:]]
            for one_file in args
            for one_line in one_file]
