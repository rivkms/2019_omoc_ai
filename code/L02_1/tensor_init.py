import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf

sess = tf.Session()

C = [None]*7
C[0] = tf.zeros([3,4], tf.int32)  # [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
C[1] = tf.zeros_like([[1,2,3], [4,5,6]])  # [[0,0,0], [0,0,0]]
C[2] = tf.fill([2,3], 9)  # [[9,9,9], [9,9,9]]
C[3] = tf.constant([[1,3], [2,2], [4,6]])  # [[1,3], [2,2], [4,6]]

C[4] = tf.random_uniform([2,3], -1,1)  
C[5] = tf.random_normal([2,3], 5,2)
C[6] = tf.random_shuffle(C[3])  # shuffles C[3] along its first dimension

V = tf.Variable(C[3])

for i in range(len(C)):
    print ("C[%d]" %i)
    print (sess.run(C[i]))

sess.run(tf.global_variables_initializer())
print ("V")
print (sess.run(V))

print ("Type of C[3]:", type(C[3]))
print ("Type of V:", type(V))
