# cpho juux uvwy clnd

from mailerpy import Mailer

password = "cpho juux uvwy clnd"

my_mailer = Mailer("smtp.gmail.com", 587, "rabindrasapkota2@gmail.com", password)

to_emails = ['bijayayer68@gmail.com', 'joshipratikdhn@gmail.com']
attachment = [r'C:\Users\hp\OneDrive\Desktop\PersonalSite\public\courses\data_science\data_files\app.log'
              ]
subject = "Test From Python"
body = f"""
Hello Guys,

This is from code.

Regards,
Automation Engine
"""


for to_email in to_emails:
    mail_body = body.replace("Guys", to_email.split('@')[0])
    my_mailer.send_mail([to_email], subject, mail_body, attachments=attachment)