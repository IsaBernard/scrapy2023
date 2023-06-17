import mysql.connector
import configparser

# Read the MySQL connection details from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

host = config.get('mysql', 'host')
user = config.get('mysql', 'user')
password = config.get('mysql', 'password')
database = config.get('mysql', 'database')

# Create a connection to MySQL
try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connected to MySQL!")

    # Perform a sample query
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()[0]
    print(f"MySQL version: {version}")

    # Close the connection
    conn.close()

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
