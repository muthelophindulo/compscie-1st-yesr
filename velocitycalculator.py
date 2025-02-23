#inputs of the initial velocity of the car and its accelaration and time

initial_velocity = float(input("Enter the initial velocity of the car: "))

accelaration = float(input("Enter the accelaration of the car: "))

time = float(input("Enter the time: "))

#add everything up to produce the final velocity
#the formula is v(fianl) = v(initial) + accelaration * time

final_velocity = initial_velocity + accelaration * time

print(f"The final velocity of the car is {final_velocity}")

#initial_velocity = 15.4
#accelaration = 9.8
#time = 2.3
#output =  37.94
