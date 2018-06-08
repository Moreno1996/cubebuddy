from main import db
from models import DailyTiming
db.drop_all()
db.create_all()
db.session.add(DailyTiming(50,None))
db.session.commit()