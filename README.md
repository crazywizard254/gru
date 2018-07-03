# gru

## Introduction
This sample application runs a docker environment with:
* Nginx web server
* uWSGI as the Gateway interface
* RabbitMQ as the queueing service
* Celery as the worker
* MySQL server as the Database
* Django as the Application 

## Docker setup

```
docker-compose up
```

## Running the test
Run the test by navigating to the URL `http://localhost/test`
It should display a typical Apache like **It Works!** page.

In the terminal logs, you will see a random quote printed by the worker container every time you hit the above URL
