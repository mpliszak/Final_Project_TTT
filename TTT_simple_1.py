import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from TTTClass import TTTClass

class TTTIntroClass(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'C:\Program Files\Icon.ico')
        self.geometry('300x250')
        self.play_again=False
        self.clickedX=True
        self.countClick=0
        self.players= ['X', 'O']
        self.current_player_idx=0
        self.play_mode = ['manual', 'against AI']
        self.selected_mode = tk.StringVar()
        self.selected_mode.trace("w", self.menu_item_selected)
        self.AImessage=''
        self.msg_b=''
        self.overrideredirect(1)

    def choose_symobl_x(self):
        self.current_player_idx = 0
        # X starts so True
        self.clickedX = True
        self.play_again = True
        self.quit()
        print("you chose selectionX :", self.players[self.current_player_idx])

    def choose_symbol_0(self):
        self.current_player_idx = 1
        self.clickedX = False
        self.play_again = True
        self.quit()
        print("you chose selectionO:", self.players[self.current_player_idx])

    def exit_game(self):
        self.play_again = False
        if self.play_again == False:
            messagebox.showinfo('tic tak toe', 'Thank you for playing')
        self.quit()

    def menu_item_selected(self,*args):

        self.selected_mode.get()
        print ("selected mode is ",self.selected_mode.get())

    def make_intro_window(self):

        tk.Label(self, text='Play tic tac toe .').pack(padx=10, pady=10)
        tk.Label(self, text='\n\n\n\n\nChoose your symbol:').pack(padx=10, pady=10)
        x_b= tk.Button(self, text='Choose X', command=self.choose_symobl_x)
        x_b.pack(side='right', padx=10, pady=10)
        x_b.place(x=80, y =160)
        o_b =tk.Button(self, text='Choose O', command=self.choose_symbol_0)
        o_b.pack(side='right', padx=10, pady=10)
        o_b.place(x=160, y =160)
        quit_b = tk.Button(self, text="QUIT GAME", command=self.exit_game)
        quit_b.pack(side='right', padx=10, pady=10)
        quit_b.place(x=110, y=40)

        menu_button = tk.Menubutton(self, text='Select a mode',relief=tk.RAISED)
        menu =  tk.Menu(menu_button, tearoff=1)
        for mode in self.play_mode:
            menu.add_radiobutton(
                label=mode,
                value=mode,
                variable=self.selected_mode)
        menu_button["menu"] = menu
        menu_button.place(x=110,y=80)
        self.mainloop()

    def playGame(self):
        """
        this is the main function that runs the game and is only interupted when the quit button is pressed
        """
        self.make_intro_window()
        while self.play_again == True :
            ticGUI = TTTClass()
            ticGUI.clickedX = self.clickedX
            ticGUI.current_player_idx = self.current_player_idx
            if (self.selected_mode.get() == 'manual'):
                print("playing in manual mode")
                ticGUI.make_buttons()
                ticGUI.makePlayGrid()
            elif (self.selected_mode.get() == 'against AI'):
                print("playing against computer")
                ticGUI.make_buttonsAgainst()
                ticGUI.makePlayGridAgainstComputer()
            else:
                self.play_again = False
                self.quit()
                messagebox.showinfo('tic tac toe ERROR! ', ' ERROR!! MODE of PLAY was not SELECTED')


if __name__ == "__main__":
    playfullTTT = TTTIntroClass()
    playfullTTT.playGame()

#main code
#playGame()