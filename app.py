from flask import Flask
from flask_cors import CORS
from src.routes.user_routes import user_routes
from src.routes.login_routes import login_routes
from src.routes.materialesX_routes import materialx_routes
from src.routes.materialesY_routes import materialy_routes
from src.routes.home import home
from src.configs.config import DEBUG, PORT

#inicializando servidor
app = Flask(__name__)

#habilitando cors
CORS(app)

#routes
app.register_blueprint(user_routes)
app.register_blueprint(home)
app.register_blueprint(login_routes)
app.register_blueprint(materialx_routes)
app.register_blueprint(materialy_routes)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
