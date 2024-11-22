# flow2.py
import testmail as tst
import mongo as mg
from datetime import *
import logging as lg

def send_return_alert():
    # Define the return date for which books need to be alerted
    d = date(2024, 11, 23)
    rd = datetime.combine(d, datetime.min.time())
    dt = {"Return Date": rd}

    # Fetch the relevant records from MongoDB
    ev = mg.extract(dt)

    # Print how many records were returned
    print(f"Found {len(ev)} entries with return date {rd}")

    # Loop through the records and send alerts
    for i in range(len(ev)):
        try:
            tad = ev[i]["email id"]
            nam = ev[i]["name"]
            id = ev[i]["Book Id"]
            t = datetime.now().date()
            sd = datetime.combine(t, datetime.min.time())
            sub = "Book Returning Due"
            mesg = f"Book with ID {id}, submission is due on {t}"

            # Send the email
            tst.email(tad, mesg, sub, nam)
            print(f"Email sent to {tad} for Book ID: {id}")

        except KeyError as key_err:
            lg.error(f"Missing field in record {ev[i]}: {key_err}")
            print(f"Missing field in record {ev[i]}: {key_err}")

        except Exception as ex:
            lg.error(f"Failed to send mail! Error: {ex}")
            print(f"Failed to send mail to {tad} due to error: {ex}")
