"""
You're to write a function, "scorecard", that takes a single argument.
 That argument will be a function that takes a single argument, and which returns a True or False value.
The "scorecard" function will ask the user for input.
 Its output will be a dict, "scores", with two key-value pairs.
 The keys will be the boolean "True" and "False", and the values will be integers.
 Each time the user enters input, one of three things will happen:
If you get an empty string as input from the user, return the "scores" dict.
If the result from running the user-supplied function on the user's input is True, then add 1 to the "True" key in "scores"
If the result from running the user-supplied function on the user's input is False, then add 1 to the "False" key in "scores".
"""


def scorecard(func):
    scores = {True: 0, False: 0}
    while True:
        s = input("Enter input: ").strip()

        if not s:
            return scores

        elif func(s):
            scores[True] += 1

        else:
            scores[False] += 1
