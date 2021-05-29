import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(num_points):
    x_data = np.random.random(num_points) * 9 + 1
    x_data.sort()
    y_data = 3.5*np.log(x_data) + 7.5 + np.random.normal(0, 0.5, num_points)
    print (x_data.dtype, y_data.dtype)
    return x_data.astype(np.float32), y_data.astype(np.float32)

#############################################
def regression(x_data, y_data):
    a = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

    # IMPLEMENT HERE!!
    
    return sess.run(a), sess.run(b)
            
#############################################
def run():
    num_points = 1000
    x_data, y_data = generate_random_points(num_points)

    a, b = regression(x_data, y_data)  # y = alog(x) + b
    plt.plot(x_data, y_data, 'ro')
    plt.plot(x_data, a*np.log(x_data) + b)
    plt.show()

run()
