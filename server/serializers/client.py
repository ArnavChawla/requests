""" Module containing client schema implementation """
from marshmallow import fields
from .base import BaseSchema
from middleware.validations import (validate_string_length, validate_url)


class ClientSchema(BaseSchema):
    """
    Serialization specification for client schema
    """
    username = fields.String(validate=validate_string_length(60),
                             required=True)
    avatar_url = fields.String(
        validate=[validate_string_length(250), validate_url], required=True)
