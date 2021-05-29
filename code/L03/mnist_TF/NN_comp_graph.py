import tensorflow as tf

size_in = 784  # 28**2
size_hidden = 100
size_out = 10

def NN_comp_graph_without_hidden_layer(x_in, y_in):  # input: placeholders
    W = tf.Variable(tf.zeros([size_in, size_out]))
    b = tf.Variable(tf.zeros([size_out]))
    
    y_nn = tf.nn.softmax(tf.matmul(x_in,W) + b)

    correct = tf.equal(tf.argmax(y_nn,1), tf.argmax(y_in,1))
    accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

    cross_entropy = -tf.reduce_sum(y_in*tf.log(y_nn))
    train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    return accuracy, train
    
def NN_comp_graph_with_hidden_layer(x_in, y_in):  # NN with one hidden kayer
    # weight/bias bet'n input layer & hidden layer
    W1 = tf.Variable(tf.zeros([size_in, size_hidden]))
    b1 = tf.Variable(tf.zeros([size_hidden]))
    y1 = tf.sigmoid(tf.matmul(x_in, W1) + b1)   # shape: [?,100]
    # y1 = tf.nn.relu(tf.matmul(x_in, W1) + b1)
    
    # weight/bias bet'n hidden layer & output layer
    W2 = tf.Variable(tf.zeros([size_hidden, size_out]))
    b2 = tf.Variable(tf.zeros([size_out]))
    y_nn = tf.nn.softmax(tf.matmul(y1, W2) + b2)

    correct = tf.equal(tf.argmax(y_nn,1), tf.argmax(y_in,1))
    accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

    cross_entropy = -tf.reduce_sum(y_in*tf.log(y_nn))
    train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    return accuracy, train


NN_comp_graph = NN_comp_graph_without_hidden_layer
# NN_comp_graph = NN_comp_graph_with_hidden_layer
