print('-' * 70)

# Mail Handling
import smtplib

# Attachment
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import getpass

# From and To Address
from_addr = 'learnatkit@gmail.com'
to_addr = 'mohanaraj.jagadesan@gmail.com'

# Create the object of MIMEMultipart
msg = MIMEMultipart()

# Store the mail ids
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Test Mail with an Attachment'

# Body of the mail
body = '''Hi There,

This is an Automated Test Mail with an Attachment.

Thanks,
Admin
'''

# Attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# Open the file to be sent
filename = 'ssh_automation.py'
attach = open(filename, 'rb')

# Instance of MIMEBase
base = MIMEBase('application', 'octet-stream')
base.set_payload((attach).read())
encoders.encode_base64(base)
base.add_header('Content-Disposition',
                "attachment; filename=%s" % filename)
msg.attach(base)
print('Message Created')

try:
    # Create SMTP Session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()

    # Authentication
    smtp.login('learnatkit@gmail.com', getpass.getpass())
    print('Server Connected and Authentication Successful')

    # Convert the Multipart msg to a string
    text = msg.as_string()

    # Sending the mail
    smtp.sendmail(from_addr, to_addr, text)

    # Terminate the session
    smtp.quit()

except Exception as e:
    print(e.__class__.__name__ + ' -> ' + str(e))

print('-' * 70)
