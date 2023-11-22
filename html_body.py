
def return_html_head() -> str:
    html_head = \
    """
    <!DOCTYPE html>
    <html lang="pt-br">
        <meta charset="UTF-8" />
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
    return html_head

def return_html_body(contato_nome:str, contato_from:str,
    contato_telefone:str,time:str, MSG:str) -> str:
    
    html_body = \
    f"""
        <body>
            <div class="centered-info">
                <p class="info-heading">Informações do Remetente:</p>
                <p class="info-item"><strong>Nome: {contato_nome}</strong></p>
                <p class="info-item"><strong>Email: {contato_from}</strong></p>
                <p class="info-item"><strong>Telefone: {contato_telefone}</strong></p>
            </div>
            {MSG}
            <p><strong>{time}<strong/></p>

        </body>
    </html>
    """
    return html_body