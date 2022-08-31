from optparse import OptionConflictError
import os
from unittest.mock import patch 

class Ciudad():
    codigo = ''
    ciudad = ''
    pais = ''
    clima = ''

ciudad = Ciudad()
def registrar_archivo(obj):
    archivo = open ('ciudades.txt' , 'a')
    archivo.write(obj.codigo + ';' + obj.ciudad + ';' + obj.pais + ';' + obj.clima + ';' + '\n' )
    archivo.close

def archivo_ciudad(obj,opc):
    archivo = open ('ciudades.txt' )
    for indice, linea in enumerate(archivo):
        datos = linea.split(';')
        if opc == '1':
            try:
                if obj.ciudad == datos[1]:
                    return True        
            except:
                pass
        elif opc == '2':
            print(datos[0]+'\t'+datos[1]+'\t'+datos[2]+'\t'+datos[3])
        elif opc == '3':
            try:
                if obj.codigo == datos[0]:
                    print(datos[0]+'\t'+datos[1]+'\t'+datos[2]+'\t'+datos[3])
                           
            except:
                pass
        elif opc == '4':
            try:
                if obj.clima == datos[3]:
                    print(datos[0]+'\t'+datos[1]+'\t'+datos[2]+'\t'+datos[3])   
            except:
                pass
        elif opc == '5':
            try:
                if obj.ciudad == datos[1]:
                    eliminar(indice)
            except:
                pass
        
def eliminar(indice):
    contenido = list ()
    with open('ciudades.txt', 'r+') as archivo:
        contenido = archivo.readlines()
        for i in range(contenido):
            if indice != i:
                print(contenido[i])
                with open('ciudades.txt', 'w') as archivo:
                    archivo.writelines(contenido[i])   
    
def crear_ciudad (obj,opc):
    while True:
        obj.codigo = input('ingrese el numero postal de la ciudad ')
        obj.ciudad = input('ingrese el nombre de la ciudad ')
        obj.pais = input('ingrese el nombre del país ')
        obj.clima = input('ingrese el clima ')
        archivo = archivo_ciudad(obj,opc)
        if archivo != True:
            registrar_archivo(obj)
            return True
        else:
            print('la ciudad esta registrada')
            continue

def buscar_ciudad(opc,obj):
    if opc == '3':
        print('Buscar una ciudad por codigo')
        obj.codigo = input('ingrese el codigo de la ciudad')
        archivo_ciudad(obj,opc)
        return True
    elif  opc == '4':
        print('Buscar una ciudad por clima')
        obj.clima = input('ingrese el codigo el clima de la ciudad')
        archivo_ciudad(obj,opc)
        return True
 
def eliminar_ciudad(obj,opc):
    print('Eliminar una ciudad ')
    obj.ciudad = input('ingrese el nombre de  la ciudad')
    archivo_ciudad(obj,opc)

    
def opciones_del_programa(obj):
    while True:
        print('----------------')
        print('CIUDADES')
        print('----------------')
        print('1.   Crear ciudad')
        print('2.   listar')
        print('3.   Buscar una ciudad por código')
        print('4.   buscar ciudad por clima')
        print('5.   Eliminar una ciudad')
        print('6.   Salir')
        opcion = input('seleecione una opcion: ')
        if opcion == '1':
            ciudad = crear_ciudad(obj,opcion)
        elif opcion == '2':
            lista = archivo_ciudad(obj,opcion)
        elif opcion == '3':
            codigo =''
            buscar_ciudad(opcion,obj)
        elif opcion == '4':
            clima = ''
            buscar_ciudad(opcion,obj)
        elif opcion == '5':
            eliminar_ciudad(obj,opcion)
        elif opcion == '6':
            break
        else:
            print('la opcion ingresada no es valida')
            continue


def main ():
    opciones_del_programa(ciudad)

if __name__ == '__main__':
    main()
        




