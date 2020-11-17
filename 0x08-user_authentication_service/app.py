#!/usr/bin/env python3
"""Flask App"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def main():
    """Main execute"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def get_user():
    """Get an user"""
    email = request.form.get('email')
    pwd = request.form.get('password')

    if email is None or pwd is None:
        abort(400)

    try:
        user = AUTH.register_user(email=email, password=pwd)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    else:
        return jsonify({
            "email": f"{user.email}",
            "message": "user created"
        }), 200


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Create a session
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if email is None or pwd is None:
        abort(401)

    if AUTH.valid_login(email=email, password=pwd) is False:
        abort(401)

    session = AUTH.create_session(email=email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")