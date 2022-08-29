# :snake: Python SMTP Test
This is very simple and easy python script to test if it is possible to send email via your SMTP Server using STARTTLS.

## Requirements
You need to have `Python 3.x` installed and the script are using `smtplib` library.

## Setup, Configuration and Run
Download the Git repo locally on your computer, 

Modify the `mail.py` file with your favorit editor and change the lines
- mailuser (E-Mail account that you will send from)
- password (From E-Mail account password)
- to (E-Mail address you want to test send your e-mail to)
- smtp_server_address (DNS record to your SMTP Server)
- smtp_port (Your STARTTLS SMTP Port default is 587)

```
mailuser = 'test@mail.com'
password = 'MySuperPassword'
to = 'your.email@mail.com'
smtp_server_adress = 'smtp.mail.com'
smtp_port = '587'
```

And to run the command you just need to run
```
python mail.py
```

If succssfull your will see the output `Email sent successfully!'
If unsuccssfull your will get the error example `Somthing went wrong... [Errno 110] Connection timed out`

## License
This is just a quick script, use it, help to maintain it, or use it as a guideline for free. 