"""
printable(): string of characters which are considered printable.

"""
import string    # .printable()
import random
import pickle

def genPass(n):
    password = " "

    for i in range(n):
        int = random.randint(10,34)
        password += string.printable[int]
    return password


# print (genPass(6))
# print(string.printable)

"""
saves password as a txt file 
"""
def savePass(passkey):
    password = []
    try:
        with open(passkey,'wb') as password_file:
            pickle.dump(password,password_file)
    except pickle.PickleError as peer:
        print('pickle error'+str(peer))

savePass(genPass(6))

"""
return save passwords
"""

