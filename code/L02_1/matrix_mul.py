import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf

A = [ [1,1], [1,1] ]
B = [ [1,1], [1,1] ]

P = tf.matmul(A, B)    # matrix multiplication
Q = tf.multiply(A, B)  # 2x2 pairwise multiplication

sess = tf.Session()

print (sess.run(P))
print (sess.run(Q))

        

