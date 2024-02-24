# Fuel theft finder

Install the needed pip modules:

```
pip install mysql-connector-python pandas
```

Create a database called fuel. Create a new MySQL user and grant him privileges to the fuel database:

```
CREATE USER 'fuel'@'localhost' IDENTIFIED BY 'CHANGE_ME';
GRANT ALL PRIVILEGES ON fuel.* TO 'fuel'@'localhost' WITH GRANT OPTION;
```

Import the fuel database from the fuel.sql file:

```
mysql fuel < fuel.sql
```

Change the MySQL details in theft_finder.py:

```
db = mysql.connector.connect(user='fuel', password='CHANGE_ME', host='localhost', database='fuel')
```

Run the theft_finder.py:

```
python3 theft_finder.py
```

Toli
