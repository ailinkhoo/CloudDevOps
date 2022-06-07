# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("devopspractice88@gmail.com", "321*cba!")

# email addresses

receiver_email_id = input("Type the receiver email and press enter:")

# message to be sent
message = input("Type the message and press enter:")

# sending the mail

s.sendmail("devopspractice88@gmail.com", receiver_email_id, message)

# terminating the session
s.quit()
