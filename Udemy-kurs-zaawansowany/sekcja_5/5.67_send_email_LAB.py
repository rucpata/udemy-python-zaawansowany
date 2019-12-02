import smtplib

mailFrom = 'rucinska.patrycja@gmail.com'
mailTo = ['rucinska.patrycja@gmail.com']
mailSubject = 'Test'
mailBody = '''Testujemy
Test.

Test.'''

message ='''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)

user = ''
password = ''

try:
    server =smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(mailFrom, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')