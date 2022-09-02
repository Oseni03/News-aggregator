from django.core.management import BaseCommand

from news.models import Category
from news.scraper import Scraper

class Command(BaseCommand):
    help = 'Update category'
    
    def handle(self, *args, **kwargs):
        scraper = Scraper()
        categories = scraper.categories()
        
        for category in categories:
            new = Category.objects.create(title=category["title"], url=category["url"])
            new.save()