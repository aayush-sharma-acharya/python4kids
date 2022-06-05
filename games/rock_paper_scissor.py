import random
def rock_paper_scissors():
    mylist = ["r", "p", "s"]
    user_count = 0
    computer_count = 0
    while True:
        usr_command = input("Do you want to Continue? ").lower()
        if usr_command == "no" :
            print(f"You won {user_count} Times")
            print(f"Computer won {computer_count} Times")
            if computer_count > user_count:
                print("Overall Computer Won!")
            elif computer_count == user_count:
                print("Overall Tie")
            else:
                print("Overall You Won!")
            break
        else:
            print("Lets Start the game!")
            computer = random.choice(mylist)
            user = input("Enter R for rock , P for paper and S for scissor: ").lower()
            if user  not in mylist:
                continue
            print("Computer Choose : ",computer)
            print("You choose: ", user)
            if computer == "r" and user == "r":
                print("Its a Tie!")
            elif computer == "p" and user == "p":
                print("Its a Tie!")
            elif computer == "s" and user == "s":
                print("Its a Tie!")
            elif computer == "r" and user == "p":
                user_count += 1
                print("You win!")
            elif computer == "r" and user == "s":
                computer_count += 1
                print("You lose!")
            elif computer == "p" and user == "s":
                user_count += 1
                print("You win!")
            elif computer == "p" and user == "r":
                computer_count += 1
                print("You lose!")
            elif computer == "s" and user == "r":
                user_count += 1
                print("You win!")
            else:
                print("You lose!")
                computer_count += 1
rock_paper_scissors()