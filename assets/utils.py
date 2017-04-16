import aiohttp
import aiocache
from . import settings


@aiocache.cached(key_from_attr='url', ttl=settings.TTL)
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=60) as r:
            data = [await r.read(), r.headers['Content-Type']]

    return data
