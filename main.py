from tkinter import *
import json
import random


def get_quote():
    try:
        with open('nine-nine-quotes.json', 'r') as file:
            data = json.load(file)

        quotes = data["root"]
        quote = random.choice(quotes)["QuoteText"]
        canvas.itemconfig(quote_text, text=quote)
    except FileNotFoundError:
        canvas.itemconfig(quote_text, text="Error: quotes.json file not found.")
    except json.JSONDecodeError:
        canvas.itemconfig(quote_text, text="Error: JSON decode error. Check the file format.")
    except KeyError:
        canvas.itemconfig(quote_text, text="Error: Unexpected JSON structure.")
    except Exception as e:
        canvas.itemconfig(quote_text, text=f"An unexpected error occurred: {e}")


window = Tk()
window.title("NINE NINE Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="NINE NINE says", width=250, font=("Arial", 10, "bold"))
canvas.grid(row=0, column=0)

jake_img = PhotoImage(file="jake (1).png")
jake_button = Button(image=jake_img, highlightthickness=0, command=get_quote)
jake_button.grid(row=1, column=0)

window.mainloop()
