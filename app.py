import redis
import time
import os

redis_host = os.getenv("REDIS_HOST", None)

while(True):
    time.sleep(1)
    print(f"Running {redis_host}")
