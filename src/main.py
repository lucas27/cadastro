import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from UI_register import Ui_MainWindow


from buttonSend import ButtonOperation
from buttonSave import ButtonSave
from checker import Checker
# from buttonSave import ButtonSave

class Register(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.list_name = []
        self.list_email = []

        self.operation()
        self.save_()

    def operation(self):
        self.send = ButtonOperation(self)
        self.send.pushButtonClicked()

    def save_(self):
        self.save = ButtonSave(self)
        self.save.pushButtonClicked()

    # limpa as linhas
    def clearLine(self):
        self.line_name.clear()
        self.line_email.clear()

    # verifica se o espaço está completo    
    def checkSpaceIsCompleted(self):
        text_name = self.line_name.text()
        text_email = self.line_email.text()

        self.checkIfLine(text_name, text_email)
        
        self.clearLine()

    # verifica se as linhas estão vazias. No final adiciona na lista o texto
    def checkIfLine(self, name, email):
        # se o nome não está vazio
        if not name:
            self.label_text.setText('Espaço do Nome está vazio')

        # se o nome não é números
        elif name.isdigit(): 
            self.label_text.setText('Escreva apenas o seu nome')

        # se o email não está vazio
        elif not email:
            self.label_text.setText('Espaço do E-mail está vazio')
        
        else:
            # armazenar o nome e email
            self.list_name.append(name)
            self.list_email.append(email)
            # self.label_text.setText('Completo')
            

    # cria um dict
    def CreateDict(self):
        name = self.list_name
        email = self.list_email

        concatenated = [{"name": nome, "email": email} for nome, email in zip(name, email)]
        return concatenated

if __name__ == '__main__':
    app = QApplication(sys.argv)
    register = Register()
    register.show()
    app.exec()
