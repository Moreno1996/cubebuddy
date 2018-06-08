from main import db
import time
class DailyTiming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timing = db.Column(db.BigInteger, nullable=False)
    date = db.Column(db.BigInteger, nullable=False)

    def __init__(self,timing1,date1):
        self.timing = timing1
        if date1 is None:
            self.date = int(round(time.time() * 1000))
        else:
            self.date = date1

    def __repr__(self):
        return '<Time %r>' % self.timing

    def serialize(self):
        return {
            'Time': self.timing,
            'Date': self.date,
        }