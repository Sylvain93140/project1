# project1
Archived Windows old files

Créé par Sylvain ARUMUGAM
Version 1.0

OS : Windows 10 Pro (20H2)

Python Version : 3.9

Ce script permet de lister les différents dossiers d’un répertoire sous Windows 
puis de les compresser au format ZIP si la date de dernière modification de ses dossiers dépasse une certaine période.
Le script génère un fichier de log à chaque compression d’un dossier et envoi également l’information par mail.

Les paramètres à moduler selon vos besoins sont ceux ci :

ARCHIVE_PATH = 'C:\python' 												#le chemin du dossier que vous souhaitez analyser

nbresjours = 365														#le nombre de jour suite a laquelle le script archive les dossiers

logs = 'C:/Windows/logarchive\data.txt'									#l'emplacement du fichier de log qui sera implémenter d'une nouvelle ligne à chaque archivage

gmail_user = 'xxxxx'													#compte mail 

gmail_password = 'xxxxxx'												#mot de passe du compte mail

to = 'xxxxxx'															#destinataire du fichier log

subject = "New file add to archive"										#sujet du mail

body = ("[%s] Add %s to archive \n" % (now, directoryPath))				#corps du mail (par défaut : contient fichier archivé, empalcement, date, heure)



