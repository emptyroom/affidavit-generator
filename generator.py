#!/usr/bin/python
# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt
from tkinter import *
from tkinter import ttk
import tkSimpleDialog
import subprocess


class mainapp:
    def __init__(self, master):

        self.master = master
        master.title("Affidavit Generator")

        self.label = Label(root, text="Select the type of affidavit").grid(row=1)
        self.label = Label(root, text="What you'll need").grid(row=3, column=0)

        self.afftype_text = StringVar()
        self.afftype_text = 'No program selected'
        self.afftype = ttk.Combobox(root, textvariable=self.afftype_text)
        self.afftype['values'] = aff_script.keys()
        self.afftype.grid(row=2)
        self.afftype.bind('<<ComboboxSelected>>')

        self.quit = Button(root, text="Quit", command=self.client_exit).grid(row=3, column=2)
        self.make = Button(root, text="Start", command=self.make_doc(afftype)).grid(row=3, column = 1)


    def client_exit(self):
        exit()

    #def run_program(self):
    #    self.var_Selected = self.afftype.get()
    #    print "will run program %s" % self.var_Selected
    #
    #    for i in afflist:
    #        print i
    #        if i == self.var_Selected:
    #            print afflist[i]
    #            subprocess.Popen(['python', afflist[self.var_Selected]])


def make_doc(type):

    #use template and generate new
    document = Document('affidavit-template.docx')
    document.save('affidavit-%s.docx' %studentName)
    document._body.clear_content()



if __name__ == '__main__':

   root = Tk()

   aff_script = {'Common Law No Kids' : 'affidavit-marriage.py', 'Common Law Kids' : 'affidavit-marriage-kids.py'}

   #document structures
   marital_no_kids = [legal.title,   ]

   #document questions

   

   main_app = mainapp(root)
   root.geometry('300x100')
   root.mainloop()
