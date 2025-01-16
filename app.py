from flask import Flask
from waitress import serve
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment (default to 'development')
ENV = os.getenv('FLASK_ENV', 'development')
IS_DEV = ENV == 'development'

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if IS_DEV else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Debug: Print environment variables
port = int(os.getenv('PORT', 8080))

app = Flask(__name__)
app.debug = IS_DEV

@app.route("/")
def hello_world():
    log_func = logger.debug if IS_DEV else logger.info
    log_func(f"Hello endpoint was called in {ENV} mode")
    return "<p>Hello from Flask 2!</p>"

if __name__ == "__main__":
    host = "localhost" if IS_DEV else "0.0.0.0"
    port = int(os.getenv('PORT', 8080))
    
    logger.info(f"Starting server in {ENV} mode on port {port}...")
    serve(app, host=host, port=port)