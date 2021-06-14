from app import create_app,db
from flask_script import Manager,Server
# Manager: initialises our extension
# Server: Launches the application
from app.models import User, Pitch, Comment
from  flask_migrate import Migrate, MigrateCommand


# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

# initialising the migrate exts by passing the app instance and db sqlalchemy instance
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    # passing the pitch and comment classes to shell context
    return dict(app = app,db = db,User = User, Pitch = Pitch, Comment = Comment  )





if __name__ == '__main__':
    manager.run()