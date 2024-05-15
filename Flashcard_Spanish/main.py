from tkinter import *
from pandas import *
import random
import time
# ----------------------- READING DATA AND CHOSING THE WORD ---------------------------#
data = read_excel("Flashcard_Spanish/spanish_words.xlsx")
to_learn = data.to_dict(orient="records")
current_card = {}

known_words = []

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text= current_card["SPANISH"], fill="black")
    canvas.itemconfig(card_background, image= cardfront_img)
    flip_timer = window.after(3000, func= flip_card)
    

def known_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text= current_card["SPANISH"], fill="black")
    canvas.itemconfig(card_background, image= cardfront_img)
    flip_timer = window.after(3000, func= flip_card)

    to_learn.remove(current_card)
    known_words.append(current_card)

    df = DataFrame(known_words)
    df.to_csv("Flashcard_Spanish/Words/Known_words.csv", index=False)

    
   
def flip_card():
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text= current_card["ENGLISH"], fill="white")
    canvas.itemconfig(card_background, image= cardback_img)

# ---------------------- REMOVE KNOWN WORD AND ADD TO ANOTHER CSV FILE ------------- #

def known_word():
    global current_card

    print(current_card["ENGLISH"])


# ----------------------- UI --------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

# For slipping first card
flip_timer = window.after(3000, func= flip_card)

canvas = Canvas(width= 800, height= 526)
cardfront_img = PhotoImage(file="Flashcard_Spanish\images\card_front.png")
cardback_img = PhotoImage(file="Flashcard_Spanish\images\card_back.png")
card_background = canvas.create_image(400, 263, image= cardfront_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row= 0, column=0, columnspan=2)

cross_image = PhotoImage(file="Flashcard_Spanish\images\wrong.png")
check_image = PhotoImage(file="Flashcard_Spanish/images/right.png")

unknown_button = Button(image= cross_image, command= next_card)
unknown_button.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
unknown_button.grid(row=1, column=0)

known_button = Button(image= check_image, command= known_card)
known_button.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
known_button.grid(row=1, column=1)




next_card()
window.mainloop()



