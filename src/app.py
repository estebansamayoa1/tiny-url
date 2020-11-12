import redis
import time
import os

REDIS_HOST = os.getenv("REDIS_HOST", None)
cache = redis.Redis(host=REDIS_HOST, port=6379)

print("Starting app")

while(True):
    print("=> Running")
    time.sleep(1)
    retries = 5
    try:
        current_hits = cache.incr('hits')
        print(f"Running {REDIS_HOST}, current hits:{current_hits}")
    except redis.exceptions.ConnectionError as exc:
        if retries == 0:
            #raise exc
            print("'No Redis Connection'")
        retries -= 1
