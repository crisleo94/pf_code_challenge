from . import db


class Sprocket(db.Model):
    __tablename__ = 'sprocket'
    id = db.Column(db.Integer, primary_key=True)
    teeth = db.Column(db.Integer, nullable=False)
    pitch_diameter = db.Column(db.Float, nullable=False)
    outside_diameter = db.Column(db.Float, nullable=False)
    pitch = db.Column(db.Integer, nullable=False)
    factories = db.relationship('Factory', secondary='factory_sprocket', backref='sprockets')

    @classmethod
    def new(cls, teeth, pitch_diameter, outside_diameter, pitch):
        return Sprocket(teeth=teeth, pitch_diameter=pitch_diameter, outside_diameter=outside_diameter, pitch=pitch)
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def serialize(self):
        return {
            'id': self.id,
            'teeth': self.teeth,
            'pitch_diameter': self.pitch_diameter,
            'outside_diameter': self.outside_diameter,
            'pitch': self.pitch
        }