from datetime import datetime

#modelo de heramientas
class HerramientasModel:
    def __init__(self, data):
        self.perimetro = data.get('perimetro', 0)
        self.area = data.get('area', 0)
        self.volumen = data.get('volumen', 0)
        self.conversion = data.get('conversion', 0)
        self.pared = data.get('pared', 0)
        self.pilar = data.get('pilar', 0)
        self.embaldosado = data.get('embaldosado', 0)
        self.loza = data.get('loza', 0)
        self.proyecto = data.get('proyecto', 0)
        self.materiales = data.get('materiales', 0)
        self.chatbot = data.get('chatbot', 0)
        self.create_at = data.get('create_at', datetime.now())
        self.update_at = data.get('update_at', datetime.now())