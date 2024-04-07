## Server Architecture

### Overview
This server architecture consists of several components responsible for managing the database, defining its structure, interacting with storage, handling API requests, loading environment variables, and providing utility functions.

### Components

#### 1. `database.py`
- **Description**: This module creates the PostgreSQL database engine and manages sessions for each database transaction.

#### 2. `models.py`
- **Description**: Defines the structure of the database, including tables and relationships between them using SQLAlchemy's ORM.

#### 3. `schemas.py`
- **Description**: Constructs data schemas serving as parameters for the server's API endpoints. These schemas define the structure of data accepted by the server and returned in responses.

#### 4. `repository.py`
- **Description**: This layer interacts with storage, handling CRUD operations and abstracting database interactions from other components.

#### 5. `server.py`
- **Description**: Serves as a controller to manage the REST interface to the software logics. It handles incoming HTTP requests, processes them, and sends back appropriate responses.

#### 6. `config.py`
- **Description**: Loads environment variables from a `.env` file whenever the server is started. This allows for configuration without hardcoding sensitive information.

#### 7. `utils.py`
- **Description**: Provides utility functions for various tasks, including generating symmetric keys for encryption upon requests from the malware.


## Docker Compose Configuration

### Overview
This `docker-compose.yaml` file defines a multi-container Docker application consisting of two services: `postgres` and `server`. It sets up a PostgreSQL database container and a server container for hosting the application.

### Services

#### 1. `postgres`
- **Image**: `postgres:14-alpine`
- **Description**: Sets up a PostgreSQL database container.
- **Environment Variables**:
  - `POSTGRES_USER`: Username for accessing the PostgreSQL database (set to `root`).
  - `POSTGRES_PASSWORD`: Password for the PostgreSQL user (set to `secret`).
  - `POSTGRES_DB`: Name of the database (set to `project1`).
- **Ports**: Maps port `5432` of the host to port `5432` of the container, allowing access to the PostgreSQL database.

#### 2. `server`
- **Build Configuration**:
  - **Context**: Specifies the build context for the server container.
  - **Dockerfile**: Specifies the Dockerfile to build the server container.
- **Ports**: Maps port `8000` of the host to port `8000` of the container, allowing access to the server.
- **Environment Variables**:
  - `DB_SOURCE`: Connection string for accessing the PostgreSQL database. It includes the username, password, host, port, database name, and SSL mode.
- **Dependencies**: Specifies that this service depends on the `postgres` service.
- **Entrypoint**: Specifies the entrypoint script to run before starting the server container. It waits for the PostgreSQL service to be available using `wait-for.sh` before executing `start.sh`.
- **Command**: Specifies the command to run inside the container. It starts the server using Uvicorn, a Python ASGI web server, with the `server:app` module and listens on `0.0.0.0`.

### Usage
1. Ensure Docker and Docker Compose are installed on your system.
2. Place the `docker-compose.yaml` file in the root directory of your project.
3. Run `docker-compose up --build` to start the services defined in the `docker-compose.yaml` file.
4. Access your application via `http://localhost:8000`.
