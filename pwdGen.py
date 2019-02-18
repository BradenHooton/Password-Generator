#Password Generator

import random

vals[] = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+=:;?><.,0123456789"

len = input('How long do you need the password to be?')
length = int(len)

pwd = ""

for i in range (length):
    pwd += random.choice(vals)
print(password)