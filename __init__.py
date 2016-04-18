# -*- coding: utf-8 -*-
from ParseXMLFactura import *
from CargaFactura import *

if __name__ == "__main__":
        parseFactura = ParseXMLFactura()
        factura = parseFactura.getFactura("0704201601109170775200120010030030019921234567817.xml")
        #Imprime objeto Factura
        parseFactura.imprimir()
        carga = CargaFactura()
        carga.carga(factura)
