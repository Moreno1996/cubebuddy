from main import db
import time
import datetime
class DailyTiming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timing = db.Column(db.BigInteger, nullable=False)
    date = db.Column(db.BigInteger, nullable=False)
    userName =db.Column(db.String)
    def __init__(self,timing1,date1,userName):
        self.timing = timing1
        if date1 is None:
            self.date = int(round(time.time() * 1000))
        else:
            self.date = date1
        self.userName = userName

    def __repr__(self):
        return '<Time %r>' % self.timing

    def serialize(self):
        return {
            'time': self.timing,
            'date': self.date,
            'user': self.userName
            # 'Date': datetime.datetime.fromtimestamp(self.date/1000.0)

        }

class User(db.Model):
    userName =db.Column(db.String, nullable=False)

