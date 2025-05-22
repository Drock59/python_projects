import tkinter as tk
import random
from tkinter import messagebox

# --- Game Logic ---
def start_game():
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0
    feedback_label.config(text="Guess a number between 1 and 100!", fg="#333", font=default_font)
    guess_entry.delete(0, tk.END)
    guess_button.config(state="normal")

def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1

        if guess < target_number:
            feedback = "Too low! Try again."
            feedback_color = "#D35400"
        elif guess > target_number:
            feedback = "Too high! Try again."
            feedback_color = "#2980B9"
        else:
            feedback = f"🎉 Correct! You guessed it in {attempts} attempts."
            feedback_color = "#27AE60"
            guess_button.config(state="disabled")
            bounce_text(feedback)
            messagebox.showinfo("Congratulations!", feedback)
            return  # skip normal label update

        animate_feedback(feedback, feedback_color)
        guess_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showwarning("Invalid input", "Please enter a valid number.")

# --- Animation Functions ---
def animate_feedback(text, color, steps=10, delay=40):
    """Fade in the feedback label."""
    def fade(step=0):
        if step > steps:
            return
        intensity = int(255 * step / steps)
        hex_color = f"#{int(intensity):02x}{int(intensity*0.6):02x}{int(intensity*0.2):02x}"
        feedback_label.config(text=text, fg=color)
        root.after(delay, fade, step + 1)

    fade()

def bounce_text(text):
    """Bounce the text size when guessed correctly."""
    sizes = [14, 16, 18, 20, 22, 20, 18, 16, 14]
    
    def animate(index=0):
        if index < len(sizes):
            feedback_label.config(text=text, font=("Helvetica", sizes[index], "bold"), fg="#27AE60")
            root.after(50, animate, index + 1)

    animate()

# --- GUI SETUP ---
root = tk.Tk()
root.title("🎯 Number Guessing Game")
root.geometry("420x300")
root.configure(bg="#fdf6e3")

default_font = ("Helvetica", 14)
header_font = ("Helvetica", 20, "bold")

base_btn_style = {
    "font": default_font,
    "fg": "white",
    "bd": 0,
    "activeforeground": "white",
    "cursor": "hand2",
    "padx": 10,
    "pady": 6
}

# --- Widgets ---
title_label = tk.Label(root, text="🎯 Guess the Number!", font=header_font, bg="#fdf6e3", fg="#2c3e50")
title_label.pack(pady=15)

feedback_label = tk.Label(root, text="", font=default_font, bg="#fdf6e3")
feedback_label.pack()

guess_entry = tk.Entry(root, font=default_font, justify="center", width=10, bd=2, relief="groove")
guess_entry.pack(pady=10)

guess_button = tk.Button(root, text="Submit Guess", bg="#3498DB", activebackground="#2980B9", command=check_guess, **base_btn_style)
guess_button.pack(pady=5)

reset_button = tk.Button(root, text="New Game", bg="#2ECC71", activebackground="#27AE60", command=start_game, **base_btn_style)
reset_button.pack(pady=10)

# Start the first game
start_game()

# Run the GUI
root.mainloop()
