from sqlalchemy.orm import relationship
from sqlalchemy import Column, VARCHAR, Integer, DATETIME, text, ForeignKey, Boolean

from model import Base


class Post(Base):
    __tablename__ = 'post'

    id_pk = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(20), nullable=False)
    content = Column(VARCHAR(255), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    inherence = Column(VARCHAR(20), nullable=False)
    url = Column(VARCHAR(255))
    Favorites = Column(Boolean(), nullable=False)
    user_nick = Column(VARCHAR(20), ForeignKey('user.nick'))
