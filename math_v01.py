#MODULO DE MATEMATICAS
#division, area rectangulo, area circulo[]
#perimetro circulo[]
#area y perimetro de triangulo
#volumen de la esfera  
#TESTEAR EL RESTO DE FUNCIONES MATEMATICAS
import math

def division(a, b):
    if (b != 0):
        div = a / b
        return div
    return "No se puede dividir entre cero"


def area_rec(a, b):
    if (a >= 0 and b >= 0):
        area = a * b
        return area
    return "areas negativas no existen"

def area_circ(a):
    if(a>=0):
        PI=3.14
        area = PI*(pow(a, 2))
        return area
    return "areas negativas no existen"

def perime_circu(a):
    if(a>=0):
        PI=3.14
        perimetro=(2*PI*a)
        return perimetro
    return "el perimetro de un circulo no puede ser negativo"

def area_tria(a,b):
    if(a >= 0 and b >= 0):
        area=(a*b)/2
        return area
    return "base o altura no puede ser negativa"

def perime_tria(a,b,c):
    if(a >= 0 and b >=0 and c>=0):
        perimetro=a+b+c
        return perimetro
    return "La longitud del lado del triángulo debe ser un número positivo"

def vol_esfe(a):
    if(a>=0):
        PI=3.14
        volumen=(4*PI*(pow(a,3)))/3
        return volumen
    return "El radio de la esfera no puede ser negativo"