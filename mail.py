import smtplib 

mailuser = '<SEND MAIL FROM USER>'
password = '<PASSWORD>'
to = '<SEND MAIL TO>'
smtp_server_adress = 'smtp.mailserver.com'
smtp_port = '587'

sent_from = mailuser
subject = 'Test from Python mail'
body = 'Test from Python Script'

email_text = """\
    From: %s
    To: %s
    Subject %s

    %s
""" % (sent_from, to, subject, body)

try:
    smtp_server = smtplib.SMTP(smtp_server_adress, smtp_port)
    smtp_server.starttls()
    smtp_server.login(mailuser, password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.quit()
    print ("Email sent successfully!")
except Exception as e:
    print("Somthing went wrong...", e)