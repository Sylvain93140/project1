import os
from datetime import datetime, timedelta
import shutil
import smtplib

ARCHIVE_PATH = 'C:\python'
nbresjours = 365
now = datetime.today()
delta = timedelta(days=nbresjours)
logs = 'C:\Windows\log archive\log.txt'
gmail_user = ''
gmail_password = 'xxxxxx'
to = ['xxxxxx']


for directory in os.listdir(ARCHIVE_PATH):
    directoryPath = os.path.join(ARCHIVE_PATH, directory)
    if os.path.isdir(directoryPath):
        directoryTime = datetime.fromtimestamp(os.path.getmtime(directoryPath))
        if now - directoryTime > delta:

            try:

                shutil.make_archive(directoryPath, 'zip',
                                    directoryPath) and shutil.rmtree(directoryPath, ignore_errors=True)

            except IOError:
                print("chemin non existant")

            try:

                f = open(logs, "a")

                f.write("[%s] Add %s to archive \n" % (now, directoryPath))

                f.close()

            except IOError:
                print("file not accessible")

            sent_from = gmail_user
            subject = "New file add to archive"
            body = ("[%s] Add %s to archive \n" % (now, directoryPath))

            email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, email_text)
                server.close()
            except:
                print("probleme mail")
