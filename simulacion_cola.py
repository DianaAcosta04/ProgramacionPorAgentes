from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.datacollection import DataCollector
import numpy as np
import random

class Cliente(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.tiempo_servicio = np.random.exponential(1.0)  # Tiempo de servicio exponencial
        
    def step(self):
        # Aquí defines lo que hace el cliente en cada paso, por ejemplo, esperar en la cola
        pass

class Servidor(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.ocupado = False
        
    def step(self):
        # Aquí defines lo que hace el servidor, por ejemplo, atender a un cliente si hay
        pass

class SistemaColas(Model):
    def __init__(self, tasa_llegada, tasa_servicio, capacidad):
        self.num_agents = 0
        self.schedule = SimultaneousActivation(self)
        self.tasa_llegada = tasa_llegada
        self.tasa_servicio = tasa_servicio
        self.capacidad = capacidad  # k capacidad máxima de la cola
        self.servidor = Servidor(self.num_agents, self)
        self.schedule.add(self.servidor)
        self.cola = []

    def step(self):
        # Llegada de nuevos clientes
        if random.random() < self.tasa_llegada and len(self.cola) < self.capacidad:
            cliente = Cliente(self.num_agents, self)
            self.schedule.add(cliente)
            self.cola.append(cliente)
            self.num_agents += 1
        
        # Procesar los pasos de todos los agentes
        self.schedule.step()

# Parámetros de la simulación
tasa_llegada = 0.8  # Ejemplo, clientes por unidad de tiempo
tasa_servicio = 1.0  # Ejemplo, tasa de servicio por unidad de tiempo
capacidad = 10  # Capacidad máxima de la cola

# Crear el modelo
modelo = SistemaColas(tasa_llegada, tasa_servicio, capacidad)

# Ejecutar la simulación por 100 pasos
for i in range(100):
    modelo.step()
