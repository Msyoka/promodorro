from app import app
from app import create_app,db

from app.models import User,Activity
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Activity=Activity )
if __name__ == '__main__':
 manage.run()