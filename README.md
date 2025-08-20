# 🐍 Django Boilerplate with PostgreSQL, Redis, Channels, and Docker

This project is a boilerplate ready for backend development with Django 5.2.5, Docker, PostgreSQL, Redis, and Channels (WebSockets), using **Uvicorn** as the ASGI server and **WhiteNoise** to serve static files.

---

###  Included Services

- **Django (ASGI)**: Backend server with WebSocket support.
- **PostgreSQL**: Relational database.
- **Redis**: Used for caching and as the backend for Channels.
- **Docker**: For local development and deployment.

---

###  How to get the project up and running?

1. **Clone the repository** and make sure you have Docker and Docker Compose installed.

2. **Copy the `.env` file** if it's not present:

    ```bash
    cp core/.env.example core/.env
    ```

3. **Build and start the containers**:

    ```bash
    docker-compose up --build
    ```

4. **Apply migrations (inside the `django` container)**:

    ```bash
    docker exec -it django python manage.py migrate
    ```

5. (Optional) **Create a superuser**:

    ```bash
    docker exec -it django python manage.py createsuperuser
    ```

6. Access the project at:

    [http://localhost:8000](http://localhost:8000)

---

### Tech Stack

- **Python 3.12**
- **Django 5.2.5**
- **Django REST Framework**
- **Django Channels**
- **Redis / Channels Redis**
- **PostgreSQL**
- **Docker + Docker Compose**
- **Uvicorn**
- **WhiteNoise**
- **django-environ** for managing environment variables

---

###  Important Notes

- The `.env` file **must be inside the `core` folder**. Make sure it's configured correctly.

- **Redis is not working with TLS**, so a non-secure connection is being used. If deploying to production, consider configuring Redis with TLS.

- **Don't forget to check the `DEBUG` variable** in `settings.py`
