from datetime import datetime

class UserModel:
    def __init__(self, data):
        self.nombre = data.get('nombre', '')
        self.apellido = data.get('apellido', '')
        self.edad = data.get('edad', 0)
        self.rol = data.get('rol', '')
        self.telefono = data.get('telefono', 0)
        self.email = data.get('email', '')
        self.password = data.get('password', '')
        self.create_at = data.get('create_at', datetime.now())
        self.update_at = data.get('update_at', datetime.now())
