def dividir_numeros():
    try:
        # Solicitar al usuario que introduzca dos números
        numero1 = input("Introduce el primer numero: ")
        numero2 = input("Introduce el segundo numero: ")
 
        # Convertir las entradas a números enteros
        numero1 = int(numero1)
        numero2 = int(numero2)
 
        # Realizar la división del primer número entre el segundo
        resultado = numero1 / numero2
 
        # Devolver el resultado de la división
        return resultado
 
    except ValueError:
        print("Error: Debes introducir un numero valido")
 
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
 
    finally:
        # Se ejecuta siempre, haya o no excepcion
        print("Operacion finalizada")
 
 
# Llamada a la función
resultado = dividir_numeros()
if resultado is not None:
    print(f"El resultado es: {resultado}")
 
print("\n--- ejemplo completo: obtener edad ---")
def obtener_edad_validada():
    while True:
        try:
            entrada = input("Introduce tu edad: ")
 
            if not entrada.strip():
                raise ValueError("La entrada no puede estar vacia")
 
            edad = int(entrada)  # Lanza ValueError si no es numero
 
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
 
            if edad > 120:
                raise ValueError("La edad parece demasiado alta")
 
            return edad  # Solo retorna si todo fue valido
 
        except ValueError as e:
            # Distinguimos el ValueError de int() del que lanzamos nosotros
            if "invalid literal for int" in str(e):
                print("Por favor, introduce un numero valido")
            else:
                print(f"Error: {e}")
 
# Llamada principal con manejo de Ctrl+C para cancelar el programa
# try:
#     edad_usuario = obtener_edad_validada()
#     print(f"Tu edad es: {edad_usuario}")
# except KeyboardInterrupt:
#     print("\nOperacion cancelada por el usuario")