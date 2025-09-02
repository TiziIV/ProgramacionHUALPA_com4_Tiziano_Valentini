#Ejercicio 3

#PEDIMOS DATOS
nombre=input("INGRESE SU NOMBRE: ")
apellido=input("INGRESE SU APELLIDO: ")
cuit=(input("INGRESE SU CUIT: "))

#VALIDAR CUIT
def validar_cuit(cuit):
    if len(cuit) != 11:
        return "El CUIT tiene que contener 11 dígitos"
    if not cuit.isdigit():
        return "El CUIT solo puede tener números"
    if cuit[:2] not in {"20", "23", "24", "27", "30", "33", "34"}:
        return f"El prefijo '{cuit[:2]}' no existe en ningún CUIT."
    return True

# Validamos CUIT
resultado = validar_cuit(cuit)

# Mostramos resultado
if resultado is True:
    print("CUIT VALIDADO")
else:
    print(f"Error con el CUIT: {resultado}")

# PEDIMOS LOS DATOS RESTANTES(INGRESOS,ANTIGUEDAD,HISTORIAL)
ingresos=float(input("INGRESE SUS INGRESOS MENSUALES: "))
antiguedad_laboral=int(input("INGRESE SU ANTIGUEDAD LABORAL EN AÑOS: "))
historial_crediticio=input("INGRESE SU HISTORIAL CREDITICIO: BUENO / REGULAR / MALO: ")
historial_crediticio=historial_crediticio.capitalize()

#VALIDAR LOS DATOS
#LIMPIAR VARIABLE
monto_aprobado=0
if historial_crediticio == "Malo":
    print("SE HA RECHAZADO SU PETICIÓN (HISTORIAL NEGATIVO)")
elif ingresos < 200000:
    print("SE HA RECHAZADO SU PETICIÓN (INGRESOS INSUFICIENTES)")
else:
    if antiguedad_laboral < 2:
        if historial_crediticio in ["Bueno", "Regular"]:
            monto_aprobado=500000
    else:  
        if historial_crediticio == "Bueno":
            monto_aprobado=3000000
        elif historial_crediticio == "Regular":
            monto_aprobado=1000000

# SALIDA DE DATOS
print(f"CLIENTE: {nombre} {apellido}")
print(f"CUIT: {cuit}")
print(f"INGRESOS: {ingresos}")
print(f"ANTIGUEDAD: {antiguedad_laboral}")
print(f"HISTORIAL: {historial_crediticio}")
print(f"MONTO APROBADO: {monto_aprobado}")

