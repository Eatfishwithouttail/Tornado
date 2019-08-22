

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://root:19960207@118.178.180.116:3306/lm')


#生成数据库连接的类
DbSession = sessionmaker(bind=engine)
#创建了一个会话类对象
session = DbSession()

#生成所有模型的父类
Base = declarative_base(bind=engine)


