class FacturaDetalle(object):
    codigoPrincipal = None
    descripcion = None
    cantidad = None
    precioUnitario = None
    descuento = None
    total = None

    def __init__(self, codigoPrincipal="", descripcion="", cantidad=0, precioUnitario=0,
                descuento=0, total=0):
        self.codigoPrincipal = codigoPrincipal
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario
        self.descuento = descuento
        self.total = total