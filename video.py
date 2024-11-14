from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from models import db, Video
from flask_jwt_extended import jwt_required

video_bp = Blueprint('video', __name__)


@video_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_video():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join('static/uploads', filename)
    file.save(filepath)

    new_video = Video(filename=filename)
    db.session.add(new_video)
    db.session.commit()

    return jsonify({"message": "Video uploaded successfully"}), 201
