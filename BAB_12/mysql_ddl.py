import mysql.connector

def main():
    mariadb_connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "1untuksemua",
    database="toko1")
    
    
    cur = mariadb_connection.cursor()

    ddl = """
        CREATE TABLE PRODUCTS (
            product_id INT NOT NULL PRIMARY KEY,
            name VARCHAR(50),
            category VARCHAR(30),
            price INTEGER,
            stock INTEGER
        )
        """