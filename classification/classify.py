from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation

lr = 0.0001
batch_size = 32
input_shape = (,)

ROOT = 'data/'

model = Sequential()
model.add(LSTM(128, dropout=0.8, input_shape=input_shape, batch_size=batch_size))
# kick, snare, closed, open, clap
model.add(Dense(5, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy',
                metrics=['accuracy'])
