from main import db
from models import DailyTiming

db.create_all()

db.session.add(DailyTiming(6500))
db.session.add(DailyTiming(6500))

db.session.commit()