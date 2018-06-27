import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils

print('ok')
seed = 7
numpy.random.seed(seed)

#加载数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# reshape to be [samples][channels][width][height]
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28).astype('float32')

# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255

# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

print(X_train.shape)
print(x_test.shape)
print(num_classes)

import matplotlib.pyplot as plt # matplotlib的使用，subplot是子视图 里面有3个数分别是列，行，第几个视图。

plt.subplot(321)
plt.imshow(x_train[0], cmap=plt.get_cmap('gray'))
plt.subplot(322)
plt.imshow(x_train[1], cmap=plt.get_cmap('gray'))
plt.subplot(323)
plt.imshow(x_train[2], cmap=plt.get_cmap('gray'))
plt.subplot(324)
plt.imshow(x_train[3], cmap=plt.get_cmap('gray'))
plt.subplot(325)
plt.imshow(x_train[4], cmap=plt.get_cmap('gray'))
# show the plot
plt.show()