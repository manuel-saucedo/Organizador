import os #libreria pra trabajar con las rutas
import shutil #libreri para mover archivos o eliminarlos

extenciones_dict ={ #directorio de archivos, es posible agregar más
    '.txt': 'documentosTXT',
    '.docx': 'Word',
    '.pdf': 'PDF',
    '.pptx': 'PowerPoint',
    '.jpg': 'imagenes',
    '.png': 'imagenes',
    '.webp': 'imagenes',
    '.rar': 'extraible',
    '.zip': 'extraible',
    '.exe': 'ejecutable'
}

predeterminada ='otros' #si no hay extenciones definidas se almacenan en esta carpeta
carpeta_organizar_ruta = r'C:\Users\User\Documents' #ruta la cual deseas organizar, es un ejemplo de ruta, cambialo si lo quieres usar

archivos = os.listdir(carpeta_organizar_ruta)
for archivo in archivos:
    archivo_origen_ruta = os.path.join(carpeta_organizar_ruta,
                                       archivo) 

    if os.path.isfile(archivo_origen_ruta): #comprobamos si es un archivo
        _, extension = os.path.splitext(archivo)
        nombre_carpeta = extenciones_dict.get(extension.lower(), #buscamos su extención y si esta en el directorio se guarda en la carpeta
                                              predeterminada) #si no existe su extención en el directorio se guarda en predeterminada

        archivo_destino_ruta = os.path.join(carpeta_organizar_ruta,
                                            nombre_carpeta)

        if not os.path.exists(archivo_destino_ruta):
            os.makedirs(archivo_destino_ruta) #si no existe la capeta con la extencion se crea una nueva.

        shutil.move(archivo_origen_ruta, archivo_destino_ruta) #mueve los archivos al destino