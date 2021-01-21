from flask import Flask, jsonify, request
import os
from flask_cors import CORS


def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    # main route
    @app.route('/')
    def hello():
        return jsonify({'message': 'Hello'})

    @app.route('/smile')
    def smile():
        return jsonify({'message': 'Smile'})

    
    @app.route('/entrees/<int:entree_id>')
    def retrieve_entree(entree_id):
        return 'Entree %d' % entree_id

    @app.route('/hello', methods=['GET', 'POST'])
    def greeting():
        if request.method == 'POST':
            return create_greeting()
        else:
            return send_greeting()

    def send_greeting():
        return jsonify({'message':'hello','status':'sucess','method':'get'})

    return app
