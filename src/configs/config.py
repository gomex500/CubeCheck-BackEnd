from ctypes import cast
from email.policy import default
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
PORT = config('PORT', default=5000, cast=int)
# MONGO_URI = config('MONGO_URI')