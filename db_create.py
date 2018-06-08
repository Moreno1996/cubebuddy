from main import db
from models import DailyTiming
db.drop_all()
db.add(DailyTiming(50,None))
db.create_all()
db.session.commit()