#!/usr/bin/python

import sys

"""
Create a Tic Tac Toe Program
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/04-Milestone%20Project%20-%201


Step 1 - Create Board
Step 2 - Accept input from user in form of X or O
Step 3 - Allow keypad entry (1-9) to Display Mark on Board
STep 4 - Display Board with X and O marks
Step 5 -

"""

board_values = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


class TicTacToe():
    '''
    TicTacToe Class
    Arguments:  <player>, <position>

    CLASS - Template for creating object
    OBJECT - An instance of a ClASS
    INSTANTIATE - Create an instance of a CLass
    METHOD - A function defined in a class
    ATTRIBUTE - a variable bound to an instance of a class

    '''

    def __init__(self, player='X', position=0):
        self.current_player = player
        self.position = position
        self.move_count = 0
        self.count = 0
        self.columns = 0
        self.rows = 0
        #assert isinstance(player, object)



    def gen_board(self):
        self.rows = 0
        while self.rows < 3:
            print("   |   |   ")
            print(" {} | {} | {} ".format(board_values[self.rows][0],board_values[self.rows][1],board_values[self.rows][2]))
            print("   |   |   ")
            if self.rows < 2:
                print("------------")
            self.rows += 1



    def set_player(self):
        while True:
            select_player = input("Please select player to start [X or O]: ")
            if select_player == 'X' or select_player == 'O':
                self.current_player = select_player
                print(self.current_player) # has value entered
                break


    def set_next_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
            return 'O'
        else:
            self.current_player = 'X'
            return 'X'


    def set_location(self):

        while True:
            select_block = input("Please Select Square: ")
            if select_block != 'q' and int(select_block) in range(0,10) and self.move_count < 9:
                if int(select_block) == 7:
                    if board_values[0][0] == ' ':
                        board_values[0][0] = self.current_player
                        self.move_count += 1
                        break
                    else:
                        print("This block already has a value - please choose another square")
                elif int(select_block) == 8:
                    if board_values[0][1] == ' ':
                        board_values[0][1] = self.current_player
                        self.move_count += 1
                        break
                    else:
                        print("This block already has a value - please choose another square")
                elif int(select_block) == 9:
                    if board_values[0][2] == ' ':
                        board_values[0][2] = self.current_player
                        self.move_count += 1
                        break
                    else:
                        print("This block already has a value - please choose another square")
                elif int(select_block) == 4:
                    if board_values[1][0] == ' ':
                        board_values[1][0] = self.current_player
                        self.move_count += 1
                        break
                    else:
                        print("This block already has a value - please choose another square")
                elif int(select_block) == 5:
                    if board_values[1][1] == ' ':
                        board_values[1][1] = self.current_player
                        self.move_count += 1
                        break
                    else:
                        print("This block already has a value - please choose another square")
                elif int(select_block) == 6:
                    if board_values[1][2] == ' ':
                        board_values[1][2] = self.current_player
                        self.move_count += 1
                        break
                    else:
                        print("This block already has a value - please choose another square")
                elif int(select_block) == 1:
                    if board_values[2][0] == ' ':
                        board_values[2][0] = self.current_player
                        self.move_count += 1
                        break
                    else:
                        print("This block already has a value - please choose another square")
                elif int(select_block) == 2:
                    if board_values[2][1] == ' ':
                        board_values[2][1] = self.current_player
                        self.move_count += 1
                        break
                    else:
                        print("This block already has a value - please choose another square")
                elif int(select_block) == 3:
                    if board_values[2][2] == ' ':
                        board_values[2][2] = self.current_player
                        self.move_count += 1
                        break
                    else:
                        print("This block already has a value - please choose another square")
            elif select_block == 'q':
                quit()
                #sys.exit()
            else:
                break


    def calc_tictactoe(self):
        self.rows = 0
        self.columns = 0
        for x in range(0,3):
            if board_values[x][self.columns] == 'O' and board_values[x][self.columns + 1] == 'O' and board_values[x][self.columns + 2] == 'O':
                print("Congratulations Player {}, You have Won TicTacToe!".format(self.current_player))
                return True
            elif board_values[x][self.columns] == 'X' and board_values[x][self.columns + 1] == 'X' and board_values[x][self.columns + 2] == 'X':
                print("Congratulations Player {}, You have Won TicTacToe!".format(self.current_player))
                return True
            elif board_values[self.rows][x] == 'O' and board_values[self.rows + 1][x] == 'O' and board_values[self.rows + 2][x] == 'O':
                print("Congratulations Player {}, You have Won TicTacToe!".format(self.current_player))
                return True
            elif board_values[self.rows][x] == 'X' and board_values[self.rows + 1][x] == 'X' and board_values[self.rows + 2][x] == 'X':
                print("Congratulations Player {}, You have Won TicTacToe!".format(self.current_player))
                return True
            elif board_values[x][x] == 'O' and board_values[x + 1][x + 1] == 'O' and board_values[x + 2][x + 2] == 'O':
                print("Congratulations Player {}, You have Won TicTacToe!".format(self.current_player))
                return True
            elif board_values[x][x] == 'X' and board_values[x + 1][x + 1] == 'X' and board_values[x + 2][x + 2] == 'X':
                print("Congratulations Player {}, You have Won TicTacToe!".format(self.current_player))
                return True
            elif board_values[x + 2][x] == 'O' and board_values[x + 1][x + 1] == 'O' and board_values[x][x + 2] == 'O':
                print("Congratulations Player {}, You have Won TicTacToe!".format(self.current_player))
                return True
            elif board_values[x + 2][x] == 'X' and board_values[x + 1][x + 1] == 'X' and board_values[x][x + 2] == 'X':
                print("Congratulations Player {}, You have Won TicTacToe!".format(self.current_player))
                return True
            else:
                return False




if __name__ == '__main__':

    tictac = TicTacToe()

    winner = False
    tictac.set_player()
    while winner == False:
        tictac.set_location()
        tictac.gen_board()
        if tictac.calc_tictactoe() == True:
            break
        tictac.set_next_player()





