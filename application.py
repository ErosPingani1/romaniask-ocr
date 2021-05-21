# Service main file
from flask import Flask, request
from flask_cors import CORS
from service import image_ocr, delete_private_files

app = Flask(__name__) 
CORS(app)

@app.route('/')
def homepage():
    return 'Server is running'

@app.route('/imageocr', methods=['POST'])
def recognize_image():
    imageB64 = request.get_json()['image']
    contract_info = request.get_json()['contract_info']
    image_ocr(imageB64, contract_info)
    delete_private_files()
    '''return ocr'''
    