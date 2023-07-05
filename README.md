projectx
========

This is a custom setup of a Django project.  It includes:
- Docker configuration.
- Pre-commit hooks.
- Settings organisation.
- Pytest configuration.
- Celery and Celery Beat services for periodic tasks.

All project naming is `projectx`, so find and replace this with the desired project name.

You will also need to rename the directory `backend/projectx` to your project name.

---
# Dev Environment

Install Docker https://www.docker.com/get-started/

Install pre-commit hooks
```shell
brew install pre-commit
pre-commit install
```

---
# Run
```shell
docker compose up
```
Browse data on the admin
- Admin: http://0.0.0.0:8000/admin/login
- User: `testuser`
- Password: `testpassword`

---
# Test
```shell
docker compose run backend pytest
```

---
# Database
## Connect to local instance
- Full URL: `jdbc:postgresql://0.0.0.0:5432/projectx`

- host: `0.0.0.0:5432`
- user: `projectx`
- password: `projectx`
- database: `projectx`

## Migrate DB Changes
```shell
docker compose run backend python manage.py makemigrations
docker compose run backend python manage.py migrate
```
