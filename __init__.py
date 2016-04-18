# -*- coding: utf-8 -*-
#import parseXMLeni as p
from parseXMLFactura import *


if __name__ == "__main__":

        #ce = ComprobanteElectronico('FACTURA')
        #p.extraerDatosFactura("0704201601109170775200120010030030019921234567817.xml", ce)
        #oracle = CargarBaseOracle("localhost", "armando", "a")
        #oracle.connect()
        ##oracle.execute("select sysdate from dual")

        #print((ce.autorizacion))
        #oracle.executetran("INSERT INTO ELE_DOCUMENTOS VALUES (s_ele_documentos.nextval,'"
        #+ ce.autorizacion + "','" + ce.documento + "','" + ce.razonSocial + "','"
        #+ ce.nombreComercial + "','" + ce.direccion + "','" + ce.establecimiento + "','"
        #+ ce.puntoEmision + "','" + ce.secuencial + "',TO_DATE('" + ce.fechaEmision
        #+ "', 'dd/mm/yyyy'),'" + ce.autorizacion + "','" + ce.tipo + "')")
        #oracle.execute("select * from ELE_DOCUMENTOS")
        #oracle.disconnect()
        parseFactura = parseXMLFactura()
        parseFactura.getFactura("0704201601109170775200120010030030019921234567817.xml")
        parseFactura.imprimir()
