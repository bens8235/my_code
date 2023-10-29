import pandas
from tkinter import *
import random
import json

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

counter = 5
data = pandas.read_csv("french_words.csv")

try:
    with open("list_of_french_words.json", "r") as fl:
        french_list = json.load(fl)
except:
    french_list = data["French"].to_list()

def get_word():
    random_french_word = random.choice(french_list)
    for (index, row) in data.iterrows():
        if row.French == random_french_word:
            english_word = row.English
    return random_french_word, english_word

front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")

words = ()

# If ticked will remove French word from words that appear on screen.

def tick():
    global counter
    if counter == 0:
        french_list.remove(words[0])
        with open("list_of_french_words.json", "w") as data:
            json.dump(french_list, data)
        counter = 5
        front_screen(5)
    else:
        pass

def cross():
    global counter
    if counter == 0:
        counter = 5
        front_screen((5))
    else:
        pass

def front_screen(count):
    global counter
    global words
    if count == 5:
        words = get_word()
    if count > 0:
        canvas = Canvas(width=800, height=400)
        canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        canvas.create_image(400,200, image=front_img)
        canvas.grid(column=0, row = 0, columnspan = 2)
        timer_text = canvas.create_text(700, 100, text=5, fill="black", font=("Ariel", 60, "bold"))
        canvas_text = canvas.create_text(400,150, text="French", fill="black", font = ("Ariel", 40, "italic"))
        canvas_text2 = canvas.create_text(400,250, text=words[0], fill="black", font = ("Ariel", 60, "bold"))
        window.after(1000, front_screen, count - 1)
        canvas.itemconfig(timer_text, text = count)
        counter -= 1

    else:
        canvas2 = Canvas(width=800, height=400)
        canvas2.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        canvas2.create_image(400, 200, image=back_img)
        canvas2.grid(column=0, row=0, columnspan=2)
        canvas_text2 = canvas2.create_text(400, 150, text="English", fill="black", font=("Ariel", 40, "italic"))
        canvas_text3 = canvas2.create_text(400, 250, text=words[1], fill="black", font=("Ariel", 60, "bold"))

front_screen(5)

my_image = PhotoImage(file="right.png")
correct_button = Button(image=my_image, highlightthickness=0, command=tick)
correct_button.grid(column= 1, row = 1)
my_image2 = PhotoImage(file="wrong.png")
wrong_button = Button(image=my_image2, highlightthickness=0, command=cross)
wrong_button.grid(column= 0, row = 1)

window.mainloop()