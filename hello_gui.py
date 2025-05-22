import tkinter as tk
from tkinter import messagebox

def generate_greeting():
    name = name_entry.get().strip()
    style = greeting_style.get()

    if not name:
        messagebox.showwarning("Input Error", "Please enter your name.")
        return

    if style == "casual":
        greeting = f"Hey {name}, what's up?"
    else:
        greeting = f"Hello {name}, it's a pleasure to meet you."

    greeting_label.config(text=greeting)
    save_greeting(greeting)

def save_greeting(message):
    try:
        with open("greeting.txt", "w") as file:
            file.write(message + "\n")
        print("Greeting saved to greeting.txt")
    except Exception as e:
        messagebox.showerror("Save Error", f"Failed to save greeting: {e}")

# --- GUI SETUP ---
root = tk.Tk()
root.title("Personalized Hello World")
root.geometry("400x300")
root.configure(bg="lightblue")

# Widgets
title_label = tk.Label(root, text="Welcome!", font=("Helvetica", 18), bg="lightblue")
title_label.pack(pady=10)

name_label = tk.Label(root, text="Enter your name:", bg="lightblue")
name_label.pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Greeting style radio buttons
greeting_style = tk.StringVar(value="casual")

casual_radio = tk.Radiobutton(root, text="Casual", variable=greeting_style, value="casual", bg="lightblue")
formal_radio = tk.Radiobutton(root, text="Formal", variable=greeting_style, value="formal", bg="lightblue")

casual_radio.pack()
formal_radio.pack()

# Button
generate_button = tk.Button(root, text="Generate Greeting", command=generate_greeting)
generate_button.pack(pady=10)

# Output label
greeting_label = tk.Label(root, text="", font=("Helvetica", 14), fg="darkgreen", bg="lightblue")
greeting_label.pack(pady=20)

# Run the application
root.mainloop()
