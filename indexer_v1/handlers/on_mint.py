from dipdup.context import HandlerContext
from dipdup.models.tezos import TezosBigMapDiff
from indexer_v1 import models as models
from indexer_v1.types.tzsvl.tezos_big_maps.tokens_key import TokensKey
from indexer_v1.types.tzsvl.tezos_big_maps.tokens_value import TokensValue


async def on_mint(
    ctx: HandlerContext,
    tokens: TezosBigMapDiff[TokensKey, TokensValue],
) -> None:
    if not tokens.key: return
    elif not tokens.value.owner: return
    elif not tokens.value.metadata: return

    id = tokens.key
    owner_address = tokens.value.owner
    cid = tokens.value.metadata
    ctx.logger.info(f"id:{id}")
    ctx.logger.info(f"Owner address:{owner_address}")
    ctx.logger.info(f"SVL CID:{cid}")

    await models.Holder.update_or_create(
        id=id, 
        address=owner_address,
        svl_cid=cid
    )