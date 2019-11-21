# TypeError Demo

I noticed the following error when trying to use launch darkly in a fastapi project with code reloading:

```
TypeError: backoff.on_exception applied to a regular function inside coroutine, this will lead to event loop hiccups. Use backoff.on_exception on coroutines in asynchronous code.
```

The error is thrown from [this line](https://github.com/launchdarkly/python-server-sdk/blob/8adfe4c1607ca5a890b436491d9bec77ed2e1b6f/ldclient/streaming.py#L85) in python-server-sdk.


The command to run uvicorn is [here](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/8e690ce601f28d204411c48749943653c48ffe59/python3.7-alpine3.8/start-reload.sh#L28) in the base image.

## Reproduce the issue

Run `docker-compose up` in this repository.
