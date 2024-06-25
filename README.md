# Haki Backend

This project is the backend for the Haki Hub, handling the main backend functionality and communicating with the Wagtail CMS microservice for content management. It is built using Flask and interfaces with a PostgreSQL database.

## Project Structure

The project is organized using a **Modular Paradigm** as follows:

```code
│
├── flask_app/
│   ├── app/
│   │   ├── __init__.py             # Initialize the Flask application and register blueprints
│   │   ├── routes/
│   │   │   ├── __init__.py         # Init file for routes module
│   │   │   ├── main.py             # Main routes for the application
│   │   │   ├── wagtail.py          # Routes for Wagtail API communication
│   │   ├── models.py               # Database models
│   │   ├── services/
│   │       ├── __init__.py         # Init file for services module
│   │       ├── wagtail_service.py  # Service functions for Wagtail API communication
│   ├── migrations/                 # Database migration files
│   ├── tests/
│   │   ├── test_basic.py           # Basic tests for the application
│   ├── config.py                   # Configuration settings
│   ├── requirements.txt            # List of dependencies
│   ├── run.py                      # Entry point to run the Flask application
│
├── .env                            # Environment variables
├── .gitignore                      # Git ignore file
├── README.md                       # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.9
- Conda/Venv
- PostgreSQL

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/haki-hub/haki-backend.git
    ```

2. **Create and activate a Conda environment:**

   ```bash
   conda create --name haki_backend python=3.9
   conda activate haki_backend
   ```

3. **Install dependencies:**

   ```python
   pip install -r flask_app/requirements.txt
   ```

4. **Set up the environment variables:**

   Create a `.env` file in the project root directory:

   ```bash
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgresql://username:password@localhost/dbname
   WAGTAIL_API_BASE_URL=https://your-wagtail-site.com/api/v2/
   ```

5. **Run the application:**

   ```bash
   cd flask_app
   python run.py
   ```

## Project Structure Details

- **flask_app/app/**init**.py**: Initializes the Flask application, sets up the configuration, and registers the blueprints for routes.

- **flask_app/app/routes/**:
  - `main.py`: Contains the main routes for the application, including the home and index routes.
  - `wagtail.py`: Contains routes for communicating with the Wagtail CMS API.

- **flask_app/app/models.py**: Defines the database models for the application.

- **flask_app/app/services/**:
  - `wagtail_service.py`: Contains functions to interact with the Wagtail API.

- **flask_app/migrations/**: Directory for database migration files, managed by Flask-Migrate.

- **flask_app/tests/**:
  - `test_basic.py`: Contains basic tests to ensure the application is working correctly.

- **flask_app/config.py**: Contains configuration settings for the Flask application, including database URI and Wagtail API base URL.

- **flask_app/requirements.txt**: Lists the dependencies required for the Flask application.

- **flask_app/run.py**: Entry point to run the Flask application.

## Running Tests

To run the tests, use the following command:

```python
cd flask_app
python -m unittest discover -s tests
```

## Deployment

To deploy the application, follow these steps:

1. Set up the environment variables on the server.
2. Install the dependencies using `pip install -r flask_app/requirements.txt`.
3. Use a WSGI server like Gunicorn to serve the Flask application.
4. Set up a reverse proxy using Nginx or Apache to forward requests to the WSGI server.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.
