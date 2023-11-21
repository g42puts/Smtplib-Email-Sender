import smtplib
from smtplib import (
    SMTPDataError,          # Error in data passed
    SMTPHeloError,          
    SMTPConnectError,
    SMTPResponseException,
    SMTPNotSupportedError,  # 
    SMTPAuthenticationError # Error in auth
)

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from os import getenv as os_getenv
from dotenv import load_dotenv
from datetime import datetime

from typing import Literal


load_dotenv()

SMTPEMAIL_HOST          = os_getenv(key="SMTPEMAIL_HOST")
SMTPEMAIL_PORT          = os_getenv(key="SMTPEMAIL_PORT")
SMTPEMAIL_USER          = os_getenv(key="SMTPEMAIL_USER")
SMTPEMAIL_PASSWORD      = os_getenv(key="SMTPEMAIL_PASSWORD")
SMTPEMAIL_FROM          = os_getenv(key="SMTPEMAIL_FROM")
SMTPEMAIL_TO            = os_getenv(key="SMTPEMAIL_TO")

def send_email(data) -> Literal[False] | None:
    contato_nome        = data.get("nome",      "Teste")
    contato_from        = data.get("email",     "Teste")
    contato_telefone    = data.get("telefone",  "xxxxx-xxxx")
    contato_assunto     = data.get("assunto",   "Assunto X")
    MSG                 = data.get("descricao", "Mensagem de teste")    
    
    html_body = \
    """
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }

                .centered-info {
                    text-align: center;
                }

                .info-heading {
                    font-size: 18px;
                    color: #333;
                    margin-bottom: 10px;
                }

                .info-item {
                    font-size: 16px;
                    color: #555;
                    margin-bottom: 5px;
                }

                p {
                    font-size: 16px;
                    color: #333;
                    margin-top: 20px;
                }
            </style>
        </head>
    """
    
    html_body += \
    f"""
        <body>

            <div class="centered-info">
                <p class="info-heading">Informações do Remetente:</p>
                <p class="info-item"><strong>Nome: {contato_nome}</strong></p>
                <p class="info-item"><strong>Email: {contato_from}</strong></p>
                <p class="info-item"><strong>Telefone: {contato_telefone}</strong></p>
            </div>
            <p>{MSG}</p>
            <p><strong>{datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}<strong/></p>

        </body>
    </html>
    """

    # Construindo o objeto MIMEMultipart para representar a mensagem
    message = MIMEMultipart()
    message['From'] = SMTPEMAIL_FROM
    message['To'] = SMTPEMAIL_TO
    message['Subject'] = contato_assunto
    
    # Adicionando o corpo em formato HTML à mensagem
    message.attach(payload=MIMEText(_text=html_body, _subtype='html'))
    
    try:
        with smtplib.SMTP(host=SMTPEMAIL_HOST, port=int(SMTPEMAIL_PORT)) as smtp_connection: # type: ignore
            smtp_connection.starttls()
            smtp_connection.login(user=SMTPEMAIL_USER, password=SMTPEMAIL_PASSWORD) # type: ignore
            smtp_connection.send_message
            smtp_connection.sendmail(from_addr=SMTPEMAIL_FROM, to_addrs=SMTPEMAIL_TO, msg=message.as_string()) # type: ignore
            print(f"Mensagem de {contato_nome} enviada com sucesso!")
    except:
        print("Error")
        return False
    
if __name__ == "__main__":    
    send_email(data={})