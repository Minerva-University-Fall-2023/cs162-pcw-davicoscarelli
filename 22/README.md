# Docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED              STATUS          PORTS                                       NAMES
f77b9c4414e2   adminer              "entrypoint.sh php -…"   46 seconds ago       Up 16 seconds   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   db-admin
f73e28db9796   postgres:alpine      "docker-entrypoint.s…"   About a minute ago   Up 18 seconds   5432/tcp                                    db
3a41b47e8b72   simple-cs162-flask   "python app.py"          12 days ago          Up 14 seconds   0.0.0.0:5162->5162/tcp, :::5162->5162/tcp   simple-cs162-instance
fe1da422a615   postgres             "docker-entrypoint.s…"   2 years ago          Up 4 days       0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   postgres


# Class Differences
The changes collectively suggest a significant shift in the project's backend infrastructure, particularly moving from a simpler SQLite database to a more robust PostgreSQL setup. The introduction of Docker Compose and changes in the Dockerfile indicate a move towards a more complex, production-oriented containerized environment. The adjustments in app.py and parse.py reflect these backend changes.


# Components:

1. **Web Application (app.py)**:
   - This is the core of your project, a Flask-based web application written in Python.
   - It handles web requests, performs operations (like calculations), and interacts with the database.

2. **Database (PostgreSQL)**:
   - In Session 22, the project has transitioned to using PostgreSQL, a powerful, open-source object-relational database system.
   - It stores and manages data required by the web application, such as calculation results or user data.

3. **Docker Containers**:
   - Docker is used to containerize the application and its environment. This means the application and its dependencies are packaged together in a container, which can be run on any system that has Docker installed.
   - The `Dockerfile` defines how the Docker container for the web application is built, including the Python environment and necessary libraries.

4. **Docker Compose (docker-compose.yml)**:
   - Introduced in Session 22, Docker Compose is a tool for defining and running multi-container Docker applications.
   - It allows you to configure and link multiple containers (like your web app and PostgreSQL database) to work together.

5. **Web Server (Flask)**:
   - Flask is a lightweight WSGI web application framework in Python, used to build the web application.
   - It handles HTTP requests and serves web pages.

6. **Parser (parse.py)**:
   - A Python script for parsing and possibly handling calculations or data processing.
   - It seems to be used within the web application for specific operations.

### Interaction:

- **User Interaction**: Users interact with the web application through a web browser. They send HTTP requests (like visiting pages or submitting forms), which are handled by the Flask application running inside a Docker container.

- **Application and Database Interaction**: The Flask application communicates with the PostgreSQL database to store and retrieve data. This interaction is likely managed through SQLAlchemy (a Python SQL toolkit and ORM).

- **Docker and Docker Compose**: Docker Compose orchestrates the interaction between the web application container and the PostgreSQL database container. It ensures that these containers can communicate with each other and are set up with the correct configurations.

- **Local Machine and Containers**: All these components (Flask app, PostgreSQL database) are running in containers on your local machine, managed by Docker. Docker abstracts away the underlying system differences, providing a consistent environment for the application.

### Terminology and Acronyms:

- **Flask**: A micro web framework written in Python. It's called a micro-framework because it does not require particular tools or libraries.

- **PostgreSQL**: An advanced open-source relational database. It supports both SQL (relational) and JSON (non-relational) querying.

- **Docker**: A platform for developing, shipping, and running applications inside containers. Containers are isolated environments that contain all the necessary software to run an application.

- **Docker Compose**: A tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application's services.

- **WSGI (Web Server Gateway Interface)**: A specification for a universal interface between web servers and web applications or frameworks for the Python programming language.

