# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_register.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.layout_text = QHBoxLayout()
        self.layout_text.setObjectName(u"layout_text")
        self.label_text = QLabel(self.centralwidget)
        self.label_text.setObjectName(u"label_text")
        font = QFont()
        font.setPointSize(30)
        self.label_text.setFont(font)
        self.label_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_text.addWidget(self.label_text)


        self.gridLayout.addLayout(self.layout_text, 0, 0, 1, 1)

        self.layout_name = QHBoxLayout()
        self.layout_name.setObjectName(u"layout_name")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_name.setFont(font1)

        self.layout_name.addWidget(self.label_name)

        self.line_name = QLineEdit(self.centralwidget)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setFont(font1)

        self.layout_name.addWidget(self.line_name)


        self.gridLayout.addLayout(self.layout_name, 1, 0, 1, 1)

        self.layout_email = QHBoxLayout()
        self.layout_email.setObjectName(u"layout_email")
        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setFont(font1)

        self.layout_email.addWidget(self.label_email)

        self.line_email = QLineEdit(self.centralwidget)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setFont(font1)
        self.line_email.setDragEnabled(False)

        self.layout_email.addWidget(self.line_email)


        self.gridLayout.addLayout(self.layout_email, 2, 0, 1, 1)

        self.layout_button = QHBoxLayout()
        self.layout_button.setObjectName(u"layout_button")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.layout_button.addWidget(self.pushButton)

        self.button_send = QPushButton(self.centralwidget)
        self.button_send.setObjectName(u"button_send")
        self.button_send.setFont(font1)

        self.layout_button.addWidget(self.button_send)


        self.gridLayout.addLayout(self.layout_button, 3, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_text.setText(QCoreApplication.translate("MainWindow", u"Texto", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.line_name.setText(QCoreApplication.translate("MainWindow", u"Escreva seu nome", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.line_email.setInputMask("")
        self.line_email.setText(QCoreApplication.translate("MainWindow", u"Escreva seu E-mail", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.button_send.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
    # retranslateUi

