from tkinter import *
import json
import random


def get_quote():
    try:
        with open('nine-nine-quotes.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        quotes = data["root"]
        quote = random.choice(quotes)["QuoteText"]
        canvas.itemconfig(quote_text, text=quote)
    except FileNotFoundError:
        canvas.itemconfig(quote_text, text="Error: nine-nine-quotes.json file not found.")
    except json.JSONDecodeError as e:
        canvas.itemconfig(quote_text, text=f"Error: JSON decode error. Check the file format.\n{e}")
    except KeyError:
        canvas.itemconfig(quote_text, text="Error: Unexpected JSON structure.")
    except Exception as e:
        canvas.itemconfig(quote_text, text=f"An unexpected error occurred: {e}")


window = Tk()
window.title("NINE NINE Says...")
window.config(padx=50, pady=50)

# Create a frame to contain the canvas and button
frame = Frame(window)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, width=300, height=414)
background_img = PhotoImage(file="dialogue-box.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="NINE NINE says", width=250, font=("Arial", 10, "bold"))
canvas.pack(pady=20)

jake_img = PhotoImage(file="jake (1).png")
jake_button = Button(frame, image=jake_img, highlightthickness=0, command=get_quote)
jake_button.pack(pady=20)

window.mainloop()
