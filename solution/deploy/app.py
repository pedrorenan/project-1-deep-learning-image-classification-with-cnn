import requests
import json
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify, render_template, send_from_directory
import os

app = Flask(__name__)

# CIFAR-10 class names
class_names = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

# Ensure the uploads directory exists within the app directory
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((32, 32))
    image = np.array(image) / 255.0
    return image

def get_prediction(image_path):
    url = 'http://localhost:8501/v1/models/cifar10_cnn_model:predict'
    image = preprocess_image(image_path)
    data = json.dumps({"instances": image[None, ...].tolist()})
    headers = {"content-type": "application/json"}
    response = requests.post(url, data=data, headers=headers)
    predictions = json.loads(response.text)['predictions']
    return predictions

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'files[]' not in request.files:
        return 'No file part'
    files = request.files.getlist('files[]')
    results = []
    for file in files:
        if file and file.filename != '':
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            predictions = get_prediction(file_path)
            results.append((file.filename, predictions))
    return render_template('result.html', results=results, class_names=class_names)
        
@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv("PORT", default=5000))
