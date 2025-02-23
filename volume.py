#the code inputs the radius and length of a cylinder then outputs the volume#
#inputs
radius = float(input("Enter the radius: "))
length = float(input("Enter the lenth: "))
pi = 3.14

'''the formulas
    area = radius^2 * pi
    volume = area * length
    constant pi = 3.14
'''
#to find the area
area = radius **2 * pi
volume = area * length

#print the outcomes
print(f"The area is: {area},and the volume is {volume}")

