import smtplib
from email.message import EmailMessage
from pathlib import Path

# Dados de envio de email
email_remetente = 'qualquercoisa@email.com'
senha_app = 'sua_senha_app_aqui'
email_destinatario = 'outracoisa@gmail.com'

# Criação da mensagem de email
msg = EmailMessage()
msg['Subject'] = 'Teste de Envio de Email'
msg['From'] = email_remetente
msg['To'] = email_destinatario
msg.set_content('Este é um teste de envio de email usando Python.')

# Anexando um arquivo, se necessário
caminho_archive = 'documento.pdf'
archive = Path(caminho_archive).read_bytes()
msg.add_attachment(archive, maintype='application', subtype='pdf', filename=Path(caminho_archive).name)

# Envio do email usando SMTP com SSL
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_remetente, senha_app)
    smtp.send_message(msg)

print("Email enviado com sucesso!")