import os
import base64
from ocr import preprocess_image

def image_ocr(image):
    base64_to_img(image)
    # Creazione PDF da asset
    # Eliminazione file immagine storata
    return preprocess_image()

# Image decoded from base64 to .png and saved momentarily
def base64_to_img(image):
    imgdata = base64.b64decode(image.split(',')[1])
    filename = 'id.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)

# Image removal from storage
def delete_image():
    os.remove('id.png')