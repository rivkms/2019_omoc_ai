import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

figure_width = 28
figure_height = 28
##############################################
def merge_figures(data, offset, n_hor, n_ver):
    border = 2

    whole_width = figure_width*n_hor + border*(n_hor-1)
    whole_height = figure_height*n_ver + border*(n_ver-1)
    L = np.ones((whole_height, whole_width))
    for i in range(n_ver):
        for j in range(n_hor):
            figure = data[offset + i*n_hor + j]
            for p in range(figure_height):
                for q in range(figure_width):
                    u = i*(figure_height+border) + p
                    v = j*(figure_width+border) + q
                    L[u][v] = figure[p][q]
    return L
            
##############################################
def show_mnist_data():
    mnist =  tf.keras.datasets.mnist.load_data()  # ~/.keras/datasets/mnist.npz
    (x_train, y_train), _ = mnist
    x_train = x_train / 255.0
    print(x_train.shape, y_train.shape, y_train[:10])

    n_hor = 30
    n_ver = 20
    step = n_hor * n_ver
    offset = 0
    while offset + step <= step:  # len(x_train):
        plt.imshow(merge_figures(x_train, offset, n_hor, n_ver), cmap=cm.Greys_r)
        # plt.savefig("mnist_data.png", dpi=300)
        
        for i in range(n_ver):
            for j in range(n_hor):
                print(y_train[offset + i*n_hor + j], end=" ")
            print()
        plt.xticks([]); plt.yticks([]); plt.show()
        
        offset += step

show_mnist_data()