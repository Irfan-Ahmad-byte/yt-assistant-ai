
# Notifications Microservice

This is a microservice built with FastAPI/Python that handles notifications-related functionality. You can run the service in three different ways:

1. **Building the image manually**
2. **Running with Docker Compose**
3. **Running with Kubernetes**

## 1. Build image and run manually

To build the Docker image and run the service manually, use the provided shell scripts:

1. Give execution permission to the script:
   ```bash
   chmod +x run.sh
   ```

2. Run the service:
   ```bash
   ./run.sh
   ```

3. To stop the service:
   ```bash
   ./stop.sh
   ```

## 2. Run through Docker Compose

To run the service using Docker Compose, use the following command:

```bash
docker compose up
```

Or run it in detached mode:

```bash
docker compose up -d
```

## 3. Run with Kubernetes

To run the microservice using Kubernetes, execute the setup script:

```bash
./setup_k8s.sh
```

This will deploy the service on your Kubernetes cluster. To remove the Kubernetes setup, use:

```bash
./remove_k8s.sh
```

Ensure your Kubernetes cluster is configured and authenticated before running these commands.

## Github Secrets

Add the following secrets to your GitHub Actions to automate the build and deployment process:

- `DATABASE_URL`
- `DOCKERHUB_REPO`
- `DOCKERHUB_TOKEN`
- `DOCKERHUB_USERNAME`
- `POSTGRES_DB`
- `POSTGRES_PASSWORD`
- `POSTGRES_USER`

These secrets are essential for deploying the service through Docker or Kubernetes in CI/CD workflows. Customize them according to your deployment environment.

**Note:** This microservice is part of a larger orchestrated microservices architecture. For more details on orchestration and setup, check the Orchestrated Microservices repository.
