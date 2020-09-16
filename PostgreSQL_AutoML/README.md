# PostgreSQL integration with AutoML


Set up example database:
```
docker build -t mydb:latest .
docker run --name my_local_db -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=db -p 5555:5432 mydb:latest
```

Create table and insert training data:
```
python init_db.py
```

Train AutoML:
```
python train_automl.py
```

Insert test records:
```
python insert_test_records.py
```

Compute predictions with AutoML and insert into the database:
```
python predict.py
```

