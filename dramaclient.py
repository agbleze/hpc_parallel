import dramatiq
import time
from dramaserver import wait
from dramatiq import group
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend


broker = RedisBroker(host="localhost")
dramatiq.set_broker(broker)
result_backend = RedisBackend(host="localhost")
broker.add_middleware(Results(backend=result_backend))


# [wait.send(10,i) for i in range(10)]
# print("END")


g = group([wait.message(10, "A"),
           wait.message(10, "B"),
           wait.message(4, "C"),
           wait.message(7, "D")
           ]).run()

for res in g.get_results(block=True, timeout=12_000):
    print(res)
print("END of group actors")