import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

# https://keras.io/getting-started/sequential-model-guide/

##########################################################    
size_in = 3072  # 32*32*3
size_hidden1 = 3000
size_hidden2 = 2000
size_out = 10

def NN_model():
    # IMPLEMENT HERE!!
    
    
##########################################################    
def train(x_train, y_train):
    model = NN_model()

    model.fit(x_train, y_train, batch_size=100, epochs=15, verbose=1, validation_split=0.1)
    score = model.evaluate(x_train, y_train, batch_size=100, verbose=1)
    print("Accuracy:", score[1])

    model.save("./model/cifar_NN_model.h5")
    
##############################################
def run():
    cifar = keras.datasets.cifar10.load_data()  # ~/.keras/datasets/cifar...
    (x_train, y_train), (_, _) = cifar
    x_train = x_train.reshape(-1, 32*32*3)
    y_train = keras.utils.to_categorical(y_train)
    # print(x_train.shape, y_train.shape)  # (50000,3072)  (50000,10)
    train(x_train, y_train)
    
run()