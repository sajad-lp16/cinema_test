from core_apps.redis_app.redis_gateway import RedisGateway


class TicketCache:
    _cache_gw = RedisGateway("PAYMENT")
    _ticket_lock_cache_key = "TICKET_LOCKED:{ticket_id}"
    _tickets_lock_pattern = "TICKET_LOCKED:*"
    _lock_ttl = 60 * 10  # should be dynamically configurable using [django-constance]

    @classmethod
    def get_locked_tickets_ids(cls) -> list[int]:
        locked_tickets = cls._cache_gw.scan_for_pattern(cls._tickets_lock_pattern)
        return list(map(lambda x: int(x.split(":")[-1]), locked_tickets))

    @classmethod
    def lock_tickets_by_id(cls, ticket_id: int) -> None:
        cache_key = cls._ticket_lock_cache_key.format(ticket_id=ticket_id)
        cls._cache_gw.set(key=cache_key, value=1, ttl=cls._lock_ttl)
