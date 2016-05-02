# -*- coding: utf-8 -*-
from ParseXMLFactura import *
from CargaFacturaOracle import *
import sys

if __name__ == "__main__":

    if len(sys.argv) == 2:
        print("Documento electrónico", sys.argv[1])
        parseFactura = ParseXMLFactura()
        factura = parseFactura.getFactura(sys.argv[1])
        parseFactura.imprimir()
        carga = CargaFacturaOracle()
        carga.carga(factura)
    else:
        print("Por favor añadir la ruta de archivo")
        #configOra = ConfigDB("oracle")
        #configOra.getConfig()
        #configOra.imprimir()


        #parseFactura = ParseXMLFactura()
        ##factura = parseFactura.getFactura("/home/jorjoluiso/python/RecupeEle/"
        ##+ "0704201601109170775200120010030030019921234567817.xml")
        #factura = parseFactura.getFactura("0704201601109170775200120010030030019921234567817.xml")
        ##Imprime objeto Factura
        #parseFactura.imprimir()
        #carga = CargaFacturaOracle()
        #carga.carga(factura)


