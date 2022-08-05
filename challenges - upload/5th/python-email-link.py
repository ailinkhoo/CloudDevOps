import smtplib
import pytracking

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

msg["From"] = "devopspractice88@gmail.com"
# msg["To"] = input("Type the destination and press enter: ")
msg["To"] = "ytbryan@gmail.com"
msg["Subject"] = input("Type the subject and press enter: ")
#msg.attach(MIMEText(input("Type the message and press enter: "), "plain"))

# Create the plain-text and HTML version of your message
text = ""
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
        <img src="https://pastepixel.com/image/eW4Yu9ew9PN7E8DBTekU.png" alt=""/>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
msg.attach(part1)
msg.attach(part2)

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
server.login("XX", "XX")
server.send_message(msg)

# terminating the session
server.quit()
print ("Email sent.")
