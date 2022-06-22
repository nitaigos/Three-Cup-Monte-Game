from random import shuffle

# Game Functions
# This function mixes up the cups to make it harder to find the cup with the red ball
def shuffle_list(cup_list):
    shuffle(cup_list)
    return cup_list

# This function saves the player's guess
def player_guess():
    guess = ''
    
    # This loop makes sure that it will only accept the values of 1, 2, or 3 and no others
    while guess not in ['1', '2', '3']:
        guess = input("Pick a number: 1, 2, or 3. Your guess: ")
    
    # This turns the user values into index values for the list of cups
    if guess == '1':
        guess = '0'
    elif guess == '2':
        guess = '1'
    elif guess == '3':
        guess = '2'

    return int(guess)

# This function checks if the guess of the user is correct or incorrect
def check_guess(cup_list, guess):
    if cup_list[guess] == 'O':
        print('Correct!')
    else:
        print("Incorrect! Try again!")
        print("The correct answer was: ", cup_list)

# This function manages the interactions between the other functions
def three_cup_monte_game():
    while True:
        # Initial list
        cup_list = [' ', 'O', ' ']

        # Shuffling the list
        shuffled_cup_list = shuffle_list(cup_list)

        # Saving the guess of the playing
        guess = player_guess()

        # Checking if the player's guess is correct
        check_guess(shuffled_cup_list, guess)
        
        # Keep playing or take a break?
        if cup_list[guess] == 'O':
            choice = ''
        
            while choice not in ['play', 'break']:
                choice = input('Do you want keep playing or take a break? Type "play" to keep playing and "break" to take a break. Your choice: ')
            
            if choice == 'play':
                continue
            elif choice == 'break':
                break
    
    print("Thank you for playing!")

# Three cup monte game!
three_cup_monte_game()
