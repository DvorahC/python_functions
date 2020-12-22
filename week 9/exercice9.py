"""
 Write a function that asks the user to enter, on one line, the name of a city and the temperature in that city.
 When the user enters an empty string, the we break out of a loop and return a result.
 If the user enters more than one word,
 then the final word in the string is taken to be the temperature, and everything before it is considered to be the name of a city.
So if the user enters:
    Boston 15
then we'll understand that it was 15 degrees in Boston.  But if the person writes
    New York 20
then we should understand it was 20 degrees in New York.
Assuming that the temperature is numeric (i.e., can be turned into an integer),
I want you to add the temperature to a dictionary in which the keys are city names and the values are lists of integers,
representing all of the temperatures that the user has entered.
Meaning, if the user enters:
    A 10
    B 20
    A 15
    B 17
    A 13
    C 25
    B 20
The result should be a dictionary that looks like:
    {'A':[10, 15, 13], 'B':[20, 17, 20], 'C':[25]}
You should create the above using a "defaultdict",
which will (I believe) make the addition of new temperatures more elegant, and the code more readable.

But is that what the function should return?
Of course not; that would be too easy!
I want you to use a dict comprehension to turn the above dictionary into one that has the same keys,
but whose values contain the mean of each list.  In other words, given the above accumulation of temperatures, the function will return:
    {'A': 12.6, 'B': 19, 'C': 25}
"""
from collections import defaultdict


def mean(numbers):
    return sum(numbers) / len(numbers)


def average_city_temps():
    all_temps = defaultdict(list)
    while True:
        s = input("Enter a city and temperature: ").strip()
        if not s:
            break
        if ' ' not in s:
            print("No whitespace; enter a city and temp!")
            continue
        city, temp = s.rsplit(None, 1)
        if not temp.isdigit():
            print(f"{temp} is not a valid temperature")
            continue
        all_temps[city].append(int(temp))
    return {city: mean(temps)
            for city, temps in all_temps.items()}
