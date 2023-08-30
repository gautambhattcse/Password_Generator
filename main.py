import random
import string
from tkinter import *
import tkinter as tk
from tkinter import messagebox

global password_generated

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x300+20+30")
root.resizable(0, 0)

password_generated=""
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_password_clicked():
    global password_generated
    try:
        length = int(entry_box.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
        else:
            password_generated = generate_password(length)
            password_box.delete(0,END)
            password_box.insert(0, password_generated)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")


def copy_to_clipboard():
    global password_generated
    if password_generated:
        root.clipboard_clear()
        root.clipboard_append(password_generated)
        messagebox.showinfo("Copied", "Password copied to the clipboard")
    else:
        messagebox.showerror("Error", "No password generated yet")


def enter_key_pressed(event):
    generate_password_clicked()


# Create and place widgets
label_frame = LabelFrame(root, text="Enter the desired length...")
label_frame.pack(pady=20)

entry_box = Entry(label_frame, font=("Helvetica", 24))
entry_box.pack(pady=20, padx=20)
entry_box.bind("<Return>", enter_key_pressed)

password_box = Entry(root, text="", font=("Helvetica", 24), bd=0, bg="systembuttonface")
password_box.pack(pady=20)

frame = Frame(root)
frame.pack(pady=20)

button1 = Button(frame, text="Generate Password", command=generate_password_clicked)
button1.grid(row=0, column=0, padx=10)

button2 = Button(frame, text="Copy to clipboard", command=copy_to_clipboard)
button2.grid(row=0, column=1, padx=10)

# Start the GUI event loop
root.mainloop()
