# crear_cuenta.py
# Este script permite a los usuarios crear una cuenta en Revolut Py.
# Asegúrate de que el usuario tenga instalado OpenCV y tenga acceso a la cámara.
# Importante: Este código es un ejemplo y no debe usarse en producción sin las debidas medidas de seguridad y validación.
# -*- coding: utf-8 -*-
import os
import cv2 
import iniciar_sesion
import time
import json
import Tomar_foto


def crear_cuenta():
    print("Crear cuenta en Revolut Py")
    # Aquí puedes agregar la lógica para crear una cuenta
    print("crea tu cuenta de Revolut Py")
    #nota: Asegúrate de que el usuario tenga instalado OpenCV y tenga acceso a la cámara

    # Opening JSON file
    f = open('json/countries.json')
    # returns JSON object as a dictionary
    countries = json.load(f)

    # Iterating through the json list
    # Iterar sobre la lista y mostrar los nombres en español
    for country in countries:
        PhoneCode = (country["phoneCode"])

    
    
    
    #****************************** introducir numero de telefono y codigo de verificacion ******************************
    # Mostrar países y pedir selección
    print("Selecciona tu país:")
    for idx, country in enumerate(countries):
        nameES=(f"{idx + 1}. {country['nameES']}").lower()
   

    # Pedir país al usuario y buscarlo en la lista
    # This loop will continue until a valid country is selected
    #This loop will maked for AI
    while True:
        pais_usuario = input("Introduce el nombre de tu país: ").strip().lower()
        pais_seleccionado = None
        for country in countries:
            if country.get("nameES", "").strip().lower() == pais_usuario:
                pais_seleccionado = country
                PhoneCode = pais_seleccionado["phoneCode"]
                break
        if pais_seleccionado:
            print(f"País seleccionado: {pais_seleccionado['nameES']} (código: +{PhoneCode})")
            break
        else:
            print("País no encontrado. Por favor, revisa la ortografía e intenta de nuevo.")
    #*****************************************************************************
    # Validar número de teléfono
    print("Introduce tu número de teléfono :")
    while True:
        telefono = input(f"Número de teléfono: +{PhoneCode} ")
        
        if not telefono[1:].replace(" ", "").isdigit():
            print("El número de teléfono debe contener solo dígitos después del código de país.")
            continue
        elif len(telefono) < 10:
            print("El número de teléfono debe tener al menos 10 dígitos.")
            continue
        elif len(telefono) > 15:
            print("El número de teléfono no debe exceder los 15 dígitos.")
            continue
        print(f"Enviando código de verificación al {telefono}...")
        codigo_verificacion = input("Introduce el código de verificación recibido: ")
        print(f"Código de verificación {codigo_verificacion} recibido.")
        break
    f.close()
    #************************************ fin de introducir numero de telefono y codigo de verificacion ****************************
    
    # Aquí podrías agregar más lógica para completar el proceso de creación de cuenta
    #pais = input("Introduce tu país: ")
    #time.sleep(0.5)
    while True:
        correo = input("Introduce tu correo electrónico: ")
        if '@' not in correo or '.' not in correo:
            print("Correo electrónico no válido. Asegúrate de que contenga '@' y un dominio.")
        elif len(correo) < 5:
            print("El correo electrónico debe tener al menos 5 caracteres.")
        else:
            print(f"Correo electrónico {correo} válido.")
            break
    # Validar clave de acceso
    while True:
        crea_la_clave_acceso = input("Crea una clave de acceso (mínimo 4 caracteres): ")
        if len(crea_la_clave_acceso) < 4:
            print("Por favor, introduce al menos 4 caracteres.")
            continue
        elif crea_la_clave_acceso in ["1234", "12345", "123456", "1234567"]:
            print("Clave de acceso débil. Por favor, crea una clave más segura.")
            continue
        print("Clave de acceso creada correctamente.")
        break
    

    # Validar nombre y apellidos
    
    while True:
        nombre = input("Introduce tu nombre: ")
        apellido = input("Introduce tu apellido: ")
        if not nombre.isalpha() or not apellido.isalpha():
            print("El nombre y el apellido deben contener solo letras.")
            continue
        elif len(nombre) < 2 or len(apellido) < 2:
            print("El nombre y el apellido deben tener al menos 2 caracteres.")
            continue
        print(f"Nombre completo: {nombre} {apellido}")
        break

    # Validar fecha de nacimiento
    while True:
        fecha_de_nacimiento = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")
        if len(fecha_de_nacimiento) != 10 or fecha_de_nacimiento[2] != '/' or fecha_de_nacimiento[5] != '/':
            print("Fecha de nacimiento no válida. Debe estar en formato DD/MM/AAAA.")
            continue
        dia, mes, anio = map(int, fecha_de_nacimiento.split('/'))
        if anio > 2005:  # Asumiendo que el usuario debe tener al menos 18 años
            print("Debes tener al menos 18 años para crear una cuenta.")
            continue
        print(f"Fecha de nacimiento: {fecha_de_nacimiento}")
        break
    # Validar dirección y área profesional
    while True:
        direccion = input("Introduce tu dirección: ")
        if len(direccion) < 5:
            print("La dirección debe tener al menos 5 caracteres.")
            continue
        print(f"Dirección: {direccion}")
        break
    # Validar área profesional
    while True:
        area_profesional = input("Introduce tu área profesional: ")
        if len(area_profesional) < 3:
            print("El área profesional debe tener al menos 3 caracteres.")
            continue
        print(f"Área profesional: {area_profesional}")
        break
    # Validar documento de identidad foto formato png o jpg ejemplo: /boot/Documents/foto_identidad/nombre_apellido.jpg
    while True:
        document_identidad = input("Introduce la ruta del documento de identidad (formato .jpg o .png): ")
        if not os.path.exists(document_identidad):
            print("Documento de identidad no encontrado. Por favor, verifica la ruta del archivo.")
            continue
        elif not (document_identidad.endswith('.jpg') or document_identidad.endswith('.png')):
            print("El documento de identidad debe ser un archivo .jpg o .png.")
            continue
        nombre_en_el_documento = os.path.basename(document_identidad).split('_')[0]
        apellido_en_el_documento = os.path.basename(document_identidad).split('_')[1].split('.')[0]
        print(f"Documento de identidad verificado: {nombre_en_el_documento} {apellido_en_el_documento}")
        break

    # Tomar foto con la cámara
    
    Tomar_foto.captura_foto_con_gui("img", f"{nombre}_{apellido}.jpg")
    print("Cuenta creada exitosamente.")
    print("Bienvenido a Revolut Py, " + nombre + " " + apellido + "!")
    print("Por favor, inicia sesión para continuar.") 
    iniciar_sesion.iniciar_sesion()
    return nombre, apellido, telefono, correo, fecha_de_nacimiento, direccion, area_profesional, crea_la_clave_acceso
# Guardar datos del usuario en un archivo data ejemplo: data/nombre_apellido.json

def data_usuario(nombre, apellido, telefono, correo, fecha_de_nacimiento, direccion, area_profesional, clave_acceso):
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "correo": correo,
        "fecha_de_nacimiento": fecha_de_nacimiento,
        "direccion": direccion,
        "area_profesional": area_profesional,
        "clave_acceso": clave_acceso
    }
    ruta = f"data/{nombre}_{apellido}.json"
    with open(ruta, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Datos del usuario guardados en {ruta}")     
def main():
    nombre, apellido, telefono, correo, fecha_de_nacimiento, direccion, area_profesional, crea_la_clave_acceso = crear_cuenta()
    data_usuario(nombre, apellido, telefono, correo, fecha_de_nacimiento, direccion, area_profesional, crea_la_clave_acceso)

if __name__ == "__main__":
    main()