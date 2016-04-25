# -*- coding: utf-8 -*-

import sqlite3

class BaseSqlite(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def conectar(self):
        pass

    def ejecutar(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur

    def desconectar(self):
        self.conn.close()


def main():	
    dbmgr = BaseSqlite("testdb.db")
    for row in dbmgr.ejecutar("select * from users")
        print row

if __name__ == "__main__":
	main()