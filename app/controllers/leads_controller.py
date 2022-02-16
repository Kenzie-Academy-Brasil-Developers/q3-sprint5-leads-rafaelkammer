from sqlalchemy.orm.session import Session
from flask import request, jsonify

from http import HTTPStatus
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError

from app.models.leads_model import Lead
from app.configs.database import db

import re
from datetime import datetime

def get_lead_by_email(lead_email: int):
    session: Session = db.session
    base_query = session.query(Lead)
    try:
        lead = base_query.filter_by(email=lead_email).first_or_404(
            description="email not found"
        )
    except NotFound as e:
        return {"error": e.description}, HTTPStatus.NOT_FOUND

    return jsonify(lead), HTTPStatus.OK


def get_leads():
    session: Session = db.session
    base_query = session.query(Lead)

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 3, type=int)
    leads = base_query.order_by(Lead.visits).paginate(page, per_page)

    if not leads.items:
        return {"error": "no data found"}

    return jsonify(leads.items), HTTPStatus.OK


def create_lead():
    data = request.get_json()

    for value in data.values():
        if type(value) != type("string"):
            return {"error": "All fields must be on string format"}, HTTPStatus.BAD_REQUEST
    
    default_keys = ["name", "email", "phone"]

    for key in default_keys:
        if key not in data.keys():
            return {"error": f"Incomplete request, check {key} field"}, HTTPStatus.BAD_REQUEST

    for key in data.keys():
        if key not in default_keys:
            return {"error": f"Incomplete request, check {key} field"}, HTTPStatus.BAD_REQUEST

    phone_regex = "\([1-9]\d\)\s?\d{5}-\d{4}"
    validated_phone = re.fullmatch(phone_regex, data["phone"])

    if not validated_phone:
        return {"error": "Wrong phone format"}, HTTPStatus.BAD_REQUEST

    try:
        lead = Lead(**data)

        db.session.add(lead)
        db.session.commit()

    except IntegrityError:
        return {"error": "user already registred"}, HTTPStatus.CONFLICT
    
    return jsonify(lead), HTTPStatus.CREATED

def update_lead():
    data = request.get_json()
    session: Session = db.session
    base_query = session.query(Lead)

    lead = base_query.filter_by(email=data["email"]).first()

    if not lead:
        return {"error": "email not found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(lead, key, value)
    setattr(lead, "visits",( lead.__dict__["visits"] + 1))
    setattr(lead, "last_visit", datetime.now())
    
    session.add(lead)
    session.commit()

    return "", HTTPStatus.OK

def delete_lead():
    data = request.get_json()
    session: Session = db.session
    base_query = session.query(Lead)

    lead = base_query.filter_by(email=data["email"]).first()

    if not lead:
        return {"error": "email not found"}, HTTPStatus.NOT_FOUND

    session.delete(lead)
    session.commit()

    return "", HTTPStatus.NO_CONTENT