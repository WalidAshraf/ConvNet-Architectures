## 1	Introduction

This is a simple implementation for ResNet as specified in the ResNet paper. I implemented it with with tensorflow on my own machine.

## 2	Dataset

For training the model I used Cifar 10 Dataset which contains 60000 images, 49000 for training, 1000 for validation and 10000 for testing. All images are of fixed size 32 * 32 * 3. No preprocessing is done except for subtracting the mean over the training set from all images.

## 3 	The Architecture

All convolutional layers used are with 3 * 3 filter size. The basic Residual block consists of 3 convolutional layers with the input of the block added to the output of the last conv layer before the activation. A RELU activation is used after every convolution. A batch normalization layer is used just after a convolution and befor RELU. DownSampling is done by a ConvLayer with a stride of two. The full architecture is as follows:<br />
	1. ConvLayer with 16 filters.<br />
	2. ResBlock with 16 filters.<br />
	3. ConvLayer with 32 filters and stride of 2.<br />
	4. ResBlock with 32 filters.<br />
	5. ConvLayer with 64 filters and a stride of 2.<br />
	6. ResBlock with 64 filters.<br />
	7. AvgPooling layer with pool size 2 * 2 and strides 2 * 2.<br />
	8. A fully connected layer with 10 units with a softmax activation for cassification task.<br />

## 4	Details of Training

All weights are initialized with xavier initialization and biases are initialized to zeroes. An L2 regularizer is used with 0.0001 L2 penalty. No data augmentation is done although it would help reducing the varience. An SGD Optimizer is used with a momentum of 0.9. The learning Rate is initialized to be 0.001 and is divided by 10 after every 15 epochs. A batch size of 256 is used. The training process held for about 100 epochs. Here is a figure shows the ralation between Training, Validation accuracy with the number of epochs:<br />

![](https://github.com/omarsgalal/ConvNet-Architectures/blob/master/ResNet/train_val_acc2.jpg)

## 4	Results

While training the model the best validation accuracy was about 70.6% and that model gets a test accuracy of 69.8%.
