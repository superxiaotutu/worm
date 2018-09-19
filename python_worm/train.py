import tensorflow as tf
import tensorflow.contrib.slim as slim
import tensorflow.contrib.slim.nets as nets
import PIL
import numpy as np
import V3

sess = tf.InteractiveSession()

height, width = 299, 299
X = tf.placeholder(tf.float32, [None, height, width, 3])
Y = tf.placeholder(tf.float32, [None, 79])

def inception(preprocessed, reuse = tf.AUTO_REUSE):
    # preprocessed = tf.multiply(tf.subtract(tf.expand_dims(image, 0), 0.5), 2.0)
    arg_scope = nets.inception.inception_v3_arg_scope()
    with slim.arg_scope(arg_scope):
        logits, end_point = V3.inception_v3(preprocessed, 79, is_training=True, reuse=reuse)
        probs = tf.nn.softmax(logits) # probabilities
    return logits, probs, end_point

logits, probs, end_point = inception(X)

restore_vars = [
    var for var in tf.global_variables()
    if var.name.startswith('InceptionV3/Mixed')
]

train_list = [var for var in tf.global_variables() if var not in restore_vars]

loss = tf.reduce_mean(tf.losses.softmax_cross_entropy(onehot_labels=Y, logits=logits), name='loss')

# train = tf.train.AdamOptimizer(0.001).minimize(loss, var_list=[train_list])
train = tf.train.AdamOptimizer(0.001).minimize(loss)

sess.run(tf.global_variables_initializer())
saver = tf.train.Saver()
saver.restore(sess, "model/model_all.ckpt")

def load_img(path):
    I = PIL.Image.open(path)
    I = I.resize((299, 299)).crop((0, 0, 299, 299))
    I = (np.asarray(I) / 255.0).astype(np.float32)
    return I

def save():
    saver = tf.train.Saver()
    saver.save(sess, "model/model_all.ckpt")

list_file = open("name.txt").readlines()

data_X = []
data_Y = []

zero = np.zeros([79])

for line in list_file:
    l = line.split(" ")
    img = load_img(l[0])
    if len(img.shape) == 2:
        continue
    data_X.append(img)
    zero = np.zeros([79])
    zero[int(l[1])] = 1
    data_Y.append(zero)

len_of_data = len(data_X)

count = 0
for i in range(len_of_data):
    ans = sess.run(probs, feed_dict={X: data_X[i:i+1]})
    A = np.argmax(ans)
    B = np.argmax(data_Y[i])
    if A == B:
        count += 1
print(count/len_of_data*100, end="")
print("%")


# for iter in range(1000):
#     loss_N = 0
#     for i in range(len_of_data//50+1):
#         sess.run(train, feed_dict={X: data_X[50*i:50*(i+1) if 50*(i+1)<=(len_of_data-1) else (len_of_data-1)], Y: data_Y[50*i:50*(i+1) if 50*(i+1)<=(len_of_data-1) else (len_of_data-1)]})
#         loss_N += sess.run(loss, feed_dict={X: data_X[50*i:50*(i+1) if 50*(i+1)<=(len_of_data-1) else (len_of_data-1)], Y: data_Y[50*i:50*(i+1) if 50*(i+1)<=(len_of_data-1) else (len_of_data-1)]})
#     print('Loss' + str(iter) + ': ' + str(loss_N))
#     if iter % 10 == 0 and iter != 0:
#         save()
