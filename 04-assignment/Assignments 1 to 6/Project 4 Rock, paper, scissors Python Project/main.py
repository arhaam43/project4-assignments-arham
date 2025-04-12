import random

#introduction
print("Weclcome to the Rock, Paper and Scissor Game!")
print("You will play against the computer. Lets Start!")

#choices list
choices = ["rock", "paper", "scissor"]

while True:
    user_choice = input("Enter your choice (rock, paper or scissor or 'quit' to stop)").lower()

    if user_choice == 'quit':
        print("Thanks for playing| Goodbye|")
        break
    #validate your choice
    if user_choice not in choices:
        print("invalid choice! please choose rock, paper, or scissor.")
        continue

    #generate computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    #result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
    (user_choice == "scissor" and computer_choice == "paper") or \
    (user_choice == "paper" and computer_choice == "rock"):
        print("You WIN!")
    else:
        print("Computer WIN!")
    
