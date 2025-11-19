from  tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import numpy as np
import tensorflow as tf
from data import generate_image_dataset
from sklearn.model_selection import train_test_split
import pickle
# RANDOM_SEED = 28
# np.random.seed(RANDOM_SEED)
# tf.random.set_seed(RANDOM_SEED)
def make_model():
    X,y = generate_image_dataset(200)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = Sequential()
    model.add(Dense(32, input_shape=(64,), activation='relu'))
    model.add(Dense(16, input_shape=(64,), activation='relu'))
    model.add(Dense(units=3, activation='softmax'))

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(X_train, y_train,epochs=20)
    return model,X_test,y_test

