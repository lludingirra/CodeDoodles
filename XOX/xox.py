print(f"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'##::::'##::'#######::'##::::'##:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(f"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. ##::'##::'##.... ##:. ##::'##::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(f":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. ##'##::: ##:::: ##::. ##'##:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(f"::::':::::::::::::::::::::::#######:'#######:'#######:'#######:'#######:::. ###:::: ##:::: ##:::. ###::::'#######:'#######:'#######:'#######:'#######::::::::::::::::::::::::::::")
print(f"........:........:........:........:........:........:........:........::: ## ##::: ##:::: ##::: ## ##:::........:........:........:........:........:........:........:.........")
print(f"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ##:. ##:: ##:::: ##:: ##:. ##::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(f":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ##:::. ##:. #######:: ##:::. ##:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(f"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..:::::..:::.......:::..:::::..::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

# Controls the main game loop to play multiple rounds
xox = True

# Dictionary to keep track of scores
scores = {"X": 0, "O": 0, "Tie": 0}

while xox :

    # Initialize the game board for a new game
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-",]

    # Valid string inputs for positions
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Game state variables for the current round
    game_still_going = True
    winner = None
    current_player = "X"

    def play_game() :
        # Display the initial empty board
        displey_board()
        
        # Main loop for a single game
        while game_still_going :
            # Handle turn for the current player
            handle_turn(current_player)
            
            # Check if the game has ended (win or tie)
            check_if_game_over()
            # Switch to the next player
            flip_player()
            
        # Print final game result and update scores
        if winner == "X" or winner == "O" :
            print(winner + " Won! \\_O_/ ")
            scores[winner] += 1 
        elif winner is None :
            print("It's a Tie! \\_O_/ \\_O_/")
            scores["Tie"] += 1
        
        # Display current total scores
        print(f"\nCurrent Score: X: {scores['X']} | O: {scores['O']} | Tie: {scores['Tie']}")

    def displey_board() :
        # Prints the current state of the Tic-Tac-Toe board
        print("\n")
        print(board[0] + " | " + board[1] + " | " + board[2] + "       1 | 2 | 3")
        print(board[3] + " | " + board[4] + " | " + board[5] + "       4 | 5 | 6")
        print(board[6] + " | " + board[7] + " | " + board[8] + "       7 | 8 | 9")
        print("\n")
            
    def handle_turn(player) :
        # Announce whose turn it is
        if player == "X" :
            print(player + "'s turn.")
            
        elif player == "O" :
            print(player + "'s turn.")
            
        valid = False
        while not valid :
            # Get player input for position
            position_input = input("Choose a number from 1 to 9: ") 
            
            try: # Attempt to convert input to integer
                position = int(position_input)
                # Check if the number is within the valid range (1-9)
                if str(position) not in numbers: 
                    print("Invalid input. Please choose a number from 1 to 9.")
                    continue 
            except ValueError: # Handle non-numeric input
                print("Invalid input. Please enter a number (1-9).")
                continue 

            # Convert 1-9 to 0-8 index
            position = int(position) - 1 
            
            # Check if the chosen spot on the board is empty
            if board[position] == "-" :
                valid = True
                
            else :
                print("That spot is taken. You can't choose that spot, choose again!")
                
        # Place the player's mark on the board
        board[position] = player
        displey_board() 
        
    def flip_player() :
        # Switch the current player (X to O, O to X)
        global current_player
        
        if current_player == "X" :
            current_player = "O"
        
        elif current_player == "O" :
            current_player = "X"
            
    def check_if_game_over() :
        # Calls functions to check for win or tie
        check_for_winner()
        check_for_tie()
        
    def check_for_winner() :
        # Checks all rows, columns, and diagonals for a win
        global winner
        global game_still_going
        
        row_winner = check_rows()
        column_winner = check_columns()
        diagonal_winner = check_diagonals()
        
        if row_winner :
            winner = row_winner
            game_still_going = False 
        elif column_winner :
            winner = column_winner
            game_still_going = False 
        elif diagonal_winner :
            winner = diagonal_winner
            game_still_going = False 
            
        else :
            winner = None # No winner yet
        
    def check_rows() :
        # Check if any of the three rows have a winner
        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"
        
        if row_1 or row_2 or row_3 :
            game_still_going = False
            
        if row_1 :
            return board[0]
        elif row_2 :
            return board[3]
        elif row_3 :
            return board[6]
        
        else :
            return None
            
    def check_columns() :
        # Check if any of the three columns have a winner
        columns_1 = board[0] == board[3] == board[6] != "-"
        columns_2 = board[1] == board[4] == board[7] != "-"
        columns_3 = board[2] == board[5] == board[8] != "-"
        
        if columns_1 or columns_2 or columns_3 :
            game_still_going = False
            
        if columns_1 :
            return board[0]
        elif columns_2 :
            return board[1]
        elif columns_3 :
            return board[2]
        
        else :
            return None
            
    def check_diagonals() :
        # Check if any of the two diagonals have a winner
        diagonals_1 = board[0] == board[4] == board[8] != "-"
        diagonals_2 = board[2] == board[4] == board[6] != "-"
        
        if diagonals_1 or diagonals_2:
            game_still_going = False
            
        if diagonals_1 :
            return board[0]
        elif diagonals_2 :
            return board[2]
        
        else :
            return None
            
    def check_for_tie() :
        # Check if all spots are filled and there is no winner
        global game_still_going
        
        if "-" not in board :
            game_still_going = False
    
    # Start a single game round
    play_game()
    
    # Loop to ask if the player wants to play again
    loop = True
    while loop :
        print()
        yes_no = input("Do you want to play a new game? Yes : e | No : h ")
        
        if yes_no == "e" :
            loop = False
            xox = True # Continue main loop for a new game
            
        elif yes_no == "h" :
            loop = False
            xox = False # Exit main loop
            print("Thanks for playing!")
            
        # Handle invalid input for replay choice
        else:
            print("Invalid input. Please enter 'e' or 'h'.")