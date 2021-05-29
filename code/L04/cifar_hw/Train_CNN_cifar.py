import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Convolution2D, MaxPooling2D, Dropout, Flatten

# https://keras.io/layers/convolutional/

##########################################################    
def CNN_model():
    # IMPLEMENT HERE!!
    
##########################################################    
def train(x_train, y_train):
    model = CNN_model()

    model.fit(x_train, y_train, batch_size=100, epochs=20, verbose=1, validation_split=0.1)
    score = model.evaluate(x_train, y_train, batch_size=100, verbose=1)
    print("Accuracy:", score[1])

    model.save("./model/cifar_CNN_model.h5")
    
##############################################
def run():
    cifar = keras.datasets.cifar10.load_data()  # ~/.keras/datasets/cifar...
    (x_train, y_train), (_, _) = cifar   # 
    y_train = keras.utils.to_categorical(y_train)
    # print(x_train.shape, y_train.shape)  # (50000,32,32,3)  (5000,10)
    train(x_train, y_train)
    
run()