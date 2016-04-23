# -*- coding: utf-8 -*-
from BaseOracle import *
from Factura import *


class CargaFacturaOracle(object):

    def __init__(self):
        pass

    def carga(self, factura):
        oracle = BaseOracle("localhost", "armando", "a", "XE")
        oracle.conectar()

        oracle.ejecutar("delete ELE_DOCUMENTOS where CLAVE_ACCESO = '" + factura.claveAcceso + "'")

        oracle.ejecutar("INSERT INTO ELE_DOCUMENTOS VALUES ('"
        + factura.claveAcceso + "','" + factura.documento + "','" + factura.razonSocial + "','"
        + factura.nombreComercial + "','" + factura.direccion + "','" + factura.establecimiento + "','"
        + factura.puntoEmision + "','" + factura.secuencial + "',TO_DATE('" + factura.fechaEmision
        + "', 'dd/mm/yyyy'),'" + factura.autorizacion + "','" + factura.tipo + "')")

        i = 1
        for det in factura.detalle:
            oracle.ejecutar("INSERT INTO ELE_FACTURA_DETALLES"
            + "(CLAVE_ACCESO_ELE_DOCUMENTOS,NUMFILA,CODIGO_PRINCIPAL,DESCRIPCION,CANTIDAD,"
            + "PRECIO_UNITARIO,DESCUENTO,PRECIO_TOTAL_SIN_IMPUESTO)"
            + "VALUES ('" + factura.claveAcceso + "'," + str(i) + ",'" + det.codigoPrincipal + "','"
            + det.descripcion + "'," + str(det.cantidad) + "," + str(det.precioUnitario) + ","
            + str(det.descuento) + ","
            + str(det.total) + ")")
            i = i + 1
            for imp in factura.detalle.impuesto:
                pass

        oracle.desconectar()