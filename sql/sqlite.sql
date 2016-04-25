--
-- File generated with SQLiteStudio v3.0.7 on sáb abr 23 09:01:21 2016
--
-- Text encoding used: windows-1252
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: ele_factura_impuestos
DROP TABLE IF EXISTS ele_factura_impuestos;

CREATE TABLE ele_factura_impuestos (
    clave_acceso_ele_documentos   VARCHAR (100) NOT NULL,
    num_fila_ele_factura_detalles NUMBER        NOT NULL,
    num_fila                      NUMBER        NOT NULL,
    codigo                        VARCHAR (10),
    codigo_porcentaje             VARCHAR (10),
    tarifa                        NUMBER,
    base_imponible                NUMBER,
    valor                         NUMBER,
    PRIMARY KEY (
        clave_acceso_ele_documentos,
        num_fila_ele_factura_detalles,
        num_fila ASC
    ),
    FOREIGN KEY (
        clave_acceso_ele_documentos,
        num_fila_ele_factura_detalles
    )
    REFERENCES ele_factura_detalles (clave_acceso_ele_documentos,
    numfila) ON DELETE CASCADE
);


-- Table: ele_factura_detalles
DROP TABLE IF EXISTS ele_factura_detalles;

CREATE TABLE ele_factura_detalles (
    clave_acceso_ele_documentos VARCHAR (100) NOT NULL
                                              REFERENCES ele_documentos (clave_acceso) ON DELETE CASCADE,
    numfila                     NUMBER        NOT NULL,
    codigo_principal            VARCHAR (50),
    descripcion                 VARCHAR (200),
    cantidad                    NUMBER,
    precio_unitario             NUMBER,
    descuento                   NUMBER,
    precio_total_sin_impuesto   NUMBER,
    codigo_articulo             VARCHAR (10),
    unidad_medida               VARCHAR (10),
    estado                      VARCHAR (10),
    PRIMARY KEY (
        clave_acceso_ele_documentos,
        numfila ASC
    )
);


-- Table: ele_documentos
DROP TABLE IF EXISTS ele_documentos;

CREATE TABLE ele_documentos (
    clave_acceso     VARCHAR (100) NOT NULL
                                   PRIMARY KEY,
    documento        VARCHAR (50),
    razon_social     VARCHAR (200),
    nombre_comercial VARCHAR (200),
    direccion        VARCHAR (200),
    establecimiento  VARCHAR (10),
    punto_emision    VARCHAR (10),
    secuencial       VARCHAR (10),
    fecha_emision    DATE,
    autorizacion     VARCHAR (100),
    tipo             VARCHAR (10) 
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
