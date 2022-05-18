import email.message
msg = email.message.EmailMessage()
msg["from"] = "tbo79435@gmail.com"
msg["To"] = "tt5436301@gmail.com"
msg["Subject"] = "你好"

msg.set_content("測試看看")
#msg.add_alternative("<h3>HTML內容</h3>安安這是寄送郵件測試",subtype="html") 

import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login('tbo79435@gmail.com','mctztyaucasqbbpr')
server.send_message(msg)
server.close()