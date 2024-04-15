import os
import smtplib
from datetime import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_username = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASS')


def build_message_email(list_acao_object: list, list_indice_object: list):
    subject = 'Relatório Ações {}'.format(datetime.now().strftime('%d-%m-%Y'))
    message = ''

    for indice_object in list_indice_object:
        message += '\n{}\nAbertura: {} pontos\nEncerramento: {} pontos\nVariação Diária: {}%\n'.format(
            indice_object.longName,
            indice_object.regularMarketOpen,
            indice_object.regularMarketPrice,
            indice_object.regularMarketChangePercent
        )

    for acao_object in list_acao_object:
        message += '\nAção: {}\nPreço Abertura: {}\nPreço Encerramento: {}\nVariação Diária: {}%\n'.format(
            acao_object.symbol,
            acao_object.regularMarketOpen,
            acao_object.regularMarketPrice,
            acao_object.regularMarketChangePercent
        )

    print(message)

    send_email(message, subject)


def send_email(message: str, subject: str):
    smtp_server = 'smtp.office365.com'
    smtp_port = 587

    para = 'rickteixeira28@gmail.com'

    mensagem = MIMEMultipart()
    mensagem['To'] = para
    mensagem['Subject'] = subject

    mensagem.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        texto_email = mensagem.as_string()
        server.sendmail(smtp_username, para, texto_email)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
    finally:
        server.quit()