import os
import multiprocessing

api_version = 'v1'

PORT = int(os.getenv('ASSETS_PORT', '80'))
WORKERS = int(os.getenv('ASSETS_WORKERS', multiprocessing.cpu_count()))

REDIS_HOST = os.getenv('ASSETS_REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('ASSETS_REDIS_PORT', '6379')

TTL = int(os.getenv('ASSETS_TTL', '3600'))

ALLOWED_PREFIXES = os.getenv('ASSETS_ALLOWED_PREFIXES', 'https').split(',')
