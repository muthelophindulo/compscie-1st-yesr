#this code generates different number and checks if the digits are the same or not
import random 

random_number = random.randint(10,1000)

print(f"random number is: {random_number}")

random_number_str = str(random_number)

has_repeated_digits = len(set(random_number_str)) < len(random_number_str)

if has_repeated_digits:
    print(f"the generated number has repeated digits")
else:
    print("No digits repeated")