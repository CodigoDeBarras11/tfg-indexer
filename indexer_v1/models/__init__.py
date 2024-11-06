from dipdup import fields
from dipdup.models import Model


class Holder(Model):
    id = fields.CharField(max_length=100, primary_key=True)
    address = fields.TextField()
    svl_cid = fields.CharField(max_length=100)

