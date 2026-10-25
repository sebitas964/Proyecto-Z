import numpy as np
from sklearn.linear_model import LinearRegression

X_train = np.array([[10, 3], [20, 5], [30, 2], [40, 4], [50, 1]], dtype=float)
y_train = np.array([15, 25, 35, 45, 55], dtype=float)

model = LinearRegression()
model.fit(X_train, y_train)

print("--- SISTEMA DE PREDICCION DE VENTAS ---")
gasto_usuario = float(input("Ingrese el gasto en publicidad (miles USD): "))
mercado_usuario = float(input("Ingrese el tamano del mercado (nivel 1 al 5): "))

nuevo_escenario = np.array([[gasto_usuario, mercado_usuario]], dtype=float)
prediccion = model.predict(nuevo_escenario)

print(f"\nPrediccion de ventas para su escenario: {prediccion[0]:.2f} miles USD")
