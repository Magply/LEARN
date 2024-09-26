from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Path to the file where user information will be stored
FILE_PATH = './users.txt'

@app.route('/save_user', methods=['POST'])
def save_user():
    # Get user information in JSON format from the request body
    user_data = request.get_json()
    
    # Check if all required fields are present
    if 'name' in user_data and 'surname' in user_data and 'email' in user_data:
        with open(FILE_PATH, 'a') as f:
            f.write(json.dumps(user_data) + '\n')  # Append the user data as a JSON string to users.txt
        return jsonify({"message": "User information saved."}), 200
    else:
        return jsonify({"error": "Invalid input. Must contain 'name', 'surname', and 'email'."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
