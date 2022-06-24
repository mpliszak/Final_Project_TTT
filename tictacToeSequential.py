from tkinter import *
from tkinter import messagebox
import numpy as np
from math import inf as infinity
import TTTSettings


# button TTTSettings.clickedX function
def b_click(b):
    if b['state'] == NORMAL and TTTSettings.clickedX == True:
        b['state'] = DISABLED
        b['text'] = 'X'
        TTTSettings.clickedX = False
        TTTSettings.countClick += 1
        #checkifwon()
        findSmartwon()
    elif b['state'] == NORMAL and TTTSettings.clickedX == False:
        b['state'] = DISABLED
        b['text'] = 'O'
        TTTSettings.clickedX = True
        TTTSettings.countClick += 1
        #checkifwon()
        findSmartwon()

def b_click_computer(b):
    if b['state'] == NORMAL and TTTSettings.current_player_idx==0:
        b['state'] = DISABLED
        b['text'] = 'X'
        TTTSettings.clickedX = False
        TTTSettings.countClick += 1
        #checkifwon()
        print('click X detected calling smart won')
        findSmartwon()
        TTTSettings.mattGame.after(500, lambda: play_Computer_move_O())
    elif b['state'] == NORMAL and TTTSettings.current_player_idx==1:
        b['state'] = DISABLED
        b['text'] = 'O'
        TTTSettings.clickedX = True
        TTTSettings.countClick += 1
        print('click 0 detected calling smart won')
        #checkifwon()
        findSmartwon()
        TTTSettings.mattGame.after(500, lambda: play_Computer_move_X())

# check to see if someone won can be refined
def findSmartwon():
    winning_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 4, 6], [0, 4, 8]]
    #check for x
    for i in range(len(winning_comb)):
        cnt = 0
        for j in range(len(winning_comb[i])):
            if TTTSettings.button_lst[winning_comb[i][j]]['text'] == 'X':
                cnt +=1
                if cnt == 3:
                    TTTSettings.winner = True
                    for k in winning_comb[i]:
                        TTTSettings.button_lst[k].config(bg='blue')
                    messagebox.showinfo('tic tac toe', 'we have a winner')
                    break

    #check for 'O'
    for i in range(len(winning_comb)):
        cnt = 0
        for j in range(len(winning_comb[i])):
            if TTTSettings.button_lst[winning_comb[i][j]]['text'] == 'O':
                cnt +=1
                if cnt == 3:
                    TTTSettings.winner = True
                    for k in winning_comb[i]:
                        TTTSettings.button_lst[k].config(bg='blue')
                    messagebox.showinfo('tic tac toe', 'we have a winner')
                    break


def make_buttons():
    TTTSettings.mattGame = Tk()
    TTTSettings.button_lst = []
    vDict1 ={}
    for i in range(1, 10):
        # b1 = Button(mattGame,text=' ', font=('Helvetica', 20), height = 3, width = 6, bg = 'SystemButtonFace', command = lambda: b_click(b1) )
        vDict1[str(i)] = "TTTSettings.button_lst.append(Button(TTTSettings.mattGame, relief = GROOVE, text='b"+str(i)\
                         +" ', font=('Helvetica', 20), height = 3, width = 6, bd = 4, bg = 'SystemButtonFace', " \
                          "command =lambda:b_click(TTTSettings.button_lst["+str(i)+"-1])))"
    for key, val in vDict1.items():
        print(val)
        exec(val)

def make_buttonsAgainst():
    TTTSettings.mattGame = Tk()
    TTTSettings.button_lst = []
    vDict1 ={}
    for i in range(1, 10):
        vDict1[str(i)] = "TTTSettings.button_lst.append(Button(TTTSettings.mattGame, relief = GROOVE, text='b"+str(i)\
                         +" ', font=('Helvetica', 20), height = 3, width = 6, bd = 4, bg = 'SystemButtonFace', " \
                            "command =lambda:b_click_computer(TTTSettings.button_lst["+str(i)+"-1])))"
    for key, val in vDict1.items():
        #print(val)
        exec(val)


def makePlayGrid():
    TTTSettings.mattGame.title('Tik Tac Toe')
    TTTSettings.mattGame.iconbitmap(r'C:\Program Files\Icon.ico')

    row = 0
    column = 0
    indx = 0
    for button in TTTSettings.button_lst:
        #print("index=", indx, ", row= ", row,",  column= ", column)
        button.grid(row=row, column=column)
        indx += 1
        column = indx % 3
        #update row only when index is ==3
        if indx % 3 == 0:
            row += 1
    TTTSettings.mattGame.mainloop()

def check_current_state(game_state):
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


def getBestMove(state, player):
   #min max algorithm code
    if (player == 'X'):
        AIis0 = True
    else:
        AIis0 = False

    #print('dbg AIis0',AIis0)
    winner_loser, done = check_current_state(state)
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
        new_state = copy_game_state(state)
        play_move(new_state, player, empty_cell)

        if AIis0 == True:
            # AI uses 0, player is X
            if player == 'O':  # If AI
                result = getBestMove(new_state, 'X')  # make more depth tree for human
                move['score'] = result
            else:
                result = getBestMove(new_state, 'O')  # make more depth tree for AI
                move['score'] = result
        elif AIis0 == False:
            #AI uses X, player is 0
            if player == 'X':  # If AI
                result = getBestMove(new_state, 'X')  # make more depth tree for human
                move['score'] = result
            else:
                result = getBestMove(new_state, 'O')  # make more depth tree for AI
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


