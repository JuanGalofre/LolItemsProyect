import subprocess
import datetime

def backup_postgres_db(usuario, host, puerto, nombre_bd, archivo_respaldo):
    # Construir el comando de pg_dump
    comando = [
        "pg_dump",              # Llamamos a la herramienta pg_dump
        "-U", usuario,          # Nombre de usuario
        "-h", host,             # Host (por ejemplo, localhost)
        "-p", str(puerto),      # Puerto de conexión
        "-F", "p",              # Formato plain (archivo .sql)
        "-f", archivo_respaldo, # Ruta donde guardar el respaldo
        nombre_bd               # Nombre de la base de datos
    ]

    # Establecer la variable de entorno para la contraseña
    # Esto es necesario si no quieres que te pida la contraseña interactiva.
    # De lo contrario, puedes eliminar esta línea y escribir la contraseña cuando se te pida.
    import os
    os.environ["PGPASSWORD"] = "HappySoulsSmile"

    try:
        # Ejecutar el comando usando subprocess
        subprocess.run(comando, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Respaldo de la base de datos {nombre_bd} realizado exitosamente en {archivo_respaldo}")
    except subprocess.CalledProcessError as e:
        print(f"Error al hacer el respaldo: {e.stderr.decode()}")
    finally:
        # Limpiar la variable de entorno de la contraseña
        del os.environ["PGPASSWORD"]



