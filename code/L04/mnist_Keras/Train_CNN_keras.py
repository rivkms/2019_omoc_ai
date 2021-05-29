import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Convolution2D, MaxPooling2D, Dropout, Flatten

# https://keras.io/layers/convolutional/

##########################################################    
def CNN_model():
    model = Sequential()
    
    # 1st convolution-pooling layer
    model.add(Convolution2D(filters=32, kernel_size=(5,5), strides=(1,1), \
                            input_shape=(28,28,1)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    # print(model.output_shape)   # (None, 12, 12, 32)
    
    # 2nd convolution-pooling layer
    model.add(Convolution2D(filters=64, kernel_size=(5,5), strides=(1,1)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    # print(model.output_shape)   # (None, 4, 4, 64)

    model.add(Flatten())
    # print(model.output_shape)   # (None, 1024)

    # 1st full-connection layer
    model.add(Dense(1000))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))  
    # print(model.output_shape)   # (None, 1000)

    # 2nd full-connection layer
    model.add(Dense(10))
    model.add(Activation("softmax"))
    # print(model.output_shape)   # (None, 10)

    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adadelta')

    return model
    
##########################################################    
def train(x_train, y_train):
    model = CNN_model()

    model.fit(x_train, y_train, batch_size=100, epochs=8, verbose=1, validation_split=0.1)
    score = model.evaluate(x_train, y_train, batch_size=100, verbose=1)
    print("Accuracy:", score[1])

    model.save("./model/mnist_CNN_model.h5")
    
##############################################
def run():
    mnist = keras.datasets.mnist.load_data()  # ~/.keras/datasets/mnist.npz
    (x_train, y_train), (_, _) = mnist
    x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
    y_train = keras.utils.to_categorical(y_train)
    # print(x_train.shape, y_train.shape)  # (60000,28,28,1)  (60000,10)
    train(x_train, y_train)
    
run()