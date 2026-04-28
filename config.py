from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

# dialect+driver://username:password@host:port/database

DB_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('DB_USER', 'postgres')}:"
    f"{quote_plus(os.getenv('DB_PASSWORD', ''))}@"
    f"{os.getenv('DB_HOST', 'localhost')}:"
    f"{os.getenv('DB_PORT', '5432')}/"
    f"{os.getenv('DB_NAME', 'task_tracker')}"
)

print(DB_URL) # Test na sprawdzenie URL, który wychodzi do silnika (engine)