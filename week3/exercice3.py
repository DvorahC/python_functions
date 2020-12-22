"""
write a function that takes a writable file-like object as a first argument.
That'll be the file into which we write our output.
All other arguments should be passed as kwargs, in "name=value" format.
What will we be passing in this "name=value" format?  The names of people in your family, along with their ages.
ex: family_ages('ages.txt', reuven=48, atara=18, shikma=16, amotz=13)
The result of the above call would be to write into the file "ages.txt", with the following output:
    reuven,48
    atara,18
    shikma,16
    amotz,13
    I should add that this would be the order, from eldest to youngest
"""
from _operator import itemgetter


def family_ages(output_file, **family):
    sorted_family = sorted(family.items(), key=lambda member: member[1], reverse=True)
    with open(output_file, 'w') as f:
        for name, age in sorted_family:
            f.write(f"{name},{age}\n")


family_ages('my_family.txt', dvorah=35, sarah=24, rebecca=33)


# solution:
def family_ages2(f, **kwargs):
    for name, age in sorted(kwargs.items(), key=itemgetter(1), reverse=True):
        f.write(f'{name},{age}\n')
