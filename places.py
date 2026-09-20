import requests
from flask import Blueprint, request, current_app
from flask_jwt_extended import jwt_required

places_bp=Blueprint("places",__name__)

@places_bp.get("/search")
@jwt_required()
def search():
    query=request.args.get("q","").strip()
    key=current_app.config.get("GOOGLE_MAPS_API_KEY")
    if not query: return {"results":[]}
    if not key: return {"results":[],"message":"Configure GOOGLE_MAPS_API_KEY to enable Google Places search."}
    url="https://maps.googleapis.com/maps/api/place/textsearch/json"
    r=requests.get(url,params={"query":query,"key":key},timeout=10)
    r.raise_for_status()
    return r.json()
