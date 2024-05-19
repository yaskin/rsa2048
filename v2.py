#pip install ecpy
from ecpy.curves import Curve, Point
from ecpy.fields import FiniteField
from ecpy.keys import ECPublicKey, ECPrivateKey

def egcd(a, b):
    if a == 0:
        return b
    else:
        return egcd(b % a, a)

def elliptic_curve_gcd(a, b):
    # Определяем кривую и поля для эллиптических кривых
    F = FiniteField(p=a+b+1)  # Поле для эллиптической кривой
    curve = Curve(a=F(0), b=F(7), field=F)  # Эллиптическая кривая y^2 = x^3 + 7

    # Конечные точки A и B
    A = Point(curve, F(a), F(1))
    B = Point(curve, F(b), F(1))

    # Находим точку пересечения кривой с отрезком A,B
    gcd_point = curve.mul(A + B, abs(egcd(a, b)))  # abs(egcd(a, b)) используется для нахождения общего делителя

    return gcd_point.x, gcd_point.y

# Пример использования
a = int("123456789012345678901234567890")
b = int("987654321098765432109876543210")
gcd_x, gcd_y = elliptic_curve_gcd(a, b)
print(f"Наибольший общий делитель чисел {a} и {b}: {gcd_x}")
