from . import db


class Sprocket(db.Model):
    __tablename__ = 'sprockets'
    id = db.Column(db.Integer, primary_key=True)
    teeth = db.Column(db.Integer, nullable=False)
    pitch_diameter = db.Column(db.Integer, nullable=False)
    outside_diameter = db.Column(db.Integer, nullable=False)
    pitch = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=db.func.now())