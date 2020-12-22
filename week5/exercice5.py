"""
[Weekly Python Exercise 2020 A2] Exercise #5 — Files by size:
The idea is to write a function that takes any number of open (for reading) file-like objects.
For each of these objects, you are to return a list of dictionaries. Each dictionary should contain two keys:
"name" (containing the filename)
"size" (the size, in characters)

The list of dicts should be sorted by file size, from smallest to largest.

Hint: You might want to write an additional function that creates the dict, based on the current file.

"""
import operator


def file_to_dict(file):
    my_d = dict()
    my_d.update({'name': file})
    size = my_d.__sizeof__()
    my_d.update({'size': size})
    return my_d


def file_sizes(*files):
    for file in files:
        dict_file = file_to_dict(file)
        t = sorted(dict_file, key=lambda el: el[1])
        return t


file_sizes('file1.txt', 'file2.txt')


def file_to_dict(one_file):
    size = 0
    for one_line in one_file:
        size += len(one_line)

    return {'name': one_file.name, 'size': size}


def file_sizes(*args):
    return sorted([file_to_dict(one_file)
                   for one_file in args], key=operator.itemgetter('size'))
