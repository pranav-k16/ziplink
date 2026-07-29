from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:pranav161@localhost:5432/ziplink"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)