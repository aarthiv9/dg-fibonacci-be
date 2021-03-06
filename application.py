import os
import math

import flask
from flask import Flask, jsonify, send_file, Response, request
from flask.ext.cors import CORS

from fib_calc import fib


# Create the Flask app
app = flask.Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, methods=['GET'])

@app.errorhandler(400)
def bad_request(e=None):
	return jsonify({'error': 'bad request'}), 400

@app.errorhandler(404)
def not_found(e=None):
	return jsonify({'error': 'resource not found'}), 404

@app.errorhandler(405)
def method_not_supported(e):
	return jsonify({'error': 'method not supported'}), 405

@app.errorhandler(500)
def internal_server_error(e=None):
	return jsonify({'error': 'internal server error'}), 500

@app.route('/api/fibonacci/<int:num>', methods=['GET'])
def fibonacci(num):
    return jsonify({'fibonacci': fib(num)})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
