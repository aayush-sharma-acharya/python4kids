import random
user_score = 0
computer_score = 0
hard = ["a","e","i","o","u"]
medium = ["a","e","i","o"]
easy = ["a","e","i"]
a = input("Enter mode E for easy M for medium and H for hard: ").lower()
if a == "e":
    n = easy
elif a == "m":
    n = medium
elif a == "h":
    n = hard
else:
    print("Invalid mode!")
    exit()

while True:
    usr_command = input("Do you want to continue? Enter Y for yes and N for no: ").lower()
    if usr_command == "n":
        print("\n*********** Your results ************\n")
        print("Your score is: ",user_score)
        print("computer_score is: ",computer_score)

        if user_score == computer_score:
            print("Overall Tie!")
        elif computer_score < user_score:
            print("You won Overall!")
        else:
            print("You lost Overall")
        break
    computer = random.choice(n)
    user = input("Enter a vowel letter: ").lower()
    if user == computer:
        print("You won!")
        user_score += 1
    else:
        print("You lost!")
        computer_score += 1
        


