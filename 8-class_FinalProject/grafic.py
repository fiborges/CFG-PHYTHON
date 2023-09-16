import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

import tkinter.messagebox as messagebox

def show_result(result_game):
    result_window = tk.Toplevel()
    result_window.title("Result")
    
    frame = tk.Frame(result_window, padx=10, pady=10)
    frame.pack()

    if result_game == "WINNER":
        result_text = "Congratulations! You are the winner!"
        result_color = "green"
        hint_text = "Congratulations on your victory! To improve your chances in future rounds, consider the following:\n\n"
        hint_text += "1. Focus on increasing your character's power and courage.\n"
        hint_text += "2. Make strategic spell choices in the final challenge.\n"
        hint_text += "3. Remember that intelligence and courage can make a difference."
    else:
        result_text = "Unfortunately, victory narrowly escaped. Don't give up!"
        result_color = "red"
        hint_text = "Don't be discouraged by the loss. Here are some tips to help you improve:\n\n"
        hint_text += "1. Work on boosting your character's power and courage.\n"
        hint_text += "2. Carefully choose your spells in the final challenge.\n"
        hint_text += "3. Remember that intelligence and courage can be crucial factors."

    # Create a label for the result text with custom styling
    result_label = tk.Label(frame, text=result_text, font=("Helvetica", 16), fg=result_color)
    result_label.pack()

    # Button to show a hint or explanation
    hint_button = tk.Button(frame, text="OK", command=lambda: confirm_show_hint(result_game, hint_text))
    hint_button.pack()

    def confirm_show_hint(result, hint_text):
        # Display a confirmation dialog
        response = messagebox.askyesno("Hint Confirmation", "Would you like to learn how to improve your chances?")
        if response:
            show_hint(result, hint_text)

    def show_hint(result, hint_text):
        hint_window = tk.Toplevel()
        hint_window.title("Hint")

        hint_frame = tk.Frame(hint_window, padx=10, pady=10)
        hint_frame.pack()

        hint_label = tk.Label(hint_frame, text=hint_text, font=("Helvetica", 14))
        hint_label.pack()

        # You can customize the hint window further, e.g., add more information or tips

        # Button to close the hint window
        close_button = tk.Button(hint_frame, text="Close", command=hint_window.destroy)
        close_button.pack()

    # Load and display a result image (WINNER.png or LOSER.png)
    image_path = f"{result_game}.png"
    try:
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        # Display the image in a label
        image_label = tk.Label(result_window, image=photo)
        image_label.image = photo
        image_label.pack()
    except Exception as e:
        print(f"Error loading image: {e}")

    # Button to close the result window
    close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack()

    result_window.mainloop()








