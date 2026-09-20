from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import func
from ..models import Destination, Trip

dashboard_bp=Blueprint("dashboard",__name__)

@dashboard_bp.get("/stats")
@jwt_required()
def stats():
    uid=int(get_jwt_identity())
    q=Destination.query.filter_by(user_id=uid)
    destinations=q.count()
    visited=q.filter_by(visited=True).count()
    trips=Trip.query.filter_by(user_id=uid).count()
    countries=q.with_entities(Destination.country).filter(Destination.country!="").distinct().count()
    return {"destinations":destinations,"visited":visited,"wishlist":destinations-visited,"trips":trips,"countries":countries}
