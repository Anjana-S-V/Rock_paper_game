
import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0

        # Labels
        self.score_label = tk.Label(root, text=f"Score - You: {self.player_score}, Computer: {self.computer_score}, Ties: {self.ties}")
        self.score_label.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.computer_choice_label = tk.Label(root, text="")
        self.computer_choice_label.pack(pady=10)

        # Buttons
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_game)
        self.quit_button.pack(side=tk.BOTTOM, pady=10)

    def play(self, player_choice):
        computer_choice = get_computer_choice()
        self.computer_choice_label.config(text=f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        self.result_label.config(text=result)
        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        elif result == "It's a tie!":
            self.ties += 1
        self.score_label.config(text=f"Score - You: {self.player_score}, Computer: {self.computer_score}, Ties: {self.ties}")

    def quit_game(self):
        messagebox.showinfo("Game Over", f"Thanks for playing!\nFinal Score - You: {self.player_score}, Computer: {self.computer_score}, Ties: {self.ties}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    gui = RockPaperScissorsGUI(root)
    root.mainloop()
