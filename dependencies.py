from database import SessionLocal, engine

# db connection
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

