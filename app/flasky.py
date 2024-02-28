

## import function ---> entry point to run the application

# from app import create_app

# if __name__ == '__main__':
#     app = create_app("prd")
#     app.run()
    
    
    
from flask import Flask
from app.config import config_options as AppConfig
from app.models import db
from flask_migrate import Migrate
from app.__init__ import create_app

if __name__ == '__main__':
    app = create_app("prd")
    app.run()
    