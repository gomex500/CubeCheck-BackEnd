from datetime import datetime

class ProyectoModel:
    def __init__(self, data):
        self.nombre = data.get('nombre', '')
        self.descripcion = data.get('descripcion', '')
        self.presupuesto = data.get('presupuesto', 0.0)
        self.create_at = data.get('create_at', datetime.now())
        self.update_at = data.get('update_at', datetime.now())
        self.contruccion = data.get('contruccion', {})