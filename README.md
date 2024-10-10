# Django Movie and Person Search API

This is a Django project that provides an API for searching movies and persons. It supports JWT authentication for user login and integrates with a PostgreSQL database.

## Features

- User registration, login, and logout functionality.
- Search for movies with various filters (year, genre, type).
- Search for persons with filters (movie title, name, profession).
- JWT authentication for secure API access.
- Bootstrap-styled frontend for better user experience.

## Technology Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: React
- **Authentication**: JSON Web Tokens (JWT)

## Prerequisites

- Python 3.x
- Node.js and npm (for the React frontend)
- PostgreSQL database
- pip (Python package manager)

## Installation

### Backend Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a PostgreSQL database and update the database settings in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '<your-database-name>',
            'USER': '<your-database-username>',
            'PASSWORD': '<your-database-password>',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Run migrations to set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:
    ```bash
    python manage.py runserver
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd frontend  # Adjust the path as necessary
    ```

2. Install required npm packages:
    ```bash
    npm install
    ```

3. Start the React development server:
    ```bash
    npm start
    ```

## API Endpoints

### Authentication

- **Login**: `POST /api/login/`
  - Request body: `{ "username": "<username>", "password": "<password>" }`
  - Response: Returns JWT token for authenticated users.

### Movies

- **Search Movies**: `GET /api/movies/search/`
  - Query parameters: `year`, `genre`, `type`
  - Response: List of movies matching the criteria.

### Persons

- **Search Persons**: `GET /api/persons/search/`
  - Query parameters: `movieTitle`, `name`, `profession`
  - Response: List of persons matching the criteria.

## Frontend Usage

- The React application provides a user-friendly interface to interact with the API.
- Users can register, log in, search for movies and persons, and view details.
- The interface is styled with Bootstrap for responsiveness and ease of use.

## Running Tests

To run tests for the Django application, use:
```bash
python manage.py test
