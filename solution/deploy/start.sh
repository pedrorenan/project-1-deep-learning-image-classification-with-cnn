#!/bin/bash

# Start Flask app in the background
python3 /app/app.py &

# Start TensorFlow Serving
tensorflow_model_server --rest_api_port=8501 --model_name=cifar10_cnn_model --model_base_path=/models/cifar10_cnn_model
Make sure to give it execute permissions: