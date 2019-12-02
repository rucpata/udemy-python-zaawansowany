import smtplib

mailFrom = 'Your automation system' #od kogo mail
mailTo = ['rucinska.patrycja@gmail.com', 'soulrelive@gmail.com'] #do kogo mail
mailSubject = 'Proccesing finished successfully' #temat

mailBody ='''Hello
This mail confirms that processing has finished without proclems,

Have a nice day!''' #treść maila

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)

user = ''
password = ''

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')
