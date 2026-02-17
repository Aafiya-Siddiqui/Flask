from flask import Flask, jsonify, request

app = Flask(__name__)

# Line 3: Ensure the variable name is 'users' (plural)
users = [
    {"id": 1, "name": "Amit", "email": "amit@example.com"},
    {"id": 2, "name": "Asha", "email": "asha@example.com"}
]

@app.route('/user', methods=['GET'])
def get_user():
    # Return the plural 'users' list
    return jsonify(users), 200

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1, 
        "name": data['name'], 
        "email": data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id): # Added user_id parameter here
    # Use 'users' (plural) for the generator expression
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    data = request.get_json()
    user.update({
        "name": data.get('name', user['name']),
        "email": data.get('email', user['email'])
    })
    return jsonify(user), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": "user deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)