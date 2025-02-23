import random

#generate random int between 0 and a 1000
random_int = random.randint(0,1000)
random_int = str(random_int)

print(random_int)
sum_digits = 0
for digits in random_int:
    sum_digits += int(digits)

print(sum_digits) 