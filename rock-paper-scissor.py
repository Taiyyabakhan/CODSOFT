from random import randint
options = ["Rock", "Paper", "Scissors"]
player = False

while not player:

    player = input("Rock, Paper, Scissors? (or type 'quit' to exit): ").capitalize()
    
    if player == "Quit":
        print("Thanks for playing!")
        break

    computer = options[randint(0, 2)]
    
    if player in options:
        if player == computer:
            print(f"Tie! Both chose {player}.")
        elif player == "Rock":
            if computer == "Paper":
                print(f"You lose! {computer} covers {player}.")
            else:
                print(f"You win! {player} smashes {computer}.")
        elif player == "Paper":
            if computer == "Scissors":
                print(f"You lose! {computer} cuts {player}.")
            else:
                print(f"You win! {player} covers {computer}.")
        elif player == "Scissors":
            if computer == "Rock":
                print(f"You lose! {computer} smashes {player}.")
            else:
                print(f"You win! {player} cuts {computer}.")
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
