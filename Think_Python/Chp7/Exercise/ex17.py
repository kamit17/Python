#You and your friend are in a team to write a two-player game, human against computer, such as Tic-Tac-Toe / Noughts and Crosses. Your friend will write the logic to play one round of the game, while you will write the logic to allow many rounds of play, keep score, decide who plays, first, etc. The two of you negotiate on how the two parts of the program will fit together, and you come up with this simple scaffolding (which your friend will improve later):


# your Friends will complete this function

def play_once(human_plays_first):
    """
    Must play ne round of the game . If the parameter is true, the human gets to play first, esle the computer gets to play first. When the round ends, the return value of the function is one of -1(human wins),0(game drawn),1(computer wins).
    """
    #This is all dummy scaffolding code right at the moment
    import random
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
    human = 0   # counter to keep score
    computer = 0
    draws = 0
    games = 0  # counter to keep games played

    while n == "Yes":
        for i in (True,False):    #add logic so that players take turn first
            outcome = play_once(i)
            if outcome == -1:
                human += 1 # counter to keep score
                games += 1 # counter to keep games played
                percentage_won = (human /games) * 100  # percentage of wins for human
                print("you win" "\n"
                      "your score: ",human,
                      "My Score: ",computer,
                      "Draws: ",draws,"\n",
                      'You won ',percentage_won, '% of all games palyed!')
                n = input('Do you want to play again? ')
            elif outcome == 0:
                draws += 1
                games += 1
                percentage_won = (human/games) * 100
                print("you win" "\n"
                      "your score: ",human,
                      "My Score: ",computer,
                      "Draws: ",draws,"\n",
                      'You won ',percentage_won, '% of all games palyed!')
                n = input('Do you want to play again? ')
                
            elif outcome == 1:
                draws += 1
                games += 1
                percentage_won = (human/games) * 100
                print("you win" "\n"
                      "your score: ",human,
                      "My Score: ",computer,
                      "Draws: ",draws,"\n",
                      'You won ',percentage_won, '% of all games palyed!')
                n = input('Do you want to play again? ')

            else:
                print("Goodbye")
            return 


play_game()

