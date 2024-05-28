# Native python

To start HTTP server that displays scores
-
```shell
python -m flask run
```

To play games
-
```shell
python cli.py
```

# Docker

First build image
```shell
docker build -t wog .
```


To start HTTP server that displays scores
-
```shell
docker run --rm -d -v app:/srv/wog:ro -p 5000:5000 --name wog-scores wog python -m flask run
```

To play games
-
```shell
docker run --rm -v app:/srv/wog -it wog python cli.py
```