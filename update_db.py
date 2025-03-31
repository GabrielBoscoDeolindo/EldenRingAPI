from sqlmodel import create_engine
from sqlalchemy import text

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

with engine.connect() as connection:
    connection.execute(text("ALTER TABLE boss DROP COLUMN difficulty;"))
    connection.commit()


