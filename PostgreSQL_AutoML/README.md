

docker run --name my_local_db -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=db -p 5555:5432 mydb:latest


docker build -t mydb:latest .

