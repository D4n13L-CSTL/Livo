from datetime import date

# Definición de categorías por deporte y rangos de edad
CATEGORIAS_POR_DEPORTE = {
    'VOLLEYBALL': [
        ('Juvenil', 2007, 2010),  # nacidos entre 2007 y 2010
        ('Adulto', 1990, 2006),
        ('Senior', 1900, 1989),
    ],
    'FUTBOLL': [
        ('Infantil', 2012, 2015),
        ('Juvenil', 2005, 2011),
        ('Adulto', 1985, 2004),
    ],
    'BASQUE': [
        ('Sub-18', 2006, 2007),
        ('Sub-23', 2001, 2005),
        ('Libre', 1900, 2000),
    ],
    'BASEBALL': [
        ('Pequeños', 2013, 2016),
        ('Medianos', 2008, 2012),
        ('Grandes', 1900, 2007),
    ],
}




def determinar_categoria(deporte_nombre: str, fecha_nacimiento: date) -> str:
    año_nacimiento = fecha_nacimiento.year
    deporte = deporte_nombre.upper()

    if deporte not in CATEGORIAS_POR_DEPORTE:
        return 'Desconocida'

    for categoria, inicio, fin in CATEGORIAS_POR_DEPORTE[deporte]:
        if inicio <= año_nacimiento <= fin:
            return categoria

    return 'Desconocida'


