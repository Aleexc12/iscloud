from flask import Flask, jsonify, request
import psycopg2  # La importación "psycopg2"

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="mysecretpassword"
    )
    return conn

@app.route('/')
def index():
    return "Hello, Flask with PostgreSQL!"

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    new_user = request.json['name']
    cursor.execute('INSERT INTO users (name) VALUES (%s);', (new_user,))
    conn.commit()
    cursor.close()
    conn.close()
    return f"User {new_user} added successfully", 201

if __name__ == '__main__':
    app.run(debug=True)
