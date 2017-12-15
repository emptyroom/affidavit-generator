import datetime
import time

i = time.strftime("%c")
now = datetime.datetime.now()

underline = "_______________________________________"

affirmed = "SWORN/AFFIRMED BEFORE ME, at Carleton University, Ottawa, Ontario this %s day of %s, %s" % (time.strftime("%d"), time.strftime("%B"), now.year)
