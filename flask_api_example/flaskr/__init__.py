from flask import Flask, jsonify
import os


def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

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

    return app
