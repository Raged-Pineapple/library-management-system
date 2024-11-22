# Library Management System  

## Overview  
The **Library Management System** is a Python-based GUI application designed to streamline library operations. This intuitive system simplifies book lending, return alerts, and return tracking with clearly defined sections, enhancing user experience and operational efficiency.  

---

![Sample Run](images/Sample%20run.jpg)

- Submitting the Name, USN, Book ID, and E-Mail. Click on **Submit** to insert the data into the database.

![Sample Run 2](images/Sample%20run%202.jpg)

- **Send Alert** Feature

![Sample Run 3](images/Sample%20run%203.jpg)

- Enter **USN** to return a book.

---

## Features  

### 1. **Lending Books**  
- Accepts details like Name, USN, Book ID, and Email to lend books.  
- Validates input to ensure all fields are completed.  
- Includes "Submit" and "Cancel" options to manage lending operations.  

### 2. **Sending Return Alerts**  
- A feature to send email alerts to users for overdue book returns.  
- Simple interface for quick alert generation.  

### 3. **Marking Book Returns**  
- Allows librarians to mark books as returned by entering the user's USN.  
- Ensures efficient tracking of returned books.  

### 4. **Dynamic Section Selection**  
- Users can switch between functionalities (Lending, Alerts, Returns) via intuitive radio buttons.  
- Only the selected section is displayed, keeping the interface clutter-free.  

### 5. **User-Friendly GUI**  
- Built using Tkinter for a clean and visually appealing design.  
- Displays clear messages for input errors and successful actions.  

---

## Technologies Used  
- **Programming Language:** Python  
- **GUI Framework:** Tkinter  
- **Database:** MongoDB  
- **Mail:** SMTP  

---

## Installation  

### Prerequisites  
Ensure you have the following installed:  
- Python 3.12 or later  

### Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/raged-pineapple/library-management-system.git
   cd library-management-system
