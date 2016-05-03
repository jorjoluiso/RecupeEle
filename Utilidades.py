# -*- coding: utf-8 -*-
import ntpath


class Utilidades(object):

    def __init__(self):
        pass

    #Quita los espacios en blanco del archivo XML
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