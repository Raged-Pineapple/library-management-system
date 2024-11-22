from pymongo import MongoClient

# Create a MongoDB client instance
client = MongoClient('mongodb://localhost:27017/')  # Change to your DB URL

# Access your database
db = client["library_management"]

# Access the collection where you want to store books data
books_collection = db["books"]  # Ensure this line is in the correct scope

# Function to insert data into the 'books' collection
def insert_data(name, usn, book_id, email):
    """ Insert book information into the database. """
    book_data = {
        "name": name,
        "usn": usn,
        "book_id": book_id,
        "email": email,
        "status": "issued"  # You can adjust the status based on your requirements
    }
    try:
        result = books_collection.insert_one(book_data)
        if result.acknowledged:
            print("Data inserted successfully")
        else:
            print("Data insertion failed")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Function to extract data from MongoDB based on a query
def extract(query):
    """ Extract data based on a query (e.g., USN, book ID). """
    try:
        ev = list(books_collection.find(query))  # Convert Cursor to list for further processing
        return ev
    except Exception as e:
        print(f"Error extracting data: {e}")
        return []

# Function to send alert for a book with a specific return date
def send_return_alert(return_date):
    """ Send alert for books that need to be returned by a specific date. """
    try:
        ev = list(books_collection.find({"status": "issued", "return_date": {"$lte": return_date}}))  # Adjust query if necessary
        print(f"Found {len(ev)} entries with return date {return_date}")
        for entry in ev:
            print(f"Sending alert for: {entry['email']}")
            # Add email sending code here if needed
    except Exception as e:
        print(f"Error sending return alert: {e}")

# Function to mark the book as returned (by USN)
def mark_book_returned(usn):
    """ Mark the book as returned by updating its status. """
    try:
        result = books_collection.update_one(
            {"usn": usn, "status": "issued"},  # Search condition (book issued)
            {"$set": {"status": "returned"}}   # Update the status to "returned"
        )
        if result.matched_count > 0:
            print(f"Book returned for USN: {usn}")
        else:
            print(f"No book found for USN: {usn} or already returned.")
    except Exception as e:
        print(f"Error marking book returned: {e}")

# # Test insertion with sample data
# insert_data("John Doe", "12345", "001", "john.doe@example.com")
