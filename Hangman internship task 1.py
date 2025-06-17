import tkinter as tk
import random

# Word list
word_list = ["python", "hangman", "challenge", "programming", "developer", "keyboard", "function", "variable"]

# Initialize game variables
secret_word = random.choice(word_list)
guessed_letters = []
max_attempts = 6
attempts = 0

# Set up main window
window = tk.Tk()
window.title("Hangman Game")
window.geometry("400x300")

# Functions
def update_display():
    display = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    word_label.config(text=display)
    attempts_label.config(text=f"Attempts left: {max_attempts - attempts}")

    if "_" not in display:
        result_label.config(text="You Win!")
        guess_button.config(state="disabled")

    elif attempts >= max_attempts:
        result_label.config(text=f"You Lost! Word was '{secret_word}'")
        guess_button.config(state="disabled")

def make_guess():
    global attempts
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if not guess.isalpha() or len(guess) != 1:
        result_label.config(text="Enter a single letter.")
        return

    if guess in guessed_letters:
        result_label.config(text="Letter already guessed.")
        return

    guessed_letters.append(guess)

    if guess in secret_word:
        result_label.config(text=f"Correct! '{guess}' is in the word.")
    else:
        attempts += 1
        result_label.config(text=f"Wrong! '{guess}' is not in the word.")

    update_display()

# Widgets
word_label = tk.Label(window, text="_ " * len(secret_word), font=("Helvetica", 24))
word_label.pack(pady=20)

entry = tk.Entry(window, font=("Helvetica", 18), width=5, justify="center")
entry.pack()

guess_button = tk.Button(window, text="Guess", command=make_guess)
guess_button.pack(pady=10)

attempts_label = tk.Label(window, text=f"Attempts left: {max_attempts}", font=("Helvetica", 14))
attempts_label.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Start game
update_display()
window.mainloop()
