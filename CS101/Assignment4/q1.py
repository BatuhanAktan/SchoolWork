"""
Creates a table based on the given information by the user about fruitfly population.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Sept 2020
"""


StartingFlies = int(input("Starting number of organisms: "))
AvgIncrease = int(input("Average daily increase (percentage): "))
leftToMultiply = int(input("Number of days to multiply: "))


print("\nDay Approximate \t | \t Population")
for i in range(leftToMultiply):
    
    print("-----------------------------------------------------------")
    print( str(i+1) + "\t\t\t | \t\t" + str(round(StartingFlies,4)))
    StartingFlies = StartingFlies * (1+(AvgIncrease/100))
