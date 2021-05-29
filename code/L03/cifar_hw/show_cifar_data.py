import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

figure_width = 32
figure_height = 32
##############################################
def merge_figures(data, offset, n_hor, n_ver):
    border = 2

    whole_width = figure_width*n_hor + border*(n_hor-1)
    whole_height = figure_height*n_ver + border*(n_ver-1)
    L = np.zeros((whole_height, whole_width, 3))
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
def show_cifar_data():
    cifar =  tf.keras.datasets.cifar10.load_data()  # ~/.keras/datasets/cifar...
    (x_train, y_train), _ = cifar
    x_train = x_train.astype(np.float32) / 255.0
    y_train = y_train.reshape(-1)
    print(x_train.shape, y_train.shape, y_train[:10])
    
    n_hor = 15
    n_ver = 10
    step = n_hor * n_ver
    offset = 0
    while offset + step <= step:  # len(x_train):
        plt.imshow(merge_figures(x_train, offset, n_hor, n_ver)) #, cmap=cm.Greys_r)
        # plt.savefig("cifar_data.png", dpi=300)
        
        for i in range(n_ver):
            for j in range(n_hor):
                print(y_train[offset + i*n_hor + j], end=" ")
            print()
        plt.xticks([]); plt.yticks([]);
        plt.show()
        
        offset += step

show_cifar_data()
