"Código de Aprendizaje Automático Simple"

#Este código implementa un algoritmo de aprendizaje automático muy básico que ajusta un peso w para hacer predicciones lineales

inputs = [1, 2, 3, 4]       #datos de entrada (x)
targets = [2, 4, 6, 8]      #y = 2x

w = 0.1                     #peso inicial (comienza con una estimación pobre)
learning_rate = 0.1         #tasa de aprendizaje (controla cuánto ajustamos w en cada paso)

def predict(i):
    return w*i              #predicción simple: multiplica entrada por peso

for _ in range(100):
    #hace predicciones para todas las entradas
    pred = [predict(i) for i in inputs]
    
    #calcula errores (diferencia entre objetivo y predicción)
    errors = [t - p for p, t in zip(pred, targets)]
    
    #calcula costo (error promedio)
    cost = sum(errors)/len(targets)
    
    #muestra información para monitorear el entrenamiento
    print(f"Targets: ", targets)
    print(f"Predictions: ", pred)
    print(f"Errors: ", errors)
    print(f"Weight: {w: .10f}, Cost: {cost:.6f}")
    
    #ajusta el peso usando el error promedio
    w += learning_rate*cost


