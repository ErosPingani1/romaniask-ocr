# Service main file
from flask import Flask, request
from app.service import image_ocr, delete_image

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Server is running'

@app.route('/imageocr', methods=['POST'])
def recognize_image():
    imageB64 = request.get_json()['image']
    ocr = image_ocr(imageB64)
    delete_image()
    return ocr
    