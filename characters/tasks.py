from characters.models import Character
from characters.scraper import sync_characters_with_api
from celery import shared_task


@shared_task
def count_characters():
    return Character.objects.count()


@shared_task
def run_sync_with_api():
    sync_characters_with_api()
