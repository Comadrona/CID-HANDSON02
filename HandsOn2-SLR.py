'''
Centro Universitario de Ciencias exactas e ingenierias
Ingenieria en informatica
Clasificacion inteligente de Datos
2024-B

Hernandez Rodriguez Jose Luis
Codigo 217783351
'''
from SLRModelFile import SLRModel
import re
import os
def main():
    try:
        modelo=SLRModel('benetton.csv','advertising','sales')
        print(modelo.getDataSet())
        print("La ecuacion del modelo generado es la siguiente: "+modelo.getEquation())
        while True:
            print("Si desea inyectar una instancia nueva al modelo, digite la tecla n...")
            print("Si desea probar el modelo con un valor, digite la tecla p...")
            print("Si desea terminar el codigo, digite la cualquier otra tecla...")
            print("Si desea graficar el modelo, digite la tecla g")
            value=input('Digite la opcion deseada: ')
            if value.lower() == 'n':
                valuex=input("Digite el valor de x que desea insertar: ")
                valuey=input("Digite el valor de y que desea insertar: ")
                if re.match(r'^-?\d+(\.\d+)?$', valuex) and re.match(r'^-?\d+(\.\d+)?$', valuey):
                    modelo.insertInstance(float(valuex),float(valuey))
                    print("El dataset queda de la siguiente manera: ")
                    print(modelo.getDataSet())
                    print("La nueva ecuacion del modelo generado es la siguiente: "+modelo.getEquation())
                else:
                    print("Uno de los valores insertados no es numerico")
            elif value.lower() == 'p':
                value=input("Digite el valor de x que desea probar: ")
                if re.match(r'^-?\d+(\.\d+)?$', value):
                    print("De acuerdo al algoritmo de SLR el valor de eje X "+
                        value+" corresponde a "+
                        modelo.getEstimatedValue(float(value))+" en eje Y")
                else:
                    print("El valor no es un numero")
            elif value.lower() == 'g':
                modelo.plot()
            else:
                print("Saliendo del codigo")
                break
            input("Presione cualquier tecla para continuar...")
            if os.name == 'nt':
                os.system('cls')
            else:  
                os.system('clear')
    except ValueError as e:
        print(e)
    
if __name__ == "__main__":
    main()