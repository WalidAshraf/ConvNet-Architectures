## 1	Introduction

This is an implementation for VGGNet as specified in the VGGNet paper. I implemented it with with tensorflow on my own machine.

## 2	Dataset

For training the model I used Caltech 101 dataset. It consists of pictures of objects belonging to 101 categories. About 40 to 800 images per category. Most categories have about 50 images. Collected in September 2003 by Fei-Fei Li, Marco Andreetto, and Marc 'Aurelio Ranzato.  The size of each image is roughly 300 x 200 pixels. The total number of images is about 9125 images for all categories which is considered small for training a ConvNet and this small number increases the overfitting of the network but I used it to fit my PC resources :D.

The input for VGGNet is 224 * 224 * 3 but the images is variable sized so I just resized every image to match the input shape and subtracted the mean over the training set from the images. No other preprocessing is done.

## 3 	The Architecture

I used the same architecture as VGG-13 with 13 weight layers 10 of them are ConvLayers with fixed filter size 3 * 3 and strides of 1 and after every two layers a maxpooling layer is used with pool size of 2 * 2 and strides of 2 * 2. The three last layers are FullyConnected ones with dimensions 4096, 4096, 102 respectively. A RELU activation is used after wight layers and dropout layers after the first FC layers to reduce over fitting.

## 4	Pretrained Models

I trained a model on this dataset that achives 59% validation accuracy and 54.6% for test accuracy. This model achieves a training accuracy more than 90% which shows there is a huge over fitting caused by the small number of the training data. I suppose doing data augmentation will reduce alot of this overfitting but due to my PC resources a huge number of images will be a problem.
