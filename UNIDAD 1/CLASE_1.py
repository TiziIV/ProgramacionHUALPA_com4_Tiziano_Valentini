# INGRESO DE CALIFICACIONES
parcial_1=float(input("INGRESE LA NOTA DEL PRIMER PARCIAL: "))
parcial_2=float(input("INGRESE LA NOTA DEL SEGUNDO PARCIAL: "))
parcial_3=float(input("INGRESE LA NOTA DEL TERCER PARCIAL: "))

# EXAMEN FINAL Y TRABAJO
nota_final=float(input("INGRESE LA NOTA DEL EXAMEN FINAL: "))
trabajo_final=float(input("INGRESE LA NOTA DEL TRABAJO FINAL: "))

# CALCULOS 
nota_final_parcial= (parcial_1+parcial_2+parcial_3)/3
calificacion_final= (nota_final_parcial*0.55)+(nota_final*0.30)+(trabajo_final*0.15)

# MOSTRAR RESULTADO
print(f"La nota final es de {calificacion_final}")

# EJERCICIO 7
monto_dolares = float(input("INGRESE EL MONTO EN DOLARES: "))
monto_pesos = monto_dolares*1333.99
monto_colombianos = monto_dolares*4027.54
monto_euros = monto_dolares*0.86
print(f"EL MONTO EN PESOS ES DE {monto_pesos}")
print(f"EL MONTO EN COLOMBIANOS ES DE {monto_colombianos}")
print(f"EL MONTO EN EUROS ES DE {monto_euros}")

# EJERCICIO 8
gasto_auto = 8/100
distancia_en_km = float(input("INGRESE LA DISTANCIA: "))
precio_gasolina = float(input("INGRESE EL PRECIO DE LA GASOLINA: "))
cantidad_litros = gasto_auto*distancia_en_km
valor_viaje = cantidad_litros*precio_gasolina
horas_de_viaje = distancia_en_km/90
print(f"LA CANTIDAD DE LITROS NECESARIA PARA EL VIAJE ES DE {cantidad_litros}")
print(f"EL VALOR DEL VIAJE ES DE {valor_viaje}")
print(f"LAS HORAS DE VIAJE EN TOTAL SERAN DE {horas_de_viaje}")

# EJERCICIO 9
monto_solicitado = float(input("INGRESE EL MONTO A SOLICITAR"))
cuota_base = monto_solicitado / 12  
interes_mensual = cuota_base * 0.02  
valor_mensual = cuota_base + interes_mensual  
monto_devolucion = valor_mensual * 12  

print(f"EL VALOR TOTAL A DEVOLVER ES DE {monto_devolucion}")
print(f"CADA CUOTA TIENE UN VALOR DE {valor_mensual}")