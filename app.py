from flask import Flask
from backend.config import LocalDevelopmentConfig
from backend.models import db
from backend.models import User, Subject, Chapter, Quiz, Question, Score
from flask_security import Security, SQLAlchemyUserDatastore

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    datastore = SQLAlchemyUserDatastore(db, User)
    app.security =  Security(app, datastore)
    app.app_context().push()

    return app

app = create_app()

app.config.from_object(LocalDevelopmentConfig)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'Test'

if __name__ == '__main__':
    app.run(debug=True)
