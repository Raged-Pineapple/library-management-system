# flow3.py
import mongo as mg
import testmail as tst
import logging as lg
from datetime import *

def mark_book_returned(usn):
    # Fetch the user's data by USN
    dt = {"USN": usn}
    ev = mg.extract(dt)

    if not ev:
        print("No record found for the given USN.")
        return

    tad = ev[0]["email id"]
    nam = ev[0]["name"]
    id = ev[0]["Book Id"]
    t = datetime.now()
    sub = "Book Returned to Library"
    mesg = f"You have submitted the book with ID {id} on {t}"

    try:
        tst.email(tad, mesg, sub, nam)
        print(f"Email sent to {tad} confirming return of Book ID: {id}")
    except Exception as ex:
        lg.error(f"Failed to send mail! Error: {ex}")
        print(f"Failed to send mail to {tad} due to error: {ex}")
