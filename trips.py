from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models import Trip, Destination

trips_bp = Blueprint("trips", __name__)

def uid(): return int(get_jwt_identity())

@trips_bp.get("")
@jwt_required()
def list_trips():
    return [t.to_dict() for t in Trip.query.filter_by(user_id=uid()).all()]

@trips_bp.post("")
@jwt_required()
def create_trip():
    data = request.get_json() or {}
    if not data.get("name"): return {"error":"Trip name required"},400
    t=Trip(user_id=uid(), name=data["name"], description=data.get("description",""),
           status=data.get("status","Planned"))
    if data.get("start_date"): t.start_date=date.fromisoformat(data["start_date"])
    if data.get("end_date"): t.end_date=date.fromisoformat(data["end_date"])
    db.session.add(t); db.session.commit()
    return t.to_dict(),201

@trips_bp.put("/<int:id>")
@jwt_required()
def update_trip(id):
    t=Trip.query.filter_by(id=id,user_id=uid()).first_or_404()
    data=request.get_json() or {}
    for f in ["name","description","status"]:
        if f in data: setattr(t,f,data[f])
    for f in ["start_date","end_date"]:
        if f in data: setattr(t,f,date.fromisoformat(data[f]) if data[f] else None)
    db.session.commit(); return t.to_dict()

@trips_bp.delete("/<int:id>")
@jwt_required()
def delete_trip(id):
    t=Trip.query.filter_by(id=id,user_id=uid()).first_or_404()
    db.session.delete(t); db.session.commit()
    return {"message":"Trip deleted"}

@trips_bp.post("/<int:trip_id>/destinations/<int:destination_id>")
@jwt_required()
def add_destination(trip_id,destination_id):
    t=Trip.query.filter_by(id=trip_id,user_id=uid()).first_or_404()
    d=Destination.query.filter_by(id=destination_id,user_id=uid()).first_or_404()
    if d not in t.destinations: t.destinations.append(d)
    db.session.commit(); return t.to_dict()

@trips_bp.delete("/<int:trip_id>/destinations/<int:destination_id>")
@jwt_required()
def remove_destination(trip_id,destination_id):
    t=Trip.query.filter_by(id=trip_id,user_id=uid()).first_or_404()
    d=Destination.query.filter_by(id=destination_id,user_id=uid()).first_or_404()
    if d in t.destinations: t.destinations.remove(d)
    db.session.commit(); return t.to_dict()
