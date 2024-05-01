import os
import smtplib
from datetime import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_username = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASS')
destination_email = os.getenv('DESTINATION_EMAIL')


def send_email(message: str, subject: str):
    smtp_server = 'smtp.office365.com'
    smtp_port = 587

    mensagem = MIMEMultipart()
    mensagem['From'] = 'Stocks Report'
    mensagem['To'] = destination_email
    mensagem['Subject'] = subject

    mensagem.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        texto_email = mensagem.as_string()
        server.sendmail(smtp_username, destination_email, texto_email)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
    finally:
        server.quit()
