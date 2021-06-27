#Exercise 8

import sys,numpy
from matplotlib import pyplot
from keras.datasets import cifar10
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.layers import GaussianNoise
 

def load_dataset():
	# load dataset
	(x_train, y_train), (x_test, y_test) = cifar10.load_data()
	# one hot encode target values
	y_train = to_categorical(y_train)
	y_test = to_categorical(y_test)
	return x_train, y_train, x_test, y_test


def prep_pixels(train, test):
	# convert from integers to floats
	train_norm = train.astype('float32')
	test_norm = test.astype('float32')
	# normalize to range 0-1
	train_norm = train_norm / 255.0
	test_norm = test_norm / 255.0
	# return normalized images
	return train_norm, test_norm
 

def define_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(32, 32, 3)))
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(MaxPooling2D((2, 2)))
	model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(10, activation='softmax'))
	# compile model
	opt = SGD(lr=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
	return model
 

def summarize_diagnostics(history):
	# plot loss
	pyplot.subplot(211)
	pyplot.title('Cross Entropy Loss')
	pyplot.plot(history.history['loss'], color='blue', label='train')
	pyplot.plot(history.history['val_loss'], color='orange', label='test')
	# plot accuracy
	pyplot.subplot(212)
	pyplot.title('Classification Accuracy')
	pyplot.plot(history.history['accuracy'], color='blue', label='train')
	pyplot.plot(history.history['val_accuracy'], color='orange', label='test')
	# save plot to file
	filename = sys.argv[0].split('/')[-1]
	pyplot.savefig(filename + '_plot.png')
	pyplot.close()
 

def run_result():
	# load dataset
	x_train, y_train, x_test, y_test = load_dataset()
	# prepare pixel data
	x_train, x_test = prep_pixels(x_train, x_test)
	# define model
	model = define_model()
	model2 = define_model()

	# fit model

	noise_x_train = GaussianNoise(0.1)(x_train, training=True)
	#noise_x_train = numpy.clip(noise_x_train, 0, 1)

	#Task 1
	print("Task 1")
	history = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test), verbose=1)

	#Task 2 & 3
	print("Task 2")
	history2 = model2.fit(noise_x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test), verbose=1)

	# evaluate model
	_, acc = model.evaluate(x_test, y_test, verbose=1)
	print('> %.3f' % (acc * 100.0))
	_, acc = model2.evaluate(x_test, y_test, verbose=1)
	print('> %.3f' % (acc * 100.0))

	# learning curves
	summarize_diagnostics(history)
	summarize_diagnostics(history2)

run_result()
