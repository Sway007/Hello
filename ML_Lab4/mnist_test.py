from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

import tensorflow as tf

import math

#hiddenLayerSize = (int)(math.log2(784) + 4)
hiddenLayerSize = 30
print(hiddenLayerSize)

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([hiddenLayerSize, 10]))
b = tf.Variable(tf.zeros([10]))

WN = tf.Variable(tf.zeros([784, hiddenLayerSize]))
bN = tf.Variable(tf.zeros([hiddenLayerSize]))
yh = tf.nn.sigmoid(tf.matmul(x, WN) + bN)
y = tf.nn.softmax(tf.matmul(yh, W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


# import numpy as np
# import matplotlib.pyplot as plt

# acc = sess.run(correct_prediction, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
# ind, = np.where(acc == False)

# print(ind)

# failedImgs = mnist.test.images[ind]
# testi = 0
# theFaildeImg = failedImgs[testi]
# plt.imshow(theFaildeImg.reshape(28,28))
# print(mnist.test.labels[ind[testi]])
# correct = np.argmax(mnist.test.labels[ind[testi]])
# print('correct: ',correct)

# wrong = y.eval({x: mnist.test.images, y_: mnist.test.labels}, sess)[ind][testi]
# print(wrong)
# print('wrong: ', np.argmax(wrong))

# plt.show()
