import numpy as np;
import tensorflow as tf;
import numpy.random as random;
import matplotlib as mlp;
import matplotlib.pyplot as plt;
a=np.zeros(2);
print(a);
np.random.seed(42);
x=np.linspace(0,5,100);
y=2*np.sin(x)+0.3*x**2;
plt.figure('Random number');
plt.plot(x,y);
plt.show();
b=tf.constant('hello world');
sess=tf.Session();
print(sess.run(b));