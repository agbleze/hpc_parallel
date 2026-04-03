import dramatiq
import time
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend


broker = RedisBroker(host="localhost")
dramatiq.set_broker(broker)

result_backend = RedisBackend(host="localhost")
broker.add_middleware(Results(backend=result_backend))


@dramatiq.actor(store_results=True)
def wait(t,n):
    time.sleep(t)
    print(f"Actor {n} waited for {t} seconds")
    return f"I waited for {t} seconds"