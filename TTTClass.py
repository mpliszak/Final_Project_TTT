import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from math import inf as infinity


class TTTClass(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tik Tac Toe')
        # find tic tac toe icon on the web and put it in corner of the app
        self.iconbitmap(r'C:\Program Files\Icon.ico')
        # X starts so True
        self.clicked = True
        self.count = 0
        self.winner = False
        self.button_lst = []
        self.vDict1 = {}
        self.game_state = \
                 [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
        self.current_state="Not Done"
        self.clickedX=True
        self.countClick=0
        self.players= ['X', 'O']
        self.current_player_idx=0
        self.play_mode = ['manual', 'against AI']
        self.AImessage=''
        self.msg_b=''


    def b_click(self,b):
        if b['state'] == tk.NORMAL and self.clickedX == True:
            b['state'] = tk.DISABLED
            b['text'] = 'X'
            self.clickedX = False
            self.countClick += 1
            self.findSmartwon()
        elif b['state'] == tk.NORMAL and self.clickedX == False:
            b['state'] = tk.DISABLED
            b['text'] = 'O'
            self.clickedX = True
            self.countClick += 1
            self.findSmartwon()

    def b_clickAI(self,b):
        if b['state'] == tk.NORMAL and self.current_player_idx == 0:
            b['state'] = tk.DISABLED
            b['text'] = 'X'
            self.clickedX = False
            self.countClick += 1
            print('click X detected calling smart won')
            self.findSmartwon()
            self.after(500, lambda: self.play_Computer_move_O())
        elif b['state'] == tk.NORMAL and self.current_player_idx == 1:
            b['state'] = tk.DISABLED
            b['text'] = 'O'
            self.clickedX = True
            self.countClick += 1
            print('click 0 detected calling smart won')
            self.findSmartwon()
            self.after(500, lambda: self.play_Computer_move_X())

    def make_buttons(self):
        for i in range(1, 10):
            self.vDict1[str(i)] = "b"+str(i)+" = tk.Button(self, text='b"+str(i)+" ', " \
                                  "font=('Helvetica', 20), height=3, width=6, bd=4, " \
                                  "bg='SystemButtonFace',command=lambda:self.b_clickAI(b"+str(i)+"))\nself.button_lst.append(b"+str(i)+")"
        for key, val in self.vDict1.items():
            print(val)
            #exec(val)
        self.button_lst = []
        b1 = tk.Button(self, text='b1 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_click(b1))
        self.button_lst.append(b1)
        b2 = tk.Button(self, text='b2 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_click(b2))
        self.button_lst.append(b2)
        b3 = tk.Button(self, text='b3 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_click(b3))
        self.button_lst.append(b3)
        b4 = tk.Button(self, text='b4 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_click(b4))
        self.button_lst.append(b4)
        b5 = tk.Button(self, text='b5 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_click(b5))
        self.button_lst.append(b5)
        b6 = tk.Button(self, text='b6 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_click(b6))
        self.button_lst.append(b6)
        b7 = tk.Button(self, text='b7 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_click(b7))
        self.button_lst.append(b7)
        b8 = tk.Button(self, text='b8 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_click(b8))
        self.button_lst.append(b8)
        b9 = tk.Button(self, text='b9 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_click(b9))
        self.button_lst.append(b9)

    def make_buttonsAgainst(self):
        b1 = tk.Button(self, text='b1 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_clickAI(b1))
        self.button_lst.append(b1)
        b2 = tk.Button(self, text='b2 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_clickAI(b2))
        self.button_lst.append(b2)
        b3 = tk.Button(self, text='b3 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_clickAI(b3))
        self.button_lst.append(b3)
        b4 = tk.Button(self, text='b4 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_clickAI(b4))
        self.button_lst.append(b4)
        b5 = tk.Button(self, text='b5 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_clickAI(b5))
        self.button_lst.append(b5)
        b6 = tk.Button(self, text='b6 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_clickAI(b6))
        self.button_lst.append(b6)
        b7 = tk.Button(self, text='b7 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_clickAI(b7))
        self.button_lst.append(b7)
        b8 = tk.Button(self, text='b8 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_clickAI(b8))
        self.button_lst.append(b8)
        b9 = tk.Button(self, text='b9 ', font=('Helvetica', 20), height=3, width=6, bd=4, bg='SystemButtonFace',
                       command=lambda: self.b_clickAI(b9))
        self.button_lst.append(b9)

    def makePlayGrid(self):
        row = 0
        column = 0
        indx = 0
        for button in self.button_lst:
            print("index=", indx, ", row= ", row, ",  column= ", column)
            button.grid(row=row, column=column)
            indx += 1
            column = indx % 3
            # update row only when index is ==3
            if indx % 3 == 0:
                row += 1
        self.mainloop()

    # check to see if someone won can be refined
    def findSmartwon(self):
        winning_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 4, 6], [0, 4, 8]]
        #check for x
        for i in range(len(winning_comb)):
            cnt = 0
            for j in range(len(winning_comb[i])):
                if self.button_lst[winning_comb[i][j]]['text'] == 'X':
                    cnt +=1
                    if cnt == 3:
                        self.winner = True
                        for k in winning_comb[i]:
                            self.button_lst[k].config(bg='blue')
                        messagebox.showinfo('tic tac toe', 'we have a winner')
                        return

    
        #check for 'O'
        for i in range(len(winning_comb)):
            cnt = 0
            for j in range(len(winning_comb[i])):
                if self.button_lst[winning_comb[i][j]]['text'] == 'O':
                    cnt +=1
                    if cnt == 3:
                        self.winner = True
                        for k in winning_comb[i]:
                            self.button_lst[k].config(bg='blue')
                        messagebox.showinfo('tic tac toe', 'we have a winner')
                        return

    def check_current_state(self,game_state):
        # Check if draw
        draw_flag = 0
        for i in range(3):
            for j in range(3):
                if game_state[i][j] == ' ':
                    draw_flag = 1
        if draw_flag == 0:
            return None, "Draw"
    
        # Check horizontals
        if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] != ' '):
            return game_state[0][0], "Done"
        if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] != ' '):
            return game_state[1][0], "Done"
        if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0]  !=  ' '):
            return game_state[2][0], "Done"
    
        # Check verticals
        if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0]  != ' '):
            return game_state[0][0], "Done"
        if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1]  != ' '):
            return game_state[0][1], "Done"
        if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2]  != ' '):
            return game_state[0][2], "Done"
    
        # Check diagonals
        if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0]  != ' '):
            return game_state[1][1], "Done"
        if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0]  != ' '):
            return game_state[1][1], "Done"
    
        return None, "Not Done"
    
    
    def getBestMove(self,state, player):
       #min max algorithm code
        if (player == 'X'):
            AIis0 = True
        else:
            AIis0 = False
    

        winner_loser, done = self.check_current_state(state)
        if done == "Done" and winner_loser == 'O' and AIis0==True:  # AI won
            return 1
        elif done == "Done" and winner_loser == 'X' and AIis0==True:  #  you won
            return -1
        if done == "Done" and winner_loser == 'O' and AIis0 == False:  # you won
            return -1
        elif done == "Done" and winner_loser == 'X' and AIis0 == False:  # AI won
            return 1
        elif done == "Draw":  # Draw condition
            return 0
    
        moves = []
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    empty_cells.append(i * 3 + (j + 1))
    
        for empty_cell in empty_cells:
            move = {}
            move['index'] = empty_cell
            new_state = self.copy_game_state(state)
            self.play_move(new_state, player, empty_cell)
    
            if AIis0 == True:
                # AI uses 0, player is X
                if player == 'O':  # If AI
                    result = self.getBestMove(new_state, 'X')  # make more depth tree for human
                    move['score'] = result
                else:
                    result = self.getBestMove(new_state, 'O')  # make more depth tree for AI
                    move['score'] = result
            elif AIis0 == False:
                #AI uses X, player is 0
                if player == 'X':  # If AI
                    result = self.getBestMove(new_state, 'X')  # make more depth tree for human
                    move['score'] = result
                else:
                    result = self.getBestMove(new_state, 'O')  # make more depth tree for AI
                    move['score'] = result
    
            moves.append(move)
    
        # Find best move
        best_move = None
    
        if AIis0 == True:
            if player == 'O':  # If AI player
                best = -infinity
                for move in moves:
                    if move['score'] > best:
                        best = move['score']
                        best_move = move['index']
            else:
                best = infinity
                for move in moves:
                    if move['score'] < best:
                        best = move['score']
                        best_move = move['index']
        elif AIis0 == False:
            if player == 'X':  # If AI player
                best = -infinity
                for move in moves:
                    if move['score'] > best:
                        best = move['score']
                        best_move = move['index']
            else:
                best = infinity
                for move in moves:
                    #print('move[score]',move['score'], 'best', best)
                    if move['score'] < best:
                        best = move['score']
                        best_move = move['index']
    
        return best_move
    
    
    def play_move(self,state, player, block_num):
        if state[int((block_num - 1) / 3)][(block_num - 1) % 3] == ' ':
            state[int((block_num - 1) / 3)][(block_num - 1) % 3] = player
        else:
            block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
            self.play_move(state, player, block_num)
    
    def copy_game_state(self,state):
        new_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for i in range(3):
            for j in range(3):
                new_state[i][j] = state[i][j]
        return new_state
    
    def copy_game_stateGUI(self,game_state):
        i=0
        j=0
        for button in self.button_lst:
            if button['state'] == tk.NORMAL:
                self.game_state[j][i%3]= ' '
            else:
                self.game_state[j][i % 3] = button['text']
            #print('j: ', j,'i : ', i)
            #print('self.game_state[j][i % 3]',self.game_state[j][i % 3])
            i+=1
            if i%3 == 0:
                j+=1
    
    def print_board(self,game_state):
        #for debug only
        print('----------------')
        print('| ' + str(game_state[0][0]) + ' | ' + str(game_state[0][1]) + ' | ' + str(game_state[0][2]) + ' |')
        print('----------------')
        print('| ' + str(game_state[1][0]) + ' | ' + str(game_state[1][1]) + ' | ' + str(game_state[1][2]) + ' |')
        print('----------------')
        print('| ' + str(game_state[2][0]) + ' | ' + str(game_state[2][1]) + ' | ' + str(game_state[2][2]) + ' |')
        print('----------------')
    
    def play_Computer_move_X(self): #player inex = 1, AI index =0
        #find current state of the board
        self.copy_game_stateGUI(self.game_state)
        self.print_board(self.game_state)
        best_move = self.getBestMove(self.game_state,self.players[1])
        print("AI_x is ready to make it's best move b", best_move)
        self.button_lst[best_move-1]['text'] = 'X'
        self.button_lst[best_move-1]['state'] = tk.DISABLED
        self.countClick += 1
        self.findSmartwon()
        if self.countClick == 9 and self.winner == False:
            self.msg_b['text'] = 'tic tac toe', 'IT IS A DRAW'
            return
        print("AI_x self.countClick  self.winner  ", self.countClick, self.winner)
        self.copy_game_stateGUI(self.game_state)
        self.best_move = self.getBestMove(self.game_state, self.players[0])
        self.msg_b['text'] = 'AI found best move for you: b' + str(best_move)

    def play_Computer_move_O(self):#player index 1, computer 0
        print("AI_o self.countClick  self.winner  ", self.countClick, self.winner)
        if self.countClick == 9 and self.winner == False:
            self.msg_b['text'] = 'tic tac toe', 'IT IS A DRAW'
            return
        #find current state of the board
        self.copy_game_stateGUI(self.game_state)
        self.print_board(self.game_state)
        self.best_move = self.getBestMove(self.game_state,self.players[0])
        print("AI_o is ready to make it's best move b", self.best_move)
        self.msg_b['text'] = 'AI found best move to be b'+str(self.best_move)
        self.button_lst[self.best_move-1]['text'] = 'O'
        self.button_lst[self.best_move-1]['state'] = tk.DISABLED
        self.countClick += 1
        self.findSmartwon()
        self.copy_game_stateGUI(self.game_state)
        self.best_move = self.getBestMove(self.game_state, self.players[1])
        self.msg_b['text'] = 'AI found best move for you: b' + str(self.best_move)

    def playComputer(self):
        print('playing computer')
        if self.current_player_idx == 0:
            print("you chose :", self.players[self.current_player_idx])
            print("computer is using 0 you go first")
            self.AImessage += '\n You : X  AI : 0\n You go first'
            self.msg_b['text'] = self.AImessage
    
        elif self.current_player_idx == 1: #
            print("you chose :", self.players[self.current_player_idx])
            print("computer is using X and X goes first")
            self.AImessage += '\n You : O  AI : X\n AI goes first'
            self.play_Computer_move_X()
            self.msg_b['text'] = self.AImessage
    
    def makePlayGridAgainstComputer(self):
        row = 0
        column = 0
        indx = 0
        for button in self.button_lst:
            print("index=", indx, ", row= ", row,",  column= ", column)
            button.grid(row=row, column=column)
            indx += 1
            column = indx % 3
            #update row only when index is ==3
            if indx % 3 == 0:
                row += 1
        self.AImessage = "You are playing against AI:"
        self.msg_b = tk.Button(self, relief=tk.GROOVE, text= self.AImessage , font=('Helvetica', 19), height=3, width=0,bd=10, bg='white')
        #msg_b.grid(row = 3,column =0)
        self.msg_b.grid(row=3, column=0, sticky=tk.W, columnspan=3)
        self.after(1000,lambda:self.playComputer())
        self.mainloop()

# if __name__ == "__main__":
#     playTTT = TTTClass()
#     playTTT.make_buttons()
#     playTTT.makePlayGrid()
#     playTTT.mainloop()