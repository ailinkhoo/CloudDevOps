import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg["From"] = "devopspractice88@gmail.com"
msg["To"] = input("Type the destination and press enter: ")
msg["Subject"] = input("Type the subject and press enter: ")
msg.attach(MIMEText(input("Type the message and press enter: "), "plain"))


filename = "meme.jpg"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)    

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
msg.attach(part)
text = msg.as_string()


# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("devopspractice88@gmail.com", "321*cba!")
server.send_message(msg)

# terminating the session
server.quit()
print ("Email sent.")
