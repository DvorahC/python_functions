"""
Your function should take:
Any number of filenames (yes, filenames -- here, file objects would be too hard)
Any number of key-value pairs, indicating which characters should be translated into other characters
An "extension" parameter, whose default value is "crypt"
The idea is that your function should take each file in the input, translate it according to the key-value pairs,
and then write the output to a new file -- whose name is the same as the original, plus the value of "extension".
For example, if I call:
    cryptogram('test.txt', 'test2.txt', a='e', e='i', i='o')

And if "test.text" is:
    This is a test.

    I'm testing it.

Then the output will be:
    Thos os e tist.

    I'm tistong ot.
"""


def cryptogrammer(*filenames, extension='.crypt', **pairs):
    table = str.maketrans(pairs)
    for one_filename in filenames:
        with open(one_filename) as infile, open(f'{one_filename}{extension}', 'w') as outfile:
            for one_line in infile:
                outfile.write(one_line.translate(table))
        print(f"Done with {one_filename}")
