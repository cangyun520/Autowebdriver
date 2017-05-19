from random import Random
def random_str(randomlength=8, cycle=10):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwxyz123456789'
    length = len(chars) - 1
    random = Random()
    i =0
    while i< cycle:
        for i in range(randomlength):
            str += chars[random.randint(0, length)]
        return str
        i += 1


import random

print(random.randrange(1, 5))