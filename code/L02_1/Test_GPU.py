import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
import datetime

def build_comp_graph():
    power = 2
    n = 5000
    A = np.random.rand(n, n).astype('float32')
    P = A
    for i in range(power):
        P = tf.matmul(P, A)
    return P

def test(numGPU):
    if numGPU == 0:
        gpu  = ["/cpu:0"]
    else:
        gpu = [ "/gpu:"+str(i)  for i in range(numGPU) ]

    M = []
    for g in gpu:
        with tf.device(g):
            P = build_comp_graph()
        M.append(P)

    with tf.device("cpu:0"):
        sum = tf.add_n(M)

    t1 = datetime.datetime.now()
    with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
        sess.run(sum)
    t2 = datetime.datetime.now()

    if numGPU == 0:
        print ("CPU only:", t2-t1)
    else:
        print (str(numGPU) + "GPU:", t2-t1)
    print ("=" * 30)

##############################################
numGPU = 4
test(numGPU)
#for g in range(1,numGPU+1): test(g)
    
