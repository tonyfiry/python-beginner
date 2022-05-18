import email.message
msg = email.message.EmailMessage()
msg["from"] = "tt5436301@gmail.com"
msg["To"] = "tt5436301@gmail.com"
msg["Subject"] = "安安"

#msg.set_content("測試看看")
msg.add_alternative("<h3>HTML內容</h3>安安這是寄送郵件測試",subtype="html") 

import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login('tt5436301@gmail.com','fstohfbtvwqihsgf')
server.send_message(msg)
server.close()