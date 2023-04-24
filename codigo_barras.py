
while True:
    codigo=input("Introduce codigo de barras (Escribe -1 para salir)\n")
    if not type(codigo) is int:
        if len(codigo)==13:
            #Controlar que todos los digitos son numeros
            try:
                numeroCodigo=int(codigo)
            except:
                print("Error, introduce solo numeros")
            else:
                #Recorrer la variable como un array
                contador=0
                suma=0
                for i in codigo[:12]:
                    #Contabilizar la posicion
                    contador+=1
                    #Si la posicion es par se multiplica por 3 y se suma al total
                    #Si la posicion es impar se multiplica por 1 y se suma al total
                    if contador%2==0:
                        suma+=int(i)*3
                    else:
                        suma+=int(i)*1
                #Se divide entre 10 para convertirlo en entero y multiparlo por 10 para sacar la siguiente decena
                total=(int(suma/10)+1)*10
                if total-suma==int(codigo[-1:]):
                    print("Codigo de barras correcto\n")
                    print("Fin del programa\n")
                    print("¡¡¡Adios!!!")
                    break
        else:
            if codigo=="-1":
                print("Programa finalizado")
                break
            print("Tamaño erroneo, tiene que tener 13 digitos")
