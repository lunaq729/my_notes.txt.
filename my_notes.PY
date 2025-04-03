# Escritura en un archivo de texto
with open("my_notes.txt", "w") as file:
    # Escribimos varias líneas de notas personales en el archivo usando writelines()
    notes = [
        "Linea 1: Estas son mis metas personales.\n",
        "Linea 2: Estoy practicando manejo de archivos en Excel.\n",
        "Linea 3: Es importante cerrar los archivos después de usarlos.\n",
        "Linea 4: Usar writelines() facilita la escritura de múltiples líneas.\n",
        "Linea 5: Ahora probaremos una forma diferente de leer el archivo.\n"
    ]
    file.writelines(notes)

# Lectura del archivo de texto
try:
    with open("my_notes.txt", "r") as file:
        # Leer todas las líneas de una sola vez con readlines()
        lines = file.readlines()
        for line in lines:
            print(line.strip())  # Mostrar la línea eliminando espacios en blanco y saltos de línea innecesarios
except FileNotFoundError:
    print("Error: El archivo no existe.")

# El archivo se cierra automáticamente al salir del bloque with