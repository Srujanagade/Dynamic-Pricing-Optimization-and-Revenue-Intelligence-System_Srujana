from sqlalchemy import create_engine
from sqlalchemy.engine import URL

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="srujana",
    host="localhost",
    port=5432,
    database="pricepilot_ai"
)

engine = create_engine(DATABASE_URL)