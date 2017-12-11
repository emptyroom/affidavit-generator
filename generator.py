#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
   root = Tk()
   Label(root, text="Select the type of affidavit").grid(row=1)


   afflist = ['Common Law No Kids', 'Common Law Kids']

   afftypevar = StringVar()

   afftype = ttk.Combobox(root, textvariable=afftypevar)
   afftype['values'] = afflist
   afftype.grid(row=2)


   quit = Button(root, text="Quit", command=quit).grid(row=3, column=2)
   generate = Button(root, text="Select").grid(row=3, column = 1)

   root.geometry('300x200')
   root.mainloop()
