import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def show_result(result):
    result_window = tk.Toplevel()
    result_window.title("Result:")

    if result == "WINNER":
        image_path = "WINNER.png"
        message = "CONGRATULATIONS! You are the winner!"
    else:
        image_path = "LOSER.png"
        message = "Unfortunately, victory narrowly escaped. Don't give up!"

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(result_window, image=photo)
    image_label.image = photo
    image_label.pack()

    message_label = tk.Label(result_window, text=message, font=("Helvetica", 14))
    message_label.pack()

    ok_button = ttk.Button(result_window, text="OK", command=result_window.destroy)
    ok_button.pack()