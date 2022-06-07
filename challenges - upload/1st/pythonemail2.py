import smtplib

from email.message import EmailMessage

try:
    msg = EmailMessage()

    msg['Subject'] = input("Type the subject and press enter: ")
    msg.set_content(input("Type the message and press enter: "))
    msg['From'] = "devopspractice88@gmail.com"
    msg['To'] = input("Type the destination and press enter: ")

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("devopspractice88@gmail.com", "321*cba!")
    server.send_message(msg)

    # terminating the session
    server.quit()
    print ("Email sent.")
    
except:
    print ("error")