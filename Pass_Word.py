#! /usr/bin/env python3

import random
import string

#print(f'New file')

characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters + string.ascii_lowercase

how_long = int(input("How long:"))
password = ''
for i in range(how_long):
    if i > how_long * .75:
        if not any(char in password for char in string.punctuation):
            letter = random.choice(string.punctuation)
            print(f'need special character: {letter}')
            password += letter
            i += 1
        if not any(char in password for char in string.digits):
            number = random.choice(string.digits)
            print(f'need number: {number}')
            password += number
            i += 1
    else:
        password += random.choice(characters)

print(f'Use this password if you dare: \n{password}')
