import os
import shutil #podrás utilizar sus funciones y métodos para realizar operaciones de manipulación de archivos y directorios, como mover, copiar, eliminar, etc.

# Obtener la ruta de la carpeta que contiene los archivos XML
xml_ruta = input('Ingrese la ruta de la carpeta que contiene los XML: ')

#VERIFICA SI LA RUTA ES VALIDA
if os.path.isdir(xml_ruta):
    for archive in os.listdir(xml_ruta):
        if archive.endswith('.xml'):
            archive_name = os.path.splitext(archive)[0]
        
#Obtiene la ruta completa del archivo y la carpeta destino
            ruta_archivo = os.path.join(xml_ruta, archive)
            ruta_destino = os.path.join(xml_ruta, archive_name)
        
#SI LA CARPETA NO EXISTE, SE CREA UNA CON EL MISMO NOMBRE DE ARCHIVO
            if not os.path.exists(ruta_destino):
                os.mkdir(ruta_destino)
        
#MUEVE ARCHIVOS A CARPETAS
            shutil.move(ruta_archivo, ruta_destino)
            print(f'Archivo "{archive}" movido a la carpeta "{archive_name}"')
#ERROR     
else:
    print('La ruta es invalida')
        

