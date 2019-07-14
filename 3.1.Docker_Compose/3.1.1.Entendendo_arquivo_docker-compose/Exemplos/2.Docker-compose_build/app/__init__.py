#!/usr/bin/python

from flask import Flask
import redis
import time

app = Flask(__name__)
redis = redis
time = time

from app import routes
