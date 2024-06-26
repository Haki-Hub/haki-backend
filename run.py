import os
from dotenv import load_dotenv
from app import create_app

# Load environment variables from .env file
load_dotenv()

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
