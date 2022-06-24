from tkinter import *
from tkinter import messagebox
import numpy as np
import tictacToeSequential
import TTTSettings

def fist_init():
    TTTSettings.selected_mode = StringVar()
    TTTSettings.selected_mode.trace("w", menu_item_selected)
    # X starts so True
    TTTSettings.clickedX = True
    TTTSettings.vDict1 = {}
    TTTSettings.countClick= 0
    TTTSettings.winner = False
    TTTSettings.button_lst = []
    TTTSettings.game_state = \
                 [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    TTTSettings.current_state = "Not Done"
    TTTSettings.play_again = False
    TTTSettings.players= ['X', 'O']

def init_TicTacToe():
    TTTSettings.vDict1 = {}
    TTTSettings.countClick= 0
    TTTSettings.winner = False
    TTTSettings.button_lst = []
    TTTSettings.game_state = \
                 [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    TTTSettings.current_state = "Not Done"
    TTTSettings.play_again = False

    #players are  ['X', 'O']
def choose_symobl_x():
    TTTSettings.current_player_idx = 0
    # X starts so True
    TTTSettings.clickedX = True
    TTTSettings.play_again = True
    TTTSettings.intro_frame.quit()
    print("you chose selectionX :", TTTSettings.players[TTTSettings.current_player_idx])
def choose_symbol_0():
    TTTSettings.current_player_idx = 1
    TTTSettings.clickedX = False
    TTTSettings.play_again = True
    TTTSettings.intro_frame.quit()
    print("you chose selectionO:", TTTSettings.players[TTTSettings.current_player_idx])

def exit_game():
    if TTTSettings.play_again == False:
        messagebox.showinfo('tic tak toe', 'Thank you for playing')
    TTTSettings.intro_frame.quit()

def menu_item_selected(*args):
    TTTSettings.selected_mode.get()
    print ("seleacted mode is ",TTTSettings.selected_mode.get())

def make_intro_window():

    TTTSettings.intro_frame.iconbitmap(r'C:\Program Files\Icon.ico')
    TTTSettings.intro_frame.geometry('300x250')
    Label(TTTSettings.intro_frame, text='Play tic tac toe .').pack(padx=10, pady=10)
    Label(TTTSettings.intro_frame, text='\n\n\n\n\nChoose your symbol:').pack(padx=10, pady=10)
    x_b= Button(TTTSettings.intro_frame, text='Choose X', command=choose_symobl_x)
    x_b.pack(side='right', padx=10, pady=10)
    x_b.place(x=80, y =160)
    o_b =Button(TTTSettings.intro_frame, text='Choose O', command=choose_symbol_0)
    o_b.pack(side='right', padx=10, pady=10)
    o_b.place(x=160, y =160)
    quit_b = Button(TTTSettings.intro_frame, text="QUIT GAME", command=exit_game)
    quit_b.pack(side='right', padx=10, pady=10)
    quit_b.place(x=110, y=40)


    menu_button = Menubutton(TTTSettings.intro_frame, text='Select a mode',relief=RAISED)
    menu =  Menu(menu_button, tearoff=1)
    for mode in TTTSettings.play_mode:
        menu.add_radiobutton(
            label=mode,
            value=mode,
            variable=TTTSettings.selected_mode)

    menu_button["menu"] = menu
    menu_button.place(x=110,y=80)
    TTTSettings.intro_frame.mainloop()



def playGame():
    fist_init()
    make_intro_window()
    while TTTSettings.play_again == True :
        if (TTTSettings.selected_mode.get() == 'manual'):
            init_TicTacToe()
            print("playing in manual mode")
            tictacToeSequential.make_buttons()
            tictacToeSequential.makePlayGrid()
        elif (TTTSettings.selected_mode.get() == 'against AI'):
            init_TicTacToe()
            print("playing against computer")
            tictacToeSequential.make_buttonsAgainst()
            tictacToeSequential.makePlayGridAgainstComputer()
        else:
            TTTSettings.play_again = False
            TTTSettings.intro_frame.quit()
            messagebox.showinfo('tic tac toe ERROR! ', ' ERROR!! MODE of PLAY was not SELECTED')

#main code
playGame()