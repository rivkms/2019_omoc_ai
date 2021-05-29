import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(num_points):
    x_data, y_data = [], []
    for i in range(num_points):
        x = np.random.normal(0.0, 0.55)
        y = x * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
        x_data.append(x)
        y_data.append(y)
        
    return x_data, y_data

#############################################
def regression(x_data, y_data):
    W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    b = tf.Variable(tf.zeros([1]))
    y = W * x_data + b

    cost = tf.reduce_mean(tf.square(y - y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(cost)

    cost_hist = tf.summary.scalar("cost_scalar", cost)
    merged = tf.summary.merge_all()
    # merged = tf.merge_summary([cost_hist])
    
    init = tf.global_variables_initializer()
    
    sess = tf.Session()
    sess.run(init)
    
    writer = tf.summary.FileWriter("./regression_tboard", sess.graph)
    
    for step in range(101):
        sess.run(train)  # minimize cost
        if step % 10 == 0:			
            print (step, sess.run(W), sess.run(b), sess.run(cost))
            
            summary = sess.run(merged)
            writer.add_summary(summary, step)
    
    return sess.run(W), sess.run(b)
            
#############################################
def run():
    num_points = 1000
    x_data, y_data = generate_random_points(num_points)

    a, b = regression(x_data, y_data)  # y = ax+b

run()

################################################
# Run "python3 regression_tensorboard.py" in terminal
# Run "tensorboard --logdir=regression_tboard" in terminal"
# Open firefox with address 127.0.1.1:6006