def play_move(state, player, block_num):
    if state[int((block_num - 1) / 3)][(block_num - 1) % 3] == ' ':
        state[int((block_num - 1) / 3)][(block_num - 1) % 3] = player
    else:
        block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
        play_move(state, player, block_num)

def copy_game_state(state):
    new_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(3):
        for j in range(3):
            new_state[i][j] = state[i][j]
    return new_state

def copy_game_stateGUI(game_state):
    i=0
    j=0
    for button in TTTSettings.button_lst:
        if button['state'] == NORMAL:
            TTTSettings.game_state[j][i%3]= ' '
        else:
            TTTSettings.game_state[j][i % 3] = button['text']
        #print('j: ', j,'i : ', i)
        #print('TTTSettings.game_state[j][i % 3]',TTTSettings.game_state[j][i % 3])
        i+=1
        if i%3 == 0:
            j+=1

def print_board(game_state):
    #for debug only
    print('----------------')
    print('| ' + str(game_state[0][0]) + ' | ' + str(game_state[0][1]) + ' | ' + str(game_state[0][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[1][0]) + ' | ' + str(game_state[1][1]) + ' | ' + str(game_state[1][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[2][0]) + ' | ' + str(game_state[2][1]) + ' | ' + str(game_state[2][2]) + ' |')
    print('----------------')

def play_Computer_move_X(): #player inex = 1, AI index =0
    #find current state of the board
    copy_game_stateGUI(TTTSettings.game_state)
    print_board(TTTSettings.game_state)
    best_move = getBestMove(TTTSettings.game_state,TTTSettings.players[1])
    print("AI_x is ready to make it's best move b", best_move)
    TTTSettings.button_lst[best_move-1]['text'] = 'X'
    TTTSettings.button_lst[best_move-1]['state'] = DISABLED
    TTTSettings.countClick += 1
    findSmartwon()
    if TTTSettings.countClick == 9 and TTTSettings.winner == False:
        TTTSettings.msg_b['text'] = 'tic tac toe', 'IT IS A DRAW'
        return
    print("AI_x TTTSettings.countClick  TTTSettings.winner  ", TTTSettings.countClick, TTTSettings.winner)
    copy_game_stateGUI(TTTSettings.game_state)
    best_move = getBestMove(TTTSettings.game_state, TTTSettings.players[0])
    TTTSettings.msg_b['text'] = 'AI found best move for you: b' + str(best_move)
def play_Computer_move_O():#player index 1, computer 0
    print("AI_o TTTSettings.countClick  TTTSettings.winner  ", TTTSettings.countClick, TTTSettings.winner)
    if TTTSettings.countClick == 9 and TTTSettings.winner == False:
        TTTSettings.msg_b['text'] = 'tic tac toe', 'IT IS A DRAW'
        return
    #find current state of the board
    copy_game_stateGUI(TTTSettings.game_state)
    print_board(TTTSettings.game_state)
    best_move = getBestMove(TTTSettings.game_state,TTTSettings.players[0])
    print("AI_o is ready to make it's best move b", best_move)
    TTTSettings.msg_b['text'] = 'AI found best move to be b'+str(best_move)
    TTTSettings.button_lst[best_move-1]['text'] = 'O'
    TTTSettings.button_lst[best_move-1]['state'] = DISABLED
    TTTSettings.countClick += 1
    findSmartwon()
    copy_game_stateGUI(TTTSettings.game_state)
    best_move = getBestMove(TTTSettings.game_state, TTTSettings.players[1])
    TTTSettings.msg_b['text'] = 'AI found best move for you: b' + str(best_move)
def playComputer():
    print('playing computer')
    if TTTSettings.current_player_idx == 0:
        print("you chose :", TTTSettings.players[TTTSettings.current_player_idx])
        print("computer is using 0 you go first")
        TTTSettings.AImessage += '\n You : X  AI : 0\n You go first'
        TTTSettings.msg_b['text'] = TTTSettings.AImessage

    elif TTTSettings.current_player_idx == 1: #
        print("you chose :", TTTSettings.players[TTTSettings.current_player_idx])
        print("computer is using X and X goes first")
        TTTSettings.AImessage += '\n You : O  AI : X\n AI goes first'
        play_Computer_move_X()
        TTTSettings.msg_b['text'] = TTTSettings.AImessage

def makePlayGridAgainstComputer():
    TTTSettings.mattGame.title('Tik Tac Toe Against AI')
    # find tic tac toe icon on the web and put it in corner of the app
    TTTSettings.mattGame.iconbitmap(r'C:\Program Files\Icon.ico')
    row = 0
    column = 0
    indx = 0
    for button in TTTSettings.button_lst:
        print("index=", indx, ", row= ", row,",  column= ", column)
        button.grid(row=row, column=column)
        indx += 1
        column = indx % 3
        #update row only when index is ==3
        if indx % 3 == 0:
            row += 1
    TTTSettings.AImessage = "You are playing against AI:"
    TTTSettings.msg_b = Button(TTTSettings.mattGame, relief=GROOVE, text= TTTSettings.AImessage , font=('Helvetica', 19), height=3, width=0,bd=10, bg='white')
    #msg_b.grid(row = 3,column =0)
    TTTSettings.msg_b.grid(row=3, column=0, sticky=W, columnspan=3)
    TTTSettings.mattGame.after(1000,lambda:playComputer())
    TTTSettings.mattGame.mainloop()