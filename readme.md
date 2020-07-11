# Testes com banco de dados com implementação chave/valor (key/value)

## Criar container redis
```bash
docker run -d -p 6379:6379 --name redis_test redis
```
## Criar container arango
```bash
docker run -d -p 8529:8529 -e ARANGO_ROOT_PASSWORD=openSesame --name arango_test arangodb/arangodb:3.6.4
```
## Criar container memcached
```bash
docker run -d -p 11211:11211 --name memcached_test memcached
```
## Bibliotecas para linkagem do script Python com os bancos de dados

https://pypi.org/project/redis/

https://pypi.org/project/pymemcache/

https://pypi.org/project/pyArango/
