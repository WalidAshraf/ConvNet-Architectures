import numpy as np
import matplotlib as plt
from scipy import misc
import os

def getNumImages(path):
    cs = os.listdir(path)
    num = 0
    for c in cs:
        num += len(os.listdir(path + '/' + c))
    return num


def resizeImage(img, H, W):
    return misc.imresize(img, (H, W), interp='cubic')


def loadDataSet(path):
    classes = os.listdir(path)
    classes_names = {}
    num_images = getNumImages(path)
    X = np.empty((num_images, 224, 224, 3), dtype=np.float32)
    y = np.empty((num_images,), dtype=np.uint8)
    j = 0
    for i, c in enumerate(classes):
        classes_names[i] = c
        imgs = os.listdir(path + '/' + c)
        for img_name in imgs:
            img = misc.imread(path + '/' + c + '/' + img_name, mode='RGB')
            img = resizeImage(img, 224, 224)
            X[j] = img
            y[j] = i
            j += 1
    return X, y, classes_names


def shuffleDataset(X, y):
    s = np.arange(X.shape[0])
    np.random.shuffle(s)
    X = X[s]
    y = y[s]
    return X, y


def getDataSet(path, num_val=1000, num_test=1000):
    X, y, classes_dic = loadDataSet(path)
    X, y = shuffleDataset(X, y)
    
    num_all = X.shape[0]
    num_train = num_all - num_val - num_test
    
    mask = range(num_train)
    X_train = X[mask]
    y_train = y[mask]
    
    mask = range(num_train, num_train + num_val)
    X_val = X[mask]
    y_val = y[mask]
    
    mask = range(num_train + num_val, num_train + num_val + num_test)
    X_test = X[mask]
    y_test = y[mask]
    
    mean = np.mean(X_train, axis=0, dtype=np.float32)

    X_train -= mean
    X_val -= mean
    X_test -= mean
    
    return X_train, y_train, X_val, y_val, X_test, y_test, classes_dic, mean


def deprocessImage(img, mean):
	return img + mean