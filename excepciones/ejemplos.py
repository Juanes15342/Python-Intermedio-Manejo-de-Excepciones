
try:
    # Codigo que podria generar una excepcion
    pass
except:
    # Codigo que se ejecuta si ocurre cualquier excepcion (plan B)
    pass
 
 
try:
    numero1 = 10
    numero2 = 0
    resultado = numero1 / numero2
    print(f"El resultado es: {resultado}")
except:
    print("!Ups! No se puede dividir entre cero.")
 
 

try:
    numero = int(input("Introduce un numero: "))  # Puede lanzar ValueError
    resultado = 100 / numero                       # Puede lanzar ZeroDivisionError
    print(f"100 dividido por {numero} es {resultado}")
except ZeroDivisionError:
    # Se ejecuta si el usuario ingresa 0
    print("No puedes dividir entre cero.")
except ValueError:
    # Se ejecuta si el usuario ingresa algo que no es numero (ej: "abc")
    print("Debes introducir un numero valido.")
 
 
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError as error:
    # "error" contiene la descripcion completa del error ocurrido
    print(f"Error: {error}")
    print("Creando un archivo nuevo...")
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Este es un archivo nuevo")
 
 
try:
    archivo = open("datos.txt", "r")
    valor = int(archivo.readline().strip())
    resultado = 100 / valor
except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    # type(e).__name__ nos da el nombre del tipo de excepcion que ocurrio
    print(f"Ocurrio un error: {type(e).__name__}")
    print(f"Descripcion: {e}")
 
 
