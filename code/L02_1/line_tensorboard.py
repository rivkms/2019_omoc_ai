import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

add = X+Y
mul = X*Y

# step 1: select node
add_hist = tf.summary.scalar("add_scalar", add)
mul_hist = tf.summary.scalar("mul_scalar", mul)

# step 2: collect summary
merged = tf.summary.merge_all()
# merged = tf.merge_summary([add_hist, mul_hist])

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    
    # step 3: generate writer
    writer = tf.summary.FileWriter("./line_tboard", sess.graph)

    for step in range(100):
        # step 4: add node
        summary = sess.run(merged, feed_dict={X:step*1.0, Y:2.0})
        writer.add_summary(summary, step)

################################################
# Run "python3 line_tensorboard.py" in terminal
# Run "tensorboard --logdir=line_tboard" in terminal"
# Open firefox with address 127.0.1.1:6006