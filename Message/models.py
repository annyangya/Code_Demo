from sqlalchemy import Column, Integer, String

from settings import MapBase


class MessageInfo(MapBase):
    __tablename__ = "message_info"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False, comment="用户名")
    email = Column(String(50), nullable=False, comment="用户邮箱")
    address = Column(String(200), nullable=True, default="", comment="用户地址")
    message = Column(String(500), nullable=True, default="", comment="建议")


def init_db():
    MapBase.metadata.create_all()
    print("init db success")
    return True