import datetime
import time


i = time.strftime("%c")
now = datetime.datetime.now()

# used for signature line
underline = "_______________________________________"

# legal text for body of document

declare = ("We, %s and %s, both of %s, SOLEMNLY AFFIRM AND DECLARE THAT:")

sole_declare = ("I, %s, of %s, SOLEMNLY AFFIRM AND DECLARE THAT:")

marriage_law = ("We understand that the acceptance of this affidavit by " +
                "the Carleton University Awards Office and the Ontario " +
                "Ministry of Advanced Education and Skills Development " +
                "in no way constitutes a legal determination that our " +
                "common law marriage is valid under applicable law.")

aff_purpose = ("The information contained in this affidavit is provided " +
               "for the sole purpose of supporting an application for " +
               "financial aid under the Ontario Student Assistance Program " +
               "(OSAP).")

living = ("We are living together in a conjugal relationship and have done " +
          "so continuously since %s")

separated_date = ("We separated on or about %s and have lived in separated residences ever since. We have no formal legal separation agreement")

solecust = ("I have sole physical custody of my child(ren). They reside with me on a full-time basis.")

custodial = ("We are the custodial and natural(or adoptive) parents of %d " +
             "child(ren), namely:")

separated = ("My marital status is separated")

affirmed = ("SWORN/AFFIRMED BEFORE ME, at Carleton University, " +
            "Ottawa, Ontario this %s day of %s, %s" %
            (time.strftime("%d"), time.strftime("%B"), now.year))

# questions for user input
q_student_name = ("Student Name", "Please enter the student's name")
q_spouse_name = ("Spouse Name", "Please enter the spouse's name")
q_location = ("Location", "Please enter the city and province")
q_date_living = ("Date Living Since",
                 "Please enter the date the couple began living together")

q_ch = ("Please enter the birth date of child %d in Month, Date, Year Format")

q_chn = "Please enter the full name of child %d"
