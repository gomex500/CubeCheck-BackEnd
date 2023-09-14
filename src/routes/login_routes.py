from crypt import methods
from flask import Blueprint

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login():
    pass