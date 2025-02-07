from app import create_app
from dotenv import load_dotenv
load_dotenv(override=True)
from os import getenv

app = create_app()

if __name__ == "__main__":
    
    FLASK_RUN_PORT = getenv('FLASK_RUN_PORT')
    FLASK_RUN_HOST = getenv('FLASK_RUN_HOST')

    app.run(port=FLASK_RUN_PORT, host=FLASK_RUN_HOST)