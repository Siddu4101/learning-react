# first get pull the postgres and run with below commands
# docker pull postgres:17
# docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:17
# to run in a network create the network and then while running postgres and connection between containers use --network <network_name>
# docker network create mynetwork
# docker network ls ( to view ur networks)
# docker run --name postgres -e POSTGRES_PASSWORD=postgres --network mynetwork -p 5432:5432 -d postgres:17

#now create a image for the python app
FROM python:3.13.6

#work directory
WORKDIR /connection-between-two-containers

# install dependencies
RUN pip install psycopg2

# copy the rest of the application code
COPY . /connection-between-two-containers/

# command to run the application
CMD ["python", "connect-to-database.py"]

# to run this image
# docker build -t connection-between-two-containers:1.0.0 .
# docker run -it --rm --name connection-between-two-containers connection-between-two-containers:1.0.0
#to run with network
# docker run -it --rm --name connection-between-two-containers --network mynetwork connection-between-two-containers:1.0.0