from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ZAQ12wssd@10.96.130.69:3306/tt_data?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

TT_YWData_Session = sessionmaker(bind=tt_ywdata_engine)
TT_YWData_Base = declarative_base(tt_ywdata_engine)

class tt_ywdata_author_analysed(TT_YWData_Base):
    __tablename__ = "author_analysed"
    author = Column(String(255), primary_key=True, nullable=False)
    author_id = Column(BIGINT)
    tt_number = Column(Integer)
    tt_zh_number = Column(Integer)
    cluster_bad_number = Column(Integer)
    bert_bad_number = Column(Integer)
    keyword_bad_number = Column(Integer)
    desc = Column(String(128))
    save_time = Column(Integer)
    from_src = Column(String(128))
    score = Column(Integer)