from app import create_app,db
from flask_script import Manager,Server
# Manager: initialises our extension
# Server: Launches the application
from app.models import User, Pitch, Comment


# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    # passing the pitch and comment classes to shell context
    return dict(app = app,db = db,User = User, Pitch = Pitch, Comment = Comment  )
if __name__ == '__main__':
    manager.run()