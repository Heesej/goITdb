import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(
    host="localhost",
    port=6379,
    password=None
)

lru_cache = RedisLRU(client)


@lru_cache
def fib(n):
    if n in {0, 1}:
        return n
    return fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    print(fib(60))
