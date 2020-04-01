Animals = 0
#Set variable Animals to 0
answer = "y"
#set the answer to y

while answer == "y":
#while loop to contiune while the condition is met
    answer = input("There is one animal on the list you want to add another to the list  y/n")
    Animals = Animals + 1
    print(str(Animals)+ " Animals on the list ")


print("You have no more Animals to add")
