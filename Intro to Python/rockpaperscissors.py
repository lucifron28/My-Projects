import random
while True:
    user_input = input("Enter 'Rock', 'Paper', 'Scissors or 'Quit' to exit: ").lower()
    choices = "rock", "paper", "scissors"
    while user_input not in choices and user_input != 'quit':
        print('Invalid input.')
        user_input = input("Enter 'Rock', 'Paper', 'Scissors or 'Quit' to exit: ").lower()
    
    computer = random.choice(choices)
    if user_input == 'quit':
        print("Bye!")
        break
    print(f"You: {user_input}")
    print(f"Computer: {computer}")
    if user_input == computer:
        print("It's a tie!")
    elif (
        (user_input == "rock" and computer == "scissors") or
        (user_input == "paper" and computer == "rock") or
        (user_input) == "scissors" and computer == ("paper")): 
        print("You win!")
    else:
        print("You lost!")