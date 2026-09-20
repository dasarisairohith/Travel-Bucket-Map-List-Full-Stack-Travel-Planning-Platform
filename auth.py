from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .. import db
from ..models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    data = request.get_json() or {}
    name, email, password = data.get("name"), data.get("email"), data.get("password")
    if not all([name, email, password]):
        return {"error": "name, email and password are required"}, 400
    if User.query.filter_by(email=email.lower()).first():
        return {"error": "Email already registered"}, 409
    user = User(name=name.strip(), email=email.lower().strip())
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return {"message": "Account created"}, 201

@auth_bp.post("/login")
def login():
    data = request.get_json() or {}
    user = User.query.filter_by(email=(data.get("email") or "").lower()).first()
    if not user or not user.check_password(data.get("password", "")):
        return {"error": "Invalid email or password"}, 401
    token = create_access_token(identity=str(user.id))
    return {"access_token": token, "user": {"id": user.id, "name": user.name, "email": user.email}}

@auth_bp.get("/me")
@jwt_required()
def me():
    user = User.query.get(int(get_jwt_identity()))
    return {"id": user.id, "name": user.name, "email": user.email}
