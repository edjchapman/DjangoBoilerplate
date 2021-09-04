# DjangoDefault

Default Django project, ready to be adapted and deployed.

---

# Setup

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

# Troubleshooting

### DANGER: Remove the volumes along with the containers

```shell
docker-compose down -v
```
