import email.message
msg = email.message.EmailMessage()
from_a=input("請輸入寄件人信箱：")
to_b=input("請輸入收件人信箱：")
msg["from"] = from_a
msg["To"] = to_b
msg["Subject"] = "你好"

msg.set_content("test test")
#msg.add_alternative("<h3>HTML內容</h3>安安這是寄送郵件測試",subtype="html") 

import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login('tbo79435@gmail.com','dcxpnsmytgojenav')
server.send_message(msg)
server.close()

