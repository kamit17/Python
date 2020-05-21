#You and your friend are in a team to write a two-player game, human against computer, such as Tic-Tac-Toe / Noughts and Crosses. Your friend will write the logic to play one round of the game, while you will write the logic to allow many rounds of play, keep score, decide who plays, first, etc. The two of you negotiate on how the two parts of the program will fit together, and you come up with this simple scaffolding (which your friend will improve later):


# your Friends will complete this function

def play_once(human_plays_first):
    """
    Must play ne round of the game . If the parameter is true, the human gets to play first, esle the computer gets to play first. When the round ends, the return value of the function is one of -1(human wins),0(game drawn),1(computer wins).
    """
    #This is all dummy scaffolding code right at the moment
    import ratdom
    rng = random.Random()
    #pick a random result between -1 and 1
    result = rng.randrange(-1,2)
    print("Human plays first = {0}, winner = {1}".format(human_plays_first,result))
    return result

# a) Write the main program which repeatedly calls this function to play the game, and
# after each round it announces the outcome as “I win!”, “You win!”, or “Game drawn!”.
# It then asks the player “Do you want to play again?” and either plays again, or says
# “Goodbye”, and terminates.


def play_game():
    """Function to call the function play_game"""
    n = input("Do you want to play a game?")

    while n == "Yes":
        play_once()
        print("You win","\n","Game drawn")

    else:
        print("Goodbye")
    return

play_game()

