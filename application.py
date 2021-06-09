# Service main file
from flask import Flask, request, send_file
from flask_cors import CORS
from service import image_ocr, delete_private_files
import os

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
    return send_file('contract.pdf', as_attachment=True)