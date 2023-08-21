# flask_web.py

from flask_sqlalchemy import SQLAlchemy
import json
from flask import Flask,request,render_template
app = Flask(__name__)


class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'root'
    password = 'ZAQ12wssd'
    database = 'tt_data'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@10.96.130.69:3306/%s' % (user,password,database)

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



@app.route('/',methods=['GET','POST'])
def hello():
    sql = ''
    # if request.method == 'POST':
    #     data = request.json
    #     try:
    #         sql = "insert into stat(host,mem_free,mem_usage,mem_total,load_avg,time) values ('%s',%d,%d,%d,'%s',%d)" % (data['Host'],data['MemFree'],data['MemUsage'],data['MemTotal'],data['LoadAvg'],int(data['Time']))
    #         ret = c.execute(sql)
    #     except mysql.IntegrityError:
    #         pass
    #     return 'OK'
    # else:
    #     c.execute('select time,mem_usage from stat')
    res = tt_ywdata_author_analysed.query.filter_by(author='.alice366').all()
    for r in res:
        tt_number = r.tt_number
    return render_template('mon.html',data=json.dumps(tt_number))


@app.route('/new',methods=['GET'])
def getnew():
    res = tt_ywdata_author_analysed.query.filter_by(author='.alice366').all()
    for r in res:
        tt_number = r.tt_number
    return json.dumps(tt_number)




app.run(port=8888,debug=True)