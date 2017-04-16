import aiocache

from sanic import Sanic
from sanic.log import log

from . import settings
from . import api

app = Sanic('assets')

@app.listener('before_server_start')
def before_sanic(sanic, loop):
    aiocache.settings.set_defaults(
        class_="aiocache.RedisCache",
        endpoint=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        namespace="main"
    )
    aiocache.settings.set_default_serializer("aiocache.serializers.PickleSerializer")


for version, blueprint in api.blueprints.items():
    log.info(f'Bound blueprint /{version}')
    app.blueprint(blueprint)

app.run(host='0.0.0.0', port=settings.PORT, before_start=before_sanic, workers=settings.WORKERS)
