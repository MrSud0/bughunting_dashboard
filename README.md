# Bughunting Dashboard

The BugHunting Dashboard is a Django-based application that fetches and displays data from the BugHunting API. It provides an overview of the latest bug bounty programs and allows users to view reports and ranking details of security researchers.

## Core Technologies

- Django: The main web application framework.
- Django REST framework: A toolkit for building Web APIs.
- Celery: A distributed task queue library for Python.
- Redis: A message broker for Celery.
- PostgreSQL: The primary database for storing application data.
- Gunicorn: A WSGI HTTP server for running Python web applications.
- Docker: A platform for containerizing and deploying applications.

## Deployment

1. Ensure Docker and Docker Compose are installed on your machine.
2. Clone the repository and navigate to the project root.
3. Create a `.env` file in the project root with the following contents (replace placeholders with actual values):

```DJANGO_SECRET_KEY=your_django_secret_key
DJANGO_SETTINGS_MODULE=bughunting_dashboard.settings
HACKERONE_API_TOKEN=your_hackerone_api_token
```

4. Run `docker-compose up -d` to build and start all services.
5. Access the application at `http://localhost:8000`.

## Functionalities

- Fetch and display a list of HackerOne programs.
- Show a leaderboard of security researchers based on their ranking.
- Display "hot" bug bounty programs to help researchers prioritize their work.
- Periodically update program and report data using Celery tasks.

## Roadmap

- Incorporate additional views and filters for program and report data.
- Add user authentication and customizable dashboards.
- Integrate other bug hunting platforms, such as Bugcrowd, Intigriti and Synack.
- Implement notifications and alerts for new programs and reports.
- Enhance the leaderboard with more ranking metrics and researcher profiles.
