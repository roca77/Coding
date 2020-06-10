import copy
import random

# Setting a board with an empty list of list

board = [
    ['','',''],
    ['','',''],
    ['','','']
]

# A function to display the board
def displayboard(board):
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])

# A function to take input from user, validate entry, and prompt for a new choice

def taking_input(board, player_letter):
    try:
      position = int(input("Maichata, Please enter a number between 1-9: "))
      position = position - 1
      selection = (position // 3, position % 3)
      if (8 >= position) and (position >= 0) and (board[selection[0]][selection[1]] == ''):
        board[selection[0]][selection[1]] = player_letter
        return
      else:
        print("Try another position; this is already used!")      
    except ValueError:
        print("You can only pick numbers between 1-9. Try again!")

# AI function that allows Computer to make moves
def computer_move(board, computer_letter, human_player_letter):

    open_positions = openposition(board)
    temporary_board = copy.deepcopy(board)
    middle_position = board[1][1]
    #random_position = random.choice(open_positions)

    for position in open_positions:
        move_to_position(temporary_board, computer_letter, position)
        if is_winner(temporary_board, computer_letter)==True:
            move_to_position(board, computer_letter, position)
            displayboard(board)
            break
        else:    
            temporary_board = copy.deepcopy(board)
            # Blocking move
            move_to_position(temporary_board, human_player_letter, position)
            if is_winner(temporary_board, human_player_letter)==True:
                move_to_position(board, computer_letter, position)
                displayboard(board)
                break
            elif (1,1) in open_positions:
                # Middle position
                temporary_board = copy.deepcopy(board)
                board[1][1]=computer_letter
                displayboard(board)
                break
            elif position in [(0,0),(0, 2), (2, 0), (2, 2)]:
                temporary_board = copy.deepcopy(board)
                move_to_position(board, computer_letter, position)
                displayboard(board)
                break
            else:
                #board[random_position[0]][random_position[1]]=computer_letter
                temporary_board = copy.deepcopy(board)
            
# A function to find available position
def openposition(board):
  openp = []

  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j]=='':
        openp.append((i, j))
  return(openp)

# A function to move to specific position
def move_to_position(board, letter, position):
    board[position[0]][position[1]]= letter

# A function to randomly pick who goes first
def who_goes_first():
    if random.randint(0, 1)==0:
        return 'human_player'
    else:
        return 'computer'  

# Ask human player to be either X or O
def choose_player_letter():
    letter = ''
    while (letter not in ['X', 'O']):
        letter = input('Do you want to be X or O?\n').upper()
    return letter

# a function to tell if there is a tie or if the game should continue
def game_tie(openp):
    if len(openp) < 2:
        return True
    else:
        return False

def is_winner(board, current_player):
    if board[0][0] == board[0][1] == board[0][2]==current_player or board[1][0]==board[1][1]==board[1][2]==current_player or board[2][0]==board[2][1]==board[2][2]==current_player or board[0][0]==board[1][1]==board[2][2]==current_player or board[0][2]==board[1][1]==board[2][0]==current_player or board[0][0]==board[1][0]==board[2][0]==current_player or board[0][1]==board[1][1]==board[2][1]==current_player or board[0][2]==board[1][2]==board[2][2]==current_player:
        return True
    else:
        return False


def play_game():
    while True:
        turn = who_goes_first()
        print('The ' + turn + ' will go first')

        human_player_letter = choose_player_letter()
        if human_player_letter == 'X':
            computer_letter ='O'
        else:
            computer_letter = 'X'

        game_on = True

        while(game_on):
            if turn == 'human_player':
                taking_input(board, human_player_letter)
                displayboard(board)
                if is_winner(board, human_player_letter)==True:
                    print(human_player_letter +" wins this tic tac toe game!")
                    displayboard(board)
                    game_on= False
                    break
                elif game_tie(board) == True:        
                    print("This game is a draw between the players. Start a new game.")
                    game_on= False
                else:
                    turn = 'computer'      
            elif turn == 'computer':
                computer_move(board, computer_letter, human_player_letter)
                if is_winner(board, computer_letter)==True:
                    print(computer_letter + " wins this tic tac toe game!")
                    game_on= False
                    break
                elif game_tie(board) == True:        
                    print("This game is a draw between the players. Start a new game.")
                    game_on= False
                else:
                    turn = 'human_player'
                    


play_game()