from . import db


class Factory(db.Model):
    __tablename__ = 'factory'
    id = db.Column(db.Integer, primary_key=True)
    chart_data = db.Column(db.JSON, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'chart_data': self.chart_data
        }