# Definir variables

nombre = "Elizabeth"
edad = 32
carrera = "Desarrollo"
dato1 = input("Ingrese un número ")

presentacion= f"Mi nombre es {nombre} tengo {edad} años, estudio {carrera} y presentare algunas funciones"
print(presentacion)

#if edad == 32 :
 #   print("Es verdadero")
#else:
#    print("Es falso")

#try:
 #   dato1 = int(dato1)
  #  if dato1 > 0:
   #     print("El número es positivo")
    #else:
     #   print("El número es negativo")
#except ValueError:
#    print("El número introducido no es válido")
    
# operaciones matematicas
#suma = 8 + 9 
#resta = 265 - 25
#multiplicacion = 85 * 64
#division = 8945 / 25

#print("suma:", suma)
#print("resta:", resta)
#print("multiplicacion:", multiplicacion)
#print("division:", division)

#Calculo de numeros primos 
n = int(input("Ingrese un número entero: "))
suma = 0
for i in range(2, n*2 + 1, 2):
    suma += i
print("La suma de los primeros", n, "números pares es:", suma)
