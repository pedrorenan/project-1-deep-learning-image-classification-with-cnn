# Deep Learing Image Classification Project

This is a simple application thats use TensorFlow Serve to deploy a model that was trained, using CIFAR-10 dataset, to classify images and Flask to create a simple web interface to interact with the model.

## Pre-requisites

- Docker 

## How to run

1. Clone this repository
2. Run the following command to build the docker image:

```bash
docker build -t image-classification .
```

3. Run the following command to start the container:

```bash
# on macOS 5000 is being used by AirDrop, so we need to use another port and it will works fine on Linux and Windows.

docker run -p 5005:5000 image-classification
```

4. Access the web interface at http://localhost:5005

## How to use

1. Access the web interface at http://localhost:5005

2. Click on the "Choose Files" button to select an or more images to classify
    Ten images are available here: [images](https://github.com/pedrorenan/project-1-deep-learning-image-classification-with-cnn/tree/main/solution/samples)

3. Click on the "Upload" button to classify the images

4. The result will be displayed below the "Upload" button