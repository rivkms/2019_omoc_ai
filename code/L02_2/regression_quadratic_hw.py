import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(num_points):
    x_data = np.random.normal(5, 5, num_points) 
    x_data.sort()
    y_data = 0.1*x_data*x_data - x_data + 2 + np.random.normal(0, 1, num_points)
    return x_data, y_data

#############################################
def regression(x_data, y_data):
    a = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    c = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

    # IMPLEMENT HERE!!
    
    return sess.run(a), sess.run(b), sess.run(c)
            
#############################################
def run():
    num_points = 1000 # 1000
    x_data, y_data = generate_random_points(num_points)

    a, b, c = regression(x_data, y_data)  # y = ax^2+bx+c
    print(a, b, c)
    plt.plot(x_data, y_data, 'ro')
    plt.plot(x_data, a*x_data*x_data + b*x_data + c)
    plt.show()

run()
