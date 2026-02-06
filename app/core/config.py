import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ENV = os.getenv("ENV", "dev")

    def validate(self):
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL not set")
        if not self.SECRET_KEY:
            raise ValueError("SECRET_KEY not set")

settings = Settings()
settings.validate()