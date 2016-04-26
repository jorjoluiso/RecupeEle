import configparser


class ConfigDB(object):
    maquina = None
    usuario = None
    clave = None
    servicio = None

    def __init__(self):
        pass

    def setConfigOracle(self):
        config = configparser.ConfigParser()
        config["OracleDB"] = {"maquina": "localhost", "usuario": "armando"}
        param = config["OracleDB"]
        param["clave"] = "a"
        param["puerto"] = "1521"
        param["servicio"] = "XE"

        with open('oracle.ini', 'w') as configfile:
            config.write(configfile)
