from sqlalchemy import Column, VARCHAR, text
from sqlalchemy.orm import relationship

from model import Base


class User(Base):
    __tablename__ = 'user'

    nick = Column(VARCHAR(20), primary_key=True)
    password = Column(VARCHAR(255), nullable=True)
    name = Column(VARCHAR(20), nullable=True)
    post = relationship("Post", cascade="all,delete", backref="user")
