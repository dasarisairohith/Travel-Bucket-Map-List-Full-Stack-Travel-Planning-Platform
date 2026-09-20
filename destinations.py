from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models import Destination

destinations_bp = Blueprint("destinations", __name__)

def current_user_id():
    return int(get_jwt_identity())

@destinations_bp.get("")
@jwt_required()
def list_destinations():
    items = Destination.query.filter_by(user_id=current_user_id()).order_by(Destination.created_at.desc()).all()
    return [d.to_dict() for d in items]

@destinations_bp.post("")
@jwt_required()
def create_destination():
    data = request.get_json() or {}
    required = ["name", "latitude", "longitude"]
    if any(data.get(x) is None for x in required):
        return {"error": "name, latitude and longitude are required"}, 400
    d = Destination(
        user_id=current_user_id(),
        name=data["name"], country=data.get("country",""), city=data.get("city",""),
        latitude=float(data["latitude"]), longitude=float(data["longitude"]),
        category=data.get("category","Other"), priority=data.get("priority","Medium"),
        visited=bool(data.get("visited",False)), notes=data.get("notes","")
    )
    db.session.add(d); db.session.commit()
    return d.to_dict(), 201

@destinations_bp.get("/<int:id>")
@jwt_required()
def get_destination(id):
    d = Destination.query.filter_by(id=id, user_id=current_user_id()).first_or_404()
    return d.to_dict()

@destinations_bp.put("/<int:id>")
@jwt_required()
def update_destination(id):
    d = Destination.query.filter_by(id=id, user_id=current_user_id()).first_or_404()
    data = request.get_json() or {}
    for field in ["name","country","city","category","priority","notes"]:
        if field in data: setattr(d, field, data[field])
    for field in ["latitude","longitude"]:
        if field in data: setattr(d, field, float(data[field]))
    if "visited" in data: d.visited = bool(data["visited"])
    db.session.commit()
    return d.to_dict()

@destinations_bp.delete("/<int:id>")
@jwt_required()
def delete_destination(id):
    d = Destination.query.filter_by(id=id, user_id=current_user_id()).first_or_404()
    db.session.delete(d); db.session.commit()
    return {"message": "Destination deleted"}
