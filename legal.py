import datetime
import time
import generator


i = time.strftime("%c")
now = datetime.datetime.now()

#used for signature line
underline = "_______________________________________"


#legal text for body of document
affirmed = """SWORN/AFFIRMED BEFORE ME, at Carleton University,\
              Ottawa, Ontario this %s day of %s, %s""" % (
              time.strftime("%d"), time.strftime("%B"), now.year)

marriage_law = ("We understand that the acceptance of this affidavit by" +
                "the Carleton University Awards Office and the Ontario" +
                "Ministry of Advanced Education and Skills Development" +
                "in no way constitutes a legal determination that our" +
                "common law marriage is valid under applicable law.")

#questions for user input
q_student_name("Student Name", "Please enter the student's name")
q_spouse_name("Spouse Name", "Please enter the spouse's name")
q_location("Location", "Please enter the city and province")
q_date_living("Date Living Since",
              "Please enter the date the couple began living together")

title = "Affidavit"

intro_couple = ("We, %s and %s, both of %s, SOLEMNLY AFFIRM AND DECLARE THAT:"
                 % (studentName, spouseName, location)

                
