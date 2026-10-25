import time
import json
import random

print("=== INICIANDO RED IoT CON SISTEMA DE ENFRIAMIENTO ===")
print("Conectando con el bus de datos en la nube...")
time.sleep(1)

historial_consecutivo = {1001: 0, 1002: 0, 1003: 0}
turnos_enfriamiento = {1001: 0, 1002: 0, 1003: 0}

try:
    while True:
        dispositivos_disponibles = []
        for dispositivo_id in turnos_enfriamiento.keys():
            if turnos_enfriamiento[dispositivo_id] > 0:
                turnos_enfriamiento[dispositivo_id] -= 1
            else:
                dispositivos_disponibles.append(dispositivo_id)
                
        if not dispositivos_disponibles:
            print("Todos los dispositivos estan en proceso de enfriamiento... Esperando...")
            time.sleep(2)
            continue
            
        id_aleatorio = random.choice(dispositivos_disponibles)
        temperatura_simulada = round(random.uniform(5.0, 9.5), 2)
        
        datos_iot = {
            "dispositivo_id": id_aleatorio,
            "temperatura": temperatura_simulada,
            "timestamp": int(time.time())
        }
        
        payload = json.dumps(datos_iot)
        print(f"Transmitiendo a AWS IoT Core -> {payload}")
        
        if temperatura_simulada > 8.0:
            historial_consecutivo[id_aleatorio] += 1
        else:
            historial_consecutivo[id_aleatorio] = 0
            
        if historial_consecutivo[id_aleatorio] >= 2:
            print("\n" + "!" * 60)
            print(f"!!! DISPARADOR AWS LAMBDA ACTIVADO PARA DISPOSITIVO {id_aleatorio} !!!")
            print(f"ALERTA: Temperatura critica detectada ({temperatura_simulada}°C).")
            print(f"ACCION: Sacando dispositivo {id_aleatorio} de los turnos para permitir enfriamiento.")
            print("!" * 60 + "\n")
            
            turnos_enfriamiento[id_aleatorio] = 3
            historial_consecutivo[id_aleatorio] = 0
            
        time.sleep(2)
except KeyboardInterrupt:
    print("\nEnvio de datos de los dispositivos IoT detenido por el usuario.")
