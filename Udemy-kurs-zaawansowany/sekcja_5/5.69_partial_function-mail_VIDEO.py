import smtplib
import functools

def SendInfoEmail(user,password, mailFrom, mailTo, mailSubject, mailBody):

    message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending email')
        return False

mailFrom = 'Your automation system' #od kogo mail
mailTo = ['rucinska.patrycja@gmail.com'] #do kogo mail
mailSubject = 'Proccesing finished successfully' #temat

mailBody ='''Hello
This mail confirms that processing has finished without proclems,

Have a nice day!''' #treść maila

user = ''
password = ''

SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password, mailSubject = 'Execution alert')

SendInfoEmailFromGmail(mailFrom = mailFrom, mailTo = mailTo, mailBody = mailBody)

#SendInfoEmail(user,password, mailFrom, mailTo, mailBody)