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
<<<<<<< HEAD

=======
>>>>>>> e852283d06ed8940b18440e05b236ddb69e92144

