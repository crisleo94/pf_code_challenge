from . import db


class SprocketProduction(db.Model):
    __tablename__ = 'sprocket_productivity'
    id = db.Column(db.Integer, primary_key=True)
    sprocket_id = db.Column(db.Integer, db.ForeignKey('factories.id'), nullable=False)
    production_goal = db.Column(db.Integer, nullable=False)
    production_actual = db.Column(db.Integer, nullable=False)
    production_date = db.Column(db.TIMESTAMP, nullable=False, default=db.func.now())

    factory = db.relationship('Sprocket', backref=db.backref('sprocket_productivity', lazy=True))