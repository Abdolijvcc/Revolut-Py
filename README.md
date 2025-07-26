# Revolut Py

Este proyecto es una **aplicación de consola** en Python que simula el proceso de registro e inicio de sesión para usuarios, similar a una app bancaria. Permite crear cuentas, validar datos, tomar una foto con la cámara y guardar la información en archivos JSON.

## Estructura del proyecto

- `main.py` — Menú principal para crear cuenta o iniciar sesión.
- `crear_cuenta.py` — Lógica para registrar un usuario, validar datos y tomar foto.
- `iniciar_sesion.py` — Lógica para buscar y mostrar datos de usuario.
- `Tomar_foto.py` — Captura de foto usando la cámara (requiere OpenCV y Tkinter).
- `json/countries.json` — Lista de países y códigos telefónicos.
- `data/` — Carpeta donde se guardan los datos de usuario en formato JSON.
- `img/` — Carpeta donde se guardan las fotos tomadas.

## Requisitos

- Python 3.8 o superior
- Paquetes: `opencv-python`, `tkinter` (en Linux: `sudo apt install python3-tk`)
- (Opcional) `auto-py-to-exe` o `pyinstaller` para crear ejecutables

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Crea un entorno virtual (opcional pero recomendado):

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```
   pip install opencv-python
   ```

   En Linux, instala Tkinter si no lo tienes:
   ```
   sudo apt install python3-tk
   ```

## Cómo iniciar el proyecto

1. Asegúrate de tener las carpetas `json/`, `data/` e `img/` en el directorio del proyecto.
2. Ejecuta el menú principal:

   ```
   python main.py
   ```

3. Sigue las instrucciones en pantalla para crear una cuenta o iniciar sesión.

## Crear ejecutable (.exe)

Si quieres crear un ejecutable para Windows:

1. Instala PyInstaller:

   ```
   pip install pyinstaller
   ```

2. Genera el ejecutable:

   ```
   pyinstaller --onefile --add-data="json;json" --add-data="img;img" --add-data="data;data" main.py
   ```

   El ejecutable estará en la carpeta `dist/`.

## Notas

- El proyecto es solo para fines educativos y no debe usarse en producción.
- Asegúrate de tener una cámara conectada si quieres probar la función de foto.
- Los datos se guardan en archivos JSON simples en la carpeta `data/`.

---

¡Disfruta
