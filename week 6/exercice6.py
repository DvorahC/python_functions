"""
This week, I want to write a function that will do the same thing, but for one or more directories.
That is: write a function, dir_sizes, that takes any number of directory names (strings) as arguments.

The function will return a single dictionary.
That dict's keys will be the directory names passed as arguments.
The corresponding values will be the result of calling file_sizes on that directory name.
 You should ignore anything but regular files; don't descend into subdirectories.
"""

import operator
import pathlib


def file_to_dict(one_path):
    size = 0
    for one_line in one_path.open('rb'):
        size += len(one_line)
    return {'name': one_path.name, 'size': size}


def file_sizes(*args):
    return sorted([file_to_dict(pathlib.Path(one_filename))
                   for one_filename in args], key=operator.itemgetter('size'))


def dirname_to_files(dirname):
    return [one_path
            for one_path in pathlib.Path(dirname).glob('*')
            if one_path.is_file()]


def dir_sizes(*args):
    return {one_dirname: file_sizes(*dirname_to_files(one_dirname))
            for one_dirname in args}
