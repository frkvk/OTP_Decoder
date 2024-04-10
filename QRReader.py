import cv2
from pyzbar.pyzbar import decode
from urllib.parse import unquote

def leer_codigo_qr(imagen):
    # Lee la imagen
    img = cv2.imread(imagen)

    # Convierte la imagen a escala de grises
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Decodifica los códigos QR en la imagen
    qr_codes = decode(gray_img)

    # Itera sobre los códigos QR decodificados
    for qr_code in qr_codes:
        # Extrae la información del código QR
        qr_data = qr_code.data.decode('utf-8')
        qr_data_decodificado = unquote(qr_data)
        # Imprime la información del código QR
        print("Contenido del código QR:", qr_data_decodificado)

# Nombre de la imagen JPG que contiene el código QR
imagen_jpg = 'X:\\Proyect\\test.jpg'

# Llama a la función para leer el código QR
leer_codigo_qr(imagen_jpg)
