from marshmallow import Schema, fields


class MessageInfoSchema(Schema):
    """留言信息入参"""
    name = fields.String(required=True)
    email = fields.String(required=True)
    address = fields.String(required=False, missing="")
    message = fields.String(required=False, missing="")