import iniciar_sesion
import crear_cuenta

def welcome_message():
    while True:
        print("REVOLUT Py")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Salir")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            iniciar_sesion.main()
        elif choice == '2':
            crear_cuenta.crear_cuenta()
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    welcome_message()

if __name__ == "__main__":
    main()