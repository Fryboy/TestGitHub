#Example of showing the remainder
LargeNumber = int(input("Please enter a number larger than 1000"))
SmallNumber = int(input("Please enter a number smaller than 10"))

answer = LargeNumber//SmallNumber
#The floor division //

#Initial varibles declared
answer1 = LargeNumber%SmallNumber
#The remainder %
print(SmallNumber, "will go into the", LargeNumber, answer, "times and we will have", answer1, "as the remainder")
