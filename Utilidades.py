# -*- coding: utf-8 -*-
import ntpath
import tempfile
import os

class Utilidades(object):

    def __init__(self):
        pass

    #Quita los espacios en blanco del contenido del archivo XML
    @staticmethod
    def borrarBlancosArchivo(archivo):
        clean_lines = []
        with open(archivo, "r", encoding="utf8") as f:
            lines = f.readlines()
            clean_lines = [l.strip() for l in lines if l.strip()]
        with open(archivo, "w", encoding="utf8") as f:
            f.writelines("\n".join(clean_lines))
        f.close

    #Extrae el nombre del archivo, eliminando la ruta
    @staticmethod
    def extraerNombre(rutaArchivo):
        head, tail = ntpath.split(rutaArchivo)
        return tail or ntpath.basename(head)

    #Crea un archivo temporal con la clave de acceso
    @staticmethod
    def mensajero(clave):
        with open(tempfile.gettempdir() + os.sep + "clave.ca", "w", encoding="utf8") as f:
            f.writelines(clave)
        f.close
