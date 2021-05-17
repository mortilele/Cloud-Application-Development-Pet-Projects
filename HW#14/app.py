from flask import Flask, jsonify

REDIS_HOST = 'alik.redis.cache.windows.net'
REDIS_PASSWORD = 'fdHvo4dbr0XptD3HzRXwgFracf6XUsEd3ugcnSp6280='
REDIS_PORT = 6380

app = Flask(__name__)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


@app.route("/factorial/<int:n>")
def get_factorial(n):
    import redis
    r = redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=0,
        password=REDIS_PASSWORD,
        ssl=True
    )
    key = f'factorial={n}'
    if r.get(key):
        value = int(r.get(key).decode('utf-8'))  # Get value from cache
        r.delete(key)  # Remove key from cache
    else:
        value = factorial(n)
        r.set(key, value)  # Add to cache
    return jsonify({
        'factorial': {
            'input': n,
            'output': value
        },
        'redis_clients': r.client_list(),
        'redis_host': r.info()
    })
