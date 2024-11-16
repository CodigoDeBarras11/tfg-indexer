from dipdup import fields
from dipdup.models import Model


class Holder(Model):
    id = fields.CharField(max_length=100, primary_key=True)
    address = fields.TextField()
    request = fields.TextField()
    accept_request = fields.BooleanField()
    current_cids = fields.JSONField()
    previous_info = fields.JSONField()
    price = fields.CharField(max_length=100)