# Import smtplib for the actual sending function
import smtplib

class Email(object):
    
    def __init__(self):
        pass
        
    def email(self,subject,message):
        
        me = 'barbie@deterministicprogramming.com'
        you = 'william.k.dvorak@gmail.com'
        
        message = "Subject: [BTC] " + subject + "\n" + message
        
        auth_file = open("../../Barbie_auth.txt",'r')
        key = auth_file.readline().strip()
        secret = auth_file.readline().strip()
        my_send_email = auth_file.readline().strip()
        password = auth_file.readline().strip()
        
        
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(my_send_email,password)
        s.sendmail(me, [you], message)
        s.quit()