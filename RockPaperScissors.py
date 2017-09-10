# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

again = "Yes"
while again == "Yes":
    p1 = input("Enter your move Player 1: ")
    p2 = input("Enter your move Player 2: ")

    while p1 == p2:
        print("Draw")
        p1 = input("Enter your move Player 1: ")
        p2 = input("Enter your move Player 2: ")

    if (p1 == "Rock" or p2 == "Rock") and (p1 == "Scissors" or p2 == "Scissors"):
        if p1 == "Rock":
            print("Congratulations Player 1, you win.")
        else:
            print("Congratulations Player 2, you win.")
    elif (p1 == "Paper" or p2 == "Paper") and (p1 == "Rock" or p2 == "Rock"):
        if p1 == "Paper":
            print("Congratulations Player 1, you win.")
        else:
            print("Congratulations Player 2, you win.")
    elif (p1 == "Scissors" or p2 == "Scissors") and (p1 == "Paper" or p2 == "Paper"):
        if p1 == "Scissors":
            print("Congratulations Player 1, you win.")
        else:
            print("Congratulations Player 2, you win.")

    again = input("Do you want to start a new game? ")