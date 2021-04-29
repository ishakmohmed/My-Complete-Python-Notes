# import webbrowser

# print("DEPLOYMENT COMPLETED")

# webbrowser.open("https://www.youtube.com")

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Me"
message["to"] = "ishakmohmed1911@gmail.com"
message["subject"] = "This is a test"

body = template.substitute({"name": "John"})
# or in .substitute, pass keyword argument > name="John"

message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("defaultWindows10.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("ishakmohmed1911@gmail.com", "notrealpassword")
    smtp.send_message(message)
    print("MESSAGE SENT!")
