# Service main file
from flask import Flask, request, send_file
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
    contractInfo = request.get_json()['contractInfo']
    image_ocr(imageB64, contractInfo)
    delete_private_files()
    with open('contract.pdf', 'rb') as contract:
        return send_file(contract, attachment_filename='contract.pdf')
    