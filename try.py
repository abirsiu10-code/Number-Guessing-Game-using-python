import random
computer = random.choice([-1, 0, 1])
coreDict = {"s": -1,
            "w" : 0,
            "g" : 1}
rev_coreDict = {-1: "Snake",
                0: "Water",
                1: "Gun"}
your_choice = coreDict[input("Enter your choice: ")]
print(f"You chose {rev_coreDict[your_choice]}\nComputer chose {rev_coreDict[computer]}")
if (computer == your_choice):
    print("It's a draw")

else :
    if((computer-your_choice)== -1 or (computer-your_choice)==2):
        print("You lose")
    else:
        print("You win")