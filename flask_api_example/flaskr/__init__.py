from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return jsonify({'message':'Hello'})
    @app.route('/smile')
    def smile():
        return jsonify({'message':'Smile'})


    return app