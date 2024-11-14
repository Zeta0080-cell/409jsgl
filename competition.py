from flask import Blueprint, request, jsonify
from models import db, Competition
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

competition_bp = Blueprint('competition', __name__)


@competition_bp.route('/submit', methods=['POST'])
@jwt_required()
def submit_competition():
    data = request.get_json()
    user_identity = get_jwt_identity()
    user_id = user_identity['id']

    name = data.get('name')
    category = data.get('category')
    instructor = data.get('instructor')
    award_date = datetime.strptime(data.get('award_date'), '%Y-%m-%d')
    award_certificate = data.get('award_certificate')

    new_competition = Competition(
        name=name,
        category=category,
        instructor=instructor,
        award_date=award_date,
        award_certificate=award_certificate,
        user_id=user_id
    )

    db.session.add(new_competition)
    db.session.commit()

    return jsonify({"message": "Competition submitted successfully"}), 201


@competition_bp.route('/list', methods=['GET'])
@jwt_required()
def get_competitions():
    user_identity = get_jwt_identity()
    user_id = user_identity['id']

    competitions = Competition.query.filter_by(user_id=user_id).all()
    competitions_data = [{
        "name": comp.name,
        "category": comp.category,
        "instructor": comp.instructor,
        "award_date": comp.award_date.strftime('%Y-%m-%d'),
        "award_certificate": comp.award_certificate
    } for comp in competitions]

    return jsonify({"competitions": competitions_data}), 200