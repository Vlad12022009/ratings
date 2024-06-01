from django.core.management.base import BaseCommand
from rating.models import Rating

class Command(BaseCommand):
    help = 'remove added entries to Rating model'


    def handle(self, *args, **options):
        Rating.objects.all().filter(text='created from command line').delete()