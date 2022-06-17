año = int(input("Introduce un año: "))

if año % 4 != 0:
    print("Año comun")

elif año % 100 != 0:
    print("Ano biciesto")

elif año % 400 != 0:
    print("Alo comun")

else:
    print("Año biciesto")