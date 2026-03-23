import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. Get the directory where this current file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Build the full path to the database file
# This prevents the 500 error on Render
db_path = os.path.join(BASE_DIR, "todoapplication.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"

# 3. Create the engine with the fixed path
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# 4. Setup the Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Define the Base for your models
Base = declarative_base()