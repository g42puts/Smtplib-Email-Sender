# Smtplib-Email-Sender

Script para envio de emails utilizando a Lib Smtplib, do Python e templates HTML personalizados.

É possível você mesmo criar um template do HTML, passando o Head com o Style, e o Body. Para assim enviar um email com uma aparencia mais agradavel.

## Prints dos Emails na caixa de mensagem e aberto.

<img width="400" src="/images/email-print1.png">
<img width="600" src="/images/email-print-2.png">

## Descrição do projeto

O principal objetivo deste projeto, foi trazer de uma forma simples, o envio de Emails, no intuito de informar, porém dependendo da sua necessidade, a sua utilidade pode ser facilmente flexibilizada e adaptada conforme sua necessidade.

A minha ideia veio através da necessidade de integrar uma página de contato em um site, a um meio prático de trazer essa informação para mim, o meio final que usei foi este.

Após o usuário preencher as suas informações na parte de **Contato** em um site, essa informação do formúlario ser passada via API, e a API irá se encarregar de chamar a função que fará o envio do Email para o email destinatario (o meu, nesse caso), com as informações passadas no formúlario, desta forma eu tenho um notify system prático e simples que pode inclusive ser estilizado facilmente.

Use com responsabilidade, pois ao mesmo tempo que é uma ferramenta muito útil, também é uma ferramenta bastante poderosa, levando em consideração que pode ser enviado até 10 mil emails por dia através dela.


## Requisitos

| Linguagem / Libs | Descrição |
| -----------------|-----------|
| **[Python](https://www.python.org/)** | **3.11.5** |
| *[Smtlib](https://docs.python.org/3/library/smtplib.html)* | **builtin** |
| *[Email](https://docs.python.org/3/library/email.html)* | **bultin** |
| *[Python-Dotenv](https://pypi.org/project/python-dotenv/)* * | _Instação necessária_



## Uso

Para darmos inicio ao uso, vamos primeiro fazer o clone ou download do repositório.

Após este processo, vamos fazer a instalação do package *Python-dotenv*.


### Instação do package *Python-dotenv*
Optei por guardar os dados no ambiente de arquivo **.env**, assim dá mais segurança ao código, já que guardar informações de autenticação e pessoal, que é o caso do email e a senha do App.

```bash
pip install python-dotenv
```

É atraves deste pacote que conseguiremos extrair dados do arquivo **.env**.


## Criação de conta Google para envio de emails

#### Ativando o *IMAP*
<Foto dos tutoriais>


1. Já na sua conta Google, clique no menu em formato cúbico na parte superior direita, em seguida vá em *"See all settings"*.
2. Clique na aba *"Forwarding and POP/IMAP"*, em seguida ativa a configuração IMAP, clicando no selectbox *"Enable IMAP"*.
3. Após ativar o *IMAP*, vá ao final da página onde haverá um botão para salvar as mudanças.

---
#### Ativando verificação em duas etapas e criando senha para o app (para fazer o login no servidor SMTP), para esse passo será necessário um celular para fazer a verificação.

4. Vá novamente no menu na parte superior direita da página, em seguida clique no ícone **"Account"**, isso o levará para as configurações da conta **Google**.
5. Vá para o menu lateral na parte esquerda da página, clique em *"Segurança"*, em seguida procure por **"Verificação em duas etapas"**, faço o processo de verificação, para esse passo será necessário um celular.
6. Após ativado a verificação em duas etapas, no menu de busca na parte superior, procure por **"App"**, irá aparecer algumas opções, selecione **"Senhas de app"**.
7. Na página de **App**, dê um nome ao App que você irá criar (isso é apenas para fins informativos), clique no botão **"Criar"**.
8. Neste momento uma aba se abrirá, com a senha do App gerada, copie essa senha e salve, será necessária para a variavel *.env*.


## Considerações finais

- Pensando na ideia de que não é uma boa prática deixarmos os usuário esperando por uma confirmação de que o email foi enviado ou não, pretendo trazer em breve algo que faz a validação dos dados ainda na API, e então de forma assincrona faz a execução desse script, e ao mesmo tempo retorna para o usuário a confirmação de que o email foi enviado, assim damos ao usuário uma experiência melhor, por não ter que esperar que o email seja enviado para só então a API retornar a resposta de confirmação de envio.

