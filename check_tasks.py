from tasks import add
ares = add.delay(4,4)
print(f"ares.get(): {ares.get()}")


s1 = add.signature((2,2), countdown=10)

s1.delay()

add.delay(4,5)
add.s(4,5)

## primitives and signatures
# grouping tasks
from celery import group

g = group(add.s(i, i) for i in range(10))()

print(f"group g.get(): {g.get()}")

## chaining tasks
# add the result of 1 task to the result of another task
from tasks import add, mul, xsum
from celery import chain, chord

c = chain(add.s(4,4) | mul.s(8))()

print(f"chain c.get(): {c.get()}")


# chord: execute a group of tasks and then execute a callback with the result of the group

#ch = chord((add.s(i,i) for i in range(10)), xsum.s())()
#print(f"chord ch.get(): {ch.get()}")


# chunks - split an iterable into smaller chunks and execute a task on each chunk
from celery import chunks

z = zip(range(10), range(10))
ch = add.chunks(z, 10)()
print(f"chunks ch.get(): {ch.get()}")
chunks()
