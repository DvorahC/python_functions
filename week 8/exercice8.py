"""
First: I want you to write three simple functions:
mysum, which takes any number of numeric arguments and returns their sum
mean, which takes any number of numeric arguments and returns their arithmetic mean
sumofsquares, which takes any number of numeric arguments and returns the sum of each number's square

I then want you to write a function, "callafunc",
that asks the user to enter one of the function's names, followed by numbers separated by spaces.
For example, the user could write:
    mysum 10 20 30

or
    mean 10 20 30 40 50
"""


def mysum(*numbers):
    total = 0
    for one_number in numbers:
        total += one_number
    return total


def mean(*numbers):
    return mysum(*numbers) / len(numbers)


def sumofsquares(*numbers):
    return mysum(*[one_number * one_number
                   for one_number in numbers])


def callafunc():
    d = {'mysum': mysum,
         'mean': mean,
         'sumofsquares': sumofsquares}
    s = input("Enter input: ").strip()
    func_name, *args = s.split()
    if func_name in d:
        return d[func_name](*[int(x)
                              for x in args
                              if x.isdigit()])
    else:
        return f'{func_name} is not a known function.'
