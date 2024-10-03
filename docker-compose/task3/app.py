from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Get database connection parameters from environment variables
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

# Function to create a database connection
def get_db_connection(db_name=None):
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=db_name if db_name else None  # Connect to the specific database if provided
    )
    return conn

# Function to initialize the database and table
def initialize_database():
    try:
        # Connect without specifying a database to create the database if it doesn't exist
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.commit()

        # Now connect to the specific database
        conn.database = DB_NAME

        # Create the users table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            surname VARCHAR(100),
            email VARCHAR(100)
        );
        """
        cursor.execute(create_table_query)
        conn.commit()

        cursor.close()
        conn.close()

        print("Database and table initialized successfully.")

    except mysql.connector.Error as err:
        print(f"Error initializing database: {err}")

# Route to save user data
@app.route('/save_user', methods=['POST'])
def save_user():
    user_data = request.get_json()

    # Check if required fields are present
    if 'name' in user_data and 'surname' in user_data and 'email' in user_data:
        try:
            conn = get_db_connection(DB_NAME)
            cursor = conn.cursor()
            
            # SQL query to insert user data
            insert_query = "INSERT INTO users (name, surname, email) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (user_data['name'], user_data['surname'], user_data['email']))
            
            # Commit changes to the database
            conn.commit()
            
            cursor.close()
            conn.close()
            
            return jsonify({"message": "User information saved."}), 200
        except mysql.connector.Error as err:
            return jsonify({"error": str(err)}), 500
    else:
        return jsonify({"error": "Invalid input. Must contain 'name', 'surname', and 'email'."}), 400

if __name__ == '__main__':
    # Initialize the database and table before starting the app
    initialize_database()

    # Run the application
    app.run(host='0.0.0.0', port=3000)
