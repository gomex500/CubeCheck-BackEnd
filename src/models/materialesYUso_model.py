from datetime import datetime

#modelo de objeto Material Y en uso
class MateYModel:
    def __init__(self, data):
        self.nombre = data.get('nombre', '')
        self.tipo = data.get('tipo', '')
        self.x = data.get('x', 0)
        self.y = data.get('y', 0)
        self.z = data.get('z', 0)
        self.precio = data.get('precio', 0)
        self.description = data.get('description', '')
        self.creador = data.get('creador', '')
        self.create_at = data.get('create_at', datetime.now())
        self.update_at = data.get('update_at', datetime.now())
