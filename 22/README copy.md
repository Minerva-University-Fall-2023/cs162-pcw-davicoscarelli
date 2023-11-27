## A Cluster of containers

In the previous session, you worked through building and running a single
container. In this session you will build and run a few containers and show
that they can all communicate with each other.

First we will do this manually, and once this is working we will do this using
`docker stack` and a `docker-compose.yml` file. Make sure to think through the
costs and benefits of each approach.

Again, all of these commands are typed into a shell which has changed to the
`session_22/web` directory. There are differences between the the two
directories. Make sure to find out what has changed, and why!

### 1. Do the tutorial

First, work through the tutorial on Docker. For this session, focus on parts 5–8 (Persist the DB, Use bind mounts, Multi container apps, Use Docker Compose).
_For this course there is no need to run the parts of the tutorial which require multiple virtual machines._

**Reminder: On Windows**

Docker Desktop for Windows requires Hyper-V, which is only supported for 64-bit Windows 10 Pro, Enterprise or Education. Windows 10 Home users, as well as users of 32-bit versions and older versions of Windows have to resort to a legacy solution, and use the outdated "Docker Toolbox". See [this link](https://docs.docker.com/toolbox/toolbox_install_windows/).

### 2. Build and tag the image

Start by building a docker image using:

```bash
docker build -t cs162-flask:latest .
```

### 3. Create the network

Let's create a network for all the different containers to communicate over:

```bash
docker network create -d bridge cs162-bridge-network
```

### 4. Run the instances manually

To start with we can run the instances manually. Run the following commands each in separate Terminal windows, or using the `-d` flag:

```bash
docker run --name=db --network=cs162-bridge-network -e "POSTGRES_DB=cs162" -e "POSTGRES_USER=cs162_user" -e "POSTGRES_PASSWORD=cs162_password" postgres:alpine
docker run --name=db-admin --network=cs162-bridge-network -p 8080:8080/tcp adminer
docker run --name=cs162-instance --network=cs162-bridge-network -p 5162:5162 cs162-flask
```

Once all the containers are running successfully then you should confirm that
the Computation Server is indeed running at `http://localhost:5162`. Enter a
few example calculations (eg. `1.1 * 1.1` or `50 * 50`), and confirm that the
results are successfully stored in the database.

**Reminder: On Windows Running Docker Toolbox**

Find the app on the Docker Machine IP. By default, this is `http://192.168.99.100:5162/` where the port is specified after the colon). The IP can be found with the command `docker-machine ip`.

### 5. Inspect all the running processes

```bash
docker ps
```

This will give you a list of the container ids. Whenever you need to refer to
a container's id, this is a good command to find it.

### 6. Now stop the database:

```bash
docker container stop <id of the postgres container>
```

(Hint - you will actually need to edit that above command!)

Confirm that the database is stopped by reloading `http://localhost:5162` and
observing that the webpage now throws an error. (Sometimes it can take a short
while for the database to shut down completely, so you might need to try
several times.)

### 7. Now start the database:

```bash
docker container start <id of the postgres container>
```

Reloading the webpage should show that all of the previous computations were
saved to the database and persisted to disk.

### 8. Tear it all down

Running things manually like this can be slow, fiddly and painful to maintain.
This led to the creation of a tool which can orchestrate the running of many
docker containers. First we need to tear down all the existing manual
containers:

```bash
docker rm -f cs162-instance
docker rm -f db-admin
docker rm -f db
```

# 9. Bring up a stack of services

Before you run anything, read the `docker-compose.yml` file. Since you've
worked through the tutorial already the file should be reasonably
straightforward to understand. Revisit appropriate parts of the tutorial if
this is not the case (or search the internet for more information about
particular commands / images).

Now bring the stack up using:

```bash
docker swarm init
docker stack deploy -c docker-compose.yml cs162-swarm
```

**On Windows Running Docker Toolbox**

You might need to specify an IP address to advertise. Use:

```bash
docker swarm init --advertise-addr 192.168.99.100
docker stack deploy -c docker-compose.yml cs162-swarm
```

Confirm that the expected number of containers are running using:

```bash
docker ps
```

(Note that sometimes it takes a while for the database to be fully operational
and the web containers will fail before then.)

Visit `http://localhost:5162` and verify that the computation server is running
correctly.

### 10. Load balancing

It is possible to watch the output of a single container using the following
command:

```bash
docker logs -f <id of a web container>
```

Now refresh `http://localhost:5162` in your browser several times, and confirm
that the container is indeed serving some requests.

### 11. Stop a web container

Let's knock over a container and see how it is handled by docker.

```bash
docker container stop <id of a web container>
```

Refresh `http://localhost:5162` in your browser several times, and confirm that
other web containers are still serving requests.
Examine the state of the system using:

```bash
docker ps
```

### 12. Resize the stack

Now edit `docker-compose.yml`, and make it so that the stack has only 2 replicas
of the web container. Deploy the stack and monitor what happens.

### 13. Tear it all down

Don't forget to tidy up after yourself using the following:

```bash
docker stack rm cs162-swarm
```

## Questions

Bring to class a copy of the output from `docker ps` when the entire stack has
been successfully deployed. This needs to be in plain text, so a screenshot is
not appropriate. Be prepared to explain your answers for the questions below.

### Q1. What has changed since last session?

Compare the differences between the session_21 and session_22 web directories.
What has changed, and why have those changes been made? A useful command in
this case is the `diff` command. (For those using windows, it is recommended
that you download the [DiffUtils for Windows](http://gnuwin32.sourceforge.net/packages/diffutils.htm))
or other similar tool.

### Q2. What was different between manual and automatic configurations?

Compare the state of the system when we brought it up manually, and when we
brought it up using docker stack. There is one large obvious difference.  
What is it, and what impact might this have on the system?

### Q3. Inspect the database

1. Submit several calculations to the server.
2. Visiting http://localhost:8080 will take you to a database admin login page.
   Either by examining the manual commands, or by examining the
   `docker-compose.yml` file find the information needed to log into the database.
3. Confirm that the necessary calculations are visible in the database.

### Q4. Bigger picture

Sketch out the bigger picture. What parts are running on your computer, and
how do they interact with each other? If there is terminology or acronyms that
you don't understand, search for an explanation on the internet, and bring these
explanation(s) to class to help your fellow students.

### (Optional) Q5. WSGI

Whenever we've been running the flask app, we've seen the following scary message:

```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
```

Find out what a WSGI server is, and why it is recommended that we use one in
production. Now go ahead and change things so that we are using a WSGI server.

The following [page](https://smirnov-am.github.io/running-flask-in-production-with-docker/) is useful!

**Please commit your work to your PCW repo and push it to github before class!**
