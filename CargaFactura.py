from BaseOracle import *
from Factura import *


class CargaFactura(object):

    def __init__(self):
        pass

    def carga(self, factura):
        oracle = BaseOracle("localhost", "armando", "a")
        oracle.conectar()
        oracle.ejecutar("INSERT INTO ELE_DOCUMENTOS VALUES (s_ele_documentos.nextval,'"
        + factura.autorizacion + "','" + factura.documento + "','" + factura.razonSocial + "','"
        + factura.nombreComercial + "','" + factura.direccion + "','" + factura.establecimiento + "','"
        + factura.puntoEmision + "','" + factura.secuencial + "',TO_DATE('" + factura.fechaEmision
        + "', 'dd/mm/yyyy'),'" + factura.autorizacion + "','" + factura.tipo + "')")
        oracle.desconectar()