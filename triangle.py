def isTriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del primer lado: "))
c = float(input("Ingresa la longitud del primer lado: "))

if isTriangle(a, b, c):
    print("Si, los lados forman un triángulo.")
else:
    print("No, los lados no forman un triángulo.")