from dipdup.context import HandlerContext
from dipdup.models.tezos import TezosBigMapDiff
from indexer_v9 import models as models
from indexer_v9.types.tz_svl.tezos_big_maps.svls_key import SvlsKey
from indexer_v9.types.tz_svl.tezos_big_maps.svls_value import SvlsValue


async def on_update(
    ctx: HandlerContext,
    svls: TezosBigMapDiff[SvlsKey, SvlsValue],
) -> None:
    if not svls.key: return
    svl_id = svls.key.root
    owner_address = svls.value.owner
    prev_owners_info = svls.value.prev_owners_info
    curr_owner_info = svls.value.curr_owner_info
    p_i = []
    for o in prev_owners_info:
        p_i.append({'address': o.address, 'cids': o.list})
    price = svls.value.price
    request = svls.value.request
    acceptRequest = svls.value.acceptRequest
    ctx.logger.info(f"svl_id:{svl_id}")
    ctx.logger.info(f"Owner address:{owner_address}")
    ctx.logger.info(f"Previous owners info:{p_i}")
    ctx.logger.info(f"Current owner info:{curr_owner_info}")
    ctx.logger.info(f"Price:{price}")
    ctx.logger.info(f"Request:{request}")
    ctx.logger.info(f"Accepted request:{acceptRequest}")
    holder = await models.Holder.get_or_none(id=id)
    if holder is None:
        await models.Holder.create(
            id=svl_id, 
            address=owner_address,
            prev_owners_info=p_i,
            curr_owner_info=curr_owner_info,
            price=price,
            request=request,
            accept_request=acceptRequest
        )
    else:
        holder.address = owner_address
        holder.prev_owners_info = p_i
        holder.curr_owner_info = curr_owner_info
        holder.request = request
        holder.accept_request = acceptRequest
        await holder.save()
