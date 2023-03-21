from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import pre_delete
from django.dispatch import receiver



@receiver(pre_delete, sender=None)
def delete_cache_total_sum(*args, **kwargs):
    cache.delete(settings.PRICE_CACHE_NAME)