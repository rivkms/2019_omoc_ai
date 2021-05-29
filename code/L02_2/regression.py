import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(num_points):
    x_data = np.random.normal(0.0, 0.55, num_points) 
    x_data.sort()
    y_data = 0.1*x_data + 0.3 + np.random.normal(0.0, 0.03, num_points)
    return x_data, y_data

#############################################
def regression(x_data, y_data):
    W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    b = tf.Variable(tf.zeros([1]))
    y = W * x_data + b

    cost = tf.reduce_mean(tf.square(y - y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(cost)

    init = tf.global_variables_initializer()

    sess = tf.Session()
    sess.run(init)

    for step in range(200):
        sess.run(train)  # minimize cost
        if step % 10 == 0:			
            print (step, sess.run(W), sess.run(b), sess.run(cost))
    
    return sess.run(W), sess.run(b)
            
#############################################
def run():
    num_points = 1000
    x_data, y_data = generate_random_points(num_points)

    a, b = regression(x_data, y_data)  # y = ax+b
    plt.plot(x_data, y_data, 'ro')
    plt.plot(x_data, a * x_data + b)
    plt.show()

run()
