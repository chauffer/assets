from sanic import Sanic, Blueprint
from sanic import response
from sanic.log import log
from .. import settings
from .. import utils

API_VERSION = 'v1'

app = Sanic('assets')
api_blueprint = Blueprint(API_VERSION, url_prefix=f'/{API_VERSION}')


@api_blueprint.route('/ping')
async def ping(request):
    log.info('/ping')
    return response.json({'status': 'ok'})


@api_blueprint.route('/serve')
async def serve(request):
    url = request.args.get('url')

    if not url:
        return response.json({'status': 'error', 'message': 'Missing parameter `URL`'}, status=422)

    if settings.ALLOWED_PREFIXES and not any(url.startswith(prefix) for prefix in settings.ALLOWED_PREFIXES):
        log.info(f'/serve: {url} not allowed')
        return response.json({'status': 'error', 'message': 'URL not allowed'}, status=400)

    log.info(f'/serve: {url}')
    raw, content_type = await utils.fetch(url)

    return response.raw(body=raw, content_type=content_type)
