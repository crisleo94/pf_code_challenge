from . import db


class Sprocket(db.Model):
    __tablename__ = 'sprocket'
    id = db.Column(db.Integer, primary_key=True)
    teeth = db.Column(db.Integer, nullable=False)
    pitch_diameter = db.Column(db.Float, nullable=False)
    outside_diameter = db.Column(db.Float, nullable=False)
    pitch = db.Column(db.Integer, nullable=False)
    factories = db.relationship('Factory', secondary='factory_sprocket', backref='sprockets')