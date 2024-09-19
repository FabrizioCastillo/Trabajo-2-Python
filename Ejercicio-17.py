# Cree una clase FuncionesPrograma y codifique una función estática getFechaString
# que reciba como parámetro una fecha y retorne la fecha como una cadena literal.
# Ejemplo recibo 15/10/1900, la salida debe ser
# Quince de Octubre de mil novecientos.
from num2words import num2words

meses = {
            "01": "Enero",
            "02": "Febrero",
            "03": "Marzo",
            "04": "Abril",
            "05": "Mayo",
            "06": "Junio",
            "07": "Julio",
            "08": "Agosto",
            "09": "Setiembre",
            "10": "Octubre",
            "11": "Noviemre",
            "12": "Diciembre",
        }
def diaExisteEnMes(d, m, a):
    d = int(d)
    m = int(m)
    a = int(a)
    match m:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            dias = 31
        case 4 | 6 | 9 | 11:
            dias = 30
        case 2:
            if (a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)):
                dias = 29
            else:
                dias = 28
        case _:
            dias = 2
    return 1 <= d <= dias
    
class FuncionesPrograma:

    @staticmethod
    def getFechaString(f) -> str:
        
        if f[2] == '/' and f[5] == '/' and len(f) == 10:
            dd: str = f[0:2]
            mm: str = f[3:5]
            aaaa: str = f[6:10]
            
            if 1 <= int(mm) <= 12:
                m = meses[mm]
            else:
                return f"{mm} no es un mes."
            
            if diaExisteEnMes(dd, mm, aaaa):
                d = num2words(dd, lang='es')
            else:
                return f"No existe el día {dd} en {m}"
            d = d.capitalize()
            
            m = m.capitalize()
            
            a = num2words(aaaa, lang='es')

            return f"{d} de {m} de {a}."
        else:
            return f"{f} no está en formato DD/MM/AAAA."
        
funciones = FuncionesPrograma()

fecha = str(input("Ingrese una fecha en formato DD/MM/AAAA: "))
fechaStr = funciones.getFechaString(fecha)

print(fechaStr)
