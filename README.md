# README

### Start project

- `docker-compose up -d` - to start application and mysql database
- `docker-compose exec app ./manage.py migrate` - to run migrations
- `docker-compose exec app pytest` - to check tests
- Open `localhost:8000`


### Ruff

- `sudo docker-compose exec app ruff check`
- `sudo docker-compose exec app ruff format`
