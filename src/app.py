from flask import Flask
from routes.user_routes import user_routes
from configs.config import DEBUG, PORT

app = Flask(__name__)
app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
