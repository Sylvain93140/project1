import os  # os : pour l’interaction avec l’OS
# datetime, timedelta : utilisation des dates dans le script
from datetime import datetime, timedelta
import shutil  # shutil : archivage au format zip
import smtplib  # envoi du mail

ARCHIVE_PATH = 'C:\python'
nbresjours = 365
now = datetime.today()
delta = timedelta(days=nbresjours)
logs = 'C:\Windows\log archive\log.txt'
gmail_user = ''
gmail_password = 'xxxxxx'
to = ['xxxxxx']

# possibilité d’adapter les variables selon nos besoins

# pour chaque dossier dans notre répertoire
for directory in os.listdir(ARCHIVE_PATH):
    # nous permet de manipuler les chemins de fichier
    directoryPath = os.path.join(ARCHIVE_PATH, directory)
    if os.path.isdir(directoryPath):  # si des dossiers existent
        # convertir les dates epoches au format ordinaire
        directoryTime = datetime.fromtimestamp(os.path.getmtime(directoryPath))
        if now - directoryTime > delta:  # si la date est + ancienne que 1 an

            try:

                shutil.make_archive(directoryPath, 'zip',
                                    directoryPath) and shutil.rmtree(directoryPath, ignore_errors=True)  # archive en zip

            except IOError:
                print("chemin non existant")

            try:  # rajoute une ligne à chaque archivage dans le fichier de log

                f = open(logs, "a")

                f.write("[%s] Add %s to archive \n" % (now, directoryPath))

                f.close()

            except IOError:
                print("erreur")

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

# envoi un mail avec le dossier archivé en question (récupère la ligne rajouté sur le fichier log)
