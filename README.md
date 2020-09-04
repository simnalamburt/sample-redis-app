sample-redis-app
========
Sample web server using Redis to test [Nomad]

![Screenshot]

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
docker run -it -p 5000:5000 ghcr.io/simnalamburt/sample-redis-app:1.0.1
```

[Nomad]: https://www.nomadproject.io/
[Screenshot]: https://raw.githubusercontent.com/simnalamburt/i/master/sample-redis-app/screenshot.png
[GitHub Package Registry]: https://github.com/users/simnalamburt/packages/container/sample-redis-app
