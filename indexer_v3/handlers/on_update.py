from dipdup.context import HandlerContext
from dipdup.models.tezos import TezosBigMapDiff
from indexer_v3 import models as models
from indexer_v3.types.tz_svl.tezos_big_maps.tokens_key import TokensKey
from indexer_v3.types.tz_svl.tezos_big_maps.tokens_value import TokensValue


async def on_update(
    ctx: HandlerContext,
    tokens: TezosBigMapDiff[TokensKey, TokensValue],
) -> None:
    if not tokens.key: return

    id = tokens.key
    owner_address = tokens.value.owner
    current_cids = tokens.value.current_cids
    previous_info = tokens.value.previous_info
    p_i = []
    for o in previous_info:
        ctx.logger.info(f"oooooooooo:{o}")
        p_i.append({'address': o.address,
                    'cids': o.list    
                    })
    price = tokens.value.price
    request = tokens.value.request
    ctx.logger.info(f"id:{id}")
    ctx.logger.info(f"Owner address:{owner_address}")
    ctx.logger.info(f"Current CIDs:{current_cids}")
    ctx.logger.info(f"Previous info:{p_i}")
    ctx.logger.info(f"Price:{price}")
    ctx.logger.info(f"Request:{request}")


    holder = await models.Holder.get_or_none(id=id)
    if holder is None:
        await models.Holder.create(
            id=id, 
            address=owner_address,
            current_cids=current_cids,
            previous_info=p_i,
            price=price,
            request=request
        )
    else:
        holder.current_cids = current_cids
        await holder.save()
