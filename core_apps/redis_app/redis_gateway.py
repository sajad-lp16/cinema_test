from django_redis import get_redis_connection


class RedisGateway:
    """This is a Custom gateway to interact with the Redis server, can be extended according to your needs."""
    __PREFIX_2_INSTANCE = {}

    def __new__(cls, prefix, *args, **kwargs):
        """each instance has a unique prefix"""
        instance = cls.__PREFIX_2_INSTANCE.get(prefix)
        if instance is None:
            instance = super().__new__(cls)
            cls.__PREFIX_2_INSTANCE[prefix] = instance
        return instance

    def __init__(self, prefix, *args, **kwargs):
        self.prefix = prefix
        self._db = get_redis_connection()

    def _prefixed_key(self, key: str) -> str:
        return f"{self.prefix}:{key}"

    def _decode_key(self, key: bytes) -> str:
        return key.decode()

    def set(self, key, value, ttl=None) -> None:
        prefixed_key = self._prefixed_key(key)
        self._db.set(prefixed_key, value, ex=ttl)

    def scan_for_pattern(self, key: str) -> list[str]:
        cursor = 0
        pattern = self._prefixed_key(key)
        matching_keys = []

        while True:
            cursor, keys = self._db.scan(cursor, match=pattern, count=50)
            for key in keys:
                matching_keys.append(self._decode_key(key))
            if cursor == 0:
                break
        return matching_keys
