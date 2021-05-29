import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
import keras
from keras.models import load_model

##########################################################    
def test(x_test, y_test):
    model = load_model("./model/mnist_CNN_model.h5")
    
    score = model.evaluate(x_test, y_test, batch_size=100, verbose=1)
    print("\nAccurary of trained model against test data:", score[1])

    n_random_test = 5
    print("\nRandom test with %d data.." %n_random_test)
    idx = np.random.choice(x_test.shape[0], n_random_test)  # 5 indices
    v = model.predict(x_test[idx])
    y = model.predict_classes(x_test[idx])
    np.set_printoptions(precision=1)
    for k in range(n_random_test):
        i = idx[k]
        print("="*30 + "\nRandom test %d:" %i)
        print("actual: %d,  predicted: %d" %(np.argmax(y_test[i]), y[k]))
        # print("predicted softmax:", v[k])
    
##############################################
def run():
    mnist = keras.datasets.mnist.load_data()  # ~/.keras/datasets/mnist.npz
    (_, _), (x_test, y_test) = mnist
    x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
    y_test = keras.utils.to_categorical(y_test)
    test(x_test, y_test)
    
run()