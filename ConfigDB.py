import configparser


class ConfigDB(object):
    maquina = None
    usuario = None
    clave = None
    puerto = None
    servicio = None
    ruta = None
    nombreDB = None

    def __init__(self, nombre):
        self.nombre = nombre
        self.maquina = ""
        self.usuario = ""
        self.clave = ""
        self.puerto = ""
        self.servicio = ""
        self.ruta = ""
        self.nombreDB = ""

    def setConfigOracle(self):
        config = configparser.ConfigParser()
        config["OracleDB"] = {"maquina": "localhost", "usuario": "armando"}
        param = config["OracleDB"]
        param["clave"] = "a"
        param["puerto"] = "1521"
        param["servicio"] = "XE"

        with open('base.ini', 'w') as configfile:
            config.write(configfile)

    def setConfigSqlite(self):
        config = configparser.ConfigParser()
        config["SqliteDB"] = {}
        param = config["SqliteDB"]
        param["ruta"] = "./ele.db3"

        with open('base.ini', 'w') as configfile:
            config.write(configfile)

    def getConfigOracle(self, config):
        self.maquina = config["OracleDB"]["maquina"]
        self.usuario = config["OracleDB"]["usuario"]
        self.clave = config["OracleDB"]["clave"]
        self.puerto = config["OracleDB"]["puerto"]
        self.servicio = config["OracleDB"]["servicio"]

    def getConfig(self):
        config = configparser.ConfigParser()
        config.read('base.ini')
        if self.nombre == "oracle":
            self.getConfigOracle(config)
