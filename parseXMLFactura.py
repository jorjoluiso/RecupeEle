from Factura import *
from Utilidades import *
import xml.etree.ElementTree as parsexml
import ntpath


class parseXMLFactura(object):
    factura = None

    def __init__(self):
        self.factura = Factura()

    def getFactura(self, archivo):
        Utilidades.borrarBlancosArchivo(archivo)

        tree = parsexml.parse(archivo)
        root = tree.getroot()

        for i in root.iter("numeroAutorizacion"):
            self.factura.autorizacion = i.text
            print((self.factura.autorizacion))

        self.getFacturaFirmada(archivo)
        self.getFacturaCabeza("firmado" + archivo)
        self.getFacturaDetalle("firmado" + archivo)

    def getFacturaFirmada(self, archivo):
        #Recupero el comprobante electrónico firmado
        tree = parsexml.parse(archivo)
        root = tree.getroot()

        print(("Path: ", (ntpath.basename(archivo))))

        for i in root.iter("comprobante"):
            print((i.text))
            with open("firmado" + ntpath.basename(archivo), "w") as f:
                f.writelines(i.text)
            f.close

    def getFacturaCabeza(self, archivo):
        tree = parsexml.parse(archivo)
        root = tree.getroot()

        for datosFactura in root.iter("ruc"):
            self.factura.documento = datosFactura.text

        for datosFactura in root.iter("razonSocial"):
            self.factura.razonSocial = datosFactura.text

        for datosFactura in root.iter("nombreComercial"):
            self.factura.nombreComercial = datosFactura.text

        for datosFactura in root.iter("dirMatriz"):
            self.factura.direccion = datosFactura.text

        for datosFactura in root.iter("estab"):
            self.factura.establecimiento = datosFactura.text

        for datosFactura in root.iter("ptoEmi"):
            self.factura.puntoEmision = datosFactura.text

        for datosFactura in root.iter("secuencial"):
            self.factura.secuencial = datosFactura.text

        for datosFactura in root.iter("fechaEmision"):
            self.factura.fechaEmision = datosFactura.text

        for datosFactura in root.iter("claveAcceso"):
            self.factura.claveAcceso = datosFactura.text

    def getFacturaDetalle(self, archivo):
        pass

    def imprimir(self):
        print("\n")
        print("Datos Factura")
        print(("Clave de Acceso:", self.factura.claveAcceso))
        print(("Docuemto:", self.factura.documento))
        print(("Nombre Comercial:", self.factura.nombreComercial))
        print(("Dirección:", self.factura.direccion))
        print(("Establecimiento:", self.factura.establecimiento))
        print(("Punto Emisión:", self.factura.puntoEmision))
        print(("Secuencial:", self.factura.secuencial))
        print(("Fecha Emisión:", self.factura.fechaEmision))
        print(("Autorización:", self.factura.autorizacion))
        print(("Tipo:", self.factura.tipo))
