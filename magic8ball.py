
from tkinter import *
from tkinter import ttk
from random import randint

replies = ['It is certain',
           'It is decidedly so',
           'Without a doubt',
           'Yes definitely',
           'You may rely on it',
           'As I see it, yes',
           'Most likely',
           'Outlook good',
           'Yes',
           'Signs point to yes',
           'Reply hazy try again',
           'Ask again later',
           'Better not tell you now',
           'Cannot predict now',
           'Concentrate and ask again',
           'Do not count on it',
           'My reply is no',
           'My sources say no',
           'Outlook not so good',
           'Very doubtful']


answer = ""

def ask():
    global replies
    global answer
    answer = (replies[(randint(0, 19))])
    answer.format()
    lbl.configure(text=answer)


# def restart():
#     print("Would you like to ask again? \n")
#     again = input("")
#     if again == 'y'or 'yes':
#         ask()
#     else:
#         print("\n Goodbye! \n")


window = Tk()
window.title("Magic 8 Ball")


userInput = StringVar()

prompt = ttk.Label(window, text="Please ask your question")
prompt.pack()

question = ttk.Entry(window, textvariable=userInput)
question.pack()

btn = ttk.Button(window, text="Ask the magic 8 ball", command=ask)
btn.pack()

lbl = ttk.Label(window, textvariable=answer)
lbl.pack()

window.mainloop()
