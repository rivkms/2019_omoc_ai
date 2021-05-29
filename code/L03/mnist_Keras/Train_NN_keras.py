import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

# https://keras.io/getting-started/sequential-model-guide/

##########################################################    
size_in = 784  # 28**2
size_hidden = 100
size_out = 10

def NN_model_without_hidden_layer():
    model = Sequential()
    model.add(Dense(units=size_out, input_dim=size_in, activation="softmax"))
    model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="sgd")
    return model
    
def NN_model_with_hidden_layer():
    model = Sequential()
    model.add(Dense(units=size_hidden, input_dim=size_in, activation='sigmoid'))
    model.add(Dense(units=size_out, activation='softmax'))
    model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="sgd")
    return model
    
##########################################################    
def train(x_train, y_train):
    model = NN_model_without_hidden_layer()
    # model = NN_model_with_hidden_layer()

    model.fit(x_train, y_train, batch_size=100, epochs=15, verbose=1)
    score = model.evaluate(x_train, y_train, batch_size=100, verbose=1)
    print("Accuracy:", score[1])

    model.save("./model/mnist_NN_model.h5")
    
##############################################
def run():
    mnist = keras.datasets.mnist.load_data()  # ~/.keras/datasets/mnist.npz
    (x_train, y_train), (_, _) = mnist
    x_train = x_train.reshape(-1, 28*28) / 255.0
    y_train = keras.utils.to_categorical(y_train)
    # print(x_train.shape, y_train.shape)  # (60000,784)  (60000,10)
    train(x_train, y_train)
    
run()