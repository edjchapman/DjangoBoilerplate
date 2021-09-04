# Django Boilerplate

Boilerplate Django project, including Docker configuration for developemnt and production. To be used as the base for
other projects.

---

# Development

### Build the images and spin up the containers

```shell
docker-compose up -d --build
```

### Run the migrations

```shell
docker-compose exec backend python manage.py migrate --noinput
```

### Ensure the Django tables were created

```shell
$ docker-compose exec db psql --username=hello_django --dbname=hello_django_dev
hello_django_dev=# \l
hello_django_dev=# \c hello_django_dev
hello_django_dev=# \dt
hello_django_dev=# \q
```

---

# Production

```shell
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate --noinput
```

---

# Troubleshooting

### DANGER: Remove the volumes along with the containers

```shell
docker-compose down -v
```
