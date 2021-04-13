"""
The user can play 2 player TicTacToe with tie and win detection
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Oct 2020
"""
import numpy as np

def newBoard():
    """
    This function creates a new TicTacToe board.
    Parameters: none.
    Return Value: Empty TicTacToe Board - a 2D List 
    """
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] 


def move(board, rowCol, character):
    """
    This function places the users character in their desired location.
    Parameters: board, rowCol, character - The current board is passed into the function as board a list, the users choice for the location is passed in as a tuple as rowCol and the character input is passed in as a str. . 
    Return Value: none.
    """
    row = int(rowCol[0])-1 
    col = int(rowCol[1])-1
    while True:
        if board[row][col] != ' ': # if the space is not empty asks them for another move.
            print("That move cannot be done Try again!")
            print(np.matrix(board))
            break
        else:
            board[row][col] = character # else assigns the character to that location.
            print("You Made your move.")
            print(np.matrix(board)) # displays the board as a matrix
            break

        
def winCon(board):
    """
    This function checks for a win, or a tie.
    Parameters: board - The current board is passed into the function.
    Return Value: True, False - Boolean values returning True if someone wins or there is a tie and false if those conditions are not met.
    """
    for i in board: # checking if any of the rows are full of the same character
        if i == ['x', 'x', 'x']:
          print("X wins")
          return True
        elif i == ['o', 'o', 'o']:
          print("O wins")
          return True
        else:
            colDiagCheck = []
            for i in range(len(board)):
                for j in range(len(board)):
                    colDiagCheck.append(board[j][i]) # adds columns into a list in order
            for i in range(len(board)):
                for j in range(len(board)):
                    if i == j:
                        colDiagCheck.append(board[j][i]) # adds the diagonal from top left to bottom right into that list as well
            colDiagCheck.append(board[0][2])
            colDiagCheck.append(board[1][1]) # adds the diagonal from top right to bottom left into that list
            colDiagCheck.append(board[2][0])
            colDiagCheck = [colDiagCheck[i:i + 3] for i in range(0, len(colDiagCheck), 3)] # divides the list into sublists of 3     
            if ['x', 'x', 'x'] in colDiagCheck: # checking if any of the sublists are full of the same character
              print("X wins")
              return True
            elif['o', 'o', 'o'] in colDiagCheck:
              print("O wins")
              return True
            if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2] : # if there is no space left and noone has won it must be a tie.
              print("Its a tie")
              return True
            else:
                return False

def main():
    """
    This function is where the user plays the game and can quit it.
    Parameters: none.
    Return Value: none.
    """
    while True:
      print("You can play a game of TicTacToe using this program. Whenever you would like to quit you can enter a negative number in the column section.")
      board = newBoard()
      print(np.matrix(board))
      while not winCon(board): # since winCon returns true whenever there is a win or a tie not winCon will keep this running.
          character = input("Please Input what character you would like to place (X/O): ")
          character = character.lower()
          if character == 'x' or character == 'o': # checking if the user put the right characters
              location = []
              row = int(input("Please input the row you would like to place that character in (1-3, 3 being bottom): "))
              col = int(input("Please input the column you would like to place that character in (1-3, 3 being most right): "))
              if col < 0: # ends the game
                print("Thank you for playing.")
                break
              if not 0<row<=3 or not 0<col<=3: # checking that the row and col are in range.
                  print("That is not a valid location, Please use values between 1-3 (inclusive)")
                  continue
              location.append(row)
              location.append(col) # adds row and col to location 
              location = tuple(location) # makes location a tuple
              move(board, location, character) # asks for a move
          else:
              print("That is not one of the options")
              continue
      print("If you would like to play again enter R otherwise press enter") # finally asks the user if they want to leave.
      decision = input("Your Decision: ")
      if decision.lower() == "r":
        continue
      else:
        break


main()

