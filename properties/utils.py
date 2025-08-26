from django.core.cache import cache
from django_redis import get_redis_connection
import logging
from .models import Property

def get_all_properties():
    # Try to fetch from Redis
    properties = cache.get("all_properties")

    if properties is None:
        # If not cached, query DB
        properties = list(Property.objects.all())
        # Store in Redis for 1 hour (3600 seconds)
        cache.set("all_properties", properties, 3600)

    return properties

from django.core.cache import cache
from django_redis import get_redis_connection
import logging
from .models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    # Try to fetch from Redis
    properties = cache.get("all_properties")

    if properties is None:
        # If not cached, query DB
        properties = list(Property.objects.all())
        # Store in Redis for 1 hour (3600 seconds)
        cache.set("all_properties", properties, 3600)

    return properties


def get_redis_cache_metrics():
    """
    Collect Redis cache metrics: keyspace hits, misses, and hit ratio.
    """
    try:
        conn = get_redis_connection("default")
        info = conn.info("stats")

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)

        total = hits + misses
        hit_ratio = (hits / total) if total > 0 else 0

        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": hit_ratio,
        }

        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics
    except Exception as e:
        logger.error(f"Error fetching Redis metrics: {e}")
        return {"error": str(e)}
