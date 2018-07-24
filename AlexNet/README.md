##1	Introduction

This is an implementation for AlexNet as specified in the AlexNet paper but with slight modifications. I implemented it with two models one with tensorflow and the other with keras.

##2	Dataset

For training the model I used Caltech 101 dataset. It consists of pictures of objects belonging to 101 categories. About 40 to 800 images per category. Most categories have about 50 images. Collected in September 2003 by Fei-Fei Li, Marco Andreetto, and Marc 'Aurelio Ranzato.  The size of each image is roughly 300 x 200 pixels. The total number of images is about 9125 images for all categories which is considered small for training a ConvNet like AlexNet and this small number increases the overfitting of the network but I used it to fit my PC resources :D.

The input for AlexNet is 224 * 224 * 3 but the images is variable sized so I just resized every image to match the input shape and subtracted the mean over the training set from the images. No other preprocessing is done.

##3 	The Architecture

I used the same architecture as AlexNet with 5 Convolutional layers and 3 Fully Connected ones. For local response layer I replaced it with a batch normalization layer before the RELU Activation in the first two layers. Also for the model implemented with tensorflow I putted 3 additional dropout layers after  the third, fourth and fifth convlutional layers trying to decrease overfitting.

##4	Pretrained Models

I included pretrained models one with tensorflow and the other with keras. The one with tensorflow achives an accuracy about 53% on the test set , 55 % on the validation set and 95% on the training set which shows that there is a huge overfitting on the training set. One of solution I will try later is data augmentation but my problem with it that it will increase the data by a huge factor and my resources might not be able to fit this hige data. The one trained with keras model achives about 33% accuracy on the test set which is not fine. I am still facing some problems with the model implemented with keras as its learning is two slow. 
