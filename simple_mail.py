from smtplib import SMTP, SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.header import Header
import os
from dotenv import load_dotenv
load_dotenv()
mail_id =os.environ.get('mail_id')
mail_pwd =os.environ.get('mail_pwd')
mail_server =os.environ.get('mail_server')
mail_receiver =os.environ.get('mail_receiver')


s = SMTP(host=str(mail_server), port=int(465), timeout=60)
s.starttls()
s.login(str(mail_id), str(mail_pwd))
msg = MIMEMultipart()
msg['From']=str(mail_id)
msg['To']=str(mail_receiver)
msg['Subject']=str('Testing')
msg.attach(MIMEText(str("First Test"), "plain"))
s.send_message(msg)
s.quit()
del msg

# msg = MIMEMultipart()

# msg['From'] = mail_id
# msg['To'] = mail_receiver
# msg['Subject'] = 'Testing'
# body = 'This is a test email from python.'
# msg.attach(MIMEText(body, 'plain'))
# conn = SMTP_SSL(host=mail_server, port=465)
# try:
#     # conn.starttls()
#     conn.login(user=mail_id, password=mail_pwd)
    
#     send =conn.sendmail(from_addr=mail_id,to_addrs=mail_receiver,msg=msg.as_string())
#     print(send)
# except Exception as e:
#     print('error', e)
# finally:
#     conn.quit()