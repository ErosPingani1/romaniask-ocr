import os
import cv2
import base64
import pytesseract
import numpy as np

def image_ocr(image):
    base64_to_img(image)
    return preprocess_image()

# Image decoded from base64 to .png and saved momentarily
def base64_to_img(image):
    imgdata = base64.b64decode(image.split(',')[1])
    filename = 'id.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)

# Image preprocessing, loaded from the saved file in black and white (0)
def preprocess_image():
    img = cv2.imread('id.png', 0)
    return get_required_values(img)

# Method that populates the response with all the required fields
def get_required_values(image):
    config = '--oem 3 --psm 6'
    height, width = image.shape

    cnp_img = image[int((height / 100) * 18): int((height / 100) * 24), int((width / 100) * 34): int((width / 100) * 58)]
    cnp = clean_string(pytesseract.image_to_string(cnp_img, lang='eng', config=config))

    address_img = image[int((height / 100) * 57): int((height / 100) * 63), int((width / 100) * 30): int((width / 100) * 85)]
    address = clean_string(pytesseract.image_to_string(cv2.resize(address_img, None, fx=2, fy=2), lang='ron', config=config))
    
    issued_by_img = issued_by = image[int((height / 100) * 70): int((height / 100) * 76), int((width / 100) * 30): int((width / 100) * 58)]
    issued_by = clean_string(pytesseract.image_to_string(cv2.resize(issued_by_img, None, fx=2, fy=2), lang='ron', config=config))

    mrz_code_img = image[int((height / 100) * 75): int((height / 100) * 95), int((width / 100) * 5): int((width / 100) * 95)]
    mrz_code = pytesseract.image_to_string(mrz_code_img, lang='eng', config=config)
    client_info = info_from_mrz(mrz_code)

    return { 'cnp': cnp, 'id': client_info['id'], 'lastname': client_info['lastname'], 'name': client_info['name'], 'address': address, 'issued_by': issued_by }

# Metod that cleans the not-mrz strings from all the undesired elements (newlines and useless chars)
def clean_string(string):
    return string.replace('<', '(').replace('——', '').replace('\n\f', '').strip() # Wrong chars and newlines replacement

# Obtaining of required data from MRZ code
def info_from_mrz(mrz):
    info = list(filter(None, mrz.replace(" ", "").replace('\n', '').replace('\f', '').strip().split('<'))) # The list has to be filtered in order to remove the whitespaces (<<)
    name = generate_name_from_mrz(info)
    return { 
        'lastname': info[0].replace('IDROU', '').capitalize(), 
        'name': name.strip(), 
        'id': { 
            'serial': info[len(info) - 2][0:2], 
            'number': info[len(info) - 2][2:len(info[len(info) - 2])]
        }
    }

# Name composing from MRZ (a name can consist of more than 1 string)
def generate_name_from_mrz(ci):
    ci_name = ''
    for n in range(1, (len(ci) - 2)): # The name is composed of all the values in the array up to the last two
        ci_name += ' ' + ci[n].capitalize()
    return ci_name

# Image removal from storage
def delete_image():
    os.remove('id.png')