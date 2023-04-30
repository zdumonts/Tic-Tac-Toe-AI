class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""
    def get_size(self): 
        return self.size
    def get_winner(self):
        return self.winner    
    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        index = valid_choices.index(cell)
        self.board[index] = sign
            
    def isempty(self, cell):
        # return True if the cell is empty (not marked with X or O)
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3',]
        index = valid_choices.index(cell)
        sign = self.board[index]
        if sign == ' ':
            return True
        else:
            return False
            
    def isdone(self):
        done = False
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X

        winning_conditions = [[0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 4, 8],[2, 4, 6]]

        for x in winning_conditions:
            a = self.board[x[0]]
            b = self.board[x[1]]
            c = self.board[x[2]]

            if (a == b == c) and (a == "X" or a == "O"):
                if a == "X":
                    done = True
                    self.winner = "X"
                    return done
                else:
                    done = True
                    self.winner = "O"
                    return done

        #check if game is a tie
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        tie_list = []

        for cell in valid_choices:
            if not self.isempty(cell) == True:
                tie_list.append(cell)

        if tie_list == valid_choices:
            self.winner = "TIE"
            done = True
            return done
        
    def show(self):
        # draw the board
        # need to complete the code
        print('   A   B   C') 
        print(' +---+---+---+')
        print('1| {} | {} | {} |'.format(self.board[0], self.board[3], self.board[6]))
        print(' +---+---+---+')
        print('2| {} | {} | {} |'.format(self.board[1], self.board[4], self.board[7]))
        print(' +---+---+---+')
        print('3| {} | {} | {} |'.format(self.board[2], self.board[5], self.board[8]))
        print(' +---+---+---+')

               
