---
layout: project
type: project

title: Quran Tajweed Rules Recognition
permalink: projects/tajweed-rule
modal-id: 6
image: images/thumbnails/tajweed-rule.jpg
galleryImg: /images/tajweed-rule
videoUrl: https://drive.google.com/file/d/1ZP2N09kOzt2V6csJlu4NogLvtbJfZf7L/preview?resourcekey=null
date: April - September 2020
labels:
    - computer vision
    - image processing
    - OCR
    - CNN
    - dataset
    - python
    - tensorflow
    - pytorch
    - web
    - flask
    - javascript
    - html/css
summary: Document processing using image of Quran verse for recognizing the tajweed rules type and it's location.
# describe-opening: <br>This project was my final project of my undergraduate studies at Universitas Gadjah Mada, majoring in Electronics and Instrumentation, Department of Computer Science and Electronics. The aim of my final project is to develop a method for recognizing the reading law contained in the verses of the Quran with input in the form of images and to create a web-based user interface to display the results of each process. This project consists of the following work
describe-opening: <br>This project was my undergraduate final project at Universitas Gadjah Mada, majoring in Electronics and Instrumentation (Department of Computer Science and Electronics). The goal was to develop a method for recognizing Quranic reading laws from verse images and to build a web-based interface to display each step of the processing pipeline. This project consists of the following work
describe-content:
    - Built a dataset of Arabic characters from cropped images of different variations of Arabic letters in 10 types of fonts. Implemented by creating a simple tool for automatic cropping and saving with a user interface created using the PySimpleGUI library in Python.
    - Applied image processing techniques to extract the characteristics of Arabic letters in the image of Al-Quran verse needed for the purposes of determining the reading law, including character detection that marks the occurrence of the reading law by using template matching, designing algorithms for character segmentation using image pixel values, and performing Arabic character recognition using Convolutional Neural Network (CNN) from the created dataset.
    - Developed a web-based UI using the Flask framework to integrate reading law recognition methods built in Python with a user interface built in html, css and javascript.
describe-closing: <strong>Tools Used:</strong> Python, Tensorflow, OpenCV, Flask, PySimpleGUI, Numpy, Pandas, Javascript, HTML/CSS

---
