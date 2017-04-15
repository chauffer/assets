# assets

## Usage
```
docker-compose build && docker-compose up
```

## Environment variables
 - `ASSETS_PORT` (Default: `80`) - Port the server will listen on
 - `ASSETS_WORKERS` (Default: number of CPU cores): Number of workers to start
 - `ASSETS_REDIS_HOST` (Default: `redis`) - Redis server host
 - `ASSETS_REDIS_PORT` (Default: `6379`) - Redis server port
 - `ASSETS_TTL` - (Default: `3600`) - How long the URL should be cached for
 - `ASSETS_ALLOWED_PREFIXES` (Default: `https`)- Set to comma-separated URL prefixes to enable URL white-listing

## Endpoints
 - `/v1/ping` - Returns 200
 - `/v1/serve?url=https%3A%2F%2Fsimone.sh` - Returns & caches content of [https://simone.sh](https://simone.sh)
