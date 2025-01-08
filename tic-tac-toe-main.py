BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

def print_board(board):
    RESET = '\033[0m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int):
                COLOR = RESET
            else:
                if board[row][col] == human:
                    COLOR = GREEN
                else:
                    COLOR = BLUE
            if col == 0:
                print(COLOR + str(board[row][col]) + RESET, end=' | ')
            else:
                if(col%3 == 0):
                    print(COLOR + str(board[row][col]) + RESET)
                else:
                    print(COLOR + str(board[row][col]) + RESET, end=' | ')
        print('\n---------')

def gameState(board):
    for i in range(3):
        # horizontal and vertical
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == human:
                return -1 # X won
            else:
                return 1 # O won
        elif board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == human:
                return -1 # X won
            else:
                return 1 # O won

        #diagnoal
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == human:
            return -1 # X won
        else:
            return 1 # O won
    else:
        # to check if the game can be still continued
        for i in range(3):
            for j in range(3):
                if isinstance(board[i][j], int):
                    return None
        # game ends no one won, its a draw
        return 0

def minimax(board, isMaximizing):
    score = gameState(board)
    # BASE CONDITION
    if score is not None:
        return score
    else:
        if isMaximizing:
            bestScore = float('-inf')
            for row in range(3):
                for  col in range(3):
                    if isinstance(board[row][col], int):
                        temp = board[row][col]
                        board[row][col] = ai  # AI
                        score = minimax(board, False)
                        board[row][col] = temp
                        if score > bestScore:
                            bestScore = score
            return bestScore
        else:
            # Minimizer
            bestScore = float('inf')
            for row in range(3):
                for col in range(3):
                    if isinstance(board[row][col], int):
                        temp = board[row][col]
                        board[row][col] = human   # Human
                        score = minimax(board, True)
                        board[row][col] = temp
                        if score < bestScore:
                            bestScore = score
            return bestScore

def bestMove(board):
    bestScore = float('-inf')
    bestMove = ()
    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int):
                temp = board[row][col]
                board[row][col] = ai
                score = minimax(board, False)
                board[row][col] = temp
                if score > bestScore:
                    bestScore = score
                    bestMove = (row, col)

    return bestMove

def checkWinner(a, states, board):
    if a is not None:
        gameStart = True
        print_board(board)
        print(states[a])
        return False
    else:
        return True

# Global Variables
ai = 'O'
human = 'X'
moves = [1,2,3,4,5,6,7,8,9]
def mainGame():
    board = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]
    # board = [['O', 'X', 3], 
    #         [4, 'X', 6], 
    #         [7, 'O', 'O']]
    states = {-1: 'X WONN!!', 1: 'O WONN!!', 0: 'ITS A DRAWW!!'}
    gameStart = True
    flag = False
    while gameStart:
        print_board(board)   # PRINTS THE BOARD
        try:
            choice = int(input("Mark your position (1-9): "))
        except:
            # handling alphabets and symbolical inputs
            print(RED + "Invalid choice" + RESET)
            continue

        if choice < 0 or choice > 9:
            # handling out of range values
            print(RED + 'Invalid choice!' + RESET)
            continue

        # making moves
        if choice not in moves:
            print(RED + 'Move is not available, try again' + RESET)
            continue
        else:
            for row in range(3):
                for col in range(3):
                    if board[row][col] == choice:
                        board[row][col] = human
                        moves.remove(choice)

        a = gameState(board)
        # Terminating game if someone won
        gameStart = checkWinner(a, states, board)
        if not gameStart:
            continue
        
        decision = bestMove(board)
        print("AI's Turn to play")
        i,j = decision[0], decision[1]
        moves.remove(board[i][j])
        board[i][j] = ai
        a = gameState(board)
        gameStart = checkWinner(a, states, board)

mainGame()
