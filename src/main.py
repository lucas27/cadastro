import os
import sys
import smtplib 
from PySide6.QtWidgets import QApplication, QMainWindow
from UI_register import Ui_MainWindow
from send_email import SendEmail
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ROOT_FILE = Path(__file__).parent
FILE_TXT = ROOT_FILE / 'text.txt'

class Cadastre(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.list_name = []
        self.list_email = []
        self.clearLine()

        self.pushButton.setText('salvar')

        self.button_send.clicked.connect(self.buttonSend)
        self.pushButton.clicked.connect(lambda: print('salvo'))

    def clearLine(self):
        self.line_name.clear()
        self.line_email.clear()

    def buttonSend(self):
        self.checkSpaceIsCompleted()
        self.sendDict()
        self.send_emails()
        
    def checkSpaceIsCompleted(self):
        text_name = self.line_name.text()
        text_email = self.line_email.text()

        self.checkIfLine(text_name, text_email)
        
        self.clearLine()

    def checkIfLine(self, name, email):
        if not name:
            self.label_text.setText('Espaço do Nome está vazio')

        elif name.isdigit(): 
            self.label_text.setText('Escreva apenas o seu nome')

        elif not email:
            self.label_text.setText('Espaço do E-mail está vazio')
        
        else:
            # armazenar o nome e email
            self.list_name.append(name)
            self.list_email.append(email)

    # concatena a lista
    def sendDict(self):
        name = self.list_name
        email = self.list_email
        concatenated = [{"name": nome, "email": email} for nome, email in zip(name, email)]
        # print(concatenated)
        self.concatenated = concatenated

    # envia o email
    def send_emails(self):
        self.smtp_server = os.getenv('EMAIL_SERVER', '')
        self.smtp_port = os.getenv('EMAIL_PORT', '')
        self.smtp_user = os.getenv('EMAIL_USER', '')
        self.smtp_password = os.getenv('EMAIL_PASSWORD', '')

        list_data = self.concatenated

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
                self.label_text.setText(f'E-mail enviado com sucesso.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cadastre = Cadastre()
    cadastre.show()
    app.exec()
