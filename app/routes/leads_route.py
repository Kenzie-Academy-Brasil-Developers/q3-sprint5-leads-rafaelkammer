from flask import Blueprint
from app.controllers import leads_controller

bp = Blueprint("leads", __name__, url_prefix="/leads")

bp.get("")(leads_controller.get_leads)
bp.get("/<int:lead_email>")(leads_controller.get_lead_by_email)
bp.post("")(leads_controller.create_lead)
bp.patch("/<lead_email>")(leads_controller.update_lead)
bp.delete("/<lead_email>")(leads_controller.delete_lead)