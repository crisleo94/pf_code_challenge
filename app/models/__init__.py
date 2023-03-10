from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

factory_sprocket = db.Table('factory_sprocket',
  db.Column('factory_id', db.Integer, db.ForeignKey('factory.id'), primary_key=True),
  db.Column('sprocket_id', db.Integer, db.ForeignKey('sprocket.id'), primary_key=True)                            
)
