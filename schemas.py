import uuid
from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    id = fields.UUID(dump_only=True, default=lambda: uuid.uuid4().hex)
    name = fields.String(required=True, allow_none=False, validate=validate.Length(min=2, max=80))
    price = fields.Float(required=True, allow_none=False, validate=validate.Range(min=0))
    description = fields.String(required=True, allow_none=False, validate=validate.Length(min=2, max=150))
    inventory = fields.Int(required=True, allow_none=False, validate=validate.Range(min=0))

    class Meta:
        fields = ('id', 'name', 'price', 'description', 'inventory')
        ordered = True


class ProductEditSchema(Schema):
    name = fields.String(required=False, allow_none=False, validate=validate.Length(min=2, max=80))
    price = fields.Float(required=False, allow_none=False, validate=validate.Range(min=0))
    description = fields.String(required=False, allow_none=False, validate=validate.Length(min=2, max=150))
    inventory = fields.Int(required=False, allow_none=False, validate=validate.Range(min=0))

    class Meta:
        fields = ('id', 'name', 'price', 'description', 'inventory')
        ordered = True
