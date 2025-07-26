# this file is maked for AI
# This file is used to capture a photo using the camera in Linux
# Ensure that the user has OpenCV installed and has access to the camera
import cv2
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import crear_cuenta


def captura_foto_con_gui(ruta_salida, nombre_archivo):
    """
    Abre una GUI para capturar una foto desde la cámara.
    Guarda la imagen en 'ruta_salida/nombre_archivo'.
    """

    # Asegurar que la ruta de salida existe
    ruta_salida = os.path.expanduser(ruta_salida)
    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)

    cap = cv2.VideoCapture(0)

    ventana = tk.Tk()
    ventana.title("Capturar Foto")
    ventana.geometry("700x600")
    ventana.resizable(False, False)

    etiqueta_video = tk.Label(ventana)
    etiqueta_video.pack()

    resultado = {"imagen": None}

    def actualizar_frame():
        ret, frame = cap.read()
        if not ret:
            return

        alto, ancho = frame.shape[:2]
        centro = (ancho // 2, alto // 2)
        radio = min(ancho, alto) // 4
        cv2.circle(frame, centro, radio, (0, 255, 0), 2)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        etiqueta_video.imgtk = imgtk
        etiqueta_video.configure(image=imgtk)
        ventana.after(10, actualizar_frame)

    def capturar_imagen():
        ret, frame = cap.read()
        if ret:
            resultado["imagen"] = frame.copy()

            # Mostrar vista previa en la interfaz (no usar cv2.imshow)
            imagen_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(imagen_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            '''
            ventana_previa = tk.Toplevel(ventana)
            ventana_previa.title("Imagen Capturada")
            ventana_previa.geometry("500x400")
            lbl = tk.Label(ventana_previa, image=imgtk)
            lbl.image = imgtk
            lbl.pack()

            boton_guardar.pack(side="left", padx=20, pady=20)
            boton_reintentar.pack(side="right", padx=20, pady=20)
            '''
            ventana_previa = tk.Toplevel(ventana)
            ventana_previa.title("Imagen Capturada")
            
            lbl = tk.Label(ventana_previa, image=imgtk)
            lbl.image = imgtk
            lbl.pack()
            
            frame_botones = tk.Frame(ventana_previa)
            frame_botones.pack(pady=10)
            
            btn_guardar = tk.Button(frame_botones, text="💾 Guardar", font=("Arial", 12),
                                    bg="#0066cc", fg="white", width=12, command=lambda: guardar_imagen(ventana_previa))
            btn_guardar.pack(side="left", padx=10)
            
            btn_reintentar = tk.Button(frame_botones, text="🔁 Reintentar", font=("Arial", 12),
                                       bg="#cc0000", fg="white", width=12, command=lambda: reintentar_captura(ventana_previa))
            btn_reintentar.pack(side="right", padx=10)

    def guardar_imagen(ventana_previa):
        if resultado["imagen"] is not None:
            ruta_completa = os.path.join(ruta_salida, nombre_archivo)
            cv2.imwrite(ruta_completa, resultado["imagen"])
            messagebox.showinfo("Éxito", f"Foto guardada como:\n{ruta_completa}")
            ventana_previa.destroy()
            ventana.destroy()
            cap.release()

    def reintentar_captura(ventana_previa):
        resultado["imagen"] = None
        ventana_previa.destroy()

    # Botones
    boton_capturar = tk.Button(ventana, text="📸 Capturar", font=("Arial", 16),
                               command=capturar_imagen, bg="#00aa00", fg="white",
                               height=2, width=20)
    boton_capturar.pack(pady=20)

    boton_guardar = tk.Button(ventana, text="💾 Guardar", font=("Arial", 14),
                              command=guardar_imagen, bg="#0066cc", fg="white",
                              height=2, width=10)

    boton_reintentar = tk.Button(ventana, text="🔁 Reintentar", font=("Arial", 14),
                                 command=reintentar_captura, bg="#cc0000", fg="white",
                                 height=2, width=10)

    actualizar_frame()
    ventana.mainloop()
    cv2.destroyAllWindows()

def main():
    captura_foto_con_gui("")

if __name__ == "__main__":
    main()   