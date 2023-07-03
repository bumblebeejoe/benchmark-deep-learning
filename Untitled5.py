#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()


# In[3]:


X_train.shape, X_test.shape


# In[4]:


# display single image shape
X_train[0].shape


# In[5]:


# checking labels
y_train[:5]


# In[6]:


# scaling image values between 0-1
X_train_scaled = X_train/255
X_test_scaled = X_test/255
# one hot encoding labels
y_train_encoded = keras.utils.to_categorical(y_train, num_classes = 10, dtype = 'float32')
y_test_encoded = keras.utils.to_categorical(y_test, num_classes = 10, dtype = 'float32')


# In[7]:


def get_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(32,32,3)),
        keras.layers.Dense(3000, activation='relu'),
        keras.layers.Dense(1000, activation='relu'),
        keras.layers.Dense(10, activation='sigmoid')    
    ])
    model.compile(optimizer='SGD',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
    return model


# In[9]:


get_ipython().run_line_magic('timeit', '-n1 -r1')
# CPU
with tf.device('/CPU:0'):
    model_cpu = get_model()
    model_cpu.fit(X_train_scaled, y_train_encoded, epochs = 10)


# In[10]:


get_ipython().run_line_magic('timeit', '-n1 -r1')
# GPU
with tf.device('/GPU:0'):
    model_gpu = get_model()
    model_gpu.fit(X_train_scaled, y_train_encoded, epochs = 10)


# In[ ]:




