# Deep Learning Course
Important things a model must know
- Training and validation (prediction) data
- Making a 2D image one dimensional
- Normalizing data
- Categorical Encoding of Data
- Basic Type of Model is a Sequential model from keras (to create it use model = Sequential()) Sequential comes from Keras
- A densly connected layer is a layer where every neuron is connected together (from tensorflow.keras.layers import Dense)
- To add layers, do model.add(Dense(more info on the data (like an array or a matrix)))
- Any model should have input, hidden, and output layers. Layers can use activation functions. This guy uses 'softmax', which makes all outputs of a layer add up to 1 (like probability)
- Actually running the model requires model.compile()
### Here we can specify the loss function (eg: categorical_crossentropy) & we can specify matrics = ['accuracy']
- To train a model, do history = model.fit(
    x_train, y_train, epochs=5, verbose=1, validation_data=(x_valid, y_valid)
)
- overfitting = validation acc. > training acc.
