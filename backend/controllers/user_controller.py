from flask import Blueprint, request, jsonify, abort, current_app
from models.user import User

blueprint = Blueprint('user', __name__, url_prefix='/api/v1')


@blueprint.route('/user/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    """
    # Get data from request body
    request_data = request.get_json()

    # Check if required parameters are present
    required_params = ['email', 'password', 'preferences']
    missing_params = [param for param in required_params if param not in request_data]
    if missing_params:
        abort(400, f"Missing required parameter(s): {', '.join(missing_params)}")

    # Create a new user object
    new_user = User(
        email=request_data['email'],
        password=request_data['password'],
        preferences=request_data['preferences']
    )

    current_app.logger.info(f"New user registered: {new_user.email}")

    # Save the user to db
    is_created = new_user.save_to_db()

    if is_created:
        current_app.logger.info("User registered successfully")
        return jsonify({'message': 'User registered successfully'}), 201
    else:
        current_app.logger.error("User registration failed")
        return jsonify({'message': 'User registration failed'}), 409


@blueprint.route('/user/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    """
    request_data = request.get_json()

    required_params = ['email', 'password']
    missing_params = [param for param in required_params if param not in request_data]
    if missing_params:
        abort(400, f"Missing required parameter(s): {', '.join(missing_params)}")

    current_app.logger.info(f"User attempted login: {request_data['email']}")

    logged_in = User.login(request_data['email'], request_data['password'])

    if logged_in:
        current_app.logger.info("User logged in successfully")
        return jsonify({'message': 'User logged in successfully'}), 200
    else:
        current_app.logger.error("User logged in failed")
        return jsonify({'message': 'Incorrect email or password'}), 401
