# Base image for TensorFlow Serving
FROM tensorflow/serving:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && apt-get clean

# Install Flask and other dependencies
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Copy the saved model to the serving directory
COPY /final_cnn_model /models/cifar10_cnn_model/1

# Copy Flask app files
COPY app.py /app/app.py
COPY templates /app/templates
COPY uploads /app/uploads

# Copy the startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Set environment variables
ENV MODEL_NAME=cifar10_cnn_model

# Expose TensorFlow Serving port and Flask port
EXPOSE 5000

# Command to run the start.sh script
ENTRYPOINT ["/bin/bash", "/start.sh"]
