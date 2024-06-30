import os
import pymysql
import pymysql.cursors
from dotenv import load_dotenv

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Register

load_dotenv()

TABLE_NAME = 'usuario'

class ButtonSave:
    def __init__(self, register: 'Register'):
        self._register = register
        
    def pushButtonClicked(self):
        self._register.button_save.clicked.connect(self.buttonSave)

    def buttonSave(self):
        self._register.checkSpaceIsCompleted()
        self.database()

    def database(self):
        connection = pymysql.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'],
            cursorclass=pymysql.cursors.DictCursor,
        ) 

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
                    'id INT NOT NULL AUTO_INCREMENT, '
                    'name VARCHAR(20) NOT NULL, '
                    'email VARCHAR(50) NOT NULL, '
                    'PRIMARY KEY (id)'
                    ')'
                )
                # cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
                connection.commit()

            with connection.cursor() as cursor:
                sql = (
                    f'INSERT INTO {TABLE_NAME} '
                    '(name, email) '
                    'VALUES '
                    '(%(name)s, %(email)s)'
                )
                print(self._register.CreateDict())
                for data in self._register.CreateDict(): 
                    result = cursor.execute(sql, data)
                    # print(result)
                    self._register.label_text.setText('Salvo na Base de dados.')
                    connection.commit()