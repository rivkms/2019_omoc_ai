import tensorflow as tf

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

########################################################################3
def CNN_comp_graph(x_in, y_in, keep_prob):  # input: placeholders
    x_in = tf.reshape(x_in, [-1,28,28,1])

    # 1st convolution-pooling layer
    W_conv1 = weight_variable([5,5,1,32])
    b_conv1 = bias_variable([32])

    c1 = tf.nn.conv2d(x_in, W_conv1, strides=[1,1,1,1], padding='SAME')
    conv1 = tf.nn.relu(c1 + b_conv1)
    pool1 = tf.nn.max_pool(conv1, ksize=[1,2,2,1],
                           strides=[1,2,2,1], padding='SAME')

    # 2nd convolution-pooling layer
    W_conv2 = weight_variable([5,5,32,64])
    b_conv2 = bias_variable([64])

    c2 = tf.nn.conv2d(pool1, W_conv2, strides=[1,1,1,1], padding='SAME')
    conv2 = tf.nn.relu(c2 + b_conv2)
    pool2 = tf.nn.max_pool(conv2, ksize=[1,2,2,1],
                           strides=[1,2,2,1], padding='SAME')

    print ("c1-shape:", c1.shape)
    print ("conv1-shape:", conv1.shape)
    print ("pool1-shape:", pool1.shape)
    print ("c2-shape:", c2.shape)
    print ("conv2-shape:", conv2.shape)
    print ("pool2-shape:", pool2.shape)
    
    pool2_flat = tf.reshape(pool2, [-1, 7*7*64])

    # 1st full-connection layer
    W_fc1 = weight_variable([7*7*64, 1024])
    b_fc1 = bias_variable([1024])

    fc1 = tf.nn.relu(tf.matmul(pool2_flat, W_fc1) + b_fc1)

    fc1_drop = tf.nn.dropout(fc1, keep_prob)

    # 2nd full-connection layer
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])

    y_conv = tf.nn.softmax(tf.matmul(fc1_drop, W_fc2) + b_fc2)

    # cost function for testing
    correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_in,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    
    # cost function for training
    cross_entropy = -tf.reduce_sum(y_in*tf.log(y_conv))
    train = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

    return accuracy, train
