import os
import smtplib 
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from pathlib import Path
from UI_register import Ui_MainWindow
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Register
    from checker import Checker

ROOT_FILE = Path(__file__).parent
FILE_TXT = ROOT_FILE / 'text.txt'

load_dotenv()

class ButtonOperation:
    def __init__(self, register: 'Register'):
        self._register = register
        # self.list_name = []
        # self.list_email = []

    def pushButtonClicked(self):
        self._register.button_send.clicked.connect(self.buttonSend)

    # faz a interassão do botão enviar 
    def buttonSend(self):
        self._register.checkSpaceIsCompleted()
        self.sendEmails()       

    def sendEmails(self):
        self.smtp_server = os.getenv('EMAIL_SERVER', '')
        self.smtp_port = os.getenv('EMAIL_PORT', '')
        self.smtp_user = os.getenv('EMAIL_USER', '')
        self.smtp_password = os.getenv('EMAIL_PASSWORD', '')

        list_data = self._register.sendDict()
       
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
                # print(f'E-mail enviado para {data["email"]} com sucesso.')
                self._register.label_text.setText('E-mail enviado com sucesso.')
                