# flow1.py
from datetime import datetime, timedelta
import mongo as mg
import testmail as tstm

def lend_book(name, usn, book_id, email):
    # Get the current date and return date (14 days later)
    s = datetime.now().date()
    sd = datetime.combine(s, datetime.min.time())
    ld = sd + timedelta(days=14)

    print("Date: ", sd)
    print("Date2:", ld)

    # Prepare the data for insertion into MongoDB
    dat = {
        "name": name,
        "USN": usn,
        "Book Id": book_id,
        "email id": email,
        "Submission Date": sd,
        "Return Date": ld
    }

    # Insert data into MongoDB
    try:
        mg.insert(dat)
    except Exception as e:
        print("Couldn't insert data into database.")
    else:
        print("Data added to database successfully!")

    # Prepare and send the email
    msg = f"""You have borrowed a book with id {book_id} from the library.

    Last date to return the book is {ld}.
    Enjoy reading,
    Thank you.
    """
    subject = "Borrowed Book"
    try:
        tstm.email(email, msg, subject, name)
    except Exception as e:
        print("Error in sending mail:", e)
    else:
        print("Mail sent successfully!")
