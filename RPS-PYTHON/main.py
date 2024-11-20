import tkinter as tk
from tkinter import messagebox
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("400x400")
        
        self.is_playing = True
        
        self.result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 14))
        self.result_label.pack(pady=20)
        
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play_round("rock"), width=20)
        self.rock_button.pack(pady=5)
        
        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play_round("paper"), width=20)
        self.paper_button.pack(pady=5)
        
        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play_round("scissors"), width=20)
        self.scissors_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_game, width=20)
        self.stop_button.pack(pady=20)

        self.user_choice_label = tk.Label(root, text="You chose: ", font=("Helvetica", 12))
        self.user_choice_label.pack(pady=5)
        
        self.computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Helvetica", 12))
        self.computer_choice_label.pack(pady=5)
        
        self.result_text_label = tk.Label(root, text="Result: ", font=("Helvetica", 12))
        self.result_text_label.pack(pady=5)

    def play_round(self, user_choice):
        if not self.is_playing:
            return

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        self.user_choice_label.config(text=f"You chose: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "You lose!"

        self.result_text_label.config(text=f"Result: {result}")

    def stop_game(self):
        self.is_playing = False
        self.result_label.config(text="Game Over!")
        self.user_choice_label.config(text="")
        self.computer_choice_label.config(text="")
        self.result_text_label.config(text="")
        messagebox.showinfo("Game Over", "You have stopped the game!")

root = tk.Tk()

game = RPSGame(root)

root.mainloop()
