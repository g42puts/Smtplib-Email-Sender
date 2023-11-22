import smtplib
from smtplib import (
    SMTPDataError,          # Error: Erro nas informações passada ao enviar email
    SMTPConnectError,       # Error: Erro ao tentar se conectar com o servidor
    SMTPResponseException,  # Error: Erro generalista
    SMTPNotSupportedError,  # Error: Comando não suportado
    SMTPAuthenticationError # Error: Erro de autenticação do usuário
)

from email.mime.multipart import MIMEMultipart  # Para criação de "multipart/mixed messages"
from email.mime.text import MIMEText            # Para envio de Msgs de Texto (email)
from email.mime.image import MIMEImage          # Para envio de Imagens

from os import getenv as os_getenv              # Para extração das variáveis de ambiente de arquivo .env
from dotenv import load_dotenv                  # Para carregar as variáveis de ambiente de arquivo  .env
from datetime import datetime                   # Para gerar data e hora atual


load_dotenv()                                   # Carrega as variáveis de ambiente de arquivo .env

# Aqui vão suas informações pessoais, da conta que você criou
# na plataforma escolhida.
SMTPEMAIL_HOST          = os_getenv(key="SMTPEMAIL_HOST")       # Endereço do servidor SMTP
SMTPEMAIL_PORT          = os_getenv(key="SMTPEMAIL_PORT")       # Porta do servidor SMTP
SMTPEMAIL_USER          = os_getenv(key="SMTPEMAIL_USER")       # O email da conta que vai enviar os emails
SMTPEMAIL_PASSWORD      = os_getenv(key="SMTPEMAIL_PASSWORD")   # A senha da conta que vai enviar os emails
SMTPEMAIL_FROM          = os_getenv(key="SMTPEMAIL_FROM")       # O email da conta que vai enviar os emails
SMTPEMAIL_TO            = os_getenv(key="SMTPEMAIL_TO")         # A sua conta, usada para receber os emails


def send_email(html_style:str="first", data:dict={}) -> str:
    html_style          = html_style
    contato_nome        = data.get("nome",      "Teste")
    contato_from        = data.get("email",     "Teste")
    contato_telefone    = data.get("telefone",  "xxxxx-xxxx")
    contato_assunto     = data.get("assunto",   "Assunto X")
    time                = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    MSG                 = f"<p>{data.get('descricao', 'Mensagem de teste')}</p>"

    match html_style:
        case "first":
            from html_body import return_html_head, return_html_body
            html_body = return_html_body(
                contato_nome=contato_nome,
                contato_from=contato_from,
                contato_telefone=contato_telefone,
                time=time,
                MSG=MSG
            )
            html_head = return_html_head()
            html = html_head + html_body

    
    # Construindo o objeto MIMEMultipart para representar a mensagem
    message = MIMEMultipart()
    message['From'] = SMTPEMAIL_FROM
    message['To'] = SMTPEMAIL_TO
    message['Subject'] = contato_assunto
    
    # Adicionando o corpo em formato HTML à mensagem
    message.attach(payload=MIMEText(_text=html, _subtype='html')) # type: ignore
    
    try:
        with smtplib.SMTP(host=SMTPEMAIL_HOST, port=int(SMTPEMAIL_PORT)) as smtp_connection: # type: ignore
            smtp_connection.starttls()
            smtp_connection.login(user=SMTPEMAIL_USER, password=SMTPEMAIL_PASSWORD) # type: ignore
            smtp_connection.send_message
            smtp_connection.sendmail(from_addr=SMTPEMAIL_FROM, to_addrs=SMTPEMAIL_TO, msg=message.as_string()) # type: ignore
            response = f"Mensagem de {contato_nome} enviada com sucesso!"
            return response

    # Erros handling
    except SMTPConnectError as e:
        return return_error_message(e=e, error_type='SMTPConnectError')
    except SMTPAuthenticationError as e:
        return return_error_message(e=e, error_type='SMTPAuthenticationError')
    except SMTPDataError as e:
        return return_error_message(e=e, error_type='SMTPDataError')
    except SMTPResponseException as e:
        return return_error_message(e=e, error_type='SMTPResponseException')
    except SMTPNotSupportedError as e:
        return return_error_message(e=e, error_type='SMTPNotSupportedError')
        

def return_error_message(e, error_type) -> str:
    error_code = e.smtp_code
    error_message = e.smtp_error

    match error_type:
        case 'SMTPConnectError':
            response = f"Erro na tentativa de conexção com o servidor SMTP. CODE: {error_code}\nMessage: {error_message}"
            return response
        case 'SMTPAuthenticationError':
            response = f"Erro de tentativa de autenticação do usuário. CODE: {error_code}\nMessage: {error_message}"
            return response
        case 'SMTPDataError':
            response = f"Erro de autenticação. CODE: {error_code}\nMessage: {error_message}"
            return response
        case 'SMTPResponseException':
            response = f"Erro ao enviar email. CODE: {error_code}\nMessage: {error_message}"
            return response
        case 'SMTPNotSupportedError':
            response = f"Comando não suportado. CODE: {error_code}\nMessage: {error_message}"
            return response
        case _:
            response = f"Falha ao enviar o email. CODE: {error_code}\nMessage: {error_message}"
            return response

    
if __name__ == "__main__":    
    print(send_email(data={}))