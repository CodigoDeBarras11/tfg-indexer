from dipdup.context import HandlerContext
from dipdup.models.tezos import TezosBigMapDiff
from indexer_v2 import models as models
from indexer_v2.types.tzsvl.tezos_big_maps.tokens_key import TokensKey
from indexer_v2.types.tzsvl.tezos_big_maps.tokens_value import TokensValue


async def on_mint(
    ctx: HandlerContext,
    tokens: TezosBigMapDiff[TokensKey, TokensValue],
) -> None:
    if not tokens.key: return

    id = tokens.key
    owner_address = tokens.value.owner
    current_cids = tokens.value.current_cids
    previous_info = tokens.value.previous_info
    price = tokens.value.price
    ctx.logger.info(f"id:{id}")
    ctx.logger.info(f"Owner address:{owner_address}")
    ctx.logger.info(f"Current CIDs:{current_cids}")
    ctx.logger.info(f"Previous info:{previous_info}")
    ctx.logger.info(f"Price:{price}")

    await models.Holder.update_or_create(
        id=id, 
        address=owner_address,
        current_cids=current_cids,
        previous_info=previous_info,
        price=price
    )