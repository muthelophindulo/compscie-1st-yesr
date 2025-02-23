#the code inputs the radius and length of a cylinder then outputs the volume#
#inputs
radius = float(input("Enter the radius: "))
length = float(input("Enter the lenth: "))
pi = 3.14

'''
    area = radius^2 * pi
    volume = area * length
    constant pi = 3.14
'''
#to find the area
area = radius **2 * pi
volume = area * length



#print the outcomes
print(f"The area is: {area},and the volume is {volume}")
'''
    radius = 5.9
    length = 12
    output = "The area is: 109.30340000000001,and the volume is 1311.6408000000001"
'''
