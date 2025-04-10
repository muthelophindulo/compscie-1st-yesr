import random 

#assign sum to zero to be used later
sum_ = 0

#rONDOMLY GENERATE A NUMBER THAT WILL REPRESENT the number of numbers to sum
rand_num = random.randint(1,5)
print("\nthe number of numbers to sum is ",rand_num-1,"\n")
#no generate the number that will be summed
for i in range(1,rand_num):
    rand_int = random.randint(0,10)
    print("the numbers to be summed is: ",rand_int)
    sum_ += rand_int

print("\nthe sum of the nubers is: ",sum_)