import random
score = 0
q_count = 0
level = input("Enter your difficulty: ").lower()

while True:
    usr_command = input("Do you want to play? ").lower()
    if usr_command == 'yes':
        print("Let's start the game!")
    else:
        fm = 10* q_count
        pm = fm*0.7
        print(f"\nFM: {fm}, PM: {pm} \n********** Your results **********\n")
        if score >= pm:
            print("")
            print("You passed!")
            print("Your score is: ",score)
            exit(1)
        else:
            print("You failed!")
            print("Your score is: ",score)
            exit(1)

    if level == 'easy':
        com = random.randint(1, 50)
        com2 = random.randint(1, 50)
    elif level == 'medium':
        com = random.randint(1,175)
        com2 = random.randint(1,175)
    elif level == 'hard':
        com = random.randint(1,300)
        com2 = random.randint(1,300)
    elif level == 'extreme':
        com = random.randint(1,500)
        com2 = random.randint(1,500)
    elif level == 'master':
        com = random.randint(1,750)
        com2 = random.randint(1,750)
    elif level == 'grandmaster':
        com = random.randint(1,1000)
        com2 = random.randint(1,1000)
    else:
        print("Invalid difficulty!")
        exit(1)

    q_count = q_count + 1
    t = input("Enter a symbol: ")
    if t == '+':
        com3 = com2 + com
    elif t == '-':
        if com2 < com:
            temp = com2
            com2 = com
            com = temp
        com3 = com2 - com
    elif t == '*' or t == 'X':
        com3 = com2 * com
    elif t == '//':
        com3 = com2 // com
    elif t == '/':
        com3 = com2 / com
        com3 = float(f"{com3:.2f}")
    else:
        print("Invalid symbole!")
        exit(1)

    print(f'What is {com2} {t} {com}')
    user = float(input("Enter the answer upto two decimal points: "))
    if user == com3:
        print("Your answer is correct!")
        score+=10
    else:
        print(f"Your answer is wrong and correct answer is {com3}")
        score-=5