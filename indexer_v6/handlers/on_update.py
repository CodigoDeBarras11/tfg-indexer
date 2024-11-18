from dipdup.context import HandlerContext
from dipdup.models.tezos import TezosBigMapDiff
from indexer_v6 import models as models
from indexer_v6.types.tz_svl.tezos_big_maps.svls_key import SvlsKey
from indexer_v6.types.tz_svl.tezos_big_maps.svls_value import SvlsValue

async def on_update(
    ctx: HandlerContext,
    svls: TezosBigMapDiff[SvlsKey, SvlsValue],
) -> None:
    if not svls.key: return

    id = svls.key
    owner_address = svls.value.owner
    current_cids = svls.value.current_cids
    previous_info = svls.value.previous_info
    p_i = []
    for o in previous_info:
        ctx.logger.info(f"oooooooooo:{o}")
        p_i.append({'address': o.address,
                    'cids': o.list    
                    })
    price = svls.value.price
    request = svls.value.request
    acceptRequest = svls.value.acceptRequest
    ctx.logger.info(f"id:{id}")
    ctx.logger.info(f"Owner address:{owner_address}")
    ctx.logger.info(f"Current CIDs:{current_cids}")
    ctx.logger.info(f"Previous info:{p_i}")
    ctx.logger.info(f"Price:{price}")
    ctx.logger.info(f"Request:{request}")
    ctx.logger.info(f"Accepted request:{acceptRequest}")

    holder = await models.Holder.get_or_none(id=id)
    if holder is None:
        await models.Holder.create(
            id=id, 
            address=owner_address,
            current_cids=current_cids,
            previous_info=p_i,
            price=price,
            request=request,
            accept_request=acceptRequest
        )
    else:
        holder.address = owner_address
        holder.current_cids = current_cids
        holder.previous_info = p_i
        holder.request = request
        holder.accept_request = acceptRequest
        await holder.save()