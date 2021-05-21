import os
import base64
from ocr import preprocess_image
from pdf import generate_pdf_contract

def image_ocr(image, contract_info):
    base64_to_img(image)
    id_values = preprocess_image()
    generate_pdf_contract(id_values, contract_info)

# Image decoded from base64 to .png and saved momentarily
def base64_to_img(image):
    imgdata = base64.b64decode(image.split(',')[1])
    filename = 'id.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)

# ID image and compiled documents deleted from storage
def delete_private_files():
    os.remove('id.png')
    os.remove('contract_edit.html')