import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print(f"Archivo seleccionado: {file_path}")

if file_path:
    with open(file_path, 'rb') as file:
        content = file.read()

        try:
            text = content.decode('utf-8')
            print(f"Contenido del archivo:\n{text}")
        except UnicodeDecodeError:
            print("El archivo contiene datos no textuales o usa una codificación diferente a UTF-8.")
else:
    print("No se seleccionó ningún archivo.")
