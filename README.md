# Task_managment
# Task Management API

## Overview

A Django-based API for managing tasks with token-based authentication. Users can create, update, delete, and view their tasks securely.

## Features

- **Authentication:** Token-based using DRF's TokenAuthentication.
- **CRUD Operations:** Create, Read, Update, Delete tasks.
- **Permissions:** Users can only manage their own tasks.
- **API Documentation:** Swagger and ReDoc interfaces.

## Technologies Used

- Django
- Django REST Framework
- DRF Token Authentication
- drf-yasg for API documentation
- SQLite (default) or PostgreSQL

## Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your_username/task_manager.git
    cd task_manager
    ```

2. **Create and Activate Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create Superuser**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Server**

    ```bash
    python manage.py runserver
    ```

7. **Access API Documentation**

    - **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
    - **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## Running Tests

```bash
python manage.py test
