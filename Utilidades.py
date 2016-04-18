class Utilidades(object):

    def __init__(self):
        pass

    @staticmethod
    def borrarBlancosArchivo(archivo):
        clean_lines = []
        with open(archivo, 'r') as f:
            lines = f.readlines()
            clean_lines = [l.strip() for l in lines if l.strip()]
        with open(archivo, 'w') as f:
            f.writelines('\n'.join(clean_lines))
        f.close