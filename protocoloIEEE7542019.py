<<<<<<< HEAD
#Protocolo IEEE 754-2019

res = input("Ingrese 1 para convertir de valor numerico a 32 bits o 2 para ir de 32 bits a valor numerico: ")

if res == "1":
    numero = float (input("Ingrese el valor numerico: "))
    part_entera = int(numero)
    part_decimal = numero - part_entera
    
    binario_entero = format(part_entera, 'b')
    print("Parte entera en binario: ", binario_entero)
    binario_decimal = ""
    
    for i in range(23):
        resultado = part_decimal * 2
        entero = int(resultado)
        part_decimal = resultado - entero
        binario_decimal += str(entero)
    print("Parte decimal en binario:", binario_decimal)
    
    len(binario_entero)
    exponente = len(binario_entero) - 1
    mantisa = binario_entero[1:] + binario_decimal
    mantisa = mantisa[:23]
    
    exponente_almac = exponente + 127
    binario_exponente = format(exponente_almac, '08b')
    
    if numero > 0:
        signo = "0"
        numero_completo = signo + binario_exponente + mantisa
        print("El numero en formato IEEE 754-2019 es: ", numero_completo)
        print(len(numero_completo))
    else:
        signo = "1"
        numero_completo = signo + binario_exponente + mantisa
        print("El numero en formato IEEE 754-2019 es: ", numero_completo)
        print(len(numero_completo))
    
if res == "2":
    numero = input("Ingrese el valor en 32 bits: ")
    signo = int(numero[0])
    exponente = int(numero[1:9], 2) - 127
    mantisa = numero[9:]
    
    valor_mantisa = 1
    for i in range(len(mantisa)):
        if mantisa[i] == "1":
            valor_mantisa += 2 ** -(i + 1)
    
    valor_final = valor_mantisa * (2 ** exponente)
    
    if signo == 1:
        valor_final *= -1
    
    print("El valor numerico es: ", valor_final)
        

        
