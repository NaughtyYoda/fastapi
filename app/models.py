from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base


class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key=True, nullable=False)
    post_title = Column(String, nullable=False)
    post_content = Column(String, nullable=False)
    post_published = Column(Boolean, server_default='TRUE', nullable=False)
    post_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
    #n_votes = relationship("Vote")

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, nullable=False)
    user_email = Column(String, nullable=False, unique=True)
    user_password = Column(String, nullable=False)
    user_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = 'votes'
    post_id = Column(Integer, ForeignKey("posts.post_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True, nullable=False)