def obtener_edad():
    while True:
        try:
            edad = int(input("Cual es tu edad? "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue  # Vuelve al inicio del while sin salir
            return edad   # Solo retorna si el valor es valido
        except ValueError:
            # Si el usuario escribe texto en lugar de un numero
            print("Por favor, introduce un numero entero.")
 
 
# MAL EJEMPLO: bloque try demasiado grande y except generico poco util
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    numeros = [int(x) for x in contenido.split()]
    resultado = sum(numeros) / len(numeros)
    print(f"El promedio es: {resultado}")
    archivo.close()
except:
    print("Ocurrio un error")  # No sabemos que salio mal
 
# BUEN EJEMPLO: bloques try especificos con mensajes claros
def calcular_promedio_archivo():
    try:
        archivo = open("datos.txt", "r")
    except FileNotFoundError:
        print("El archivo 'datos.txt' no existe")
        return
 
    try:
        contenido = archivo.read()
        numeros = [int(x) for x in contenido.split()]
    except ValueError:
        print("El archivo contiene datos que no son numeros")
        archivo.close()
        return
 
    try:
        resultado = sum(numeros) / len(numeros)
        print(f"El promedio es: {resultado}")
    except ZeroDivisionError:
        print("El archivo esta vacio, no se puede calcular el promedio")
 
    archivo.close()
 
 


print("\n--- ZeroDivisionError ---")
try:
    resultado = 5 / 0
except ZeroDivisionError:
    print("No es posible dividir entre cero")
 
 

print("\n--- OverflowError ---")
try:
    resultado = 10.0 ** 1000000  # 10 elevado a un millon es inmensamente grande
except OverflowError:
    print("El numero es demasiado grande para ser representado")
 
 

try:
    resultado = "42" + 10  # No se puede sumar texto con numero directamente
except TypeError:
    print("No se pueden sumar tipos diferentes")
 
 

print("\n--- ValueError ---")
try:
    numero = int("abc")  # "abc" no representa un numero valido
except ValueError:
    print("La cadena no representa un numero valido")
 
 

print("\n--- IndexError ---")
try:
    lista = [1, 2, 3]
    elemento = lista[10]  # La lista solo tiene indices 0, 1 y 2
except IndexError:
    print("El indice esta fuera del rango de la lista")
 
 

print("\n--- KeyError ---")
try:
    diccionario = {"nombre": "Ana", "edad": 25}
    valor = diccionario["telefono"]  # La clave "telefono" no existe
except KeyError:
    print("La clave 'telefono' no existe en el diccionario")
 
 

print("\n--- FileNotFoundError ---")
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
 
 

print("\n--- PermissionError ---")
try:
    with open("C:\\Windows\\System32\\prueba.txt", "w") as archivo:  # Carpeta protegida en Windows
        archivo.write("datos")
except PermissionError:
    print("No tienes permisos para modificar este archivo")
except FileNotFoundError:
    # Por si la ruta no es accesible directamente, simulamos el comportamiento
    raise PermissionError("Acceso denegado al directorio del sistema") from None
 
 

print("\n--- AttributeError ---")
try:
    texto = "Hola"
    longitud = texto.size  # El correcto seria len(texto), no texto.size
except AttributeError:
    print("El objeto string no tiene el atributo 'size'")
 
 

print("\n--- Exception (clase base) ---")
try:
    resultado = int("abc") / 0  # Puede lanzar ValueError o ZeroDivisionError
except Exception as e:
    print(f"Se produjo un error: {type(e).__name__}")
    print(f"Descripcion: {e}")
 
 

print("\n--- Identificar tipo de excepcion ---")
try:
    resultado = eval(input("Introduce una expresion matematica: "))
except Exception as e:
    print(f"Error de tipo: {type(e).__name__}")
    print(f"Descripcion: {e}")
 
 

print("\n--- else ---")
try:
    numero = int(input("Introduce un numero: "))
    resultado = 100 / numero
except ValueError:
    print("Debes introducir un numero valido.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
else:
    # Solo llega aqui si no hubo ninguna excepcion
    print(f"El resultado es: {resultado}")
 
 

try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
    contenido = ""
else:
    # Solo se ejecuta si el archivo existia y se leyo sin problemas
    print("Archivo leido correctamente.")
    archivo.close()
 
 

print("\n--- finally ---")
try:
    archivo = open("registro.txt", "w")
    archivo.write("Operacion iniciada\n")
    resultado = 10 / int(input("Introduce un numero: "))
    archivo.write(f"Resultado: {resultado}\n")
except ZeroDivisionError:
    archivo.write("Error: Division por cero\n")
except ValueError:
    archivo.write("Error: Valor no valido\n")
finally:
    # Esto se ejecuta SIN IMPORTAR que paso arriba
    archivo.write("Operacion finalizada\n")
    archivo.close()
    print("Proceso completado")
 
 

print("\n--- else + finally combinados ---")
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe, se creara uno nuevo.")
    archivo = open("datos.txt", "w")
    archivo.write("Archivo creado automaticamente")
else:
    # Solo si el archivo existia y se leyo correctamente
    print(f"Contenido leido: {contenido}")
finally:
    # Se ejecuta tanto si se leyo como si se creo el archivo
    print("Operacion de archivo completada.")
    archivo.close()
 
 

def demostrar_orden():
    try:
        print("1. Ejecutando bloque try")
        # Descomenta para generar una excepcion y ver como cambia el flujo:
        # x = 1 / 0
    except ZeroDivisionError:
        print("2. Ejecutando bloque except")
    else:
        print("3. Ejecutando bloque else (no hubo excepcion)")
    finally:
        print("4. Ejecutando bloque finally (siempre se ejecuta)")
 
    print("5. Continuando despues del bloque try")
 
demostrar_orden()
 
 

def dividir(a, b):
    try:
        resultado = a / b
        return resultado       # No retorna de inmediato; finally corre primero
    except ZeroDivisionError:
        print("Error: Division por cero")
        return None            # Tampoco retorna de inmediato
    finally:
        # Esto corre ANTES de que se devuelva cualquier valor
        print("Division finalizada")
 
print(dividir(10, 2))   # Imprime "Division finalizada" y luego 5.0
print(dividir(10, 0))   # Imprime el error, "Division finalizada" y luego None
 
 

print("\n--- raise basico ---")
def dividir_seguro(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b
 
try:
    resultado = dividir_seguro(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
 
 

print("\n--- raise ValueError ---")
def calcular_raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo")
    return numero ** 0.5
 
try:
    print(calcular_raiz_cuadrada(-9))
except ValueError as e:
    print(f"Error: {e}")
 
 

def procesar_respuesta(codigo):
    if codigo == 200:
        return "Datos recibidos correctamente"
    elif codigo == 404:
        return None
    else:
        raise RuntimeError(f"Codigo de respuesta no manejado: {codigo}")
 
try:
    print(procesar_respuesta(500))
except RuntimeError as e:
    print(f"Error inesperado: {e}")
 
 

print("\n--- raise con precondiciones ---")
def retirar_dinero(saldo, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    if cantidad > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - cantidad
 
try:
    nuevo_saldo = retirar_dinero(100, 200)
except ValueError as e:
    print(f"Error al retirar: {e}")
 
 

print("\n--- raise TypeError + ValueError ---")
def establecer_edad(edad):
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un numero entero")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 anos")
    return edad
 
try:
    establecer_edad("veinte")   # Tipo incorrecto: string en lugar de int
except TypeError as e:
    print(f"Error de tipo: {e}")
 
try:
    establecer_edad(200)        # Valor incorrecto: fuera del rango valido
except ValueError as e:
    print(f"Error de valor: {e}")
 
 

print("\n--- raise TypeError en concatenar ---")
def concatenar(texto, repeticiones):
    if not isinstance(texto, str):
        raise TypeError("El primer argumento debe ser una cadena de texto")
    if not isinstance(repeticiones, int):
        raise TypeError("El segundo argumento debe ser un numero entero")
    return texto * repeticiones
 
try:
    print(concatenar(123, 3))   # 123 es int, no string
except TypeError as e:
    print(f"Error: {e}")
 
 

print("\n--- relanzar excepcion ---")
def procesar_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError as e:
        print(f"Registrando error: {e}")
        raise  # Relanza la misma excepcion sin modificarla
 
try:
    procesar_archivo("no_existe.txt")
except FileNotFoundError:
    print("El archivo no pudo ser procesado (manejado en nivel superior)")
 
 

print("\n--- raise ... from ... ---")
 
class ConfigurationError(Exception):
    """Excepcion personalizada para errores de configuracion."""
    pass
 
def obtener_configuracion(archivo):
    try:
        with open(archivo, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        # "from e" vincula el error original con el nuevo como su causa
        raise ConfigurationError(f"Archivo de configuracion no encontrado: {archivo}") from e
 
try:
    obtener_configuracion("config.json")
except ConfigurationError as e:
    print(f"Error de configuracion: {e}")
 
 

print("\n--- excepcion personalizada ---")
 
class SaldoInsuficienteError(Exception):
    """Se lanza cuando se intenta retirar mas dinero del disponible."""
 
    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.deficit = cantidad - saldo  # Cuanto falta para poder retirar
        mensaje = f"No hay suficiente saldo. Saldo: {saldo}, Cantidad solicitada: {cantidad}"
        super().__init__(mensaje)  # Llama al constructor de Exception con el mensaje
 
def retirar(saldo, cantidad):
    if cantidad > saldo:
        raise SaldoInsuficienteError(saldo, cantidad)
    return saldo - cantidad
 
try:
    nuevo_saldo = retirar(50, 100)
except SaldoInsuficienteError as e:
    print(f"Error: {e}")
    print(f"Te faltan: {e.deficit} unidades")  # Accedemos al atributo personalizado
 
 

print("\n--- validacion temprana ---")
def procesar_datos(datos):
    # Primero validamos todo antes de procesar nada
    if datos is None:
        raise ValueError("Los datos no pueden ser None")
    if not isinstance(datos, list):
        raise TypeError("Los datos deben ser una lista")
    if len(datos) == 0:
        raise ValueError("La lista de datos no puede estar vacia")
 
    # Si llegamos aqui, los datos son validos y podemos procesarlos
    return [x * 2 for x in datos]
 
try:
    procesar_datos(None)
except ValueError as e:
    print(f"Error: {e}")
 
try:
    procesar_datos("no soy una lista")
except TypeError as e:
    print(f"Error: {e}")
 
try:
    procesar_datos([])
except ValueError as e:
    print(f"Error: {e}")
 
 

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
 