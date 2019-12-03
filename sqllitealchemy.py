#sqllitealchemy.txt
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///:memory:', echo=False)

Base = declarative_base()

# 定义映射类User，其继承上一步创建的Base
class User(Base):
    # 指定本类映射到users表
    __tablename__ = 'users'
    
    # 指定id映射到id字段; id字段为整型，为主键
    id = Column(Integer, primary_key=True)
    # 指定name映射到name字段; name字段为字符串类形，
    name = Column(String(20))
    fullname = Column(String(32))
    password = Column(String(32))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                   self.name, self.fullname, self.password)

# 查看映射对应的表
User.__table__

# 创建数据表
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

# engine是2.2中创建的连接
Session = sessionmaker(bind=engine)

# 创建Session类实例
session = Session()

# 创建User类实例
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

# 将该实例插入到users表
session.add(ed_user)

# 一次插入多条记录形式
session.add_all(
    [User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')]
)

# 当前更改只是在session中，需要使用commit确认更改才会写入数据库
session.commit()

table_and_column_name = User
filter = (User.name=='ed')

our_user = session.query(table_and_column_name).filter(filter).first()
print(our_user)



# 正常的SQL语句
sql = "select * from users"

# sqlalchemy使用execute方法直接执行SQL
records = session.execute(sql)
for x in records:
    print(x)

