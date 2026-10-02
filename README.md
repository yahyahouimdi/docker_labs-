# Lab 2 - Web Application Virtualisation

This lab demonstrates containerised web services, isolated container filesystems, Nginx load balancing, and a Flask date API.

## Prerequisites

- Docker Desktop with Docker Compose
- A browser
- Ports `5000` and `8080` available on the host

## Project Structure

- `question1/`: Static Apache web application and Dockerfile
- `question3/`: Written response about container filesystem isolation
- `question4/`: Nginx load balancer, Docker Compose stack, and benchmark response
- `question5/`: Flask date service, Dockerfile, dependencies, and benchmark response
- `benchmark/`: ApacheBench container used to generate HTTP load

## Run the Complete Lab

From the repository root, build the images:

```powershell
docker compose -f question4/docker-compose.yml build
```

Start the Apache instances, Flask service, and Nginx load balancer:

```powershell
docker compose -f question4/docker-compose.yml up -d instance1 instance2 dateservice lb
```

Open the web application at:

<http://localhost:8080>

The page is served through Nginx and retrieves the formatted date from the Flask service. The date API can also be tested directly:

```powershell
curl.exe "http://localhost:5000/date?lang=en"
curl.exe "http://localhost:5000/date?lang=fr"
```

Run the load test after the services report as healthy:

```powershell
docker compose -f question4/docker-compose.yml run --rm benchmarker
```

Stop and remove the containers and network:

```powershell
docker compose -f question4/docker-compose.yml down
```

## Compose Services

- `instance1` and `instance2`: Two independent Apache web containers
- `dateservice`: Flask API on host port `5000`
- `lb`: Nginx reverse proxy and load balancer on host port `8080`
- `benchmarker`: ApacheBench client sending 1,000 requests with concurrency 50

Healthchecks ensure Apache and Flask are ready before Nginx starts, and Nginx is healthy before the benchmark runs.

## Question Notes

### Question 1

The static page is served by Apache. The page calls the Flask API using JavaScript and displays the localized date.

### Question 3

Containers have independent writable filesystems. Changes made inside one container are not automatically visible inside another container unless a shared volume or external storage is configured.

### Question 4

Nginx distributes requests between `instance1` and `instance2`. The benchmark measures the static page through the load balancer. Results depend on the host machine and current Docker workload.

### Question 5

The Flask service exposes `GET /date`. The optional `lang` query parameter selects the Babel locale and defaults to French. CORS is enabled for the application origins `http://localhost:8080` and `http://127.0.0.1:8080`.

## Cleanup

To remove containers, the network, and the one-off benchmark container:

```powershell
docker compose -f question4/docker-compose.yml down
```
