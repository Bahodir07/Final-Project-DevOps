# 📰 Final Project: DevOps News Portal

## 📦 Overview

This project is a scalable, production-ready news portal built with Django and containerized using Docker. It demonstrates real-world DevOps practices including CI/CD, background task processing, environment isolation, and container orchestration.

The system consists of:

- A Django web application
- PostgreSQL as the relational database
- Redis as a message broker
- Celery for background task processing
- Docker and Docker Compose for deployment
- GitHub Actions for CI/CD

## 🚀 Technologies Used

- Python 3.11
- Django 4.x
- PostgreSQL 15
- Redis 7
- Celery
- Docker & Docker Compose
- GitHub Actions
- Gunicorn (WSGI HTTP server)
- Nginx (optional for production)

## 📂 Project Structure

```
.
├── .github/workflows/       # CI/CD GitHub Actions
├── mysite/                  # Main Django project
├── news/                    # News app (example)
├── static/                  # Collected static files
├── media/                   # User-uploaded media files
├── Dockerfile               # Docker instructions for the web app
├── docker-compose.yml       # Multi-container configuration
├── requirements.txt         # Python dependencies
├── manage.py
└── README.md
```

## 🛠️ Getting Started

To get this project up and running on your local machine or server:

### 1. Clone the repository

```bash
git clone https://github.com/Bahodir07/Final-Project-DevOps.git
cd Final-Project-DevOps
```

### 2. Create and configure the environment file

Copy `.env.example` to `.env` and provide your custom values:

```bash
cp .env.example .env
```

### 3. Build and start the containers

```bash
docker-compose up --build
```

### 4. Run initial migrations and create a superuser

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 5. Access the app

Visit `http://localhost:8000` in your browser.

## ✅ Continuous Integration / Continuous Deployment

This project is equipped with a GitHub Actions workflow that runs on every push to the `main` branch. It performs the following:

- Installs dependencies
- Runs migrations
- Executes unit tests
- Verifies Docker build

This ensures that your app is always deployable and validated against changes.

## 🧠 Additional Features

- **Celery + Redis** for asynchronous background tasks (e.g., sending emails, processing data)
- **Environment isolation** using `.env` for secrets and config
- **Volume persistence** for database and media data
- **Service dependency management** using Docker Compose `depends_on`
- **Security best practices**: `.env` excluded, secrets not committed

## 🌍 Deployment Tips

For production use, consider:

- Adding **Nginx** as a reverse proxy
- Using **Let's Encrypt** SSL certificates
- Hosting on platforms like **DigitalOcean, AWS, Render, or Railway**
- Integrating **monitoring** (Prometheus, Grafana)
- Adding **logging and alerting** tools

## 🧪 Testing

Unit tests are run automatically in CI, but can also be executed locally:

```bash
docker-compose exec web python manage.py test
```

## 📄 License

This project is licensed under the MIT License. Feel free to fork, contribute, or use it for educational purposes.
