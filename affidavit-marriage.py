from docx import Document
from docx.shared import Pt
from datetime import *

document = Document('affidavit-template.docx')
document.save('affidavit-new.docx')
document._body.clear_content()

print "What is the student's first and last name?"
studentName = raw_input()

print "What is the spouse's first and last name?"
spouseName = raw_input()

print "What is the city and province?"
location = raw_input()

print "What date did the couple start living together?"
livingsince = raw_input()

title = document.add_heading('AFFIDAVIT OF MARRIAGE')
title.style = document.styles['Heading 1']
run = title.add_run()
run.add_break()

p = document.add_paragraph(
    "We, %s and %s, both of %s, SOLEMNLY AFFIRM AND DECLARE THAT:" % (
    studentName, spouseName, location))

run = p.add_run()
run.add_break()

p = document.add_paragraph(
        "We are living together in a conjugal relationship, and have done so continuously since %s""" % livingsince)
p.style = document.styles['ListNumber']
run = p.add_run()
run.add_break()

p = document.add_paragraph(
        "The information contained in this affidavit is provided for the sole purpose of supporting an application for financial aid under the Ontario Student Assistance Program (OSAP).")
p.style = document.styles['ListNumber']
run = p.add_run()
run.add_break()

p = document.add_paragraph(
        "We understand that the acceptance of this affidavit by the Carleton University Awards Office and the Ontario Ministry of Advanced Education and Skills Development in no way constitutes a legal determination that our common law marriage is valid under applicable law.")
p.style = document.styles['ListNumber']
run = p.add_run()
run.add_break()

table = document.add_table(rows = 2, cols = 2)
sworn = table.cell(0, 1)
sworn.text = "SWORN/AFFIRMED BEFORE ME, at Carleton University, Ottawa, Ontario this"


document.save('affidavit-new.docx')
