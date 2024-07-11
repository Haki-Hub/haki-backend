from app import create_app
from flask_migrate import MigrateCommand
import os

app = create_app()

if __name__ == '__main__':
    app.run()
