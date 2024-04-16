"""
    Tic Tac Toe Game
    Student Name: Shashank Pandey
    Student ID: 2408414
"""

import random
import os.path
import json
random.seed()

def draw_board(board):
    """
    Prints the tic tac toe board

    """

    print('\n')
    print('-------------')
    print('|', board[0][0], '|', board[0][1], '|', board[0][2], '|')
    print('-------------')
    print('|', board[1][0], '|', board[1][1], '|', board[1][2], '|')
    print('-------------')
    print('|', board[2][0], '|', board[2][1], '|', board[2][2], '|')
    print('-------------')
    print('\n')


def welcome(board):
    """
    Prints the welcome message.

        Parameters:
            board(list)
        
        Returns:
            None

    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted,enter the number corresponding to the square you want.")


def initialise_board(board):
    """
    Makes all elements of the board to one space '  '
    """
    for row in board:
        for col_index in range(len(row)):
            row[col_index] = ' '

    return board

def get_player_move(board):
    """
    Ask the user for the cell to put the X in, and return row and col

    """
    while True:
        print('\n')
        print("\t\t 1  2  3 ")
        print("\t\t 4  5  6 ")
        print("\t\t 7  8  9")
        square = int(input("Choose your square:"))

        if square not in [1,2,3,4,5,6,7,8,9]:
            square = 0
            print('Invalid input. Please enter a number between 1 and 9.')

        # Getting the row and col based on the square
        if square in [1,2,3]:
            row = 0
        elif square in [4,5,6]:
            row = 1
        elif square in [7,8,9]:
            row = 2

        if square in [1,4,7]:
            col = 0
        elif square in [2,5,8]:
            col = 1
        elif square in [3,6,9]:
            col = 2

        if board[row][col] != ' ' or square == 0:
            print('\nInvalid cell selected! Please input a valid cell.')
        else:
            break

    return row, col

def choose_computer_move(board):
    """
    It lets the computer choose a cell to put a nought in and return row and col
     
        Parameters:
            board(list)
        Returns: 
            tuple

    """
    empty_cells =[(i, j) for i in range(len(board))
                 for j in range(len(board)) if board[i][j] ==' ']
    if empty_cells:
        row,col=random.choice(empty_cells)
    else:
        row,col=None,None
    return row,col

def check_for_win(board, mark):
    """
    To check if either the player or the computer has won

    """
    # checks for rows
    for i in range(len(board)):
        if all(board[i][j] == mark for j in range(len(board))):
            return True
    # checks for column
        if all(board[j][i] == mark for j in range(len(board))):
            return True
    # checks diagonally to see for the win.
    if (board[0][0] == board[1][1] == board[2][2] == mark or
        board[0][2] == board[1][1] == board[2][0] == mark):
        return True
    return False

def check_for_draw(board):
    """
    Checks for the draw condition

    """
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game(board):
    """
    Code to start to play the game 
        Parameter:
            board[list]
        Return
            (int)

    """
    print('\n Game Begins 🎮')
    initialise_board(board)
    draw_board(board)

    while 1:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print('Congratulations! You Won 🎊')
            return 1
        if check_for_draw(board):
            print('Draw!')
            return 0

        print("Computer's Turn:")
        row, col = choose_computer_move(board)
        board[row][col] = '0'
        draw_board(board)

        if check_for_win(board, '0'):
            print('Sorry, Computer Won this round!')
            return -1

        if check_for_draw(board):
            print('Draw!')
            return 0

    return 0

def menu():
    """
    Prints the menu and ask for the user choice

        Parameters:
            None
        
        Returns:
            str: The user's choice as a string

    """

    print('\n Enter any one of the following instructions:')
    print('\t\t 1- Play Game')
    print('\t\t 2- Save your score in the leaderboard')
    print('\t\t 3- Load and display the leaderboard')
    print('\t\t q- End the program')

    choice=input("\n 1, 2, 3 or q? ")
    return choice

def load_scores():
    """
    Opens the leaderboard file and return the scores in a Python dictionary

    """
    filename='leaderboard.txt'

    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                leaders = json.load(file)

        except json.JSONDecodeError:
            leaders = {}
    else:
        leaders = {}

    return leaders

def save_score(score):
    """
    Opens the leaderboard files and save the score of user in that file

    """
    if not score:
        score = 0

    name = input("Please enter your name: ")
    filename = 'leaderboard.txt'

    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                leaders = json.load(file)

        except json.JSONDecodeError:
            leaders = {}
    else:
        leaders = {}

    leaders[name] = score

    with open(filename, 'w') as file:
        json.dump(leaders, file)
        print('Leaderboard updated!!')

def display_leaderboard(leaders):
    """
    Prints the leaderboard from the leaderboard.txt file

            Parameters:
                    score (int)

            Returns:
                    None
    """
    
    leaders_list = list(leaders.items())
    sorted_leaders = []

    while leaders_list:
        high_score = leaders_list[0]

        for item in leaders_list:
            if item[1] > high_score[1]:
                high_score = item

        leaders_list.remove(high_score)
        sorted_leaders.append(high_score)

    for item in sorted_leaders:
        print(f"{item[0]}: {item[1]}")