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
describe-opening: This project was my final project of undergraduate study at Universitas Gadjah Mada majoring in Electronics and Instrumentation, Department of Computer Science and Electronics. The aim of my final project is to develop a method for recognizing the reading law contained in the verses of Quran with input in the form of image and creating a web-based user interface to display the results of each process. This project consist of the following work
describe-content:
    - Built a dataset of Arabic characters from cropped ​​images of various variations of Arabic letters in 10 types of fonts. Implemented by creating a simple tool for automatic cropping and saving with an user interface created using PySimpleGUI library in python.
    - Performed image processing to be able to get the characteristics of Arabic letters in the image of the Al-Quran verse needed for the purposes of determining the law of reading, including character detection that marks the occurrence of the reading law by using template matching, designing algorithms for character segmentation by utilizing image pixel values ​​and perform Arabic character recognition using Convolutional Neural Network (CNN) from the created dataset.
    - Built a web-based UI using Flask framework to be able to integrate reading law recognition methods created using python with an user interface created using html, css, and javascript.
describe-closing:

---