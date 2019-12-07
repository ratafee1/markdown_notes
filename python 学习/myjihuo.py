import random
import string

# class lengthError(ValueError):
#    def __init__(self, arg):
#       pass
#
# a = lengthError("jii")
# print(a)
#
# class aa(str):
#     pass
#
# a = aa("223")
# print(a)


# import  random
# print(random.choice(50))

# print(string.ascii_letters)
# print(string.digits)
#
#
# print([i*i for i in range(1, 11)])
#
# random_codes = lambda x, y: ''.join([random.choice(x) for i in range(y)])
#
# a=random_codes('123456789',5)
#
# print(type(a))

import random, string


class LengthError(ValueError):
    def __init__(self, arg):
        self.args = arg


def pad_zero_to_left(inputNumString, totalLength):
    lengthOfOutput = len(inputNumString)
    if lengthOfOutput > totalLength:
        raise LengthError("the length of input is greater than the total \ length")
    else:
        return '0' * (totalLength - lengthOfOutput) + inputNumString


poolOfChars = string.ascii_letters + string.digits
random_codes = lambda x, y: "".join([random.choice(x) for i in range(y)])


def invitation_code_generator(quantity, lengthOfRandom, lengthOfKey):
    placeHolderChar = 'L'

    for index in range(quantity):
        try:
            yield random_codes(poolOfChars, lengthOfRandom) + placeHolderChar + \
                  pad_zero_to_left(str(index), lengthOfKey)

        except LengthError:
            print("Index exceeds the length of key")


for invitationCode in invitation_code_generator(70, 8, 5):
    print(invitationCode)

# def Fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         # print b
#         a, b = b, a + b
#         n = n + 1
#
#
# for n in Fab(5):
#     print(n)
