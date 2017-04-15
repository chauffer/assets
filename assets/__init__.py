import aiocache
import aiohttp

from sanic import Sanic, Blueprint
from sanic import response
from sanic.log import log

from . import settings

app = Sanic(__name__)
api_v1 = Blueprint('v1', url_prefix='/v1')


@app.listener('before_server_start')
def before_sanic(sanic, loop):
    aiocache.settings.set_defaults(
        class_="aiocache.RedisCache",
        endpoint=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        namespace="main"
    )
    aiocache.settings.set_default_serializer("aiocache.serializers.JsonSerializer")


@api_v1.route('/ping')
async def ping(request):
    log.info('/ping')
    return response.json({'status': 'ok'})


@api_v1.route('/serve')
async def serve(request):
    url = request.args.get('url')

    if not url:
        return response.json({'status': 'error', 'message': 'Missing parameter `URL`'}, status=422)

    if settings.ALLOWED_PREFIXES and not any(url.startswith(prefix) for prefix in settings.ALLOWED_PREFIXES):
        log.info(f'/serve: {url} not allowed')
        return response.json({'status': 'error', 'message': 'URL not allowed'}, status=400)

    log.info(f'/serve: {url}')
    webpage = await fetch(url)

    return response.text(body=webpage)


@aiocache.cached(key_from_attr='url', ttl=settings.TTL)
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=60) as r:
            return await r.text()


app.blueprint(api_v1)

app.run(host='0.0.0.0', port=settings.PORT, before_start=before_sanic, workers=settings.WORKERS)
