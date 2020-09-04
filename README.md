sample-redis-app
========
Sample web server using Redis to test [Nomad]

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip setuptools
pip install -r requirements.txt

# development mode
FLASK_ENV=development flask run

# production mode
flask run
```

### Docker
Hosted in [GitHub Package Registry]

```bash
docker build . -t ghcr.io/simnalamburt/sample-redis-app
```

[Nomad]: https://www.nomadproject.io/
[GitHub Package Registry]: https://github.com/users/simnalamburt/packages/container/sample-redis-app
