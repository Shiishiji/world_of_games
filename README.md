# World of games

Scores are available on http://localhost:8777.

The volume is mounted in `./scoring/storage`.
Scores are stored in `scores.csv` comma separated CSV file in a NAME,SCORE format.

ex.
<pre>
Damian,1500
Matthew,1250
Steven,1325
</pre>

## Running application

Firstly, build an environment
```shell
docker compose up -d --build --remove-orphans
```

To start a game run
```shell
docker compose run app
```

## Running e2e tests in selenium

Firstly, build test environment
```shell
docker compose -f docker-compose.yml -f docker-compose.test.yml up -d --remove-orphans --build
```

Run tests (headless!!)
```shell
docker compose -f docker-compose.yml -f docker-compose.test.yml run tests python tests/e2e.py
```
