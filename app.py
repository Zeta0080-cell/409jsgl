from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
from routes.auth import auth_bp
from routes.competition import competition_bp
from routes.video import video_bp

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)  # 允许跨域请求
db.init_app(app)  # 初始化数据库
jwt = JWTManager(app)  # 初始化 JWT 扩展

# 注册蓝图
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(competition_bp, url_prefix='/competition')
app.register_blueprint(video_bp, url_prefix='/video')

if __name__ == '__main__':
    app.run(debug=True)
