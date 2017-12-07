from docx import Document
from docx.shared import Pt

document = Document('affidavit-template.docx')
document.save('affidavit-new.docx')
document._body.clear_content()

print "What is the student's first and last name?"
studentName = raw_input()

print "What is the spouse's first and last name?"
spouseName = raw_input()

print "What is the city and province?"
location = raw_input()

title = document.add_heading('AFFIDAVIT OF MARRIAGE')
title.style = document.styles['Heading 1']
run = title.add_run()
run.add_break()

p = document.add_paragraph("We, %s and %s, both of %s, SOLEMNLY AFFIRM AND DECLARE THAT:" % (studentName, spouseName, location))


document.save('affidavit-new.docx')
