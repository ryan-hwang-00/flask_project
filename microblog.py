from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

from livereload import Server

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()