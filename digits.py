number = int(input("enter a number: "))
odd = []
even = []
mult = 1
#extract digits and order them arcodingly
while number > 0:
    #extracting the digit
    digit = number % 10
    
    #check which category the digit falls under and append it there
    if digit % 2 == 0:
        even.append(digit)
        
    else:
        mult *= digit
        odd.append(digit)
    
    #to remove the last digit that was extracted
    number //= 10
    
#for line 1 
print(f"new line number 1: {mult}")

# for line 2
t = ""
for num in even:
    #print(num,end='')
    t += str(num)
t = int(t) 
print(f"new line number 2: {t}")


#for line 3
if t > mult:
    results = t - mult
    print(f"new line number 3: {results}")
else:
    results = mult - t
    print(f"new line number 3: {results}")
