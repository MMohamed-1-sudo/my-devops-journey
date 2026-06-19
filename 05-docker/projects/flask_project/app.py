from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="mysql-db",
        user="root",
        password="rootpass",
        database="mydb"
    )

@app.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")
    cursor.execute("INSERT INTO test (name) VALUES ('Hello from Flask')")
    conn.commit()

    cursor.execute("SELECT * FROM test")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return str(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)