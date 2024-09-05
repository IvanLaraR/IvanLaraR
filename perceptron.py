import random

class Perceptron:
    def __init__(self, num_inputs):
        self.weights = [random.uniform(-1,1) for _ in range(num_inputs)]
        self.bias = random.uniform(-1,1)

    def predict(self, inputs):
        activation = self.bias
        for i in range(len(inputs)):
            activation += inputs[i] * self.weights[i]
        return 1 if activation >= 0 else 0 ##funcion activacion escalonada
    
    def train(self, inputs, target):
        output= self.predict(inputs)
        error = target - output ##funcion de errror
        self.bias += error
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] ##funcion de optimizacion

    def get_weights(self): #poder imprimir el peso
        return self.weights

    def save_weights(self, filename):#genera un archivo
        with open(filename, "r") as f:
            self.blas = float(f.readline())
            self.weights = [float(line) for line in f.readlines()]
    

#AND
# X Y -> Z
#0 0 -> 0
#0 1 -> 1
#1 0 -> 1
#1 1 -> 

#EJEMPLO DE USO
Perceptron = Perceptron(2)

# SI EXISTE EL ARCHIVO, CARGA PESOS

try:
    Perceptron.load_weights("weights.txt")
except:
    print("No se pueden cargar los persos")
    print("Entrenando...")
    #Entrenar
    for _ in range(1000):
        inputs = [0, 0 ]
        Perceptron.train(inputs, 0)
        inputs = [0, 1]
        Perceptron.train(inputs, 0)
        inputs = [1, 0]
        Perceptron.train(inputs, 0)
        inputs = [1, 1]
        Perceptron.train(inputs, 1)
        #Guardar los pasos
        Perceptron.save_weights("weights.txt")
print("Este es el modelo entrenado")
print(Perceptron.get_weights())

print("predicción")
print([0, 0],"-",Perceptron.predict([0,0]))
print([0, 1],"-",Perceptron.predict([0,1]))
print([1, 0],"-",Perceptron.predict([1,0]))
print([1, 1],"-",Perceptron.predict([1,1]))

