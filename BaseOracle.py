# -*- coding: utf-8 -*-
import cx_Oracle


class BaseOracle(object):

    def __init__(self, host="localhost", user="", password="", sid=""):
        self.host = host
        self.user = user
        self.password = password
        self.sid = sid
        self.cursor = None

    def conectar(self):
        try:
            #con = cx_Oracle.connect('jorge/j@127.0.0.1/xe')
            self.db = cx_Oracle.connect(self.user + "/" + self.password + "@" + self.host + "/" + self.sid)
            print(("Conectado a la base Oracle " + (self.db.version)))
            self.cursor = self.db.cursor()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                print("Please check your credentials.")
            else:
                print(("Database connection error: %s".format(e)))
            # Very important part!
            raise

    def desconectar(self):
        try:
            self.cursor.close()
            self.db.close()
            print("Desconectado de la base Oracle")
        except cx_Oracle.DatabaseError:
            pass

    #Ejecuta sentencias de actualizaciones en la base de datos
    def ejecutar(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return self.cursor
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 955:
                print("Table already exists")
            elif error.code == 1031:
                print("Insufficient privileges")
            print((error.code))
            print((error.message))
            print((error.context))

            # Raise the exception.
            raise