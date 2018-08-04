import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logger import Logger
import datetime

class Mailer(object):

    def __init__(self, from_mail, smtp_pass):
        self.from_mail = from_mail
        self.smtp_pass = smtp_pass
        self.logger = Logger(self.__class__.__name__).get()

    def send_mail(self, subject, body, to_email):
        fromaddr = self.from_mail
        toaddr = to_email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com:465')
            server.login(fromaddr, self.smtp_pass)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            self.logger.info('Successfully sent mail %s' % datetime.datetime.now())
        except Exception as e:
            self.logger.exception(str(e))
            raise
