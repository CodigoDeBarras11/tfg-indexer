from dipdup import fields
from dipdup.models import Model

class Holder(Model):
    id = fields.CharField(max_length=100, primary_key=True)
    address = fields.TextField()
    vin = fields.TextField()
    request = fields.TextField()
    accept_request = fields.BooleanField()
    prev_owners_info = fields.JSONField()
    curr_owner_info = fields.JSONField()
    price = fields.CharField(max_length=100)