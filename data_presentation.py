from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ZAQ12wssd@10.96.130.69:3306/tt_data?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TT_YWData_Session = sessionmaker(bind=tt_ywdata_engine)
# TT_YWData_Base = declarative_base(tt_ywdata_engine)



class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'root'
    password = 'ZAQ12wssd'
    database = 'tt_data'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user,password,database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

class tt_ywdata_author_analysed(db.Model):
    __tablename__ = "author_analysed"
    author = db.Column(db.String(255), primary_key=True, nullable=False)
    author_id = db.Column(db.BIGINT)
    tt_number = db.Column(db.Integer)
    tt_zh_number = db.Column(db.Integer)
    cluster_bad_number = db.Column(db.Integer)
    bert_bad_number = db.Column(db.Integer)
    keyword_bad_number = db.Column(db.Integer)
    desc = db.Column(db.String(128))
    save_time = db.Column(db.Integer)
    from_src = db.Column(db.String(128))
    score = db.Column(db.Integer)

res = tt_ywdata_author_analysed.query.filter_by(author='wang').all()