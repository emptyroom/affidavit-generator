#!/usr/bin/python
# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt

from tkinter import *
from tkinter import ttk

import tkSimpleDialog
import tkMessageBox

import subprocess
import legal


class mainapp:

    def __init__(self, master):

        self.master = master
        master.title("Affidavit Generator")

        # top menubar
        self.menubar = Menu(root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="About", command=self.about)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        root.config(menu=self.menubar)

        self.label = Label(root, text="Select the type of affidavit",
                           padx=4, pady=4).grid(row=0, column=0)

        # frame for showing what info i needed
        self.title = Label(root, text="What you'll need").grid(row=3)

        self.info_frame = Frame(root, highlightbackground="grey",
                                highlightcolor="grey", highlightthickness=1,
                                bd=0)

        self.info_frame.grid(row=4, column=0, padx=4, pady=4)

        self.info = StringVar()
        self.info.set("What you'll need")
        self.info_label = Label(self.info_frame, wraplength=150,
                                textvariable=self.info).grid(row=4)

        # combobox
        self.value = StringVar()
        self.afftype = ttk.Combobox(self.master, textvariable=self.value,
                                    state='readonly')
        self.afftype['values'] = aff_info_required.keys()
        self.afftype.current(0)
        self.afftype.grid(row=2)
        self.afftype.bind('<<ComboboxSelected>>', self.displayinfo(self.info))

        self.make = Button(root, text="Generate", padx=2, pady=2,
                           command=self.make_doc)
        self.make.grid(row=2, column=1)

    def client_exit(self):
        exit()

    def about(self):
            tkMessageBox.showinfo("About",
                                  "made by Shaun Anderson with python-docx")

    def displayinfo(self, event):
        i = []
        for x in aff_info_required.keys():
            i.append(aff_info_required[x])
        self.info.set(i)

    def get_info(self):

            studentName = tkSimpleDialog.askstring("Student Name",
                                                   ("Please enter the "
                                                    "student's name"))
            spouseName = tkSimpleDialog.askstring("Spouse Name",
                                                  "Please enter the spouse's name")
            location = tkSimpleDialog.askstring("Location",
                                                "Please enter the city and province")
            livingsince = tkSimpleDialog.askstring("Date Living Since",
                                                   ("Please enter the date the couple "
                                                    "began living together"))

            children = tkMessageBox.askquestion("Children", "Do they have dependents?")

            childrenNames = []
            childrenBdays = []

            if children == 'yes':
                number_of_children = tkSimpleDialog.askinteger("Number", "How many kids?")
                for i in range(0, number_of_children):
                    childrenNames.append(tkSimpleDialog.askstring(
                                    "Child Name", "Please enter the name of child %d" % (i+1)))
                    childrenBdays.append(tkSimpleDialog.askstring("Child Birth Date",
                                                                  ("Please enter the birth "
                                                                   "date of child %d in "
                                                                   "MONTH DATE, YEAR format"
                                                                   % (i+1))))

            return {'Student Name': studentName, 'Spouse Name': spouseName,
                    'Location': location, 'Living Since': livingsince,
                    'Children Names': childrenNames, 'Children Birthdays':
                    childrenBdays, 'Children': number_of_children}


    def make_doc(self):
        answers = self.get_info()
        print answers
        document = Document('affidavit-template.docx')
        document.save('affidavit-%s.docx' % answers["Student Name"])
        document._body.clear_content()

        title = document.add_heading('AFFIDAVIT OF MARITAL STATUS')
        title.style = document.styles['Heading 1']
        run = title.add_run()
        run.add_break()

        country = document.add_table(rows=4, cols=2)
        country.style = 'none'

        canada = country.cell(0, 0)
        canada.text = 'Canada'

        rightBracket = country.cell(0, 1)
        rightBracket.text = ')'

        province = country.cell(1, 0)
        province.text = 'Province of Ontario'

        provinceRB = country.cell(1, 1)
        provinceRB.text = ') S. S.'

        finalRB = country.cell(2, 1)
        finalRB.text = ')'

        p = document.add_paragraph(
                "We, %s and %s, both of %s, SOLEMNLY AFFIRM AND DECLARE THAT:" % (
                 answers["Student Name"], answers["Spouse Name"],
                 answers["Location"]))

        run = p.add_run()
        run.add_break()

        p = document.add_paragraph("We are living together in a conjugal relationship"+
                                   "and have done so continuously since %s"
                                   % answers["Living Since"])

        p.style = document.styles['ListNumber']

        if answers["Children"] > 0:

            p = document.add_paragraph("We are the custodial and natural (or adoptive)" +
                                       "parents of %d child(ren), namely:" % answers['Children'])
            p.style = document.styles['ListNumber']
            run = p.add_run()
            run.add_break()
            run.add_break()

            children_names = answers['Children Names']
            children_bdays = answers['Children Birthdays']

            for i in range(0, answers["Children"]):
                    run = p.add_run("%s, born %s" % (children_names[i], children_bdays[i]))
                    run.add_break()
                    run.add_break()

        p = document.add_paragraph(legal.aff_purpose)

        p.style = document.styles['ListNumber']
        run = p.add_run()
        run.add_break()

        p = document.add_paragraph(legal.marriage_law)
        p.style = document.styles['ListNumber']

        run = p.add_run()
        run.add_break()
        run.add_break()
        run.add_break()

        table = document.add_table(rows=6, cols=2)
        table.style = 'Hello'

        sworn = table.cell(0, 0)
        sworn.text = legal.affirmed

        firstUnderline = table.cell(0, 1)
        firstUnderline.text = legal.underline

        firstSig = table.cell(0, 1)
        firstSig.add_paragraph(answers["Student Name"])

        commUnderline = table.cell(5, 0)
        commUnderline.add_paragraph(legal.underline)

        commissioner = table.cell(5, 0)
        commissioner.add_paragraph("Mark Alexander Robinson")

        secondUnderline = table.cell(5, 1)
        secondUnderline.add_paragraph(legal.underline)

        secondSig = table.cell(5, 1)
        secondSig.add_paragraph(answers["Spouse Name"])

        document.save('affidavit-%s.docx' % answers["Student Name"])

#    def run_program(self):
#        self.var_Selected = self.afftype.get()
#        print "will run program %s" % self.var_Selected
#
#        for i in afflist:
#            print i
#            if i == self.var_Selected:
#                print afflist[i]
#            subprocess.Popen(['python', afflist[self.var_Selected]])

if __name__ == '__main__':

    root = Tk()

    aff_info_required = {'Common Law': ['Student Name', 'Spouse Name',
                         'Number of Children', 'Names of Children',
                         'Birthdates of Children', 'Location',
                         'Date living since']}

    main_app = mainapp(root)
    root.geometry('300x200')
    root.mainloop()
