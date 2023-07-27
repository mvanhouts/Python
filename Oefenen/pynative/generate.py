# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:13:34 2023

@author: mhouts
"""

#------------------------------------------------------------------------------
# Exercise 1 Generate 3 random integers between 100 and 999 which is divisible by 5
#------------------------------------------------------------------------------
import random
for x in range(3):
    print(random.randrange(100,999,5))
    
#------------------------------------------------------------------------------
# Exercise 2 Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
#------------------------------------------------------------------------------
import random

lotterylist = []
for x in range(100):
    lotterylist.append(random.randrange(0000000000,9999999999))    
    
print(random.sample(lotterylist, 2))

#------------------------------------------------------------------------------
# Exercise 3 Generate 6 digit random secure OTP
#------------------------------------------------------------------------------
import secrets
import random

otp = secrets.randbelow(1000000)
print(otp)

#------------------------------------------------------------------------------
# Exercise 4 Pick a random character from a given String
#------------------------------------------------------------------------------
import random

ranString = ('This is a random string')
print(random.choice(ranString))

#------------------------------------------------------------------------------
# Exercise 5 Generate random String of length 5
#------------------------------------------------------------------------------
import string
import random

def random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(result_str)
    
random_string(5)

#------------------------------------------------------------------------------
# Exercise 6 Generate a random Password which meets the following conditions
#------------------------------------------------------------------------------
import random

def random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(result_str)
    
random_string(10)

#------------------------------------------------------------------------------
# Exercise 7 Calculate multiplication of two random float numbers
#------------------------------------------------------------------------------
import random 

float1 = random.uniform(0.1, 1)
float2 = random.uniform(9.5, 99.5)
float3 = float1 * float2
print(float1)
print(float2)
print(float3)

#------------------------------------------------------------------------------
# Exercise 8 Generate random secure token of 64 bytes and random URL
#------------------------------------------------------------------------------
import secrets

print(secrets.token_hex(64))
print(secrets.token_urlsafe(64))

#------------------------------------------------------------------------------
# Exercise 8 Roll dice in such a way that every time you get the same number
#------------------------------------------------------------------------------
