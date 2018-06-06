from main import db

class DailyTiming(db.Model):
    __tablename__ = "dailyTimes"
    id=db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Long, nullable=False)

    def __init__(self,time):
        self.time = time

    def __repr__(self):
        return '<{}>'.format(self.time)