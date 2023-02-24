# Email Service

api for sending emails

## Prerequisites

* [docker](https://docs.docker.com/get-docker/)
* [docker-compose](https://docs.docker.com/compose/)

## Install

```shell
pip install -r requirements.txt
```
### or
```shell
docker-compose up
```

## Run

```shell
uvicorn main:app --reload
```


## Env Variables

| Variable        | Default | Comments |
|-----------------|---------|---------|
| PORT            | 8080    |         |
| SMTP_SERVER     |         |         |
| SMTP_PORT       |         |         |
| SMTP_USERNAME   |         |         |
| SMTP_PASSWORD   |         |         |

