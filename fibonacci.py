"""
def next_num(n):
    f0 = 0 
    f1 = 1 
    fnext = f0 + f1
    '''if f0 == 0 and f1 == 1:
        print(f0)
        print(f1)
        print(f1)'''
    while fnext < (n-1):
        temp = fnext
        f0 = f1
        f1 = temp

        fnext = f0 + f1
        '''print(fnext)'''
    print(fnext+f1)



#read a number from the user and check if it is in the fib or not

def is_fib(m):
    f0 = 0 
    f1 = 1 
    fnext = f0 + f1

    while fnext < m:
        temp = fnext
        f0 = f1
        f1 = temp
        fnext = f0 + f1
    if fnext != m:
        print("not a fib no")
    else:
        print("a fib no")


number = int(input(">"))
next_num(number)
no = int(input(">"))
is_fib(no)"""

#write a code that substract up until it reaches a nuber that is a fib then outputs a number in front

def next(n):
    #assign a and b to their initial values
    a = 0
    b = 1

    #sum the values
    c = a + b
    if n == 0:
        print(a)
        
    #check if the sum is less or equal to the value entered by the user
    while c < n:
        #if true  then swap the values to keep the loop going and generating the sequence
        a = b
        b = c
        #sum the swapped values
        c = a + b
    
    if c == n or n == 0:
        print(f"{n} is a fib number")
    elif c != n:
        print(f"{n} not a fib number!!\n")
    #if the value is now equal to the sum print the sum of the numbers last entered to give the first positive integer that is grater than n but not itself
    print("the next fib value after",n,"is",c)

#test
next(8)
next(100)
next(300)