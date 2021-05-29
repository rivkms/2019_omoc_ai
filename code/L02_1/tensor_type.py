import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf

P = [ [1,3], [2,2], [4,6] ]
C = tf.constant(P)
V = tf.Variable(P)

print ("C:", C, " / shape:", C.get_shape())
print ("V:", V, " / shape:", V.get_shape())
print

#############################

C = tf.expand_dims(C, 0)
V = tf.expand_dims(V, 1)

print ("C:", C, " / shape:", C.get_shape())
print ("V:", V, " / shape:", V.get_shape())
