from redis import asyncio as aioredis
from redis import Redis
import os

# from redis import Redis
# import redis.asyncio as redis


async def sys_cache() -> Redis:
    # sys_cache_pool = redis.ConnectionPool(host="127.0.0.1", port=6379, db=0)
    # sys_cache_pool = redis.ConnectionPool.from_url(
    #     f"redis://{os.getenv('CACHE_HOST', '127.0.0.1')}:{os.getenv('CACHE_PORT', 6379)}",
    #     db=os.getenv("CACHE_DB", 0),
    #     encoding="utf-8",
    #     decode_responses=True,
    # )
    # return Redis(connection_pool=sys_cache_pool)
    # 从URL方式创建redis连接池
    redis = await aioredis.from_url(
        f"redis://{os.getenv('CACHE_HOST', '127.0.0.1')}:{os.getenv('CACHE_PORT', 6379)}",
        db=os.getenv("CACHE_DB", 0),
        encoding="utf-8",
        decode_responses=True,
    )
    return redis  # type: ignore
