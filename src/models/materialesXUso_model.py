from datetime import datetime

#modelo de objeto Material X en uso
class MateXUseModel:
    def __init__(self, data):
        self.nombre = data.get('nombre', '')
        self.marca = data.get('marca', '')
        self.tipo = data.get('tipo', '')
        self.medida = data.get('medida', '')
        self.cantidad = data.get('cantidad', 0)
        self.precio = data.get('precio', 0)
        self.description = data.get('description', '')
        self.creador = data.get('creador', '')
        self.create_at = data.get('create_at', datetime.now())
        self.update_at = data.get('update_at', datetime.now())