class Layer:
    def __call__(self, next_layer):
        self.next_layer = next_layer
        return next_layer

    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs
        self.name = 'Input'


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = 'Dense'


class NetworkIterator:
    def __init__(self, layer):
        self.layer = layer

    def __next__(self):
        if not self.layer:
            raise StopIteration
        while self.layer:
            result = self.layer
            self.layer = self.layer.next_layer
            return result

    def __iter__(self):
        return self


nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"