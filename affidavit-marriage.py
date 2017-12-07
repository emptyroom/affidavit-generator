from docx import Document
from docx.shared import Inches

document = Document()

print "What is the student's first and last name?"
studentName = raw_input()

print "What is the spouse's first and last name?"
spouseName = raw_input()

print "What is the city and province?"
location = raw_input()

heading.style = document.styles['Heading 1']

document.add_heading('AFFIDAVIT OF MARRIAGE', 0)

p = document.add_paragraph("We, %s and %s, both of %s, SOLEMNLY AFFIRM AND DECLARE THAT:" % (studentName, spouseName, location))

document.save('affidavit-new.docx')
