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

separated_date = ("We separated on or about %s and have lived in separated "
                  "residences ever since. We have no formal legal separation "
                  "agreement.")

solecust = ("I have sole physical custody of my child(ren). " +
            "They reside with me on a full-time basis.")

sharecust = ("My spouse and I share the physical custody of our children " +
             "as follows")

cl_cust = ("We are the custodial and natural(or adoptive) parents of %d " +
           "child(ren), namely:")

sp_cust = ("We are the adoptive or natural parents of %d child(ren), namely:")

separated = ("My marital status is separated.")

affirmed = ("SWORN/AFFIRMED BEFORE ME, at Carleton University, " +
            "Ottawa, Ontario this %s day of %s, %s" %
            (time.strftime("%d"), time.strftime("%B"), now.year))

s_oath = ("I make this solemn declaration conscientiously knowing it " +
          "to be true and knowing that it is of the same force and effect " +
          "as if made under oath.")
