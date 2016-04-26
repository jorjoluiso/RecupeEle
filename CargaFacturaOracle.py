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
        j = 1
        for det in factura.detalle:
            oracle.ejecutar("INSERT INTO ELE_FACTURA_DETALLES"
            + "(CLAVE_ACCESO_ELE_DOCUMENTOS,NUMFILA,CODIGO_PRINCIPAL,DESCRIPCION,CANTIDAD,"
            + "PRECIO_UNITARIO,DESCUENTO,PRECIO_TOTAL_SIN_IMPUESTO)"
            + "VALUES ('" + factura.claveAcceso + "'," + str(i) + ",'" + det.codigoPrincipal + "','"
            + det.descripcion + "'," + str(det.cantidad) + "," + str(det.precioUnitario) + ","
            + str(det.descuento) + ","
            + str(det.total) + ")")

            for imp in det.impuesto:
                oracle.ejecutar("INSERT INTO ELE_FACTURA_IMPUESTOS(CLAVE_ACCESO_ELE_DOCUMENTOS,"
                + "NUM_FILA_ELE_FACTURA_DETALLES,NUM_FILA,CODIGO,CODIGO_PORCENTAJE,TARIFA,"
                + "BASE_IMPONIBLE,VALOR) VALUES ('" + factura.claveAcceso + "'," + str(i) + ","
                + str(j) + ",'" + imp.codigo + "','" + imp.codigoPorcentaje + "',"
                + imp.tarifa + "," + imp.baseImponible + "," + imp.valor + ")")
                j = j + 1
            i = i + 1

        oracle.desconectar()