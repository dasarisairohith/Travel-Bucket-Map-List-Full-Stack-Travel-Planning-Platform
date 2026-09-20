from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

trip_destinations = db.Table(
    "trip_destinations",
    db.Column("trip_id", db.Integer, db.ForeignKey("trips.id"), primary_key=True),
    db.Column("destination_id", db.Integer, db.ForeignKey("destinations.id"), primary_key=True),
)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    destinations = db.relationship("Destination", backref="user", cascade="all, delete-orphan")
    trips = db.relationship("Trip", backref="user", cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Destination(db.Model):
    __tablename__ = "destinations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(180), nullable=False)
    country = db.Column(db.String(120), default="")
    city = db.Column(db.String(120), default="")
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(60), default="Other")
    priority = db.Column(db.String(20), default="Medium")
    visited = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {k: getattr(self, k) for k in [
            "id","name","country","city","latitude","longitude",
            "category","priority","visited","notes"
        ]}

class Trip(db.Model):
    __tablename__ = "trips"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(180), nullable=False)
    description = db.Column(db.Text, default="")
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(30), default="Planned")
    destinations = db.relationship("Destination", secondary=trip_destinations, lazy="subquery")

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "description": self.description,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "status": self.status,
            "destinations": [d.to_dict() for d in self.destinations]
        }
