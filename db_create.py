from main import db
db.drop_all()
db.create_all()
db.session.commit()