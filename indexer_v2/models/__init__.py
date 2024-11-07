from dipdup import fields
from dipdup.models import Model


class Holder(Model):
    id = fields.CharField(max_length=100, primary_key=True)
    address = fields.TextField()
    current_cids = fields.JSONField()
    previous_info = fields.JSONField(null=True)
    price = fields.CharField(max_length=100)