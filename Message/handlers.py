import tornado.web
from marshmallow import fields

from models import MessageInfo
from schema import MessageInfoSchema
from settings import DBSession
from webargs.tornadoparser import TornadoParser
paser = TornadoParser()
use_args = paser.use_args
use_kwargs = paser.use_kwargs


class BaseHandler(tornado.web.RequestHandler):
    """handler基类"""
    @property
    def session(self):
        if hasattr(self, "_session"):
            return self._session

        self._session = DBSession()
        return self._session


class MainHandler(BaseHandler):
    """留言信息入参"""

    def get(self):
        session = self.session
        result = session.query(MessageInfo).first()
        if not result:
            self.render("index.html", name="", email="", address="", message="")
        else:
            self.render("index.html", name=result.name, email=result.email, address=result.address, message=result.message)


class AddMessageHandler(BaseHandler):
    @use_kwargs(MessageInfoSchema)
    def post(self, name: str, email: str, address: str, message: str):
        session = self.session
        message_ = MessageInfo(
            name=name,
            email=email,
            address=address,
            message=message
        )
        session.add(message_)
        session.flush()
        session.commit()
        self.render("index.html", name=name, email=email, address=address, message=message)