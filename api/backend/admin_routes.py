from flask import Blueprint, request, jsonify, make_response, current_app
from db_connection import db

# Create a new Blueprint object for admin routes
admins = Blueprint("admins", __name__)

# ------------------------------------------------------------
# Get all system logs
@admins.route("/logs", methods=["GET"])
def get_logs():
    current_app.logger.info("GET /logs route")
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM SYSTEM_LOG")
    logs = cursor.fetchall()
    response = make_response(jsonify(logs))
    response.status_code = 200
    return response


# ------------------------------------------------------------
# Get all users in the system
@admins.route("/users", methods=["GET"])
def get_users():
    current_app.logger.info("GET /users route")
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM SYSTEM_USER")
    users = cursor.fetchall()
    response = make_response(jsonify(users))
    response.status_code = 200
    return response


# ------------------------------------------------------------
# Update the encryption settings
@admins.route("/encryption", methods=["PUT"])
def update_encryption_settings():
    current_app.logger.info("PUT /encryption route")
    data = request.get_json()
    parameter = data.get('parameter')
    value = data.get('value')

    cursor = db.get_db().cursor()
    cursor.execute(
        "UPDATE ENCRYPTION_SETTINGS SET Value = %s WHERE Parameter = %s", (value, parameter)
    )
    db.get_db().commit()

    response = make_response(jsonify({"message": "Encryption settings updated."}))
    response.status_code = 200
    return response


# ------------------------------------------------------------
# Delete a system user
@admins.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    current_app.logger.info(f"DELETE /users/{user_id} route")
    cursor = db.get_db().cursor()
    cursor.execute("DELETE FROM SYSTEM_USER WHERE UserID = %s", (user_id,))
    db.get_db().commit()

    response = make_response(jsonify({"message": f"User {user_id} deleted."}))
    response.status_code = 200
    return response
