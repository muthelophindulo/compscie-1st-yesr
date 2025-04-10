#get the number of judges from the user
number_of_judges = int(input("enter the number of judges: "))

sum_scores = 0

largest_score = -9999999
lowest_score = 9999999

#now the user has to assign a score for each judge
for scores in range(number_of_judges):
    score = int(input("enter a score between 0 and 10: "))
    #do this to ignore the largest and smallest number from being added to the um
    if score > largest_score:
        largest_score = score
    elif score < lowest_score:
        lowest_score = score
        #if the number is not large or small then add it to the sum
    else:
        sum_scores += score
print(f"the total score is: {sum_scores}\n")

#to get the avarage you ignore the score given by the two judges which is the highest and the loweat one the divide by the total number of judges left
print(sum_scores // (number_of_judges-2) )

print(f"\nthe lowest number is: {lowest_score} and the smallest number is: {largest_score}")