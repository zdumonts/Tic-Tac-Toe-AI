from math import inf
from random import choice

class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X
    def get_sign(self):
        # return an instance sign
        return self.sign
    def get_name(self):
        # return an instance name
        return self.name
    def choose(self, board):
        # prompt the user to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.isempty(cell), and board.set(cell, sign)
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        while True: 
            cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper()
            if cell in valid_choices:
                if board.isempty(cell):
                    board.set(cell, self.sign)
                    break
                else:
                    print("Please choose a different cell")          
            else:
                print("You did not choose a valid cell")

class AI (Player):
    def __init__(self, name, sign, board):
        super().__init__(name, sign)
        self.board = board

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def choose(self, board):

            # iterates through all possible moves and makes a list, valid_choices, with all the valid moves that are currently possible in the play
            all_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            
            valid_choice = []

            for choicee in all_choices:
                  if board.isempty(choicee):
                        valid_choice.append(choicee)

            # uses the choice operator from the random module to randomly pick one valid choice move
            ai_choice = choice(valid_choice)


            board.set(ai_choice, self.sign) # exexute the move with the random choice move

class MiniMax(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)
    
    def get_sign(self):
        # return an instance sign
        return self.sign
    
    def get_name(self):
        # return an instance name
        return self.name
    
    def minimax(self, board, Maximum): # Maximum is boolean 

        #1. Check the base case: if the game is over, then return -1 if self lost, 0 if it is a tie, or 1 if self won.
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == "TIE":
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1

        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        for cell in valid_choices:
            if board.isempty(cell):
                if Maximum:
                    maxscore = -inf
                    board.set(cell, self.sign)
                    score = self.minimax(board, False) # recursive call
                    board.set(cell, ' ') # set the board cell back to blank
                    if score > maxscore: # save the best score
                        maxscore = score
                    return maxscore
                else:
                    minscore = inf
                    other_sign = 'O' if self.sign == 'X' else 'X'
                    board.set(cell, other_sign)
                    score = self.minimax(board, True) # recursive call 
                    board.set(cell, ' ') # set the board cell back to blank
                    if score < minscore: # save the best score
                        minscore = score
                    return minscore

    def choose(self, board):
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        highscore = -inf
        bestMove = ""

        for cell in valid_choices:
            if board.isempty(cell): # iterate through every single valid choice on the board
                board.set(cell, self.sign) # set the board cell to AI's sign
                score = self.minimax(board, False) # recursive call
                board.set(cell, ' ') # set the board cell back to blank
                if score > highscore: # save the best score and move
                    highscore = score
                    bestMove = cell

        board.set(bestMove, self.sign) # execute the move with the best score

    
                        
                  
