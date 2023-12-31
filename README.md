# Smtplib-Email-Sender

Script para envio de emails utilizando a Lib Smtplib, do Python e templates HTML personalizados.

É possível você mesmo criar um template do HTML, passando o Head com o Style, e o Body. Para assim enviar um email com uma aparência mais agradável.

## Prints dos Emails na caixa de mensagem e aberto.
<div style="display:flex; flex-direction: column">
<p>Print da caixa de mensagens:</p>
<img width="400" src="/images/email-print1.png" alt="Print da caixa de mensagens">
</div>

----- 

<div style="display:flex; flex-direction: column">
<p>Print do email:</p>
<img width="600" src="/images/email-print-2.png" alt="Print do email">
</div>

## Descrição do projeto

Eu tinha um problema, que era enviar para mim mesmo as informações que o usuário iria preencher no site, e assim, surgiu essa ideia.

O principal objetivo deste projeto, foi fazer de uma forma simples, o envio de Emails, no intuito de informar através de um email, porém dependendo da sua necessidade, a sua utilidade pode ser facilmente flexibilizado e adaptado conforme sua necessidade.

Após o usuário preencher as suas informações na parte de **Contato** em um site, essa informação do formulário será passada via API, e a API irá se encarregar de chamar a função que fará o envio do Email para o email destinatário (o meu, nesse caso), com as informações passadas no formulário, desta forma eu tenho um **notify system** prático e simples que pode inclusive ser estilizado facilmente.

## Requisitos

| Linguagem / Libs | Descrição |
| --------------------------------------|------------|
| **[Python](https://www.python.org/)** | **3.11.5** |
| *[Smtlib](https://docs.python.org/3/library/smtplib.html)* | **builtin** |
| *[Email](https://docs.python.org/3/library/email.html)* | **bultin** |
| *[Python-Dotenv](https://pypi.org/project/python-dotenv/)* * | _Instalação necessária_ |



## Uso

Para darmos inicio ao uso, vamos primeiro fazer o clone ou download do repositório.

```
git clone https://github.com/g42puts/Smtplib-Email-Sender.git
```

Após este processo, vamos fazer a instalação do package *Python-dotenv*, passo a passo abaixo.


### Instalação do package *Python-dotenv*
Optei por guardar os dados no ambiente de arquivo **.env**, assim dá mais segurança ao código, já que guardar informações de autenticação e pessoal, que é o caso do email e a senha do App.

```bash
pip install python-dotenv
```

É através deste pacote que conseguiremos extrair dados do arquivo **.env**.

--- 

## Criação de conta Google para envio de emails

#### Ativando o *IMAP*
<div style="display:flex; flex-direction: column">
<p>Print do email:</p>
<img width="600" src="/images/passo 1-4.png" alt="Print passo a passo 1 até 4">
</div>


1. Já na sua conta Google, clique no menu em formato cúbico na parte superior direita, em seguida vá em **"See all settings"**.
2. Clique na aba **"Forwarding and POP/IMAP"**, em seguida ativa a configuração IMAP, clicando no selectbox **"Enable IMAP"**.
3. Após ativar o **IMAP**, vá ao final da página onde haverá um botão para salvar as mudanças.

---

#### Ativando verificação em duas etapas e criando senha para o app (para fazer o login no servidor SMTP), para esse passo será necessário um celular para fazer a verificação.

<div style="display:flex; flex-direction: column">
<p>Print do email:</p>
<img width="600" src="/images/passo 5-8.png" alt="Print passo a passo 5 até 8">
</div>

4. Vá novamente no menu na parte superior direita da página, em seguida clique no ícone **"Account"**, isso o levará para as configurações da conta **Google**.
5. Vá para o menu lateral na parte esquerda da página, clique em *"Segurança"*, em seguida procure por **"Verificação em duas etapas"**, faço o processo de verificação, para esse passo será necessário um celular.
6. Após ativado a verificação em duas etapas, no menu de busca na parte superior, procure por **"App"**, irá aparecer algumas opções, selecione **"Senhas de app"**.
7. Na página de **App**, dê um nome ao App que você irá criar (isso é apenas para fins informativos), clique no botão **"Criar"**.
8. Neste momento uma aba se abrirá, com a senha do App gerada, copie essa senha e salve, será necessária para a variável **.env**, porém sem o espaçamento entre elas.


#### Agora basta criar o arquivo **.env** e preencher os dados.

```
SMTPEMAIL_HOST      = smtp.gmail.com                < Servidor de emails do Google >
SMTPEMAIL_PORT      = 587                           < Porta do servidor >
SMTPEMAIL_USER      = seuemailaqui@gmail.com        < Email da conta que será usada >
SMTPEMAIL_PASSWORD  = senhadoappaqui                < A senha obtida na página de criação do App >
SMTPEMAIL_FROM      = seuemailaqui@gmail.com        < Email da conta que será usada >
SMTPEMAIL_TO        = emaildestinatario@gmail.com   < O Email para quem você enviará o Email>
```

## Considerações finais

- Pensando na ideia de que não é uma boa prática deixarmos os usuário esperando por uma confirmação de que o email foi enviado ou não, pretendo trazer em breve algo que faz a validação dos dados ainda na API, e então de forma assíncrona faz a execução desse script, e ao mesmo tempo retorna para o usuário a confirmação de que o email foi enviado, assim damos ao usuário uma experiência melhor, por não ter que esperar que o email seja enviado para só então a API retornar a resposta de confirmação de envio.

- Use com responsabilidade, pois ao mesmo tempo que é uma ferramenta muito útil, também é uma ferramenta bastante poderosa, levando em consideração que pode ser enviado até 10 mil emails por dia através dela.
