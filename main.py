from app import create_app
from config import config

environment = config.get('development')
app = create_app(environment)

if __name__ == '__main__':
    app.run()