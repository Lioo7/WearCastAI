from flask import Blueprint, request, jsonify, abort, current_app
from models.user import User

blueprint = Blueprint('user', __name__, url_prefix='/api/v1')


@blueprint.route('/user/register', methods=['POST'])
def register():
    # Get data from request body
    request_data = request.get_json()

    # Check if required parameters are present
    required_params = ['username', 'email', 'password', 'preferences']
    missing_params = [param for param in required_params if param not in request_data]
    if missing_params:
        abort(400, f"Missing required parameter(s): {', '.join(missing_params)}")

    # Create a new user object
    new_user = User(
        username=request_data['username'],
        email=request_data['email'],
        password=request_data['password'],
        preferences=request_data['preferences']
    )

    # Log the username of the new user
    current_app.logger.info(f"New user registered: {new_user.username}")

    # Save the user to Firebase
    new_user.save_to_db()

    return jsonify({'message': 'User registered successfully'}), 201
