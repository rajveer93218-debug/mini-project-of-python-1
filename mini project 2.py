#mini project 2


import tkinter as tk
from tkinter import messagebox
import random

# Main Window
root = tk.Tk()
root.title("Snake Water Gun")
root.geometry("500x400")
root.resizable(False, False)

# Variables
user_score = 0
computer_score = 0

choices = ["Snake", "Water", "Gun"]

# Functions
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result_text.config(
        text=f"You: {user_choice}\nComputer: {computer_choice}"
    )

    if user_choice == computer_choice:
        result = "Draw!"

    elif (
        (user_choice == "Snake" and computer_choice == "Water") or
        (user_choice == "Water" and computer_choice == "Gun") or
        (user_choice == "Gun" and computer_choice == "Snake")
    ):
        result = "You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    winner_label.config(text=result)

    score_label.config(
        text=f"Your Score: {user_score}    Computer Score: {computer_score}"
    )

def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    result_text.config(text="Choose Snake, Water or Gun")
    winner_label.config(text="")
    score_label.config(text="Your Score: 0    Computer Score: 0")

# Heading
title_label = tk.Label(
    root,
    text="Snake Water Gun Game",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)

# Result Display
result_text = tk.Label(
    root,
    text="Choose Snake, Water or Gun",
    font=("Arial", 14)
)
result_text.pack(pady=15)

winner_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold")
)
winner_label.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

snake_btn = tk.Button(
    button_frame,
    text="🐍 Snake",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Snake")
)
snake_btn.grid(row=0, column=0, padx=10)

water_btn = tk.Button(
    button_frame,
    text="💧 Water",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Water")
)
water_btn.grid(row=0, column=1, padx=10)

gun_btn = tk.Button(
    button_frame,
    text="🔫 Gun",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Gun")
)
gun_btn.grid(row=0, column=2, padx=10)

# Score Label
score_label = tk.Label(
    root,
    text="Your Score: 0    Computer Score: 0",
    font=("Arial", 14)
)
score_label.pack(pady=20)

# Reset Button
reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12),
    command=reset_game
)
reset_btn.pack(pady=10)

# Exit Button
exit_btn = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12),
    command=root.destroy
)
exit_btn.pack()

root.mainloop()