from dipdup.context import HandlerContext
from dipdup.models.tezos import TezosBigMapDiff
from indexer_v7 import models as models
from indexer_v7.types.tz_svl.tezos_big_maps.svls_key import SvlsKey
from indexer_v7.types.tz_svl.tezos_big_maps.svls_value import SvlsValue


async def on_update(
    ctx: HandlerContext,
    svls: TezosBigMapDiff[SvlsKey, SvlsValue],
) -> None:
    if not svls.key: return

    id = svls.key
    owner_address = svls.value.owner
    owners_info = svls.value.owners_info
    o_i = []
    for o in owners_info:
        ctx.logger.info(f"oooooooooo:{o}")
        o_i.append({'address': o.address, 'cids': o.list})
    price = svls.value.price
    request = svls.value.request
    acceptRequest = svls.value.acceptRequest
    ctx.logger.info(f"id:{id}")
    ctx.logger.info(f"Owner address:{owner_address}")
    ctx.logger.info(f"Owners info:{o_i}")
    ctx.logger.info(f"Price:{price}")
    ctx.logger.info(f"Request:{request}")
    ctx.logger.info(f"Accepted request:{acceptRequest}")

    holder = await models.Holder.get_or_none(id=id)
    if holder is None:
        await models.Holder.create(
            id=id, 
            address=owner_address,
            owners_info=o_i,
            price=price,
            request=request,
            accept_request=acceptRequest
        )
    else:
        holder.address = owner_address
        holder.owners_info = o_i
        holder.request = request
        holder.accept_request = acceptRequest
        await holder.save()
