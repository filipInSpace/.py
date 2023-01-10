
#Author: Filip Navrkal 

import tkinter as tk
from tkinter import messagebox
import random

def play_rps():
    player_choice = player_var.get()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = None
    
    if player_choice == computer_choice:
        result = "Tie!"
    elif player_choice == 'rock':
        if computer_choice == 'scissors':
            result = "You win!"
        else:
            result = "You lose!"
    elif player_choice == 'paper':
        if computer_choice == 'rock':
            result = "You win!"
        else:
            result = "You lose!"
    elif player_choice == 'scissors':
        if computer_choice == 'paper':
            result = "You win!"
        else:
            result = "You lose!"
            
    messagebox.showinfo("Result", f"{result}\nYou chose {player_choice}\nComputer chose {computer_choice}")

root = tk.Tk()
root.title("Rock, Paper, Scissors")

player_var = tk.StringVar()

rock_button = tk.Radiobutton(root, text="Rock", variable=player_var, value='rock', font=("Helvetica", 16))
rock_button.pack()

paper_button = tk.Radiobutton(root, text="Paper", variable=player_var, value='paper', font=("Helvetica", 16))
paper_button.pack()

scissors_button = tk.Radiobutton(root, text="Scissors", variable=player_var, value='scissors', font=("Helvetica", 16))
scissors_button.pack()

play_button = tk.Button(root, text="Play", command=play_rps, font=("Helvetica", 16))
play_button.pack()

root.mainloop()

