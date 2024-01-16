# PriceOye-Django
A demo back-end eCommerce project built with DJango.

## Features

- **API Endpoints:**
  - **POST:** Create new resources (e.g., products, orders, brands, categories, accounts).
  - **GET:** Retrieve information about resources.
  - **PUT:** Update existing resources.
  - **DELETE:** Remove resources from the system.
- **Dockerization**
  - Containerized the project using Docker for development, leveraging a PostgreSQL database. For production deployment, integrated Nginx as the reverse proxy server and Gunicorn as the application server.
- **Code Documentation:**
  - The project codebase includes comprehensive docstrings to provide detailed information about the purpose and usage of functions, classes, and modules. Explore the code to discover inline documentation that enhances code readability and facilitates understanding.
- **Database**
  - PostgreSQL is used as the database in both development and production.

- **Authorization & Authentication:**
  - Secure authentication using JSON Web Tokens (JWT) ensures data integrity and user identity verification.

# Django E-Commerce Project Locally
1. **Clone the Repository:**
   ```bash
   git clone 
   cd Price-oye/Simple/priceoye
2. **Create the virtual environment:**
   ```bash
   python3 -m venv venv
2. **Activate Virtual Environment:**
   ```bash
   source venv/bin/activate
3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
4. **Run Migrations:**
   ```bash
   python manage.py migrate
5. **Create Superuser**
    ```bash
   python manage.py createsuperuser

6. **Run development server:**
   ```bash
   python manage.py runserver
7. Goto http://127.0.0.1:1337 (/admin) for admin, (/swagger) for swagger dashboard.
8. **Stop the server:**
   Ctrl + C

- **Running Test Cases**
  ```bash
  python manage.py test


___________________________________________

# Django E-Commerce Project with Docker

Containerized setup with Dockers, Postgre SQL, Nginx and Gucicorn. 

## Development Environment

### Components:
- **Dockerfile:** Specifies the configuration for the development container.
- **docker-compose.yml:** Defines services, including Django, PostgreSQL, etc., for local development.
- **.env.dev:** Stores environment variables specific to the development environment.
- **entrypoint.sh:** Shell script for setup and initialization during container startup.

### Usage:
1. Ensure Docker is installed.
2. Git Clone the project.
3. Goto:
   ```bash
   cd Price-oye/Dockerized/priceoye/
4. Build the Dockers Images:
   ```bash
   sudo docker-compose up -d --build
5. Run migration:
   ```bash
   sudo docker-compose exec web python manage.py migrate --noinput
6. Running the dockers:
   ```bash
   sudo docker-compose up
7. Goto http://127.0.0.1:8000 (/admin) for admin, (/swagger) for swagger dashboard.
8. Stopping the dockers:
   ```bash
   sudo docker-compose down

## Production Environment

### Components:
- **Dockerfile.prod:** Specifies the configuration for the production container.
- **docker-compose.prod.yml:** Defines services for production, including Nginx, Gunicorn, PostgreSQL, etc.
- **.env.prod:** Stores environment variables specific to the production environment.
- **entrypoint.sh.prod:** Production version of the entrypoint script.

### Usage:
1. Stop development environment:
   ```bash
   sudo docker-compose down -v
2. Build the Dockers Images:
   ```bash
   sudo docker-compose - docker-compose.prod. yml up -d --build
3. Run migration:
   ```bash
   sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
4. Copy Static Files:
   ```bash
   sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
5. Run the production server:
   ```bash
   sudo docker-compose -f docker-compose.prod.yml up
6. In a new terminal, create a superuser:
   ```bash
   sudo docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
7. Goto http://127.0.0.1:1337 (/admin) for admin, (/swagger) for swagger dashboard.
8. Run tests:
   ```bash
   sudo docker-compose exec web python manage.py test
9. Stopping the dockers:
   ```bash
   sudo docker-compose -f docker-compose.prod.yml down
