#defiine a function:
#the parameters are two m and n
#we store the remeinder in r
# if the remeinder is not equal to 0
#we run the find_GCD of the r and n

def find_GCD(m,n):
    #determine how many times n goes to m
    goes = int(m/n)

    #store the remainder in r
    r = m % n

    #if r == 0 then the gcd is n
    if r == 0:
        print(f"therefor the GCD  for {m} and {n} is {n}")
        return n
    #if r does not equal to retry but with m = n and n = r
    elif r != 0:
        print(f"{m} goes {goes} times in {n} and the remainder is {r}")
        return find_GCD(n,r)
    #or else print that there is an error
    else:
        print("ERROR")
#test
find_GCD(27,7)
find_GCD(4,2)
find_GCD(48,16)
find_GCD(80,10)
find_GCD(27,9)

