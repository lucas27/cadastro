import os
import smtplib 
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from pathlib import Path

ROOT_FILE = Path(__file__).parent
FILE_TXT = ROOT_FILE / 'text.txt'

load_dotenv()

class SendEmail:
    def __init__(self, cadastre):
        self.smtp_server = os.getenv('EMAIL_SERVER', '')
        self.smtp_port = os.getenv('EMAIL_PORT', '')
        self.smtp_user = os.getenv('EMAIL_USER', '')
        self.smtp_password = os.getenv('EMAIL_PASSWORD', '')
        self.cadastre = cadastre

    def send_emails(self):
        list_data = self.cadastre.sendDict()

        with open(FILE_TXT, 'r', encoding='utf-8') as file:
            template_content = file.read()

        for data in list_data:
            # Substitui as variáveis do template com os dados do cadastro
            msg = Template(template_content).safe_substitute(data)
            mime_message = MIMEMultipart()
            mime_message['From'] = self.smtp_user
            mime_message['To'] = data['email']
            mime_message['Subject'] = 'Assunto do E-mail'

            # Adiciona o corpo do e-mail ao MIME multipart
            mime_message.attach(MIMEText(msg, 'plain'))

            # Envia o e-mail
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(mime_message)
                print(f'E-mail enviado para {data["email"]} com sucesso.')

if __name__ == '__main__':
    from main import Cadastre  # Importe a classe Cadastre do arquivo main.py (ou onde estiver definida)

    # Cria uma instância do Cadastre
    cadastre = Cadastre()

    # Cria uma instância de SendEmail passando o Cadastre
    sender = SendEmail(cadastre)

    # Chama o método para enviar os e-mails
    sender.send_emails()