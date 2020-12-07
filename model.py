from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///sqlite.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()


class UserInfo(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer)
    nu_caller_m = Column(Integer,default=0)
    nu_caller= Column(Integer)
    is_active = Column(Boolean)
    time_active=Column(Integer,default=0)

    def __init__(self, name, user_id, nu_caller, is_active):
        self.name = name
        self.user_id = user_id
        self.nu_caller = nu_caller
        self.is_active = is_active


class Invited(Base):
    __tablename__ = "invited"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user_info.id'))
    user_info = relationship(UserInfo)

    def __init__(self, name, user_info):
        self.name = name
        self.user_info = user_info


Base.metadata.create_all(engine)








