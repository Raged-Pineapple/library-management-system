import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email(eid,msg,sub,na):
    # Your email credentials
    sender_email = "sonu11071107@gmail.com"
    receiver_email = eid
    password = "vpoc cftu ceil noim"

    # Email content
    subject = sub
    body = f"""Hello {na},
    {msg}"""

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

email("sonu11071107@gmail.com","hello...","test bro ","mithun")


