# -*- coding: utf-8 -*-
from ParseXMLFactura import *
from CargaFacturaOracle import *
import sys

if __name__ == "__main__":

    if len(sys.argv) == 2:
        if " " in sys.argv[1]:
            print("El archivo y la ruta del archivo no deben contener espacios")
        else:
            print("Documento electrónico", sys.argv[1])
            parseFactura = ParseXMLFactura()
            factura = parseFactura.getFactura(sys.argv[1])
            Utilidades.mensajero(factura.claveAcceso)
            parseFactura.imprimir()
            carga = CargaFacturaOracle()
            carga.carga(factura)
    else:
        print("Por favor añadir la ruta de archivo")

