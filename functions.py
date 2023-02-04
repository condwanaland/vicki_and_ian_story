from email.message import EmailMessage
import smtplib

def init_email(sender_email: str, to_email: str, q_no: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = f"Weekly Question. Number {q_no}"
    message['From'] = sender_email
    message['To'] = to_email
    return message

def send_email(message, sender_email, sender_pword) -> None:
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.login(sender_email, sender_pword)
    mail_server.send_message(message)
    mail_server.quit()