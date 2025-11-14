"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-12593.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=12593,
    decode_responses=True,
    username="default",
    password="e8IYRU5wGjL9OgzU3bjyy3tuNoTELPXP",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

